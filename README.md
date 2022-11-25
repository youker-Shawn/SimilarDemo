「Assignment」

Please design and implement a web API in Python to tell the population living within an area. The API should take a latitude, longitude and radius. We’d like to see both the Python code and a working API endpoint we can test.


「本地测试接口」
- `cd SimilarDemo/`
- `python -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py loaddata population.json`
- `python manage.py runserver`
- `curl "http://127.0.0.1:8000/demo/populations/?latitude=-89.111&longitude=123&radius=5000"`
```JSON
{"code": 200, "status": "success", "message": "", "result": {"population": 2808}}
```

接口文档以及调试可访问：http://127.0.0.1:8000/docs/index.html



「单元测试&覆盖率」
- `python manage.py test`
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.Locations: ('abc', 113.280637) (39.904989, 116.405285) .Error: could not convert string to float: 'abc'
Locations: 123 (39.904989, 116.405285) .Error: A single number has been passed to the Point constructor. This is probably a mistake, because constructing a Point with just a latitude seems senseless. If this is exactly what was meant, then pass the zero longitude explicitly to get rid of this error.
...Missing parameter:40 100 None
.Parameter out of range:100.0 100.0 900
Parameter out of range:40.0 -200.0 900
Parameter out of range:40.0 100.0 10
.Parameter type wrong:40.0 abc 900
.
----------------------------------------------------------------------
Ran 7 tests in 0.290s

OK
Destroying test database for alias 'default'...
```

- `coverage run --source "." manage.py test`
- `coverage report`
```
Name                              Stmts   Miss  Cover
-----------------------------------------------------
demo/__init__.py                      0      0   100%
demo/admin.py                         1      0   100%
demo/apps.py                          4      0   100%
demo/migrations/0001_initial.py       5      0   100%
demo/migrations/__init__.py           0      0   100%
demo/models.py                        7      0   100%
demo/tests.py                        62      0   100%
demo/urls.py                          3      0   100%
demo/utils.py                        11      0   100%
demo/views.py                        38      0   100%
manage.py                            12      2    83%
similardemo/__init__.py               0      0   100%
similardemo/asgi.py                   4      4     0%
similardemo/settings.py              20      0   100%
similardemo/urls.py                   3      0   100%
similardemo/utils.py                 11      2    82%
similardemo/wsgi.py                   4      4     0%
spider.py                            42     42     0%
-----------------------------------------------------
TOTAL                               227     54    76%
```