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
    observed_out = tmp_path.with_suffix(".ipynb")
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

    assert not have_diffs(observed_out, canonical_out)


def have_diffs(*books):
    bookslines = (Path(path).read_text().lower().splitlines() for path in books)
    zippedlines = zip(*bookslines)
    for line1, line2 in zippedlines:
        if is_junk(line1) or is_junk(line2):
            continue
        assert line1 == line2


def is_junk(l):
    plat_specific = re.search(r"version|export|path|\.csv", l)
    nothing = not re.search(r"[a-z]", l)
    return plat_specific or nothing
