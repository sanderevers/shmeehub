from authlib.flask.oauth2 import AuthorizationServer, ResourceProtector
from authlib.specs.rfc6750 import BearerTokenValidator
from authlib.specs.oidc.grants import OpenIDCodeGrant
from authlib.specs.rfc7517 import JWK
from authlib.specs.rfc7518 import JWK_ALGORITHMS
import base64
import json

from .dummy_models import DummyClient, DummyToken, DummyAuthorizationCode, DummyUser

class DummyOpenIDCodeGrant(OpenIDCodeGrant):
    def create_authorization_code(self, client, user, request):
        info = {'redirect_uri':request.redirect_uri,
                'nonce':request.data.get('nonce')}
        return base64.urlsafe_b64encode(bytes(json.dumps(info),'utf-8'))

    def parse_authorization_code(self, code, client):
        info = json.loads(str(base64.urlsafe_b64decode(code),'utf-8'))
        return DummyAuthorizationCode(**info)

    def delete_authorization_code(self, authorization_code):
        pass

    def authenticate_user(self, authorization_code):
        return DummyUser()

    def exists_nonce(self, nonce, request):
        return False

class DummyBearerTokenValidator(BearerTokenValidator):
    def authenticate_token(self, token_string):
        return DummyToken()

    def request_invalid(self, request):
        return False

    def token_revoked(self, token):
        return False

def query_client(client_id):
    return DummyClient(client_id)

def save_token(token, client):
    pass


def config_oauth(app):
    with app.open_resource(app.config['DUMMY_JWT_PRIV_KEY_PATH'], 'rb') as f:
        privkey_data = f.read()
    app.config['OAUTH2_JWT_KEY'] = JWK(JWK_ALGORITHMS).dumps(privkey_data, kty='RSA')
    with app.open_resource(app.config['DUMMY_JWT_PUB_KEY_PATH'], 'rb') as f:
        pubkey_data = f.read()
    app.config['DUMMY_JWT_PUB_KEY'] = JWK(JWK_ALGORITHMS).dumps(pubkey_data, kty='RSA')

    auth_server.init_app(
        app, query_client=query_client, save_token=save_token)
    auth_server.register_grant(DummyOpenIDCodeGrant)

    # protect resource
    require_oauth.register_token_validator(DummyBearerTokenValidator())

auth_server = AuthorizationServer()
require_oauth = ResourceProtector()
