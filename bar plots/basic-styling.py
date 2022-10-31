from pathlib import Path

import matplotlib.pyplot as plt


plt.style.use(Path(r'./common-style.mplstyle').absolute().as_uri())


def get_arrow(ha, va, side='above'):
    pos_lookup = dict(
        left=0, right=1, bottom=0, top=1, center=0.5, middle=0.5
    )

    if side == 'above':
        sign = ''
    elif side == 'below':
        sign = '-'

    return dict(
        ha=ha, va=va, arrowprops=dict(
            arrowstyle='-|>', connectionstyle=f'arc3, rad={sign}0.2',
            facecolor=plt.rcParams['patch.edgecolor'], ls='--',
            relpos=(pos_lookup[ha], pos_lookup[va])
        )
    )


ANNOTATION_PROPS = dict(
    textcoords='offset pixels', family='monospace', 
    bbox=dict(fc=plt.rcParams['axes.facecolor'], pad=5, ls='--')
)


fig, axes = plt.subplots(
    figsize=(13, 13), nrows=3, ncols=3, 
    gridspec_kw=dict(hspace=0.7, wspace=0.7, bottom=0.15, top=0.80)
)

flat_axes = axes.flatten()

for i, ax in enumerate(flat_axes):
    ax.annotate(
        i+1, 
        xy=(1, 1), xycoords='axes fraction', 
        xytext=(-15, -15), textcoords='offset pixels',
        ha='right', va='top', size='large', weight='bold',
        color='white',  bbox=dict(boxstyle='circle', fc='black', pad=0.4)
    )

    ax.bar(x=['A', 'B', 'C', 'D'], height=[76, 263, -142, 84], zorder=2)

flat_axes[0].annotate(
    "fig, ax = plt.subplots()\nax.bar(\n    x=['A', 'B', 'C', 'D'],\n    height=[142, 263, -76, 84],\n    zorder=2\n)",
    xy=(0, 1), xycoords='axes fraction', xytext=(10, 15),
    ha='left', va='bottom',
    **ANNOTATION_PROPS
)


for ax in flat_axes[1:]:
    # Add axis labels
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')


flat_axes[1].annotate(
    "ax.set_xlabel('Category')", 
    xy=(0.5, -0.22), xycoords='axes fraction', 
    xytext=(-10, -40), 
    **get_arrow(ha='left', va='top', side='below'),
    **ANNOTATION_PROPS
)

flat_axes[1].annotate(
    "ax.set_ylabel('Value')", 
    xy=(-0.22, 0.57), xycoords='axes fraction', 
    xytext=(20, 120), 
    **get_arrow(ha='left', va='top'),
    **ANNOTATION_PROPS
)

for ax in flat_axes[2:]:
    # Grid
    ax.grid(axis='y', zorder=1)

flat_axes[2].annotate(
    "ax.grid(axis='y', zorder=1)", xy=(0, 200),
    xytext=(10, 60), 
    **get_arrow(ha='left', va='bottom'),
    **ANNOTATION_PROPS
)

for ax in flat_axes[3:]:
    for spine in ax.spines.values():
        spine.set_visible(False)

flat_axes[3].annotate(
    "for spine in ax.spines.values():\n    spine.set_visible(False)", 
    xy=(0, 0), xycoords='axes fraction',
    xytext=(0, -70), 
    **get_arrow(ha='left', va='top', side='below'),
    **ANNOTATION_PROPS
)

for ax in flat_axes[4:]:
    # y=0
    ax.axhline(
        c=plt.rcParams['axes.edgecolor'], 
        lw=plt.rcParams['axes.linewidth']
    )

flat_axes[4].annotate(
    "ax.axhline(\n    c=plt.rcParams['axes.edgecolor'],\n    lw=plt.rcParams['axes.linewidth']\n)", 
    xy=(0, 0), xycoords=('axes fraction', 'data'),
    xytext=(0, -125), 
    **get_arrow(ha='left', va='top', side='below'),
    **ANNOTATION_PROPS
)

for ax in flat_axes[5:]:
    # tick_length
    ax.tick_params(length=0)

flat_axes[5].annotate(
    "ax.tick_params(length=0)", xy=(0, 200), xycoords=('axes fraction', 'data'),
    xytext=(20, 60), 
    **get_arrow(ha='left', va='center', side='above'), 
    **ANNOTATION_PROPS
)

for ax in flat_axes[6:]:
    # bar labels
    for patch in ax.patches:
        ax.annotate(
            patch.get_height(), 
            (patch.get_x() + patch.get_width()/2, patch.get_height()/2), 
            ha='center', va='center', c=plt.rcParams['axes.facecolor']
        )

flat_axes[6].annotate(
    "for patch in ax.patches:\n    ax.annotate(\n        patch.get_height(), \n        (patch.get_x() + patch.get_width()/2, patch.get_height()/2), \n        ha='center', va='center', c=plt.rcParams['axes.facecolor']\n    )", 
    xy=(-0.1, 40), xycoords='data',
    xytext=(-160, -170), 
    **get_arrow(ha='left', va='top', side='below'),
    **ANNOTATION_PROPS
)

for ax in flat_axes[7:]:
    # y tick label colour
    ax.tick_params(axis='y', labelcolor=plt.rcParams['grid.color'])
    ax.set_ylabel('Value', color=plt.rcParams['grid.color'])

flat_axes[7].annotate(
    "ax.tick_params(axis='y', labelcolor=plt.rcParams['grid.color'])\nax.set_ylabel('Value', color=plt.rcParams['grid.color'])", 
    xy=(-0.1, 0.1), xycoords='axes fraction',
    xytext=(60, -80), 
    **get_arrow(ha='left', va='top', side='below'),
    **ANNOTATION_PROPS
)

for ax in flat_axes[8:]:
    ax.set_title('My Fun Bar Plot', loc='left')

flat_axes[8].annotate(
    "ax.set_title('My Fun Bar Plot', loc='left)", 
    xy=(0, 1.1), xycoords='axes fraction',
    xytext=(20, 30), 
    **get_arrow(ha='left', va='bottom'),
    **ANNOTATION_PROPS
)

fig.suptitle(
    'How to...\nstyle a simple bar plot in matplotlib', size=35, weight='bold',
)

plt.savefig(Path(__file__).with_suffix('.png'))
