create new folder - django
create virtual environment - `python3 -m venv customEnv`
activate source env - `source customEnv/bin/activate`
deactivate source env - `deactivate`

some useful command inside enviroment

pip3 --version
pip3 list
pip3 install django
django-admin --version
django-admin startproject projectName . - To Create project

# To Run Application

python manage.py runserver PORT(optional)

# To create new module under same directory

python manage.py startapp app

# To start migration or create a migration run below commands

make sure you've migrations folder inside app

python manage.py makemigrations

# To view migration

python manage.py sqlmigrate app 0001

python manage.py migrate - It will apply all migration

python manage.py showmigrations

# To perform database operation

python manage.py shell

from app.models import Model_Name

# To create admin superuser

python manage.py createsuperuser

# To register model in admin panel

go to app/admin.py

admin.site.register(NAME_OF_MODULE)
