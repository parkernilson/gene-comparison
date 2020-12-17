#!/bin/bash

if [ ${ENV} = "development" ]; then
    # if development is specified, run with flask dev server for live reloading
    flask run --host=0.0.0.0
else
    # if not in development, serve with production server
    gunicorn --bind=:5000 --timeout=45 server:app
fi