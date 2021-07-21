# Benchmarking

This repo is hosting a small benchmark with examples on how to use the tool as final user or backend developer

In the folder examples you'll find a set of main files that execute simple tests


## Run tests

Create python ennvironment, activate and install requirements:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

IMPORTANT NOTE: By default, famapy version is production version, if you want test with other version, you need install manually.

For run test:

```
pytest -sv
```

ó

```
make test
```


## Run linter

For run linter:

```
prospector
```

ó

```
make lint
```
