release: python manage.py makemigrations && python manage.py migrate
web: gunicorn agendaclinica.wsgi:application --log-file - --log-level debug


