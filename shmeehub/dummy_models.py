from authlib.specs.rfc6749.models import ClientMixin, TokenMixin
from authlib.specs.oidc.models import AuthorizationCodeMixin
from authlib.specs.oidc.claims import UserInfo
import time
import math

class DummyClient(ClientMixin):
    def __init__(self,client_id):
        self.client_id=client_id

    def check_redirect_uri(self, redirect_uri):
        return True

    def has_client_secret(self):
        return True

    def check_client_secret(self, client_secret):
        return True

    def check_token_endpoint_auth_method(self, method):
        return True

    def check_response_type(self, response_type):
        return response_type=='code'

    def check_grant_type(self, grant_type):
        return grant_type=='authorization_code'

    def check_requested_scopes(self, scopes):
        return True


class DummyAuthorizationCode(AuthorizationCodeMixin):
    def __init__(self, redirect_uri, nonce):
        self.redirect_uri = redirect_uri
        self.nonce = nonce

    def get_redirect_uri(self):
        return self.redirect_uri

    def get_scope(self):
        return 'openid profile'

    def get_nonce(self):
        return self.nonce

    def get_auth_time(self):
        return math.floor(time.time())


class DummyToken(TokenMixin):
    def get_scope(self):
        return 'openid profile'

    def get_expires_in(self):
        return 60 * 60

    def get_expires_at(self):
        return math.floor(time.time()) + 60 * 60

class DummyUser:
    def generate_user_info(self,scopes):
        return UserInfo({'sub':42,'name':'Rando Cardissian'})
