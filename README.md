# Atlantis

Backend Python/Django

Frontend Vue3-CLI

How it works?

BACKEND

1 - Create Backend docker image:

cd .\backend\api
docker build --build-arg PORT=8000 -t atlantis-backend .

2 - create the docker conteiner:

docker run -d -p 8000:8000 -v src:/backend --name atlantis-backend_app atlantis-backend

3 - test:

http://localhost:8000/

4 - create superuser:
docker exec -it atlantis-backend_app /bin/bash
python manage.py createsuperuser


