FROM node 

RUN mkdir -p testapp

COPY . /testapp


CMD [ "node", "/testapp/server.js" ]
