"""Build the China data elements dataset: data as a factor of production, from policy to market. All tables are curated from official
releases and press reports of the National Data Administration, the Ministry of Finance, CAICT and others; each row carries its source."""
import json, os, pandas as pd

OUT = 'out/data'
os.makedirs(OUT, exist_ok=True)

# ------------------------------------------------------------------ policy, law and institutions (date of adoption, publication or opening)
P = [('2015-04-14', 'Exchange', 'Guiyang Global Big Data Exchange opens', '贵阳大数据交易所挂牌', 'Guiyang', 'First data exchange in China'),
     ('2015-08-31', 'Policy', 'State Council Action Outline for Promoting Big Data Development', '促进大数据发展行动纲要', 'Beijing', 'First national big-data strategy'),
     ('2016-11-07', 'Law', 'Cybersecurity Law adopted', '网络安全法', 'Beijing', 'In force 1 June 2017'),
     ('2019-10-31', 'Policy', 'Fourth Plenum names data a factor of production', '十九届四中全会：数据作为生产要素参与分配', 'Beijing', 'Data joins labour, capital, land, knowledge, technology and management'),
     ('2020-03-30', 'Policy', 'Opinions on market-based allocation of factors', '关于构建更加完善的要素市场化配置体制机制的意见', 'Beijing', 'Data listed as the fifth factor market'),
     ('2021-03-31', 'Exchange', 'Beijing International Big Data Exchange opens', '北京国际大数据交易所', 'Beijing', ''),
     ('2021-06-10', 'Law', 'Data Security Law adopted', '数据安全法', 'Beijing', 'In force 1 September 2021'),
     ('2021-08-20', 'Law', 'Personal Information Protection Law adopted', '个人信息保护法', 'Beijing', 'In force 1 November 2021'),
     ('2021-11-25', 'Exchange', 'Shanghai Data Exchange opens', '上海数据交易所', 'Shanghai', ''),
     ('2022-09-30', 'Exchange', 'Guangzhou Data Exchange opens', '广州数据交易所', 'Guangzhou', ''),
     ('2022-11-15', 'Exchange', 'Shenzhen Data Exchange opens', '深圳数据交易所', 'Shenzhen', ''),
     ('2022-12-19', 'Policy', '"Twenty Measures on Data": opinions on the basic data system', '数据二十条', 'Beijing', 'Separates rights to hold, process and operate data'),
     ('2023-08-21', 'Accounting', 'Interim rules on accounting for enterprise data resources', '企业数据资源相关会计处理暂行规定', 'Beijing', 'Data can be booked as intangible assets or inventory from 1 January 2024'),
     ('2023-10-25', 'Institution', 'National Data Administration inaugurated', '国家数据局挂牌', 'Beijing', 'Approved in the State Council reform of March 2023'),
     ('2024-01-04', 'Policy', '"Data Element ×" three-year action plan 2024 to 2026', '"数据要素×"三年行动计划', 'Beijing', '17 departments, 12 sectors'),
     ('2024-03-22', 'Law', 'Rules on promoting and regulating cross-border data flows', '促进和规范数据跨境流动规定', 'Beijing', 'Cyberspace Administration of China'),
     ('2024-10-27', 'Competition', 'First "Data Element ×" competition final', '首届"数据要素×"大赛全国总决赛', 'Beijing', 'Over 19,000 teams'),
     ('2025-11-25', 'Competition', 'Second "Data Element ×" competition final', '2025年"数据要素×"大赛全国总决赛', 'Shanghai', 'Over 23,000 teams'),
     ('2025-12-30', 'Policy', 'National data work conference: 2026 named the year of releasing data value', '全国数据工作会议："数据要素价值释放年"', 'Beijing', ''),
     ('2026-10-23', 'Competition', 'Third "Data Element ×" competition final', '2026年"数据要素×"大赛全国总决赛', 'Qingdao', 'Over 29,000 teams; last year of the three-year plan')]
pol = pd.DataFrame(P, columns=['date', 'kind', 'event', 'event_zh', 'city', 'note'])
pol['date'] = pd.to_datetime(pol.date); pol['year'] = pol.date.dt.year
pol['date_precision'] = 'day'
pol.loc[pol.event.str.startswith('First "Data'), 'date_precision'] = 'on or shortly before (reported 27 October 2024)'
pol.to_parquet(f'{OUT}/policy_timeline.parquet', index=False)

