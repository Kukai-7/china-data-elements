import json, os, glob, textwrap, numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Polygon as MPoly
from matplotlib.lines import Line2D
from shapely.geometry import shape, box

for f in glob.glob('fonts/*.otf') + ['/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc']:
    if os.path.exists(f): fm.fontManager.addfont(f)
_n = {f.name for f in fm.fontManager.ttflist}
FONT = next((n for n in ('Noto Sans CJK SC', 'Noto Sans CJK JP') if n in _n), 'DejaVu Sans')
plt.rcParams.update({'font.family': FONT, 'font.size': 10, 'axes.edgecolor': '#BBBBBB', 'axes.linewidth': .6,
                     'xtick.color': '#666666', 'ytick.color': '#666666', 'axes.labelcolor': '#444444', 'text.color': '#1F1F1F',
                     'savefig.dpi': 200})
INK, MID, LIGHT, LAND, PAPER = '#1F1F1F', '#8A8A8A', '#C9C6BF', '#ECE9E3', '#FFFFFF'
RED, RED_SOFT, BLUE, BLUE_SOFT = '#B33A2B', '#E3B5AE', '#2F4B7C', '#B9C4D6'
os.makedirs('out/assets', exist_ok=True)

pol = pd.read_parquet('out/data/policy_timeline.parquet')
ind = pd.read_parquet('out/data/indicators.parquet')
comp = pd.read_parquet('out/data/competition.parquet')
pl = pd.read_parquet('out/data/places.parquet')
KIND = {'Policy': (RED, 'o'), 'Law': (INK, 's'), 'Institution': (RED, 'D'), 'Accounting': (BLUE, 'D'), 'Exchange': (BLUE, 'o'), 'Competition': (MID, '^')}
v = lambda k, y: ind[(ind.indicator == k) & (ind.year == y)].value.iloc[0]

def title(fig, t, s, y=.95):
    fig.text(.05, y, t, fontsize=15, weight='bold')
    fig.text(.05, y - .045, s, fontsize=9, color='#555555')
def clean(ax, left=True):
    for s_ in ('top', 'right'): ax.spines[s_].set_visible(False)
    if not left: ax.spines['left'].set_visible(False)
    ax.tick_params(length=0)

# ------------------------------------------------------------------ 1. from strategy to market: the timeline
fig, ax = plt.subplots(figsize=(13, 8))
d = pol.sort_values('date').reset_index(drop=True)
x = d.date.dt.year + (d.date.dt.dayofyear - 1) / 366
for i, r in d.iterrows():
    col, mk = KIND[r.kind]
    ax.hlines(i, 2014.6, x[i], color='#F0F0F0', lw=.8, zorder=1)
    ax.scatter(x[i], i, color=col, marker=mk, s=60, zorder=3)
    ax.text(x[i] + .12, i, f"{r.date:%b %Y}  {r.event_zh}", va='center', fontsize=7.6, color=MID)
ax.set_yticks(range(len(d))); ax.set_yticklabels(d.event, fontsize=8.2); ax.set_ylim(len(d) - .4, -1.2)
ax.axvspan(2024, 2027, color=LAND, lw=0, zorder=0); ax.text(2024.05, -.9, '"Data Element ×" plan, 2024 to 2026', fontsize=7.5, color=MID, va='bottom')
ax.set_xlim(2014.6, 2033.5); ax.set_xticks(range(2015, 2027)); clean(ax, left=False); ax.xaxis.grid(color='#F2F2F2', lw=.6); ax.set_axisbelow(True)
fig.legend(handles=[Line2D([], [], marker=m, ls='', color=c, label=k, ms=7) for k, (c, m) in KIND.items()], loc='upper left', bbox_to_anchor=(.045, .9), ncol=6, frameon=False, fontsize=8.5)
title(fig, 'From big data to data as a factor of production', 'The main laws, policies, institutions and markets for data in China, 2015 to 2026.', y=.965)
fig.text(.05, .02, 'Curated for this dataset from official releases (State Council, NPC, Ministry of Finance, National Data Administration, CAC) and press reports. '
         'Date of adoption, publication or opening.', fontsize=7, color=MID)
plt.subplots_adjust(left=.36, right=.98, top=.85, bottom=.07)
fig.savefig('out/assets/policy_timeline.png', facecolor=PAPER); plt.close(fig)

