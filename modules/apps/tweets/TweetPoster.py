class TweetPoster:
    def __init__(self, oauth):
        self.oauth = oauth
        self.__set_urls()

    def __set_urls(self):
        self.tweet_url = "https://api.twitter.com/2/tweets"

    def send_tweet(self, tweet):
        response = self.oauth.post(
            self.tweet_url,
            json={"text": tweet}
        )

        if response.status_code != 201:
            # Log into DB
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )
        else:
            print("Tweeted Successfully!")
