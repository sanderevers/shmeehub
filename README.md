# ShmeeHub - mocking KeyHub

ShmeeHub is an OAuth2 server whose endpoint URLs match those of KeyHub:

    /login/oauth2/authorize
    /login/oauth2/token
    /keyhub/rest/v1/account/me

In blatant disregard of the OAuth2 specs, it will blindly authenticate you (over HTTP!) as a random user and authorize any OAuth2 client (using the Authorization Code flow) to fetch your dummy profile. You can use it to log into any Cobra authenticator that supports KeyHub as a remote identity provider. Simply run ShmeeHub and change your `service.keyhub.url` JNDI value to `http://localhost:5000`.

## Install in your existing Python 3 environment

    git clone git@github.com:sanderevers/shmeehub
    cd shmeehub
    python setup.py install
    
Run using `shmeehub` or `python -m shmeehub`.

## Install in a clean Python 3 virtualenv

    virtualenv shmeehub
    source shmeehub/bin/activate
    git clone git@github:sanderevers/shmeehub shmeehub/src
    cd shmeehub/src
    python setup.py install

Run using `shmeehub` or `python -m shmeehub` while your virtualenv is activated.

## Install using Docker

    git clone git@github.com:sanderevers/shmeehub
    cd shmeehub
    docker build -t shmeehub .
   
Run using `docker run -it --rm 5000:80 --name shmeehub-instance shmeehub`.
Or simply use `docker-compose up -d`.
