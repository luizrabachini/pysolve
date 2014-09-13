pysolve
=======

A [pyramid](http://docs.pylonsproject.org/en/latest/) web application to solve mathematical problems.

Current solutions available:

- Coin Determiner.

Live demo available in [pysolve.luizrabachini.com](http://pysolve.luizrabachini.com/)


Usage
-----

```bash
## Coin Determiner Library

# For a number input
cd pysolve/libs/coin_determiner/
python solver.py --n 250

# For a file input
cd pysolve/libs/coin_determiner/
python solver.py --i input_test.txt

# For benchmark
cd pysolve/libs/coin_determiner/
sh benchmark.sh

## Web application

# Inside a virtual environment
python setup.py develop
pserve development.ini
http://localhost:6543/
```