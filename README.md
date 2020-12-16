# Style Transfer Project
This project is a Flask website which uses Tensforflow Hub to load a pretrained Style Transfer ML Module to perform style transfer.

# Requirements
This project requires Docker to run.

# Running this project
For development, run:
```
$ ./dev.sh
```
This command will build and then spin up the docker container in development mode. This means that:
- Whenever any changes are made in the flask-app directory, the flask server will automatically reload to reflect the changes. 
- File-caching is disabled (via HTTP Response Headers), so that changes will be reflected in the browser when you refresh
- The project can be viewed at localhost:5000

If this project is being run in a production environment, use:
```
$ ./redeploy.sh
```
This command will build and then spin up the docker container in production mode. This means that:
- The project will be served on 0.0.0.0:5000 using GUnicorn instead of the flask dev server.