# ------------------------------------------------------------------ 2. the numbers: production, AI data, market, balance sheets
fig, axs = plt.subplots(1, 4, figsize=(14, 5.2), gridspec_kw=dict(width_ratios=[1.1, .8, 1, 1.1], wspace=.55))
a = axs[0]; yrs = [2023, 2024, 2025]; vals = [v('data_production', y) for y in yrs]
a.bar(yrs, vals, color=[LIGHT, LIGHT, RED], width=.6)
for y, val in zip(yrs, vals): a.text(y, val + 1, f'{val:.1f}', ha='center', fontsize=9)
for y, g in [(2024, 25.0), (2025, 27.28)]: a.text(y, 3, f'+{g:.0f}%', ha='center', fontsize=8, color=PAPER, weight='bold')
a.set_xticks(yrs); a.set_ylim(0, 62); a.set_yticks([]); clean(a, left=False)
a.set_title('Data produced in China\n(zettabytes a year)', fontsize=9.5, loc='left')
a = axs[1]; tot, inf = v('ai_data_training_and_inference', 2025), v('ai_data_inference', 2025)
a.bar([0], [tot - inf], color=BLUE, width=.55, label='training'); a.bar([0], [inf], bottom=[tot - inf], color=RED, width=.55, label='inference')
a.text(0, (tot - inf) / 2, f'training\n{tot - inf:.1f}', ha='center', va='center', color=PAPER, fontsize=8.5)
a.text(0, tot - inf + inf / 2, f'inference\n{inf:.1f}', ha='center', va='center', color=PAPER, fontsize=8.5)
a.set_xlim(-.6, .6); a.set_xticks([]); a.set_yticks([]); clean(a, left=False)
a.set_title('Data used for AI, 2025\n(exabytes)', fontsize=9.5, loc='left')
a = axs[2]; m, e = v('data_market_trading', 2024), v('data_exchange_trading', 2024)
a.barh([1, 0], [m, e], color=[INK, BLUE], height=.55)
a.text(m, 1, f' {m / 10:,.0f} bn+', va='center', fontsize=9); a.text(e, 0, f' {e / 10:,.0f} bn+', va='center', fontsize=9)
a.set_yticks([1, 0]); a.set_yticklabels(['All data\ntrading', 'On data\nexchanges'], fontsize=8.5); a.set_xlim(0, 2300); a.set_xticks([]); clean(a, left=False)
a.set_title('Data trading, 2024\n(yuan)', fontsize=9.5, loc='left')
a = axs[3]; parts = [('Intangible\nassets', v('data_assets_booked_intangible', 2025), BLUE), ('Development\nspending', v('data_assets_booked_development', 2025), MID),
                     ('Inventory', v('data_assets_booked_inventory', 2025), LIGHT)]
left = 0
for nm, val, c in parts:
    a.barh(0, val, left=left, color=c, height=.5)
    if val > 2: a.text(left + val / 2, 0, f'{val:.1f}', ha='center', va='center', color=PAPER, fontsize=8.5)
    if val > 2: a.text(left + val / 2, -.42, nm, ha='center', va='top', fontsize=7.5, color=MID)
    left += val
a.set_xlim(0, 40); a.set_ylim(-1, .6); a.set_xticks([]); a.set_yticks([]); clean(a, left=False)
a.set_title(f'Data booked as assets by\n{int(v("listed_firms_booking_data_assets", 2025))} listed firms, 2025 (100m yuan)', fontsize=9.5, loc='left')
a.text(40, .45, 'inventory 0.2', ha='right', fontsize=7.5, color=MID)
title(fig, 'Data in numbers', 'Data produced each year, data used for AI, the data market and data on company balance sheets. China produced about 27% of the world\'s data in 2025.', y=.96)
fig.text(.05, .03, 'Data: National Data Administration (national data resources surveys 2023 to 2025; national data work conference, January 2025); SAIF data asset tracking report via Yicai (June 2026). '
         '"+" marks lower bounds ("over"). Surveys started in 2023, so there is no earlier comparable series.', fontsize=7, color=MID)
plt.subplots_adjust(left=.05, right=.98, top=.74, bottom=.14)
fig.savefig('out/assets/data_in_numbers.png', facecolor=PAPER); plt.close(fig)

