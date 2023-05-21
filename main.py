from modules.auth.Authenticator import Authenticator
from modules.apps.tweets.TweetPoster import TweetPoster


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    authenticator = Authenticator()
    oauth = authenticator.get_oauth()
    app = TweetPoster(oauth)
    app.send_tweet("Hello World!")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
