import subprocess
import sys
from pathlib import Path

here = Path(__file__).parent.resolve()

# Need a Python interpreter released before 2019 that has f-strings:
assert (3, 6) <= sys.version_info < (3, 8)

for test_case in sorted(here.glob("??-ncss??*.py")):
    process = subprocess.run(["python3", test_case], capture_output=True)
    error_message = process.stderr.decode("UTF-8").splitlines()[-1]
    print(f"{test_case.stem}: {error_message}")
