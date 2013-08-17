Flask-GoogleAuth
================
This is a partial port of torando.auth to be used with Flask.
It is small, self contained and do not use any filesystem operations.
Greate for internal apps.

Written by Alexander Saltanov, inspired by Kenneth Reitz.


Usage
-----
Example usage for Google Federated Login.

Routes ``/login/`` and ``/logout/`` will be provided automagically.

Require an account from a given Google Apps domain for your Flask apps::

    from flask import Flask, g
    from flask_googleauth import GoogleFederated

    # Setup Flask
    app = Flask(__name__)
    app.secret_key = "random secret key"

    # Setup Google Federated Auth
    auth = GoogleFederated("mokote.com", app)

    @app.route("/")
    @auth.required
    def secret():
        # Once user is authenticated, his name and email are accessible as
        # g.user.name and g.user.email.
        return "You have rights to be here, %s (%s)" % (g.user.name, g.user.email)

    app.run()

If you want to authenticate your users with general Google OpenID you should import and use ``GoogleAuth`` instead of ``GoogleFederated``::

    auth = GoogleAuth(app)


Install
-------
To install Flask-GoogleAuth::

    pip install flask-googleauth


Prerequisites
-------------
Be sure that your Google Apps domain is enabled to be an OpenID provider under "Advanced tools" → "Federated Login using OpenID".
