# Python Fibonacci Series Evaluator using RESTful API(Flask)

## Definition of the task

Write a RESTful service in Python that features the following endpoints. Try to apply general python best
practices where applicable (i.e. imagine this will be a larger application later).

1. GET /fib/<number>: Given a number, find all combinations of fibonacci number that add up to
that particular number.

Remember, the fibonacci sequence is being calculated as follows: fn = f(n−1) +f(n−2) ∀n > 2; with the first
two numbers being f1 = f2 = 1 are excluded from the sequence, hence your f1 = 2.

Example for »/fib/11« the response will be a list of all possible combinations with a status code 200.
[ [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [8, 3] ]

2. GET/health: Return health information about the service. Definition of »healt check« is up to you.
You can use any framework you like. We recommend using Flask.

What is important to us:
- code efficiency and speed
- code structure and cleanliness (a solid bet is to follow the S.O.L.I.D principles ;)
- code testability
- correctness of the result
- bonus points achieved

## Solution

### Folder structure

```shellcript
dir python_flask_fibonacci
docs/
fibonacci/
flask_fibonaaci.py
```

where
- docs/ is the folder setup to generate documentation of the source code using python package sphinx
- fibonacci/ is the placeholder which implements the requirements of the task as submodule and it also includes the tests
- flask_fibonaaci.py is the main python script which will be used to created the end points using flask framework.

### How to run the script

> Please use two terminals simultaneously

1. In terminal 1

```console
cd python_flask_fibonacci
python flask_fibonaaci.py
```

1.1 Expected results

```console
 * Serving Flask app "flask_fibonaaci" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 132-959-924
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

2. In terminal 2

```console
cd python_flask_fibonacci
curl http://127.0.0.1:5000/fib/your_number
```

2.1

> Here the integer 11 has been taken as an example.

```console
curl http://127.0.0.1:5000/fib/11
{
  "result": [
    [
      3,
      8
    ],
    [
      3,
      3,
      5
    ],
    [
      2,
      2,
      2,
      5
    ],
    [
      2,
      3,
      3,
      3
    ],
    [
      2,
      2,
      2,
      2,
      3
    ]
  ]
}
```

## About documents

> install supporting packages and perform steps as shown below in order to generate the documentation out of source code.

```console
pip install sphinx
pip install sphinx_rtd_theme
pip install sphinx-argparse
cd python_flask_fibonacci
sphinx-build -b html docs build-docs
```


1. Go to build-docs\index.html