import json
from requests_oauthlib import OAuth1Session


class Authenticator:

    def __init__(self):
        self.keys_path = './env.json'
        self.keys = None
        self.oauth = None
        self.__authenticate()

    def __authenticate(self):
        # Reads env variables from file
        self.__read_keys()

        consumer_key = self.keys.get('api-key')
        consumer_secret = self.keys.get('api-key-secret')
        access_token = self.keys.get('access-token')
        access_token_secret = self.keys.get('access-token-secret')

        try:
            oauth = OAuth1Session(
                consumer_key,
                client_secret=consumer_secret,
                resource_owner_key=access_token,
                resource_owner_secret=access_token_secret,
            )
        except Exception as e:
            print(e.__str__())
            # Log into DB
        else:
            self.oauth = oauth

    def __read_keys(self):
        with open(self.keys_path, 'r') as keys:
            self.keys = json.load(keys)
