from authlib.specs.rfc6749.models import ClientMixin, TokenMixin, AuthorizationCodeMixin
import time

class DummyClient(ClientMixin):
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
    def __init__(self, redirect_uri):
        self.redirect_uri = redirect_uri

    def get_redirect_uri(self):
        return self.redirect_uri

    def get_scope(self):
        return 'profile'


class DummyToken(TokenMixin):
    def get_scope(self):
        return 'profile'

    def get_expires_in(self):
        return 60 * 60

    def get_expires_at(self):
        return time.time() + 60 * 60
