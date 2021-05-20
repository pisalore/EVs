## EVs app
### A Django-Vue application developed for managing events.

#### Getting started
In order to get started, do the following steps:
1. **Clone the repo**:\
```git clone https://github.com/pisalore/evs```
2. **Virtualenv** \
Create and activate python virtual environment (be sure to use a >=3.6 python version):\
```cd evs```
```python -m venv .venv```\
   ```. .venv/bin/activate```
   

3. **Install requirements**:\
```pip install -r requirements.txt```
   
4. **Create a PostgreSQL DB** \
EVs uses Postgres, so create a db and change DATABASES dictionary in ```settings.py```, if needed.
   
6. **Migrate** \
Make migrations and run them: \
   ```python manage.py makemigrations```\
   ```python manage.py migrate```
   
5. **Start** \
Finally, start dev server: \
   ```python manage.py runserver```