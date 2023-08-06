from cProfile import Profile
from io import StringIO
from pstats import Stats
from typing import Callable, Any


def profile(
        target: Callable, args: list = None, kwargs: dict = None,
        lines: int = 20, sort: str = 'tottime'
) -> tuple[Any, str]:
    if args is None or not isinstance(args, list):
        args = []

    if kwargs is None or not isinstance(kwargs, dict):
        kwargs = {}

    p = Profile()
    p.enable()

    output = target(*args, **kwargs)

    p.disable()

    s = StringIO()
    ps = Stats(p, stream=s).sort_stats(sort)
    ps.print_stats(lines)
    return output, s.getvalue()
