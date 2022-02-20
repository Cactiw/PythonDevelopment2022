import os
import subprocess
import sys
import venv
from tempfile import TemporaryDirectory

PIP_PATH = "bin/pip"
PYTHON_PATH = "bin/python3"


if __name__ == "__main__":
    with TemporaryDirectory() as tmp_dir:
        venv.create(tmp_dir, with_pip=True)
        subprocess.run([os.path.join(tmp_dir, PIP_PATH), 'install', 'pyfiglet'])
        subprocess.run([os.path.join(tmp_dir, PYTHON_PATH), '-m', 'figdate', *sys.argv[1:]])
