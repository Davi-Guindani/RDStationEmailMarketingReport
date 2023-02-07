class Client:
    def __init__(self, name: str, client_id: str, client_secret: str, code: str, refresh_token: str,
                 background_color: str, first_color: str, second_color: str, bar_label_color: str):
        self.NAME = name
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.CODE = code
        self.access_token = ""
        self.REFRESH_TOKEN = refresh_token
        self.BACKGROUND_COLOR = background_color
        self.FIRST_COLOR = first_color
        self.SECOND_COLOR = second_color
        self.BAR_LABEL_COLOR = bar_label_color

    def get_name(self):
        return self.NAME

    def set_name(self, name):
        self.NAME = name

    def get_client_id(self):
        return self.CLIENT_ID

    def set_client_id(self, id):
        self.CLIENT_ID = id

    def get_client_secret(self):
        return self.CLIENT_SECRET

    def set_client_secret(self, secret):
        self.CLIENT_SECRET = secret

    def get_code(self):
        return self.CODE

    def set_code(self, code):
        self.CODE = code

    def get_access_token(self):
        return self.access_token

    def set_access_token(self, token):
        self.access_token = token

    def get_refresh_token(self):
        return self.REFRESH_TOKEN

    def set_refresh_token(self, token):
        self.REFRESH_TOKEN = token

    def get_background_color(self):
        return self.BACKGROUND_COLOR

    def set_background_color(self, color):
        self.BACKGROUND_COLOR = color

    def get_first_color(self):
        return self.FIRST_COLOR

    def set_first_color(self, color):
        self.FIRST_COLOR = color

    def get_second_color(self):
        return self.SECOND_COLOR

    def set_second_color(self, color):
        self.SECOND_COLOR = color

    def get_bar_label_color(self):
        return self.BAR_LABEL_COLOR

    def set_bar_label_color(self, color):
        self.BAR_LABEL_COLOR = color
