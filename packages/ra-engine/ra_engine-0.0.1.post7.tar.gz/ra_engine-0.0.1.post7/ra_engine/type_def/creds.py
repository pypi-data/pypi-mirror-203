class Credentials:
    def __init__(
        self,
        host,
        apiKey=None,
        project=None,
    ):
        self.host = host
        self.project = project
        self.apiKey = apiKey
