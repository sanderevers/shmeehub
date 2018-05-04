FROM python:3.6

WORKDIR /usr/src/app

COPY setup.py ./
COPY shmeehub ./shmeehub
RUN python setup.py install

EXPOSE 80

CMD [ "python", "-m", "shmeehub", "0.0.0.0:80" ]

