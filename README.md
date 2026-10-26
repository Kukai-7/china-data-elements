# China's Data Elements: Data as a Factor of Production, 2015 to 2026

[Dataset on Hugging Face](https://huggingface.co/datasets/Kukai-7/china-data-elements) · code in this repository

**How did China turn data into a factor of production, alongside land, labour and capital, and what does that look like in numbers?** This dataset follows the "data elements" (数据要素) policy from the first big-data exchange in 2015 to the end of the "Data Element ×" three-year plan in 2026: the laws and institutions, the exchanges, the accounting rules that let companies put data on their balance sheets, the national competition, the official measures of how much data China produces and trades, and the road to 2030: the targets the State has set and what recent growth would give if it held.

*数据要素：从大数据战略到数据作为生产要素，2015年至2026年的政策、市场与数字。*

![From big data to data as a factor of production](https://huggingface.co/datasets/Kukai-7/china-data-elements/resolve/main/assets/policy_timeline.png)

*Reading the chart: each row is a law, policy, institution, exchange or competition, placed at its date; colour and shape give the kind, the shaded band the 2024 to 2026 action plan. The legal base comes first (2016 to 2021), then the market (exchanges from 2021), then the State's own data administration and accounting rules (2023).*

## Dataset description

| | |
|---|---|
| Subject | Data as a factor of production in mainland China: policy, law, institutions, markets, accounting, and official statistics on data |
| Period | April 2015 to October 2026, with official targets to 2035 and scenarios to 2030 |
| Size | 6 configurations: 20 dated events, 30 indicator values, 3 competition years, 8 places, 9 official targets, 33 scenario points |
| Format | Parquet, with the pipeline in this repository |
| Owner | Kukai-7, independent compilation |
| Created | October 2026, version 1.0 |
| License | CC BY 4.0 for the compilation; figures belong to their publishers (see sources) |
| Intended use | A reference timeline and a small table of headline figures for teaching, writing and further research on data governance and the data economy. Not legal advice and not investment advice. |

## Key facts

- **Data became a factor of production in 2019.** The Fourth Plenum of the 19th Central Committee (31 October 2019) listed data with labour, capital, land, knowledge, technology and management as factors that share in distribution; the March 2020 opinions on factor markets made it the fifth factor market.
- **A legal base in five years:** the Cybersecurity Law (2016), the Data Security Law (June 2021) and the Personal Information Protection Law (August 2021), then rules on cross-border data flows (March 2024).
- **A market, then an administration.** Exchanges opened in Guiyang (2015), Beijing and Shanghai (2021), Guangzhou and Shenzhen (2022). The "Twenty Measures on Data" of December 2022 separated the rights to hold, to process and to operate data. The National Data Administration opened in October 2023.
- **Data on the balance sheet.** Since 1 January 2024 companies may book data resources as intangible assets or inventory. In their 2025 annual reports, 136 A-share companies did so, for 3.79 billion yuan in all: 82% as intangible assets, 17% as development spending, under 1% as inventory. The three telecom carriers alone account for 55% of the amount.
- **Data production up 27% a year.** China produced 32.85 zettabytes of data in 2023, 41.06 in 2024 and 52.26 in 2025, about 27% of the world's. Data used for AI reached 199 exabytes in 2025, and for the first time more of it went to inference (101 EB) than to training.
- **A market of over 160 billion yuan.** Data trading exceeded 160 billion yuan in 2024 (up more than 30%), of which more than 30 billion on exchanges, about twice the year before. The digital economy as measured by CAICT reached 59.2 trillion yuan, 43.8% of GDP.
- **A data industry of 6.78 trillion yuan.** It grew 15.7% in 2025 (5.86 trillion in 2024): above the official floor of 15% a year to 2029, below the 20% a year the "Data Element ×" plan aimed for by 2026.
- **Road to 2030.** The 15th Five-Year Plan sets core digital economy industries at 12.5% of GDP in 2030 (10.5% in 2025); the "AI+" action targets AI terminal and agent use above 70% in 2027 and 90% in 2030. If data production kept growing at 15 to 27% a year, China would produce 105 to 175 zettabytes in 2030: arithmetic, not a forecast.
- **A competition that keeps growing.** The "Data Element ×" competition drew over 19,000 teams in 2024, 23,000 in 2025 and 29,000 in 2026, with over 145,000 participants this year; the 2026 final was held in Qingdao on 23 October 2026, in the last year of the three-year plan.

![Data in numbers](https://huggingface.co/datasets/Kukai-7/china-data-elements/resolve/main/assets/data_in_numbers.png)

*Reading the chart: four separate panels, each with its own unit. Data produced each year (zettabytes, with growth inside the bars); data used for AI in 2025, split between training and inference (exabytes); data trading in 2024, all trading against exchange trading ("+" means "over"); data booked as assets by listed companies in 2025, by balance-sheet item.*

![A national contest and a few exchanges](https://huggingface.co/datasets/Kukai-7/china-data-elements/resolve/main/assets/competition_and_exchanges.png)

*Reading the chart: left, teams and participants in the "Data Element ×" competition, with the city of each national final; right, the five main data exchanges (blue) and the three finals (red rings). Activity concentrates in Beijing, Shanghai and the Greater Bay Area.*

## The 2026 milestone

The third "Data Element ×" final closed in Qingdao on 23 October 2026, organised by 22 bodies led by the National Data Administration, the Cyberspace Administration and the Shandong provincial government. The director of the National Data Administration described a "531" implementation system for market-based allocation of data, and said that data circulation was moving "from points to areas", with data vendors, exchanges and circulation platforms building a single national market; he paired "Data Element ×" with "Artificial Intelligence +" as the two lines of work ahead. The National Data Development Research Institute released an insight report on the competition, which points to a faster-closing institutional loop for data circulation, an active data market, and a "flywheel" between AI and high-quality datasets. These are official statements, recorded here as such; the dataset does not evaluate them.

## Road to 2030

![Road to 2030](https://huggingface.co/datasets/Kukai-7/china-data-elements/resolve/main/assets/vision_2030.png)

*Reading the chart: top left, data produced each year (bars, from the national surveys) and where constant growth of 15%, 20% or the 2025 pace of 27% would lead by 2030; top right, the data industry as reported (blue) against the paths implied by the two official growth targets; bottom, the official targets by year, as published. The scenarios are arithmetic: they show the size of the question, not an expected outcome.*

**Official targets.** Nine targets from six documents, kept in the `targets_2030` configuration with their Chinese wording, issuer and date.

| Year | Area | Target | Document |
|---|---|---|---|
| 2026 | Data market | Data industry over 20% a year; data trading volume doubled; 300+ application scenarios | "Data Element ×" three-year action plan (January 2024) |
| 2027 | AI | AI terminals and agents used by over 70% | Opinions on the "AI+" action (August 2025) |
| 2028 | Infrastructure | Over 100 trusted data spaces | Trusted data space action plan (November 2024) |
| 2029 | Data market | Data industry over 15% a year, compound | Guiding opinions on the data industry (December 2024) |
| 2029 | Infrastructure | Institutions for the national data infrastructure basically in place | National data infrastructure guidelines (January 2025) |
| 2030 | Public data | System for developing and using public data fully built | Opinions on public data resources (September 2024) |
| 2030 | Digital economy | Core digital economy industries at 12.5% of GDP (10.5% in 2025) | 15th Five-Year Plan outline (March 2026) |
| 2030 | AI | AI terminals and agents used by over 90% | Opinions on the "AI+" action (August 2025) |
| 2035 | AI | A new stage of intelligent economy and society | Opinions on the "AI+" action (August 2025) |

**Where things stand.** The data industry grew 15.7% in 2025: on track for the 2029 floor, short of the 2026 ambition. Holding 15% a year would take it to about 11.8 trillion yuan in 2029; the 20% path would have reached 8.4 trillion in 2026. The core digital economy needs about 0.4 point of GDP a year to reach 12.5% in 2030. Data production grew 25% in 2024 and 27% in 2025; three points are too few to estimate a trend, so the `projections` configuration gives three constant-growth paths and no central forecast.

## Load it

```python
from datasets import load_dataset

events = load_dataset("Kukai-7/china-data-elements", "policy_timeline", split="train").to_pandas()
indicators = load_dataset("Kukai-7/china-data-elements", "indicators", split="train").to_pandas()

# Every law adopted, in order
events[events.kind == "Law"][["date", "event", "event_zh", "note"]]

# Official targets to 2030 and the scenario paths
targets = load_dataset("Kukai-7/china-data-elements", "targets_2030", split="train").to_pandas()
paths = load_dataset("Kukai-7/china-data-elements", "projections", split="train").to_pandas()
```

## Configurations

### `policy_timeline` (default), 20 rows

| column | description |
|---|---|
| `date`, `year`, `date_precision` | Date of adoption, publication, opening or final; `date_precision` flags the one date known only approximately |
| `kind` | Law, policy, institution, accounting rule, exchange or competition |
| `event`, `event_zh` | Short description in English and the Chinese name |
| `city` | Where it happened (Beijing for national acts) |
| `note` | Date in force, scope or main content |

### `indicators`, 30 rows

Long format: `indicator`, `year`, `value`, `unit`, `source`. Data production, growth, storage, share of world production, data used for AI, high-quality datasets, active data, data trading, data enterprises, the data industry, the digital economy and its share of GDP (broad CAICT measure and core industries), and data booked as assets by listed companies. Units containing "lower bound" mark figures published as "over".

### `competition`, 3 rows

Year, city of the national final, teams registered, participants, projects in the national final, tracks, award-winning teams, source.

### `places`, 8 rows

Cities of the exchanges and competition finals with coordinates, for mapping.

### `targets_2030`, 9 rows

| column | description |
|---|---|
| `target_year`, `area` | Year the target refers to; data market, AI, infrastructure, public data or digital economy |
| `target`, `target_zh` | The target in English and in the original Chinese wording |
| `target_value`, `target_unit`, `quantified` | The number when there is one; `quantified` is false for qualitative goals |
| `document`, `issuer`, `announced` | Source document, issuing bodies, date published or announced |

### `projections`, 33 rows

`indicator`, `scenario`, `year`, `value`, `unit`, `method`. Data production under three constant growth rates from 2025 to 2030; the data industry along the paths implied by the 15% (to 2029) and 20% (to 2026) targets from the 2024 value; the core digital economy share on a straight line to the 2030 target.

## Dataset characterization

**Data collection method:** manual compilation from official releases and press reports, each row with its source. There is no automated scraping of official sites in this version.

**Labeling method:** the `kind` of each event was assigned by hand.

| Publisher | What it gives |
|---|---|
| National Data Administration (国家数据局) | National data resources surveys 2023, 2024 and 2025; competition figures; data work conferences; targets for trusted data spaces |
| National Data Development Research Institute, via China Daily and Xinhua | Data industry scale, 2024 and 2025 |
| National Development and Reform Commission, MIIT | Targets for the data industry and the national data infrastructure |
| 15th Five-Year Plan outline (National People's Congress, March 2026) | Core digital economy share of GDP, 2025 and 2030 target |
| State Council, CPC Central Committee, National People's Congress | Policy documents and laws |
| Ministry of Finance | Interim rules on accounting for enterprise data resources (2023) |
| Cyberspace Administration of China | Rules on cross-border data flows (2024) |
| China Academy of Information and Communications Technology (CAICT) | Digital economy size and share of GDP |
| Shanghai Advanced Institute of Finance (SAIF), via Yicai | Data assets booked by listed companies, 2025 annual reports |
| Xinhua, People's Daily, Science and Technology Daily | Press reports of the above |

## How it was built

`build.py` holds the curated tables with their sources and writes the Parquet files; `viz.py` draws the charts. There is no correlation analysis and no fitted forecast: the official series start in 2023 and give three points at most, too few for either. The projections are constant-growth arithmetic from the last reported value, shown as a range of scenarios.

## Limitations

- **Official figures, short series.** Most indicators come from government surveys or speeches. The national data resources survey started with 2023; earlier estimates of data production used other methods and are not comparable, so they are left out.
- **Lower bounds.** Many figures are published as "over" (超过); they are stored as the stated floor and flagged in the unit.
- **Definitions are new and moving.** "Data trading", "data enterprises", "active data" and "high-quality datasets" are defined by the publishers and may change. The CAICT digital economy measure is broad (it includes the digitalised part of traditional industries) and is not an official national accounts figure.
- **Data assets are small so far.** 3.79 billion yuan across 136 companies is tiny next to their total assets; booking data remains optional and concentrated in a few firms.
- **The timeline is a selection.** It keeps the national acts and the main exchanges; many local regulations and local exchanges or trading centres are not listed here.
- **No independent check.** Figures are taken as published; the dataset does not audit them.
- **Scenarios are not forecasts.** The 2030 paths assume constant growth and ignore saturation, price effects, definition changes and revisions. Data volume is not value: zettabytes say nothing about what the data is worth.
- **Targets are commitments, not outcomes.** They are listed as published; qualitative targets cannot be checked, and the dataset does not rate the chances of meeting them. The 12.5% core digital economy share and the 43.8% CAICT share measure different things.

## Ethical considerations

The dataset contains no personal data. It describes a policy area that bears on privacy, surveillance and state access to data; laws such as the Personal Information Protection Law are listed by date and scope only, without assessing how they are applied. Statements by officials are reported as statements.

## Citation

```bibtex
@misc{kukai7_china_data_elements_2026,
  title  = {China's Data Elements: Data as a Factor of Production, 2015 to 2026},
  author = {Kukai-7},
  year   = {2026},
  url    = {https://huggingface.co/datasets/Kukai-7/china-data-elements}
}
```

## Related

- [Greater Bay Area Networks](https://huggingface.co/datasets/Kukai-7/greater-bay-area-networks), logistics, technology and finance around the Pearl River estuary.
- [China, AI and Manufacturing](https://huggingface.co/datasets/Kukai-7/china-ai-manufacturing), R&D by province and the Hangzhou, Shenzhen and Beijing clusters.
- [GitHub: Kukai-7](https://github.com/Kukai-7)
