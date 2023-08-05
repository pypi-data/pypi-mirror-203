# Optimyzer API Client

This is the Python API Client for Optimyzer. Use it to conveniently run optimizations from Python.

To get access to the API you will need an Optimyzer account.

If you have any kind of issue or suggestion, please
drop us a line: [info@gauss-ml.com](mailto:info@gauss-ml.com).

## Getting started

Installing the `Optimyzer API Client` is very easy, just run `pip install optimyzer_api_client`
in your favorite Python environment and you're done. If you like it, you might want to add
`optimyzer_api_client` to your project's dependencies.

## Optimyzer Usage

`Optimyzer` has been built to be included in any kind of workflow as easily as possible. 

First you have to import it:

```python
from optimyzer_api_client import Optimyzer
```

Then you need to create an instance using your `Optimyzer` username and password.

```python
oac = Optimyzer(username="your@email.com", password="AVery$ecureP@ssw0rd!")
```

You can also use a credentials file.

```python
oac = Optimyzer.from_credentials("/path/to/credentials_file.json")
```

Once you have an `Optimyzer API Client` instance, you can start creating machines, optimizations,
and runing them.
Check out the `notebooks` on this repository for examples on how to get started.
