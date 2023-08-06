import pandas as pd
from typing import Union
from ra_engine.core.app import RAEApp
import requests
from ra_engine.type_def.results import Response
from ra_engine.core.app import App


class SKLRunner:
    app: RAEApp = None
    pred_df: pd.DataFrame = None
    pred_config: Union[dict, None] = None
    endpoint: str = "/api/v1/runner/skl"

    def __init__(
        self, app: RAEApp, pred_df: pd.DataFrame, pred_config: Union[dict, None] = None
    ):
        self.app: RAEApp = app
        self.pred_df = pred_df
        self.pred_config = pred_config

        if self.app is None:
            raise ValueError("RAEApp is not initialized properly.")
        if self.app.credentials is None:
            raise ValueError("Provided RAEApp is not have credentials.")
        if self.app.credentials.apiKey is None:
            raise ValueError("Provided RAEApp is doesn't have any API Key.")

    def inputs(self) -> dict:
        return {
            "data": self.pred_df.to_dict(),
            "config": self.pred_config,
        }

    def exec(self, id: str):
        response = requests.get(
            self.app.credentials.host + self.endpoint + f"/{id}",
            json=self.inputs(),
            headers={
                "Content-Type": "application/json",
                "X-Api-Key": self.app.credentials.apiKey,
            },
        )
        return Response(response)
