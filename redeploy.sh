sudo docker-compose down

cd front-end
npm run build

cd ..

sudo docker-compose up --build -d