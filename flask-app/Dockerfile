FROM tensorflow/tensorflow:latest

WORKDIR /code

RUN mkdir /results

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "bash", "./launch-server.sh" ]