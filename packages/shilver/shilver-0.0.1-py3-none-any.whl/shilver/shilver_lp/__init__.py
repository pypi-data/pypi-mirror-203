try:
    from importlib.resources import read_text
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    from importlib_resources import read_text

SOLVER_LP = read_text(__package__, "solver.lp")
VIZ_LP = read_text(__package__, "viz.lp")
