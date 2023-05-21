import requests



class Reader:
    def __init__(self, oauth):
        self.__set_urls()
        self.oauth = oauth

    def __set_urls(self):
        self.get_dm_events_url = "https://api.twitter.com/2/dm_events"

    def get_user_conversation_events(self):
        pass
