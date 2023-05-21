import json
from requests_oauthlib import OAuth1Session
from . import *


class Authenticator:

    def __init__(self):
        self.keys = None
        self.oauth = None
        self.__authenticate()

    def __authenticate(self):
        try:
            oauth = OAuth1Session(
                CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=ACCESS_TOKEN,
                resource_owner_secret=ACCESS_TOKEN_SECRET,
            )
        except Exception as e:
            print(e.__str__())
            # Log into DB
        else:
            self.oauth = oauth

    def get_oauth(self):
        return self.oauth
