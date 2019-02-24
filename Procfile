release: sh -c 'heroku config:add mongo=mongodb+srv://db_developer:T4qlJUKEjXmsSWtc:beyondvcs-db-0-adlff.mong
odb.net/:27017/mongoDB && cd beyondvcs && python manage.py makemigrations && python manage.py migrate'
web: sh -c 'cd beyondvcs && gunicorn beyondvcs.wsgi --log-file -'