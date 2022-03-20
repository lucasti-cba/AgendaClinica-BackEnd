migrate: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn agendaclinica.wsgi:application --log-file - --log-level debug


