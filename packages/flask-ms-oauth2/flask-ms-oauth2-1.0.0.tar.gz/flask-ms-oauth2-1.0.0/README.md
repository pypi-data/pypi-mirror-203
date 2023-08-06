# Flask Microsoft OAuth2

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/flask-ms-oauth2.svg)](https://pypi.org/project/flask-ms-oauth2)
[![CircleCI](https://circleci.com/gh/shrivastava-v-ankit/flask-ms-oauth2.svg?style=svg)](https://circleci.com/gh/shrivastava-v-ankit/flask-ms-oauth2)


flask-ms-oauth2 is a Flask implementation of authentication using Microsoft OAuth2 Service. This extension helps to implement authentication solutions based on Microsoft OAuth2 Service. It contains helpful functions and properties to handle oauth2 and token based authentication flows.

</br>

## Installation

```bash
pip install flask-ms-oauth2
```

### Usage

```python
from flask import Flask
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify
from flask_ms_oauth2 import MSOAuth2Manager
from flask_ms_oauth2 import login_handler
from flask_ms_oauth2 import logout_handler
from flask_ms_oauth2 import callback_handler

app = Flask(__name__)
app.secret_key = "my super secret key"

# Setup the flask-ms-oauth2 extention
app.config['CLIENT_ID'] = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
app.config['CLIENT_SECRET'] = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
app.config['TENANT_ID'] = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
app.config["ERROR_REDIRECT_URI"] = "page500"        # Optional
app.config["STATE"] = "mysupersecrethash"   # Optional

app.config['REDIRECT_URI'] = "https://yourdomainhere/msoauth2/callback"  # Specify this url in Callback URLs section of Appllication client settings within Microsoft OAuth2 Sevice. Post login application will redirect to this URL

app.config['SIGNOUT_URI'] = "https://yourdomainhere/login" # Specify this url in Sign out URLs section of Appllication client settings. Post logout application will redirect to this URL


msoauth2 = MSOAuth2Manager(app)


@app.route('/login', methods=['GET'])
def login():
    print("Do the stuff before login to Microsoft Oauth2 Service")
    response = redirect(url_for("msoauth2login"))
    return response


@app.route('/logout', methods=['GET'])
def logout():
    print("Do the stuff before logout from Microsoft Oauth2 Service")
    response = redirect(url_for("msoauth2logout"))
    return response


# Use @login_handler decorator on Microsoft OAuth2 login route
@app.route('/msoauth2/login', methods=['GET'])
@login_handler
def msoauth2login():
    pass


@app.route('/home', methods=['GET'])
def home():
    current_user = session["username"]
    return jsonify(logged_in_as=current_user), 200


# Use @callback_handler decorator on Microsoft OAuth2 callback route
@app.route('/auth/callback', methods=['GET'])
@callback_handler
def callback():
    for key in list(session.keys()):
        print(f"Value for {key} is {session[key]}")
    response = redirect(url_for("home"))
    return response



# Use @logout_handler decorator on Microsoft OAuth2 logout route
@app.route('/msoauth2/logout', methods=['GET'])
@logout_handler
def msoauth2logout():
    pass


@app.route('/page500', methods=['GET'])
def page500():
    return jsonify(Error="Something went wrong"), 500


if __name__ == '__main__':
    app.run(debug=True)
```



### Development Setup

Using pipenv
```bash
pipenv install --dev 
```
Using virtualenv
```bash
python3 -m venv venv
source venv/bin/activate
pip install .
```

### Contributing

1. Fork repo- https://github.com/shrivastava-v-ankit/flask-ms-oauth2.git
2. Create your feature branch - `git checkout -b feature/name`
3. Add Python test (pytest) and coverage report for new/changed feature.
4. Commit your changes - `git commit -am "Added name"`
5. Push to the branch - `git push origin feature/name`
6. Create a new pull request
