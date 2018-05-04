from flask import Blueprint, request
from .oauth2 import auth_server, require_oauth
from . import account

bp = Blueprint(__name__, 'home')

@bp.route('/login/oauth2/authorize', methods=['GET', 'POST'])
def authorize():
    return auth_server.create_authorization_response(grant_user=42)

@bp.route('/login/oauth2/token', methods=['POST'])
def issue_token():
    print(request.form)
    return auth_server.create_token_response()

@bp.route('/keyhub/rest/v1/account/me')
@require_oauth('profile')
def profile():
    return account.__doc__,{'Content-Type':'application/vnd.topicus.keyhub+xml'}

