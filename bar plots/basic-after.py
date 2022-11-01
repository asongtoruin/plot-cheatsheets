from pathlib import Path

import matplotlib.pyplot as plt


plt.style.use(Path(r'./common-style.mplstyle').absolute().as_uri())

fig, ax = plt.subplots()

ax.bar(x=['A', 'B', 'C', 'D'], height=[76, 263, -142, 84], zorder=2)

ax.set_xlabel('Category')
ax.set_ylabel('Value')

ax.grid(axis='y', zorder=1)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(
    c=plt.rcParams['axes.edgecolor'], 
    lw=plt.rcParams['axes.linewidth']
)

ax.tick_params(length=0)


for patch in ax.patches:
    ax.annotate(
        patch.get_height(), 
        (patch.get_x() + patch.get_width()/2, patch.get_height()/2), 
        ha='center', va='center', c=plt.rcParams['axes.facecolor']
    )

ax.tick_params(axis='y', labelcolor=plt.rcParams['grid.color'])
ax.set_ylabel('Value', color=plt.rcParams['grid.color'])

ax.set_title('My Fun Bar Plot', loc='left')

plt.savefig(Path(__file__).with_suffix('.png'))
