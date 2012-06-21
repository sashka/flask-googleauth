# Flask-OpenID
This is a partial port of torando.auth to be used with Flask.


## Usage
Example usage for Google Federated Login.

Require an account from a given Google Apps domain for your Flask apps.

Greate for internal apps. Inspired by Kenneth Reitz.

    from flask import Flask
    from flask_openid import GoogleFederated

    # Setup Flask
    app = Flask(__name__)
    app.secret_key = "random secret key"

    # Setup Google Federated Auth
    auth = GoogleFederated(app, "heroku.com")

    @app.route("/")
    @auth.required
    def secret():
    	# Once user is authenticated, his name and email are accessible as
    	# g.user.name and g.user.email.
        return "ssssshhhhh (c) kennethreitz"


If you want to authenticate your users with general Google OpenID you should import and use ``GoogleAuth`` instead of ``GoogleFederated``.


## Install
Installation will be simple as soon as I will publish this on PyPI.


## Prerequisites
Be sure that your Google Apps domain is enabled to be an OpenID provider under "Advanced tools" → "Federated Login using OpenID".