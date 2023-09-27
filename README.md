# Deepfake
This is a deepfake detection project built with Python, Django, and deep-learning algorithms. Users will be registered and after login, they can upload an image to verify whether the image is real or fake. 


## Commands for running the project.
python -m venv env
cd env\scripts
activate
cd ..
pip install django
django-admin startproject name
cd name
python manage.py startapp login
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
