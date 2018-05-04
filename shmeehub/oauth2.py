from authlib.flask.oauth2 import AuthorizationServer, ResourceProtector
from authlib.specs.rfc6749 import grants
from authlib.specs.rfc6750 import BearerTokenValidator
from urllib.parse import quote_plus, unquote_plus

from .dummy_models import DummyClient, DummyToken, DummyAuthorizationCode

class DummyAuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    def create_authorization_code(self, client, user, request):
        return quote_plus(request.redirect_uri)

    def parse_authorization_code(self, code, client):
        return DummyAuthorizationCode(unquote_plus(code))

    def delete_authorization_code(self, authorization_code):
        pass

    def authenticate_user(self, authorization_code):
        return 42

class DummyBearerTokenValidator(BearerTokenValidator):
    def authenticate_token(self, token_string):
        return DummyToken()

    def request_invalid(self, request):
        return False

    def token_revoked(self, token):
        return False

def query_client(client_id):
    return DummyClient()

def save_token(token, client):
    pass


def config_oauth(app):
    auth_server.init_app(
        app, query_client=query_client, save_token=save_token)
    auth_server.register_grant(DummyAuthorizationCodeGrant)

    # protect resource
    require_oauth.register_token_validator(DummyBearerTokenValidator())

auth_server = AuthorizationServer()
require_oauth = ResourceProtector()
