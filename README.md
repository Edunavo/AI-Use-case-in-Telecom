# Session 1: AI/ML Environment Setup for Telecom

**Objective:** Learn how to set up a reproducible AI/ML environment and understand telecom-specific data challenges.

**What you'll get in this folder (teaching tone):**
- A short, friendly slide deck (title slide only) you can use to start the session.
- A step-by-step Python script to validate your environment (`environment_setup.py`).
- A guided Jupyter notebook (`test_notebook.ipynb`) that loads a tiny dummy QoS dataset and creates a simple plot.
- A ready-to-run Python script version of the notebook (`test_notebook.py`).
- A short assignment (`assignment.md`) to reinforce the lab tasks.
- `requirements.txt` listing the Python dependencies for the session (Python 3.10 friendly).

---

## Before you start (prerequisites)
- Install **Anaconda** or **Miniconda** (recommended).
- Create the teaching environment:
```bash
conda create -n telecomAI python=3.10 -y
conda activate telecomAI
pip install -r requirements.txt
```

## How to run
1. Open a terminal and activate the environment:
```bash
conda activate telecomAI
```
2. Run the environment check script (it will print versions and quick checks):
```bash
python environment_setup.py
```
3. Start Jupyter Notebook:
```bash
jupyter notebook
```
4. Open `test_notebook.ipynb` and follow the **Getting Started** cell to run cells (Shift+Enter).

## Git & GitHub (quick steps for the lab)
1. Initialize a repo:
```bash
git init
git add .
git commit -m "Session 1: environment setup materials"
```
2. Create a new repository on GitHub and follow instructions to push (or use `gh` CLI).

---

If you get stuck, check the comments in `environment_setup.py` or open an issue in your learning repo. Have fun — this first session is all about making your environment reliable and repeatable!
