from flask import Blueprint, request, make_response, current_app, url_for, jsonify
from .oauth2 import auth_server, require_oauth
import json
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


@bp.route('/jwks.json')
def jwks():
    pubkey_dict = current_app.config['DUMMY_JWT_PUB_KEY']
    jwks = {'keys':[pubkey_dict]}
    return make_response(json.dumps(jwks), {'Content-Type':'application/json'})

@bp.route('/.well-known/openid-configuration')
def discovery_document():
    doc = {
        'issuer': current_app.config['OAUTH2_JWT_ISS'],
        'authorization_endpoint': url_for('.authorize', _external=True),
        'token_endpoint': url_for('.issue_token', _external=True),
        'jwks_uri': url_for('.jwks', _external=True),
    }
    return jsonify(doc)