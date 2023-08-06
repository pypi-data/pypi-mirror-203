# LOTR SDK

https://liblab.com/take-home-project

# Quickstart

Install the package:

```
pip install pl-liblab-lotr-sdk
```

Use the package:

```python
from lotr import client

client = Client(key=<api_key>)
client.get_movies()
```


# Developing

To develop his library:
0. Install [Poetry](https://python-poetry.org/)
1. Copy `.env.sample` to `.env` then add your API key.
2. Create a virtual env `python -m venv .venv`
3. Activate venv `source .venv/bin/activate`
4. Install libraries `pip install -r requirements.txt`

Run tests:
```bash
./test.sh
```

# Release

```python
poetry config pypi-token pypi-YYYYYYYY
poetry publish
```
