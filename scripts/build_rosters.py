#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'data/companies.json').read_text())
for lang in ['en','ru']:
    en=lang=='en';lines=['# '+('Complete public candidate roster' if en else 'Полный публичный реестр кандидатов'),'','[English](../../research/en/roster.md) · [Русский](../../research/ru/roster.md)','',('248 candidate organization labels; 12 initial profiles and 236 not yet researched. Not a verified legal-company count. Stand assignments come from the public floorplan, observed 2026-10-26 03:30:39 UTC.' if en else '248 названий кандидатов-организаций: 12 первичных профилей, 236 ещё не исследованы. Это не подтверждённое число юридических компаний. Стенды взяты с публичного плана, наблюдавшегося 26.10.2026 в 03:30:39 UTC.'),'','[Floorplan](https://dubaiaifestival.com/floorplan/) · [Method / Метод](../../docs/'+lang+'/public-baseline.md) · [Profiles / Профили](companies.md)','',('| # | Public label | Stand(s) | Research | Official website |' if en else '| № | Публичное название | Стенды | Исследование | Официальный сайт |'),'|---:|---|---|---|---|']
    for i,c in enumerate(x['records'],1):
        status=('Initial public profile' if en else 'Первичный публичный профиль') if c['research_status']=='initial_public_profile' else ('Not started' if en else 'Не начато')
        website=f"[Official site]({c['official_website']})" if c['official_website'] else '—'
        lines.append(f"| {i} | {c['name'].replace('|','&#124;')} | {', '.join(c['stands'])} | {status} | {website} |")
    (root/f'research/{lang}/roster.md').write_text('\n'.join(lines)+'\n')
