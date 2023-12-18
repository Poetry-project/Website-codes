
# client_id = "cVdTV2Fic1FySUF5NVp4WnFfYjk6MTpjaQ"
# client_secret = "6gVt0-BRzG6CQNV0IMfOnUPvRknmJONy8O9swMtSbn6J3RvIWH"
# auth_url = "https://twitter.com/i/oauth2/authorize"
# token_url = "https://api.twitter.com/2/oauth2/token"
# redirect_uri = "http://127.0.0.1:5000/oauth/callback"


# scopes = ["tweet.read", "users.read", "tweet.write"]
# code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
# code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)
# code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
# code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
# code_challenge = code_challenge.replace("=", "")


# # Posting the Tweet
# def post_tweet(payload, new_token):
#     print("Tweeting!")
#     return requests.request(
#         "POST",
#         "https://api.twitter.com/2/tweets",
#         json=payload,
#         headers={
#             "Authorization": "Bearer {}".format(new_token["access_token"]),
#             "Content-Type": "application/json",
#         },
#     )


# @app.route("/oauth/callback", methods=["GET"])
# def callback():
#     print ("oauth callback")
#     code = request.args.get("code")    
#     token = twitter.fetch_token(
#         token_url=token_url,
#         client_secret=client_secret,
#         code_verifier=code_verifier,
#         code=code,
#     )
#     response = post_tweet(payload, token).json()
#     return response


      
# @app.route("/poetryX", methods=['GET', 'POST'])
# def poetryX():
    # global twitter
    # twitter = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)
    # authorization_url, state = twitter.authorization_url(
    #     auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    # )
    # session["oauth_state"] = state
    # return redirect(authorization_url)

    # OAuth process, using the keys and tokens
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        
    # Creation of the actual interface, using authentication
    # api = tweepy.API(auth)

    # Sample method, used to update a status, you can write message whatever you want to post in twitter
    # api.update_status("Happy Coding!" + " #LearnPython" )