# ------------------------------------------------------------------ 3. the competition and where it happens
fig = plt.figure(figsize=(13, 6.2))
a1 = fig.add_axes([.05, .12, .36, .62]); a2 = fig.add_axes([.47, .06, .5, .78])
yrs = comp.year.values
a1.bar(yrs - .18, comp.teams_registered / 1e3, width=.34, color=INK, label='Teams registered')
a1.bar(yrs + .18, comp.participants / 1e3, width=.34, color=RED, label='Participants')
for y, t, p_, c in zip(yrs, comp.teams_registered, comp.participants, comp.final_city):
    a1.text(y - .18, t / 1e3 + 2, f'{t / 1e3:.0f}k', ha='center', fontsize=8.5)
    a1.text(y + .18, p_ / 1e3 + 2, f'{p_ / 1e3:.0f}k', ha='center', fontsize=8.5, color=RED)
    a1.text(y, -12, f'final: {c}', ha='center', fontsize=8, color=MID)
a1.set_xticks(yrs); a1.set_ylim(0, 165); a1.set_yticks([]); clean(a1, left=False); a1.legend(frameon=False, fontsize=8.5, loc='upper left')
a1.set_title('The "Data Element ×" competition', fontsize=10, loc='left')
EXT = (97, 128, 18, 43)
clip = box(EXT[0] - 2, EXT[2] - 2, EXT[1] + 2, EXT[3] + 2)
for f in json.load(open('raw/ne_50m_admin_0_countries.geojson'))['features']:
    if f['properties']['ADM0_A3'] == 'CHN': continue
    g = shape(f['geometry'])
    if not g.intersects(clip): continue
    for p in getattr(g.intersection(clip), 'geoms', [g.intersection(clip)]):
        if p.geom_type == 'Polygon': a2.add_patch(MPoly(np.array(p.exterior.coords), closed=True, fc='#F5F3EF', ec='#E2DFD9', lw=.4))
for f in json.load(open('raw/china_provinces.geojson'))['features']:
    g = shape(f['geometry'])
    for p in getattr(g, 'geoms', [g]): a2.add_patch(MPoly(np.array(p.exterior.coords), closed=True, fc=LAND, ec=PAPER, lw=.6))
for c, gp in pl.groupby('city'):
    la, lo = gp.latitude.iloc[0], gp.longitude.iloc[0]
    kinds = gp.kind.tolist()
    if 'Exchange' in kinds: a2.scatter(lo, la, s=90, marker='o', c=BLUE, ec=PAPER, lw=.8, zorder=4)
    if 'Competition' in kinds: a2.scatter(lo, la, s=200, marker='o', fc='none', ec=RED, lw=1.6, zorder=5)
    lab = '\n'.join(f'{r.year} {"exchange" if r.kind == "Exchange" else "competition final"}' for _, r in gp.sort_values('year').iterrows())
    dx, ha = (-10, 'right') if c in ('Guangzhou', 'Guiyang') else (10, 'left')
    a2.annotate(f'{c}\n{lab}', (lo, la), xytext=(dx, 0), textcoords='offset points', ha=ha, va='center', fontsize=7.8, zorder=6, linespacing=1.2)
a2.set_xlim(EXT[0], EXT[1]); a2.set_ylim(EXT[2], EXT[3]); a2.set_aspect(1 / np.cos(np.radians(30)))
a2.set_xticks([]); a2.set_yticks([]); [s_.set_visible(False) for s_ in a2.spines.values()]
a2.legend(handles=[Line2D([], [], marker='o', ls='', color=BLUE, ms=8, label='Data exchange (selection)'),
                   Line2D([], [], marker='o', ls='', mfc='none', mec=RED, mew=1.6, ms=11, label='Competition final')], loc='lower right', frameon=False, fontsize=8.5)
title(fig, 'A national contest and a few exchanges', 'Registrations to the "Data Element ×" competition grew by half in two years; the first data exchanges opened in Guiyang, Beijing, Shanghai and the Greater Bay Area.', y=.96)
fig.text(.05, .015, 'Data: National Data Administration and People\'s Daily; figures are lower bounds ("over"), except 2024 participants ("nearly 100,000"). Exchanges: the five main ones by opening date, not a complete list. Borders: Natural Earth.', fontsize=7, color=MID)
fig.savefig('out/assets/competition_and_exchanges.png', facecolor=PAPER); plt.close(fig)

# ------------------------------------------------------------------ 4. road to 2030: scenarios and official targets
tg = pd.read_parquet('out/data/targets_2030.parquet')
pj = pd.read_parquet('out/data/projections.parquet')
fig = plt.figure(figsize=(14, 9.4))
a1 = fig.add_axes([.05, .5, .37, .34]); a2 = fig.add_axes([.58, .5, .36, .34]); a3 = fig.add_axes([.05, .09, .91, .27])

