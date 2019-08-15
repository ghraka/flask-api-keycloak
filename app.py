import json
import logging

from flask import Flask, g, jsonify
from flask_oidc import OpenIDConnect
import requests

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': "API-V3",
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_OPENID_REALM': 'apiv3',
    'OIDC_SCOPES': ['openid'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_TOKEN_TYPE_HINT': 'access_token'
})


oidc = OpenIDConnect(app)

@app.route('/api', methods=['GET'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def hello_api():
    """OAuth 2.0 protected API endpoint accessible via AccessToken"""

    return json.dumps({'hello': 'Welcome %s' % g.oidc_token_info['sub']})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')