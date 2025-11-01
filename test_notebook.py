# test_notebook.py - script version of the test notebook (teaching tone)
# Run this file with: python test_notebook.py

import sys
import platform
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

print('Python:', sys.version.split()[0])
print('Platform:', platform.platform())
print('pandas:', pd.__version__)
print('numpy:', np.__version__)
print('matplotlib:', matplotlib.__version__)
print('seaborn:', sns.__version__)

data = {
    'session_id': list(range(1,11)),
    'QCI': [1,2,1,5,9,9,6,2,1,5],
    'Throughput_Mbps': [8.2, 5.5, 12.1, 3.3, 20.0, 18.5, 7.0, 4.2, 9.9, 2.1],
    'Latency_ms': [30, 50, 20, 100, 15, 18, 40, 60, 25, 120]
}
df = pd.DataFrame(data)
print("\nDummy QoS data (first 5 rows):")
print(df.head())

# Quick plot (will open a window when run locally)
sns.set(style='whitegrid')
plt.figure(figsize=(8,4))
sns.scatterplot(data=df, x='Throughput_Mbps', y='Latency_ms', hue='QCI', palette='deep')
plt.title('Throughput vs Latency (dummy QoS data)')
plt.xlabel('Throughput (Mbps)')
plt.ylabel('Latency (ms)')
plt.tight_layout()
plt.show()

# Save CSV
df.to_csv('dummy_qos_data.csv', index=False)
print('Saved dummy_qos_data.csv in the current folder')
