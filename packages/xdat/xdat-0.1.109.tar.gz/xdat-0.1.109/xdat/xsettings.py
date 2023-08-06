import os
import tempfile

import matplotlib.colors as mcolors
from scriptine import path
from slugify import slugify

PROJECT_NAME = 'xdat'
PROJECT_NAME_PRETTY = 'xDat'
IGNORE_INDEX = True                 # useful when dataframes don't have a meaningful index
SANITY_CHECKS = False               # False, "warn", "error"
NAN_TEXTS = ['', '-', '.', '--', 'X', 'x', '#DIV/0!', '#VALUE!', 'NA', 'NAN', '0R', 'NR', 'NULL', 'None']
ACCU_METHOD = 'fsum'                # method to perform accurate math

FIGSIZE = (10, 10)

COL_DESC = dict()                   # column name --> column description
DEFAULT_COLORS = mcolors.TABLEAU_COLORS.keys()
HARD_CODED_COLORS = {
    '0': 'xkcd:sea blue',
    '0.0': 'xkcd:sea blue',
    '1': 'xkcd:crimson',
    '1.0': 'xkcd:crimson',
    'NaN': 'xkcd:gray',
    'None': 'xkcd:gray',
}

DEFAULT_MARKERS = 'o^sP*DXp<>v'
HARD_CODED_MARKERS = {
    '0': 'o',
    '0.0': 'o',
    '1': 'X',
    '1.0': 'X',
    'NaN': '^',
    'None': '^',
}

OUTPUT_PATH = path()
CACHE_PATH = path()
STATIC_CATH_PATH = None
XDAT_ROOT = path(__file__).parent.abspath()


def x_add_desc(from_name, to_name):
    if from_name == to_name:
        return

    COL_DESC[from_name] = to_name


def x_get_desc(key):
    for _ in range(100):
        if key not in COL_DESC:
            return key

        assert COL_DESC[key] != key
        key = COL_DESC[key]

    raise ValueError(f"Looks like some sort of endless loop for '{key}'")


def updated_config(project_name=None, verbose=True, static_cache_folder=None):
    global OUTPUT_PATH, CACHE_PATH, PROJECT_NAME, PROJECT_NAME_PRETTY, STATIC_CATH_PATH

    PROJECT_NAME_PRETTY = project_name or PROJECT_NAME_PRETTY
    assert PROJECT_NAME_PRETTY, "need to set PROJECT_NAME"

    PROJECT_NAME = slugify(PROJECT_NAME_PRETTY.lower(), separator='_')

    base_path = os.environ.get('DSXP_OUTPUT_PATH')
    if base_path is None:
        base_path = tempfile.gettempdir()
        base_path = path(base_path).joinpath('xdat')

    OUTPUT_PATH = path(base_path).joinpath(PROJECT_NAME)
    CACHE_PATH = OUTPUT_PATH.joinpath('cache')
    OUTPUT_PATH.ensure_dir()

    if static_cache_folder:
        STATIC_CATH_PATH = path(static_cache_folder)
        STATIC_CATH_PATH.ensure_dir()

    if verbose:
        print(f"OUTPUT_PATH set to '{OUTPUT_PATH}'")

    return OUTPUT_PATH


def get_default(default, override, possible_values=None):
    if override is None:
        if possible_values:
            assert default in possible_values, default

        return default

    if possible_values:
        assert override in possible_values, override

    return override


updated_config(verbose=False)
