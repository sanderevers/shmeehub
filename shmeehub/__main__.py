import os
import sys
from flask import Flask
from .oauth2 import config_oauth
from .routes import bp

def create_app():
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    config_oauth(app)
    app.register_blueprint(bp, url_prefix='')
    return app

# entry point for cli script
def main():
    host = None
    port = None
    if len(sys.argv) > 1:
        host,port = sys.argv[1].split(':')
        port=int(port)
    app.run(host=host, port=port)

# also usable with FLASK_APP=__main__.py flask run
app = create_app()
if __name__=='__main__': # entry point for python -m
    main()
