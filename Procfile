release: sh -c 'cd decide && python manage.py migrate'
web: sh -c 'cd beyondvcs && gunicorn beyondvcs.wsgi --log-file -'