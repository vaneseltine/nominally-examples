import subprocess
import sys
from pathlib import Path
import re

import pytest

NBCONVERT = ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--output"]

ROOT_DIR = Path(__file__).parent.parent.resolve()
TEST_DIR = ROOT_DIR / "test"
NOTEBOOK_DIR = ROOT_DIR / "notebooks"
NOTEBOOKS = list(NOTEBOOK_DIR.glob("*.ipynb"))


def refresh_canonical():
    print("Refreshing notebooks...")
    for infile in NOTEBOOKS:
        canonical_out = TEST_DIR / f"{Path(infile).stem}_canonical.ipynb"
        print(" IN:", infile)
        print("OUT:", canonical_out)
        cmd = NBCONVERT + [str(canonical_out), str(infile)]
        result = subprocess.check_output(cmd)
        if result:
            print(result)
    print("Refresh complete.")


@pytest.mark.parametrize("infile", NOTEBOOKS)
def test_against_canonical(infile, tmp_path):
    observed_out = tmp_path.with_suffix(".ipynb")
    canonical_out = TEST_DIR / f"{Path(infile).stem}_canonical.ipynb"

    cmd = NBCONVERT + [str(observed_out), str(infile)]
    nbconvert_result = subprocess.check_output(cmd)
    assert not nbconvert_result

    assert not have_diffs(observed_out, canonical_out)


def have_diffs(*books):
    bookslines = (Path(path).read_text().splitlines() for path in books)
    zippedlines = zip(*bookslines)
    for i, lines in enumerate(zippedlines):
        line1, line2 = lines
        if is_junk(line1) or is_junk(line2):
            continue
        assert line1 == line2


def is_junk(l):
    plat_specific = re.search(r"version|export|path|\.csv", l, flags=re.IGNORECASE)
    nothing = not re.search(r"[a-z]", l, flags=re.IGNORECASE)
    return plat_specific or nothing


if __name__ == "__main__":
    if "--refresh" in sys.argv:
        refresh_canonical()
    else:
        print("Run with --refresh to refresh canonical notebooks.")
