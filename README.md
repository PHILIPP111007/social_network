# social_network

Hi! This is my second Django project. This time I wrote a mini-social network!

## What supports this app
1. This app supports accounts and adding friends. Each user has the opportunity to maintain their own blog, subscribe to other people and see their blogs.

2. And recently it became possible to correspond between friends! You can delete your messages. If you delete an entire dialog, it will remain in the database until your friend deletes it. If he hasn't deleted the dialog yet, the correspondence can be restored if you recreate the chat with him.

3. If you embed a share link to a YouTube video in a post, the post automatically embeds the YouTube `iframe` of that video. This function can be disabled without any problems if you tick the `low power mode button` in the settings.

4. Meet the dark theme!

5. The app supports lazy loading of posts!


\
To run the app use ```hypercorn social_network.asgi:application``` if you are using hypercorn, or ```python manage.py runserver``` if daphne

Open demo.mp4 to see user experience

\
Have fun and if you want please leave feedback!

## Technologies used:

### 1) django-channels
-- Django channels documentation https://channels.readthedocs.io/en/stable/index.html

### 2) daphne (or hypercorn)
-- ASGI and WSGI web server

### 3) AJAX

### 4) See requirements.txt for more information