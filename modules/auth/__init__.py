import json

keys_path = './env.json'
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
CLIENT_ID = ''
CLIENT_SECRET = ''


def read_keys():
    print("Executing read_keys")
    with open(keys_path, 'r') as keys:
        keys = json.load(keys)
        global CONSUMER_KEY, CONSUMER_SECRET, BEARER_TOKEN, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CLIENT_ID, CLIENT_SECRET
        CONSUMER_KEY = keys.get('api-key')
        CONSUMER_SECRET = keys.get('api-key-secret')
        BEARER_TOKEN = keys.get('bearer-token')
        ACCESS_TOKEN = keys.get('access-token')
        ACCESS_TOKEN_SECRET = keys.get('access-token-secret')
        CLIENT_ID = keys.get('client-id')
        CLIENT_SECRET = keys.get('client-secret')


read_keys()
