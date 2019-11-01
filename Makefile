dev:
	pipenv sync --dev

lint:
	pipenv run isort
	pipenv run flake8 .
	pipenv run black .


test-lint:
	pipenv run isort -c
	pipenv run flake8 .
	pipenv run black --check .

test: dev test-lint
	pipenv run ./manage.py makemigrations --check
	pipenv run pytest

prod:
	pipenv run python manage.py migrate && \
	pipenv run python manage.py compilemessages -l de && \
	pipenv run python manage.py collectstatic --noinput && \
	pipenv run gunicorn -w 2 --bind 0.0.0.0:8000 --access-logfile - bvdata.wsgi
