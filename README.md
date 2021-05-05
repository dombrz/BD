# BD


zainstalować django 

pip install django
pip install djangorestframework




można projekt odpalić w pycharmie czy innym ide korzystając z tego co wrzuciłem. Należy wtedy utworzyć kilka pustych plików w odpowiednich miejscach nazwyając je  __init__.py 
(plik db_reamde_1 pokazuje w jaki sposób powinno wyglądać drzewo projektu - w które miejsca dołączyć te puste pliki).

Ewentualnie stworzyć samemu projekt i aplikację która się w nim znajduje - w konsoli wybrać docelowy folder w którym ma być utworzony projekt a następnie wpisać:

django-admin startproject "nazwa projektu"
python manage.py startapp "nazwa aplikacji"

Następnie dodać pliki z githuba zastępując te utworzone automatycznie.


Więcej wskazówek w tutorialu (gdyby okazały się niezbędne): https://docs.djangoproject.com/pl/3.2/intro/tutorial01/




W settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopdb',
        'USER': 'root',
        'PASSWORD': 'root' ,
        'PORT' : 3306,
        'HOST' : '127.0.0.1' ,
    }
}
wpisać user, password itp. właściwe dla waszych baz danych!!!!




następnie użyć

python manage.py migrate


uruchomienie serwera:
python manage.py runserver




