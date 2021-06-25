## EVs app

## A Django-Vue application developed for managing events.

This application has been developed for the Human Computer Interaction course at University of Study of Florence, Italy.
The main idea is to develop a webapp, a social network, for events management, both for events organizers and final
customers. The following tools and technologies have been used for EVs development:

- Design: [Miro](https://miro.com/) and [Figma](https://www.figma.com/)
- Backend development: PostgreSQL for database,  [Django](https://www.djangoproject.com/)
  and [Django Rest Framework](https://www.django-rest-framework.org/) for backend and REST API
  implementation, [AWS S3](https://aws.amazon.com/) for file storage (essentially images).

- Frontend: [Vue](https://vuejs.org/) with Node and npm, and all the Vue ecosystem (Vue router, vuex, Vue CLI, Vue UI)
  for a better development experience.

- Continuous Integration: GitHub Actions for unit testing using [Tox](https://tox.readthedocs.io/en/latest/).

- Deployment: [Heroku](https://dashboard.heroku.com/).

The app is live on https://evs-hci.herokuapp.com/.

## Getting started

In order to get started and simply configure all the environment, do the following steps:

### Backend

1. **Clone the repo**:\
   ```git clone https://github.com/pisalore/evs```


2. **Virtualenv** \
   Create and activate python virtual environment (be sure to use a >=3.9 python version):\
   ```cd evs```
   ```python -m venv .venv```\
   ```. .venv/bin/activate```


3. **Install requirements**:\
   ```pip install -r requirements.txt```


4. **Create a PostgreSQL DB** \
   EVs uses Postgres, so create a postgres DB. Please, check the [Postgres documentation](https://www.postgresql.org/)
   for further details.


5. **Create an .env file**\
   This file is important since it contains configurations for database, AWS S3, development and email. This file will
   be placed at project root and will contain the following, using this syntax **<YOUR_ENV>=value**
    - ```SECRET KEY``` - the Django secret key
    - ```DEBUG``` - the Debug setting. If True, you will work with the python server and the Vue server, if False, you
      will be able to se a "production" app, after frontend build simply hitting  ```python manage.py runserver```
    - ```EMAIL_USER``` - a valid gmail email
    - ```EMAIL_PASSWORD``` - the gmail password. Email is used for some functionality inside the app, such as a "Contact
      Us" form compilation for customers requests.
    - ```DB_STRING```=<DB_TYPE>://<YOUR_USERNAME>:<YOUR_PASSWORD>@<HOST>:<PORT>/<DB_NAME>, for example: **postgres:
      //username:password@127.0.0.1:5432**. This variable is crucial for db connection.

    - ```USE_S3``` - if True, you will upload you file to your S3 bucket (which environment variables are in the
      following) if False all your uploads will be stored in a locally hosted ```\mediafiles``` folder, at project root.
    - ```AWS_ACCESS_KEY_ID```
    - ```AWS_SECRET_ACCESS_KEY```
    - ```AWS_STORAGE_BUCKET_NAME```
    - ```AWS_REGION```\
      All these AWS env variables are related to your bucket and AWS configurations. Please, check the AWS docs for more
      information. Note that you can use this app also without AWS.


6. **Migrate** \
   Make migrations and run them: \
   ```python manage.py makemigrations```\
   ```python manage.py migrate```


7. **Create a Django superuser**\
   This could be useful\
   ``` python manage.py createsuperuser```

At this point, the backend is set up!

### Frontend

We assume that you have a working Node and npm installation. We recommend the use of ```nvm``` for a better projects
environment management. Check the [nvm project](https://github.com/nvm-sh/nvm) on GitHub.\
EVs has been developed an tested using **Node 14.17.0** and **npm 6.14.13**

1. **Install dependencies** \
   Navigate to the ```frontend``` directory from project root and install the node dependencies:\
   ```cd frontend```\
   ```npm install```


2. **Create an .env file for frontend**\
   This file use the same syntax of point 5 in backend section but lives in the ```/frontend``` directory: it is another
   .env file. It contains a ```VUE_APP_GOOGLE_API_KEY``` variable: in fact, this project uses a Google api key for maps
   purposes. You can decide to dos not use it, but you will not see the event map in event detail page.


3. **Serve**\
   Serve the frontend from frontend dir in order to obtain a ```webpack-stats.json```. This auto generated file is used
   by```django-webpack-loader``` to integrate Vue app and Django app.

That's all, the frontend is set up!

### Run tests

Automatic tests are a fundamental feature while developing: they can check your work and verify if new features are
compatible with the old ones. For this repository, tests are run at every commit and PR, with CI, using tox. Obviously,
they can be run locally, simply hitting the following command:\
```tox -e py```

### Run the application

Now everything is ready to run the EVs webapp. You can use one of the following settings:

1. **Development**
    - Set ```DEBUG``` to True inside your ```.env``` file in project root
    - Run ```python manage.py runserver``` inside project root
    - Run ``` cd frontend && npm run serve``` inside project root

   Now the app is run at http://127.0.0.1:8000/ with both Django and Vue live reload.

2. **Test for production**
    - Set ```DEBUG``` to False inside your ```.env``` file in project root
    - Run ``` cd frontend && npm run serve``` inside project root
    - Run ```python manage.py runserver``` inside project root

   App is run at http://127.0.0.1:8000/ as in development mode but is displayed as in production, using bundles
   generated by webpack during the build for production.

### Deployment

Finally, the deployment phase. Again, check the webapp page at https://evs-hci.herokuapp.com/.

The deployment has been executed following the Heroku documentation, introducing two different **buildpacks** for the
two different core application inside this project:

- ```heroku/python```
- ```heroku/nodejs```

Heroku is really smart and with very few configurations it works like a charm: it detects python Django app and
automatically installs the requirements listed in ```requirements.txt```, then detects node app from
the ```package.json``` file in root project and set up the frontend exactly has we have done before in this guide; then,
in release phase declared in ```Procfile``` runs collectstatic and migrations. Finally, the app is deployed!\
If you want to work with heroku it is crucial to set up the database (it is really straightforward), maybe starting from
a local one, and all the environment variables we have seen before. These first operations can be done using the Heroku
CLI. Please, refer to the [Heroku docs](https://devcenter.heroku.com/articles/creating-apps).

Cheers!