from node 

RUN mkdir -p testapp

copy . /testapp

EXPOSE 8000

CMD [ "node", "/testapp/server.js" ]
