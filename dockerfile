from node 

RUN mkdir -p testapp

copy . /testapp

CMD [ "node", "/testapp/server.js" ]