yrs = [2023, 2024, 2025]
a1.bar(yrs, [v('data_production', y) for y in yrs], color=LIGHT, width=.55)
for y in yrs: a1.text(y, v('data_production', y) + 3, f"{v('data_production', y):.0f}", ha='center', fontsize=8.5)
for (name, g), c, lab in zip(pj[pj.indicator == 'data_production'].groupby('scenario', sort=False), [BLUE_SOFT, BLUE, RED], ['at 15% a year', 'at 20% a year', 'at the 2025 pace (27%)']):
    a1.plot(g.year, g.value, color=c, lw=2, marker='o', ms=3)
    a1.text(2030.2, g.value.iloc[-1], f"{g.value.iloc[-1]:.0f} ZB\n{lab}", va='center', fontsize=8, color=c if c != BLUE_SOFT else MID, linespacing=1.1)
a1.set_xlim(2022.4, 2030.1); a1.set_ylim(0, 190); a1.set_xticks(range(2023, 2031)); clean(a1); a1.yaxis.grid(color='#F2F2F2', lw=.6); a1.set_axisbelow(True)
a1.set_title('Data produced in China: what constant growth would give by 2030\n(zettabytes; bars: surveys, lines: arithmetic scenarios)', fontsize=9.5, loc='left')

for name, c, ls in [('target floor, 15% a year from 2024', INK, '--'), ('plan ambition, 20% a year to 2026', RED, ':')]:
    g = pj[(pj.indicator == 'data_industry_scale') & (pj.scenario == name)]
    a2.plot(g.year, g.value, color=c, lw=1.6, ls=ls)
    a2.text(g.year.iloc[-1] + .12, g.value.iloc[-1], f"{g.value.iloc[-1]:.1f}  {name.split(',')[0]}", va='center', fontsize=8, color=c)
act = [(y, v('data_industry_scale', y)) for y in (2024, 2025)]
a2.plot([a for a, _ in act], [b for _, b in act], color=BLUE, lw=2.4, marker='o', ms=6, zorder=4)
for y, val in act: a2.text(y - .08, val + .3, f'{val:.2f}', ha='right', fontsize=8.5, color=BLUE)
a2.text(2025.15, v('data_industry_scale', 2025) - .55, f"+{v('data_industry_growth', 2025):.1f}% in 2025:\nabove the 15% floor,\nbelow the 20% ambition", fontsize=8, color=BLUE, va='top', linespacing=1.15)
a2.set_xlim(2023.6, 2030.6); a2.set_ylim(4, 13); a2.set_xticks(range(2024, 2030)); clean(a2); a2.yaxis.grid(color='#F2F2F2', lw=.6); a2.set_axisbelow(True)
a2.set_title('Data industry against its targets\n(trillion yuan; blue: reported, lines: paths implied by the targets)', fontsize=9.5, loc='left')

a3.axhline(0, color=LIGHT, lw=1.2, zorder=1)
AREA = {'Data market': RED, 'AI': BLUE, 'Infrastructure': INK, 'Public data': MID, 'Digital economy': RED}
ys = sorted(tg.target_year.unique())
xs = {y: i for i, y in enumerate(ys)}
for y, g in tg.groupby('target_year'):
    x = xs[y]
    a3.scatter(x, 0, s=60, color=RED if y <= 2030 else MID, zorder=3)
    a3.text(x, .14, str(y), ha='center', fontsize=11, weight='bold')
    for k, (_, r) in enumerate(g.iterrows()):
        a3.text(x, -.16 - k * .42, f"{r.area}\n{textwrap.fill(r.target, 30)}", ha='center', va='top', fontsize=7.6, color=AREA.get(r.area, INK), linespacing=1.15)
a3.set_xlim(-.6, len(ys) - .4); a3.set_ylim(-1.15, .3); a3.axis('off')
fig.text(.05, .395, 'Official targets, as published', fontsize=10, weight='bold')
title(fig, 'Road to 2030', 'Where the data economy is heading if recent growth holds, and what the State has committed to. Scenarios are arithmetic, not forecasts.', y=.96)
fig.text(.05, .015, 'Data: National Data Administration surveys; NDDRI via China Daily (2024) and Xinhua (2025) for the data industry; targets from the State Council, NDRC, NDA, MIIT and the 15th Five-Year Plan outline. '
         '\nScenarios apply constant growth to the last reported value; they ignore saturation, definition changes and revisions.', fontsize=7, color=MID, va='bottom')
fig.savefig('out/assets/vision_2030.png', facecolor=PAPER); plt.close(fig)
print(sorted(os.listdir('out/assets')))
