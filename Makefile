test-lint:
	pipenv run seed-isort-config
	pipenv run isort -c
	pipenv run flake8 .
	pipenv run black --check .

prod:
	pipenv run python manage.py migrate && \
	pipenv run gunicorn -w 2 --bind 0.0.0.0:8000 --access-logfile - bvdata.wsgi