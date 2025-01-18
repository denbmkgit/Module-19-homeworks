#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj19.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


'''
django-admin startproject dj19 
cd dj19
python manage.py startapp app1901
python manage.py migrate  
python manage.py makemigrations 

https://github.com/denbmkgit/Module-19-homeworks.git
--
python manage.py shell   
from task1.models import Buyer 
Buyer.objects.all()
Buyer.objects.create()
 Buyer.objects.create(name='Ilya', balance=1500.05, age=24)
 Buyer.objects.create(name='Terminator2000', balance=42.15, age=52)
 Buyer.objects.create(name='Terminator2000', balance=42.15, age=52)
Buyer.objects.filter(age=52)
Buyer.objects.filter(age=52).update(age=53)
Buyer.objects.filter(age=53).update(age=52)
Buyer.objects.filter(age=52).update(balance=10000)  - изменить баланс у терминатора на 10 000
Buyer.objects.count()                           -  покажет сколько всего объектов  
b=Buyer.objects.get(id=2)                          - переменной b - присвоили объект с id=2  после чего можно:
b.delete() =                          удалит этот объект (с id = 2)  

b.balance=10000    после этого Нужно сохранить
b,save()

b2=Buyer.objects.get(id=2) 
b3=Buyer.objects.get(id=3) 
---
from task1.models import Game 
Game.objects.all() 
Game.objects.create(title='Cyberpank 2077', cost=31, size=46.2, description='Game of the year', age_limited=1)
Game.objects.create(title='Mario', cost=5, size=0.5, description='Old Game', age_limited=0)
Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kiils Mark?', age_limited=1)
g=Game.objects.get(id=1) 
--

Game.objects.get(id=3).buyers.set((b1, b2)) 
Game.objects.get(id=2).buyers.set((b1, b2, b3)) 

если в квайрисет запросах сделал следующие:    >>> Game.objects.get(id=1).buyers.set((b1, b2)) 
>>> Game.objects.get(id=2).buyers.set((b1, b2, b3)) 
>>> Game.objects.get(id=3).buyers.set((b1, b2)) 
как "отвязать" игру с id=2 от b1?
Game.objects.get(id=2).buyers.remove(b1)  - удалили у игрока b1 - игру 2 (id=2, Mario)

Game.objects.get(id=1).buyers.set((b3))  - получаем ошибку 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\pytonProjectsForUnversity\dj_Pr_for_19_01\.venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1325, in set
    objs = tuple(objs)
           ^^^^^^^^^^^
TypeError: 'Buyer' object is not iterable

'''