###
# Set up development
FROM node:latest AS development

WORKDIR /code

# copy over package and package-lock
COPY ./package*.json ./

# install dependencies
RUN npm install

# copy over the source code, so we can run the dev server
COPY . .