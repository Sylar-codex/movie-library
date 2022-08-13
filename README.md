## get started with movie-library

This was built using django, python and mySql.

## How it works?

Every user can register and sign up for each user that registers. A movie library is assigned to them,
where each can add movies they have watched and movies yet to be watched to the library

## run app

first clone app into your IDE

# cd into movie library

# go to settings

navigate to database dictionary and change it to this :

'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}

# make migration

# migrate

# run python manage.py

and now you can add movies to your movie library
