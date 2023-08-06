# Python3 - Profiler Wrapper

This package provides a wrapper function for easier usage of the built-in profiler.

It only uses builtin modules.

## Install

```bash
python3 -m pip install profiler-wrapper
```

See: [PyPI](https://pypi.org/project/profiler_wrapper/)

## Usage

```python3
from profiler_wrapper import profile

def function_to_profile(switch: bool, data: dict, msg: str):
    ...
    return {'data': 'test'}


profile(
    target=function_to_profile,
    args=[True],
    kwargs={
        'data': {'random': 'test'},
        'msg': 'Yesterday is gone.'
    },
    lines=3,
)

# (
#   {'data': 'test'},
#
#   "270011472 function calls (270011215 primitive calls) in 181.830 seconds
#    Ordered by: internal time
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    5.000    5.000    8.000    8.000 /tmp/test.py:95(function_to_profile)
#         2    2.000    2.000    3.000    3.000 /tmp/test.py:89(sub_function)
#         3    1.000    1.000    1.000    1.000 /tmp/test.py:89(sub_function2)
#    "
# )

```
