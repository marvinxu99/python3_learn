import tweepy
import time


# auth = tweepy.OAuthHandler('consumer_key', consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
auth = tweepy.OAuthHandler('xxxx',
                           'xxxx')
auth.set_access_token('xxxx',
                      'xxxx')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
print(user.id, user.name)
print(user.followers_count)

# Generate bot


def limit_handler(cursor):   # hanle the rate limit error
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)
        except StopIteration:
            break


# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.followers_count > 100:
#         follower.follow() == "xxxx":   # follow back
#         print(follower.name)

#     # if follower.name == "name":
#     #     follower.follow()


search_string = 'python'
number_of_tweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(number_of_tweets)):
    try:
        tweet.favorite()
        tweet.retweet()
        print('i like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
