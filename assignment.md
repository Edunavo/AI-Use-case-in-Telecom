# Assignment - Session 1 (Teaching Tone)

**Objective:** Practice setting up the environment and running the test notebook.

**Tasks:**

1. Create the conda environment (Python 3.10):
```bash
conda create -n telecomAI python=3.10 -y
conda activate telecomAI
pip install -r requirements.txt
```

2. Run the environment check script and note any missing packages:
```bash
python environment_setup.py
```

3. Launch Jupyter and open `test_notebook.ipynb`. Run all cells (Shift+Enter) and inspect the plot.

4. Verify that `dummy_qos_data.csv` is created. Open it with a text editor or Excel to see the rows.

5. (Git) Initialize a git repo, commit these files and push to your GitHub (or your fork):
```bash
git init
git add .
git commit -m "Session1: environment setup lab"
# create repo on GitHub and push as instructed on the website or using gh CLI
```

**Bonus (optional):** Add a new column to the dummy dataset (e.g., 'PacketLoss_pct') and plot it vs QCI.

Good luck! If you get stuck, read the comments in `environment_setup.py` or re-open this README.md for quick tips.
