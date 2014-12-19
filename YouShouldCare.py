from time import sleep

ckey = ''
csecret = ''
atoken = ''
asecret = ''


while True:

    from TwitterAPI import TwitterAPI
    api = TwitterAPI(ckey, csecret, atoken, asecret)

    r = api.request('statuses/filter', {'track': 'could care less'})

    print('Connected to stream...')
    for item in r.get_iterator():
        tweet_id = item['id']

        original_tweet_text = item['text']
        if not "@" in original_tweet_text and "#" in original_tweet_text and item['user']['screen_name'] != "YouShouldCare":
            # new_tweet_text = 'RT @' + item['user']['screen_name'] + ' ' + original_tweet_text
            new_tweet_text = original_tweet_text
            postresult = api.request('statuses/update', {'status': new_tweet_text})
            # friend_result = api.request('friendships/create', {'screen_name': item['user']['screen_name']})
            print('Tweeted: ' + new_tweet_text)

        else:
            # print('Passed on tweet: @' + str(item['user']['screen_name']) + ' ' + str(original_tweet_text))
            pass

    print('Restarting after a problem...')
    sleep(15)
