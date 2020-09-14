## Introduction to Django Pet Project 

**Contents** 
- [x] [Creating django project](#creating-a-django-project)
- [x] [Creating an application](#creating-an-application-called-adoptions)
- [x] [MVC Architecture](#mvc-architecture)
- [x] [Django Migrations](#django-migrations)
- [x] [DB Browser for SQLite](#db-browser-for-sqlite)
- [x] [Working with the Django Admin](#working-with-django-admin)
- [x] [Querying data with the Django ORM](#querying-data-with-the-django-orm)
- [x] [URL Patterns](#url-patterns-aka-url-confs)
- [x] [Building Django Templates](#building-django-templates)
- [x] [Using Static Files](#using-static-files)

## Creating a django project 
```
django-admin startproject wisdompets
```

**Folder Structure**
```
.
├── manage.py
└── wisdompets
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

File structure explanation
> Extensive documentation [HERE](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website) 
- `manage.py` file is a script to run Django tools for this project which is created using django-admin. Used to create applications, work with databases, and start the development web server
- `__init__` file tells Python that this folder contains Python files 
- `wasgi` or `wsgi` and `asgi` file provide hooks for web servers such as Apache, Nginx when Django is running on a live webiste
- `settings.py` - contains website settings, including registering any applications we create, the location of our static files, database configuration details, etc

This project uses the `settings` and `urls` files to configure Django and to set up how the URL routing works

## Creating an application called adoptions
```
python3 manage.py startapp adoptions
```
Which is laid out like this:
```
adoptions/
.
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```
File structure explanation:
- `__init__.py`
- `admin.py` is where you register your app's models with the Django admin application
- `models.py` is the module containing the models for your app
- `tests.py` contains test procedures when testing your app
- `views.py` contains views for your app, takes web requests - the user interface 


Adding adoptions application to `settings.py` in line 40:
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adoptions',
]
```

## MVC Architecture 
- Model-View-Controller
- Django uses MVC architecture
- Pattern that separates an application into three main logical components
    - `Controller` - Interface between model and view. Processes incoming requests, manipulates data using the Model component and interacts with the Views to render final output 
    - `Model` - Corresponds to data-related logic that the user works with. Can represent data being transferred between the view and controller components. 
    - `View` - UI logic e.g. text boxes, dropdowns. 
- Django uses different names:
```bash
URL
Patterns
Views 
Models
Templates
```

**URL**
- When a Django application receives a web request, it uses the `URL` patterns to decide which view to pass the request to for handling 
- This is defined at `wisdompets/urls.py`

**Views**
- `Views` provide the **logic** or **control flow** portion of the project
- A `view` is a Python callable, e.g a function that takes an HTTP request as an argument and returns an HTTP response for the web server to return
- This is defined at `adoptions/views.py`

**Models**
- Create the data layer of Django app
- To perform queries against the database, each view can leverage Django models as needed
- This is defined at `adoptions/models.py`
- A Django model is a class with attributes that define the schema or underlying structure of a database table. 
- These classes will provide built-in methods for making queries on the associated tables. 
- Each view can leverage **templates**, which return HTML responses
- Method to store and retrieve pet information from our views

**Templates**
- Renders HTML pages 
- Defined at `adoptions/templates`

## Django Migrations
- Models define the structure of our database
- Migrations are responsible for creating the necessary scripts to change this structure through time as we update code to change our models.

## Use cases for migrations 
- When new model is created, a migration creates corresponding database table 
- When a field is added or removed from an existing model 
- When attributes of a field have changed 
- First migration created for a this Django app will create tables for the models that are defined (initial migrations)

Commands for working with migrations:
```
makemigrations - generates migration files. Reads current model's file and inspects the current state of the database and checks what changes need to be made 
showmigrations - checks which migrations exist for our app 
migrate - runs generated migrations 
```

Migrating our model (initial migrations):
```bash
python3 manage.py makemigrations
```
Which returns:
```bash
Migrations for 'adoptions':
  adoptions/migrations/0001_initial.py
    - Create model Vaccine
    - Create model Pet
```

Showing our migrations:
```bash
➜  wisdompets git:(master) ✗ python3 manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
adoptions
 [ ] 0001_initial
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
```
The empty square brackets indicates that these migrations have not yet been applied 

---

Applying our migrations:
```bash
➜  wisdompets git:(master) ✗ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, adoptions, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying adoptions.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Type in `python3 manage.py showmigrations` to verify migrations

---

## DB Browser for SQLite
Using Homebrew for macOS:
```bash
brew cask install db-browser-for-sqlite
```

Open application `applications/DB Browser`
Open database 

## Working with Django admin 
- Now that we have data to work with, we use Django `admin` to create an administrative interface for our project so that admin users can see and edit their data
- Django comes with a build-in admin interface to allow us to authenticate users, display and handle forms and validate input
- Also provides a convenient interface to manage model data
- Open `adoptions/admin.py` file
- Each model we want Django to represent in the admin interface needs to be registered
```python
from django.contrib import admin

# importing our pet models

from .models import Pet


# registering class with the admin to tell it which model it is associated with using admin module Register
# creating a class that inherits from admin and overriding methods
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
```

To set up the Django Admin:
```bash
➜  wisdompets git:(master) ✗ python3 manage.py createsuperuser
Username (leave blank to use 'anaistang'):  - click enter
Email address: - click enter
Password: - enter password
Password (again): - enter password
Superuser created successfully.
```

Run server again:
```bash
$ python3 manage.py runserver
```

Enter the following into the browser to enter as admin:
```bash
http://127.0.0.1:8000/admin/
```

The models should now be registered and visible on the browser.

In order to return string representation of name instead of pet object edit the `models.py` file:
```bash
class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # method tells django what the string representation should be for this model
    def __str__(self):
        return self.name
```
Refresh the browser

---

## Querying data with the Django ORM
- Now that our data model has been set up, we are ready to query that data using the Django ORM
- Open Python shell to open an interactive python shell with Django initialised
```bash
adoptions    db.sqlite3   manage.py    pet_data.csv wisdompets
➜  wisdompets git:(master) ✗ python3 manage.py shell
Python 3.8.3 (default, Jul  8 2020, 14:25:02) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

Importing our model to query data:
```bash
>>> from adoptions.models import Pet
```

Django models have an attribute called 'Objects' with several methods e.g `.all`, `.get`

**For example:**
```bash
>>> Pet.objects.all()
<QuerySet [<Pet: Pet object (1)>, <Pet: Pet object (2)>, <Pet: Pet object (3)>, <Pet: Pet object (4)>, <Pet: Pet object (5)>, <Pet: Pet object (6)>, <Pet: Pet object (7)>, <Pet: Pet object (8)>, <Pet: Pet object (9)>, <Pet: Pet object (10)>, <Pet: Pet object (11)>, <Pet: Pet object (12)>, <Pet: Pet object (13)>, <Pet: Pet object (14)>, <Pet: Pet object (15)>, <Pet: Pet object (16)>, <Pet: Pet object (17)>, <Pet: Pet object (18)>, <Pet: Pet object (19)>, <Pet: Pet object (20)>, '...(remaining elements truncated)...']>
```

Assigning the query to a variable:
```bash
>>> pets = Pet.objects.all()
```
Examining the first tuple using the variable:
```bash
>>> pet = pets[0]
```
Querying the pet instance with methods by using the name of column:
```bash
>>> pet.name
'Pepe'
>>> pet.age
0
>>> pet.description
'Six-month-o>>> pet.sex
'M'
>>> pet.id
1
>>> pet = Pet.objects.get(id=2)
>>> pet.name
'Scooter'
```
Examining relational data
```bash
>>> pet.vaccinations.all()
<QuerySet []> - Empty query set because this pet has no vaccinations
```
The object returned by `pet.vaccinations` has the same RM methods provided by the objects attribute. When a `foreign` key or `many-to-many` field is used on a model, its instances will have this type of object attached as the name of the field.
```bash
>>> pet = Pet.objects.get(id=7)
>>> pet.vaccinations.all()
<QuerySet [<Vaccine: Canine Parvo>, <Vaccine: Canine Distemper>, <Vaccine: Canine Rabies>, <Vaccine: Canine Leptospira>]>
>>> 
```

In the `models.py` file we overrode the `dunder str` method, the vaccines show their names in the output. 

---

## URL Patterns aka URL confs
- Earlier, we defined our models in `adoptions/models.py`
- Every page on the Internet needs its own URL. This way our application knows what it should show to a user who opens that URL.
- In Django, we use `URLconf` (url configuration) which is a set of patterns that Django will try to match the requested URL to find the correct view. 
- At high level they decide what **views** should handle the request
- Defined at `adoptions/views.py`
- When a user requests a page from the site, we want to handle this request to return a `html` template
- To handle these requests, when Django sees a request, it will route to the pet detail view, which in turn, will use the pet detail template (as an example).
- This is handled in the `urls.py` file

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail'),
]
```

- The variable `urlpatterns` is a list of calls to the path function. 
- When a request comes in, Django checks the path definition in order from top to bottom and it will look at the first argument for the pattern to match the path against.
- When path `matches`, that view is called
- If there is **not** a `match`, it will continue to the next path definition. 
- If the end of this list is reached, Django will return a 404 response

---

Path explanation:
```python
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail'),
```
- `Path converter` - a pattern string, matched literally such as `adoptions/`. Anything inside `<>` angled brackets is called the `capture` group. This can match different strings, and treats this as a variable. Before colon we use `int` to define converter type and this states we are expecting an integer number in the path. This will match `adoptions/` followed by a number but will not match if adoptions was followed by slash and then `letter` or `word`. After `:` colon, we have `pet_id` which defines how we want to name the resulting variable e.g `adoptions/1`
- `View` to use
- `Name` (optional; used to create links)

---

Testing out the routing:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>Home view</p>')

def pet_data(request, pet_id):
    return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')
```
Then running `➜  wisdompets git:(master) ✗ python3 manage.py runserver` again.

---
Rendering templates `html` files
```python
# urls.py

from django.shortcuts import render
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets,

    })

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })
```

---

## Building Django Templates 
- Django templates are HTML files that use Jinja syntax
- When a view calls the render function, it passes data into the templates, and template generates the HTML to show to the user
- The syntax for Django templates has **3** pieces:
```html
{{ variable }}

{% tag %}

{{ variable|filter }}
```

- `{{ variable }}` - a variable's value is shown when used inside of doubly curly braces
- `{% tag %}` - a template tag is enclosed in curly braces with percent signs. These are used for for loops, if statements, structural elements and control logic
- `{{ variable|filter }}` - variable can have a `|` pipe character to use a template filter.
- Template filters take a string as input and return a string as output (like pipe in shell scripting).
    - Mostly used to take a string and change some formatting e.g date timeout or forcing text into title or uppercase
    
```html
# In adoptions /templates/home.html

{% for pet in pets %}
    <li>{{ pet.name }}</li>
{% endfor %}

# Resulting HTML
<li>Scooter</li>
<li>Pepe</li>
...
```

Rendering a `<ul>` tag with a list of inner li tags, each with the name of a pet and a link to its detail page:
```html
<ul>
    {% for pet in pets %}
        <li>
            <a href="{% url 'pet_detail' pet.id %}">
               {{ pet.name|capfirst }}
            </a>
        </li>
    {% endfor %}
</ul>

# Resulting HTML
  <ul>    
    <li><a href="/adoptions/1">Pepe</a></li>
    <li><a href="/adoptions/2">Scooter</a></li>
  </ul> 
```
We use the built-in template filter `capfirst` to ensure that the ouput will have its first letter capitalised 

---

## Inheritance with base.html
- Using a `base.html` to extend on every page of the website 
- The `{% block content %}` and `{% endblock %}` tag will substitute the content block with everything in this block

```html
{% extends "base.html" %}
{% block content %}
<div>
    {% for pet in pets %}
    <div class="petname">
        <a href="{% url 'pet_detail' pet.id %}">
            <h3>{{ pet.name|capfirst }}</h3>
        </a>
        <p>{{ pet.species }}</p>
        {% if pet.breed %}
            <p>Breed: {{ pet.breed }}</p>
        {% endif %}
        <p class="hidden">{{ pet.description }}</p>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

---
## Using static files

```python
# wisdompets/settings.py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

Importing static files in `base.html` file:
```html
{% load static %}
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <title>Home - Wisdom Pet Medicine</title>
        <link rel="stylesheet" id="ample-style-css" href="{% static 'style.css' %}" type="text/css" media="all">
    </head>
...
<body>
    <div id="header-logo-image">
        <a href="/">
            <img src="{% static 'images/logo.png' %}" alt="Wisdom Pet Medicine">
        </a>
    </div>
...
    <script src="{% static 'main.js' %}"></script>
</body>
```