# social_network

Hi! This is my second Django project. This time I wrote a mini-social network.

## What supports this app
1. This app supports accounts and adding friends. Each user has the opportunity to maintain their own blog, subscribe to other people and see their blogs.

2. And recently it became possible to correspond between friends!

3. If you embed a share link to a YouTube video in a post, the post automatically embeds the YouTube `iframe` of that video. This function can be disabled without any problems if you tick the `low power mode button` in the settings.

Have fun and if you want please leave feedback!


## Photos

<img src="./images_for_README/image_1.png" alt="Alt text" title="Optional title">
<img src="./images_for_README/image_2.png" alt="Alt text" title="Optional title">
<img src="./images_for_README/image_3.png" alt="Alt text" title="Optional title">
<img src="./images_for_README/image_4.png" alt="Alt text" title="Optional title">
<img src="./images_for_README/image_5.png" alt="Alt text" title="Optional title">
<img src="./images_for_README/image_6.png" alt="Alt text" title="Optional title">
<img src="./images_for_README/image_7.png" alt="Alt text" title="Optional title">
<img src="./images_for_README/image_8.png" alt="Alt text" title="Optional title">



## Technologies used:

### 1) channels
-- Django channels documentation https://channels.readthedocs.io/en/stable/index.html
```console
pip install channels
```

### 2) daphne
-- ASGI server \
-- Twisted[tls,http2] - used to support http2
```console
python -m pip install daphne
pip install -U 'Twisted[tls,http2]'
```
-- when writing literate application code, calling `python manage.py runserver` daphne starts automatically \
-- if it doesn't run, then call `daphne {app_name}.asgi:application` or `daphne -b 0.0.0.0 -p 8001 {app_name}.asgi:application`

### 2) redis
-- server too \
-- https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/
```console
brew install redis
```
```console
pip install channels_redis
```
-- run server (run without .venv)
```console
redis-server
```

### 3) selenium
-- for tests.py
```console
python -m pip install selenium
```
-- run tests
```console
python manage.py test chat.tests
```
