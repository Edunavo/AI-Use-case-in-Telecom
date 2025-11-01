#!/usr/bin/env python3
"""environment_setup.py
Teaching-tone script to help learners validate their Python 3.10 environment and installed libraries.
Run this script after activating the 'telecomAI' conda environment.

Example:
    conda activate telecomAI
    python environment_setup.py
"""

import sys

# List of packages to test (import names)
packages = [
    'pandas', 'numpy', 'matplotlib', 'seaborn', 'sklearn', 'xgboost', 'jupyter'
]

def check_python_version():
    major = sys.version_info.major
    minor = sys.version_info.minor
    print(f"Python version: {major}.{minor}")
    if not (major == 3 and minor == 10):
        print("Warning: This session targets Python 3.10. You can still continue but expect minor differences.")

def check_package(pkg_name):
    try:
        __import__(pkg_name)
        print(f"OK: import {pkg_name}")
    except Exception as e:
        print(f"MISSING: {pkg_name}  (import failed: {e})")

def main():
    print("\n=== Environment Check - Teaching Tone ===\n")
    check_python_version()
    print('\nChecking key Python packages (attempting imports)...\n')
    for p in packages:
        check_package(p)

    print('\nYou can install missing packages using: pip install -r requirements.txt\n')
    print('If you prefer conda, try: conda install pandas numpy matplotlib seaborn scikit-learn -y')

if __name__ == '__main__':
    main()
