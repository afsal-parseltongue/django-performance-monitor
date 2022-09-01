# Django Performance Monitor

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-performance-monitor) ![PyPI - License](https://img.shields.io/pypi/l/django-performance-monitor) ![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework)

 Django Performance monitor is simple django application for tracking the view which takes
 more time than a threshold value (By default 1.5 Seconds). Also using a Configuration in 
 admin we turn on or off this feature

## Installation

```bash
$ pip install django-performance-monitor
```

## Requirements
 - Python3.6+

## Usage

 - Add **django_performance_monitor** to the installed app in the settings file, 

```python
    INSTALLED_APPS = (
    # other apps
    "django_performance_monitor",
    )
```
 - Add **django_performance_monitor.middleware.LogRequestMiddleware** to the MIDDLEWARE in the settings,
 ```python
    MIDDLEWARE = [
    #other middlewares
    'django_performance_monitor.middleware.LogRequestMiddleware'
    ]
 
 ```
 - Set the **LOG_THRESHOLD** value above which we need to log the request in settings.py, By default its values is 1.5 Seconds
 ```python
    LOG_THRESHOLD = 2.05
 ```

 - Run **python manage.py migrate**, 
```bash
    $ python manage.py migrate 
```
 All the requests are logged to **Request logs** under the app **DJANGO_PERFORMANCE_MONITOR**
 To disable this logging go to **Config** under the app **DJANGO_PERFORMANCE_MONITOR**, if there is no config object
 create one with **Is active** un checked. If exist change to ** Is active ** to un checked.

## Communication
- If you **find a bug**, open an issue.
- If you **have a feature request**, open an issue.
- If you **want to contribute**, submit a pull request.

## Configuration
### `LOG_THRESHOLD`
the threshold is determined from:  

1. the `LOG_THRESHOLD` attribute on view class
2. the `LOG_THRESHOLD` from settings
3. the default 1.5

so if you know exactly some certain views will take a lot of time, you can set `LOG_THRESHOLD` to a bigger number on the view to reduce some redundant log.

### `LOG_EXCLUDE_PATTERNS`
the `LOG_EXCLUDE_PATTERNS` can exclude certain urls patterns, for example:

```python
LOG_EXCLUDE_PATTERNS = [
    re.compile("/admin/"),  # exclude all admin url
    re.compile("/slow_app/"),  # exclude slow django app
]
```

## Contribution
1. clone code

    ```bash
    git clone git@github.com:afsal-parseltongue/django-performance-monitor.git
    ```

2. install `django-performance-monitor` in editable/develop mode

    ```bash
    cd django-performance-monitor
    pip3 install -e ./
    ```

3. change the code

4. run the test

    ```bash
    cd example_project
    python3 manage.py test
    ```

## Author

Afsal Salim, afsal@parseltongue.co.in

## License

Django Performance Monitor is available under the MIT license. See the LICENSE file for more info.
