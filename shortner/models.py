from django.db import models
"""

Django web applications access and manage data through Python objects referred to as models. 
Models define the structure of stored data,including the field types and possibly also their maximum size, 
default values, selection list options, help text for documentation, label text for forms, etc.

"""
"""

A Django model is the built-in feature that Django uses to create tables, their fields, and various constraints. 
In short, Django Models is the SQL of Database one uses with Django. SQL (Structured Query Language) 
is complex and involves a lot of different queries for creating, deleting, updating or any other stuff related to database. 
Django models simplify the tasks and organize tables into models. Generally, each model maps to a single database table.
Moreover, we can use admin panel of Django to create, update, delete or retrieve fields of a model and various similar operations. Django models provide simplicity, consistency, version control and advanced metadata handling. Basics of a model include –

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API; see Making queries.

"""
"""
Whenever we create a Model, Delete a Model, or update anything in any of models.py of our project. 
We need to run two commands makemigrations and migrate. 
makemigrations basically generates the SQL commands for preinstalled apps (which can be viewed in installed apps in settings.py) and your newly created app’s model 
which you add in installed apps whereas migrate executes those SQL commands in the database file.
So when we run,

python3 manage.py makemigrations

SQL Query to create above Model as a Table is created and

python3 manage.py migrate
"""
# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)