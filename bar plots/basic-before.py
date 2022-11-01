from pathlib import Path

import matplotlib.pyplot as plt


plt.style.use(Path(r'./common-style.mplstyle').absolute().as_uri())

fig, ax = plt.subplots()

ax.bar(x=['A', 'B', 'C', 'D'], height=[76, 263, -142, 84], zorder=2)

plt.savefig(Path(__file__).with_suffix('.png'))
