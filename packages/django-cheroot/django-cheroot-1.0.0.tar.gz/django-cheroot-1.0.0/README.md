# Django Cheroot

Django Cheroot provides a bridge to use [Cheroot](https://github.com/cherrypy/cheroot) which is the high-performance, pure-Python HTTP server used by CherryPy.

_Alternative for other WSGI servers like Gunicorn, etc._

## Install

`pip install django-cheroot`

In `settings.py` add application to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
  ...
  'django_cheroot',
]
```

## Usage

Simplest usage with default settings is:

```shell
python manage.py cheroot
```

Default arguments

```shell
python manage.py cheroot
```

## Arguments

| Name                       | Short | Long          | Type | Default   |
| -------------------------- | ----- | ------------- | ---- | --------- |
| IP Address                 | -h    | --host        | str  | 127.0.0.1 |
| Port                       | -p    | --port        | int  | 8000      |
| Max Worker Threads         | -w    | --maxthreads  | int  | 40        |
| Min Threads in Thread Pool | -t    | --minthreads  | int  | 30        |
| Max Queued Connections     | -c    | --connections | int  | 20        |