# ------------------------------------------------------------------ indicators (long format)
I = [('data_production', 2023, 32.85, 'ZB', 'National data resources survey 2023 (NDA, May 2024)'),
     ('data_production', 2024, 41.06, 'ZB', 'National data resources survey 2024 (NDA, 29 April 2025)'),
     ('data_production', 2025, 52.26, 'ZB', 'National data resources survey 2025 (NDA, 29 April 2026)'),
     ('data_production_growth', 2024, 25.0, '%', 'National data resources survey 2024'),
     ('data_production_growth', 2025, 27.28, '%', 'National data resources survey 2025'),
     ('data_production_per_person', 2024, 31.31, 'TB', 'National data resources survey 2024'),
     ('data_storage', 2025, 2.53, 'ZB', 'National data resources survey 2025'),
     ('share_of_world_data_production', 2025, 27.44, '%', 'National data resources survey 2025'),
     ('ai_data_training_and_inference', 2025, 199.48, 'EB', 'National data resources survey 2025'),
     ('ai_data_inference', 2025, 101.34, 'EB', 'National data resources survey 2025'),
     ('high_quality_datasets', 2025, 110000, 'datasets (lower bound)', 'National data resources survey 2025'),
     ('high_quality_datasets_volume', 2025, 908, 'PB (lower bound)', 'National data resources survey 2025'),
     ('active_data', 2025, 1.67, 'ZB', 'NDA press conference, 11 June 2026'),
     ('data_market_trading', 2024, 1600, '100 million yuan (lower bound)', 'NDA director at the national data work conference, January 2025'),
     ('data_exchange_trading', 2024, 300, '100 million yuan (lower bound)', 'NDA director at the national data work conference, January 2025'),
     ('data_enterprises', 2024, 190000, 'enterprises (lower bound)', 'Xinhua, 28 May 2025'),
     ('digital_economy', 2024, 59.2, 'trillion yuan', 'CAICT, China digital economy development report 2025 (March 2026)'),
     ('digital_economy_share_of_gdp', 2023, 42.8, '%', 'CAICT, implied by the 2025 report (+1 point in 2024)'),
     ('digital_economy_share_of_gdp', 2024, 43.8, '%', 'CAICT, China digital economy development report 2025 (March 2026)'),
     ('listed_firms_booking_data_assets', 2025, 136, 'A-share companies', 'SAIF data asset tracking report, via Yicai, 24 June 2026'),
     ('data_assets_booked', 2025, 37.86, '100 million yuan', 'SAIF data asset tracking report, via Yicai, 24 June 2026'),
     ('data_assets_booked_intangible', 2025, 31.20, '100 million yuan', 'SAIF data asset tracking report, via Yicai, 24 June 2026'),
     ('data_assets_booked_development', 2025, 6.44, '100 million yuan', 'SAIF data asset tracking report, via Yicai, 24 June 2026'),
     ('data_assets_booked_inventory', 2025, 0.22, '100 million yuan', 'SAIF data asset tracking report, via Yicai, 24 June 2026')]
ind = pd.DataFrame(I, columns=['indicator', 'year', 'value', 'unit', 'source'])
ind.to_parquet(f'{OUT}/indicators.parquet', index=False)

# ------------------------------------------------------------------ the "Data Element ×" competition
K = [(2024, 'Beijing', 19000, 100000, None, 12, 119, 'People\'s Daily, 28 October 2024: over 19,000 teams, nearly 100,000 participants'),
     (2025, 'Shanghai', 23000, 117000, 893, 14, 183, 'National Data Administration, 28 November 2025'),
     (2026, 'Qingdao', 29000, 145000, 330, None, None, 'National Data Administration, 23 October 2026')]
comp = pd.DataFrame(K, columns=['year', 'final_city', 'teams_registered', 'participants', 'projects_in_national_final', 'tracks', 'award_winning_teams', 'source'])
comp['figures_are'] = 'lower bounds ("over"), except 2024 participants ("nearly")'
comp.to_parquet(f'{OUT}/competition.parquet', index=False)

# ------------------------------------------------------------------ places: exchanges and competition finals
C = {'Guiyang': (26.647, 106.630), 'Beijing': (39.904, 116.407), 'Shanghai': (31.230, 121.474), 'Guangzhou': (23.129, 113.264),
     'Shenzhen': (22.543, 114.058), 'Qingdao': (36.067, 120.383)}
pl = pol[pol.kind.isin(['Exchange', 'Competition'])][['city', 'kind', 'event', 'year']].copy()
pl['latitude'] = pl.city.map(lambda c: C[c][0]); pl['longitude'] = pl.city.map(lambda c: C[c][1])
pl.to_parquet(f'{OUT}/places.parquet', index=False)
json.dump(dict(events=len(pol), indicators=len(ind)), open('out/stats.json', 'w'))
print(pol.kind.value_counts().to_dict(), len(ind))
