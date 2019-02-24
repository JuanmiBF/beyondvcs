release: sh -c 'cd beyondvcs && python manage.py makemigrations && python manage.py migrate'
web: sh -c 'cd beyondvcs && gunicorn beyondvcs.wsgi --log-file -'