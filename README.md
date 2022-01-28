# EvoTask2

Requires :
Python libs
  - flask
  - sqlite3
  - json

JavaScript and css libs (link in html):
  - jquery v2.2.0
  - bootstrap v5.0.1


In project used 2 html files (index.html, userList.html) in folder template for rendering templates 
and 1 js file (app.js) in folder static/js to set listeners and make queries to server.

In role of development server is used flask in py file (main.py).

In additional in folder static/css you can find app.css. That file used to make some little changes for visuals.

Link to Heroku:
 - https://evo-task2.herokuapp.com/

Link to Dockerhub:
 - https://hub.docker.com/repository/docker/voroninol/evotask

To run docker image use command:
 - docker run -p 4000:4000 --name evotask voroninol/evotask

It will run on: localhost:4000

Thx for reading =)
