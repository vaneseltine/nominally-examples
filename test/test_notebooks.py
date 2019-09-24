import difflib
import subprocess
from pathlib import Path
import re

import pytest

ROOT_DIR = Path(__file__).parent.parent.resolve()
TEST_DIR = ROOT_DIR / "test"
NOTEBOOK_DIR = ROOT_DIR / "notebooks"


notebooks = list(NOTEBOOK_DIR.glob("*.ipynb"))


@pytest.mark.parametrize("infile", notebooks)
def test_against_canonical(infile, tmp_path):
    observed_out = Path(tmp_path.with_suffix(".ipynb"))
    canonical_out = TEST_DIR / f"{Path(infile).stem}_canonical.ipynb"

    cmd = [
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--output",
        str(observed_out),
        str(infile),
    ]

    nbconvert_result = subprocess.check_output(cmd)
    assert not nbconvert_result

    books = [clean_nb(b) for b in [observed_out, canonical_out]]
    for b in books:
        assert len(b) > 100
        print(len(b))

    diff = difflib.context_diff(*books)
    assert not list(diff)


def clean_nb(path):
    lines = Path(path).read_text().splitlines()
    return [l for l in lines if not is_junk(l)]


def is_junk(l):
    r = re.search(r"version|export|path|\.csv", l, flags=re.IGNORECASE)
    return bool(r)
