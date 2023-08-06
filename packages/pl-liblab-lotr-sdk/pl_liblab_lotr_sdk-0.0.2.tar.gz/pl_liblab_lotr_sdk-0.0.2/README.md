# LOTR SDK

https://liblab.com/take-home-project

# Quickstart

Install the package:

```
pip install pl-liblab-lotr-sdk
```

Use the package:

```python
from pl_liblab_lotr_sdk.api import Client

client = Client(api_key="<api_key>")
for movie in client.get_movie():
    print(movie.name)
```


# Developing

To develop his library:

0. Install [Poetry](https://python-poetry.org/)
1. Copy `.env.sample` to `.env` then add your API key.
2. Create a virtual env `python -m venv .venv`
3. Activate venv `source .venv/bin/activate`
4. Install libraries `pip install -r requirements.txt`
5. Run Tests: `./test.sh`

# Release

Release packages to PyPI

```python
poetry config pypi-token pypi-YYYYYYYY
poetry publish
```
