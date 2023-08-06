import requests
from ra_engine.core.app import RAEApp, XAPIKey
from ra_engine.type_def.ml import TrainData, PredData, MLData, TSData
import pandas as pd
from ra_engine.type_def.results import Response


class EvaluatorML:
    def __init__(
        self,
        endpoint: str,
        app: RAEApp,
        train_df: pd.DataFrame,
        pred_df: pd.DataFrame,
        features: list,
        targets: list,
        train_config: dict = None,
        pred_config: dict = None,
    ):
        self.app: RAEApp = app
        self.ml_data = MLData(
            TrainData(train_df, features, targets, train_config),
            PredData(pred_df, pred_config),
        )
        self.endpoint = endpoint

        if self.app is None:
            raise ValueError("RAEApp is not initialized properly.")
        if self.app.credentials is None:
            raise ValueError("Provided RAEApp is not have credentials.")
        if self.app.credentials.apiKey is None:
            raise ValueError("Provided RAEApp is doesn't have any API Key.")

    def exec(self) -> Response:
        self.response = requests.post(
            self.app.credentials.host + self.endpoint,
            json=self.ml_data.as_dict(),
            headers={
                "Content-Type": "application/json",
                "X-Api-Key": f"{self.app.credentials.apiKey}",
            },
        )
        return Response(self.response)

    def inputs(self) -> dict:
        return self.ml_data.as_dict()


class EvaluatorTS:
    def __init__(
        self,
        endpoint: str,
        app: RAEApp,
        train_df: pd.DataFrame,
        dates_col: str,
        target_col: str,
        train_config: dict = None,
        forcast_for: int = 1,
    ):

        self.app: RAEApp = app
        self.ts_data = TSData(
            train_df, dates_col, target_col, train_config, forcast_for
        )
        self.endpoint = endpoint
        self.response = None
        self._json = None

        if self.app is None:
            raise ValueError("RAEApp is not initialized properly.")
        if self.app.credentials is None:
            raise ValueError("Provided RAEApp is not have credentials.")
        if self.app.credentials.apiKey is None:
            raise ValueError("Provided RAEApp is doesn't have any API Key.")

    def exec(self) -> Response:
        self.response = requests.post(
            self.app.credentials.host + self.endpoint,
            json=self.ts_data.as_dict(),
            headers={
                "Content-Type": "application/json",
                "X-Api-Key": f"{self.app.credentials.apiKey}",
            },
        )
        return Response(self.response)

    def inputs(self) -> dict:
        return self.ts_data.as_dict()
