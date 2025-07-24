up:
	docker-compose up

build:
	docker-compose up --build

migrate:
	docker-compose run web python manage.py migrate

createsuperuser:
	docker-compose run web python manage.py createsuperuser

shell:
	docker-compose run web python manage.py shell

down:
	docker-compose down
