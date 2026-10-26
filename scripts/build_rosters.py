#!/usr/bin/env python3
"""Generate the current public coverage view; preserve historical baseline files."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(path):return json.loads((ROOT/path).read_text())
baseline=read('data/companies.json')
initial=read('data/company-profiles.json')
initial_by_id={c['company_id']:c for c in initial['profiles']}
expanded_path=ROOT/'data/value-chain/companies.json'
expanded=read('data/value-chain/companies.json') if expanded_path.exists() else {'companies':[]}
expanded_by_id={c['company_id']:c for c in expanded['companies']}
source_path=ROOT/'data/value-chain/sources.json'
expanded_sources={s['id']:s for s in read('data/value-chain/sources.json')['sources']} if source_path.exists() else {}
baseline_ids={c['id'] for c in baseline['records']}
assert len(baseline_ids)==len(baseline['records']), 'Duplicate public baseline ID'
assert len(initial_by_id)==len(initial['profiles']), 'Duplicate initial profile ID'
assert len(expanded_by_id)==len(expanded['companies']), 'Duplicate expanded profile ID'
assert set(initial_by_id)|set(expanded_by_id)<=baseline_ids, 'Profile ID is missing from the public baseline'
covered=set(initial_by_id)|set(expanded_by_id)
records=[]
for c in baseline['records']:
    cid=c['id'];a=cid in initial_by_id;b=cid in expanded_by_id
    category='initial_and_expanded' if a and b else 'expanded_only' if b else 'initial_only' if a else 'not_profiled'
    website=c['official_website']
    if not website and b:
        source_ids=expanded_by_id[cid].get('source_ids',[])
        website=next((expanded_sources[s]['url'] for s in source_ids if s in expanded_sources),None)
    identity=expanded_by_id[cid].get('identity_match') if b else None
    report_anchor=expanded_by_id[cid].get('report_anchor',re.sub(r'[^\w -]','',expanded_by_id[cid]['display_name']).casefold().replace(' ','-')) if b else None
    records.append({'company_id':cid,'floorplan_name':c['name'],'stands':c['stands'],'coverage_status':category,
        'initial_profile_available':a,'expanded_profile_available':b,'official_source_url':website,
        'brand_match_confidence':identity.get('confidence') if identity else ('brand_matched_legal_entity_unverified' if a else 'unresolved_public_label'),
        'legal_exhibitor_entity_verified':False,'report_anchor':report_anchor,
        'profile_links':{'en':f'research/en/value-chains.md#{report_anchor}','ru':f'research/ru/value-chains.md#{report_anchor}'} if b else {'en':'research/en/companies.md','ru':'research/ru/companies.md'} if a else None})
counts={'public_organization_candidates':len(baseline_ids),'initial_profile_batch':len(initial_by_id),'expanded_study':len(expanded_by_id),'additional_in_expanded_study':len(set(expanded_by_id)-set(initial_by_id)),'unique_candidates_with_public_profiles':len(covered),'candidates_not_profiled':len(baseline_ids-covered),'verified_unique_legal_company_count':None}
coverage={'schema_version':'1.0','reviewed_on':'2026-10-26','public_only':True,'source_files':['data/companies.json','data/company-profiles.json']+(['data/value-chain/companies.json','data/value-chain/sources.json'] if expanded_path.exists() else []),'counts':counts,
'note':{'en':'Current union of public research coverage, not a verified exhibitor/company count. The original baseline JSON retains the initial 12-profile checkpoint. Expanded brand matches have stated uncertainty.','ru':'Текущее объединённое покрытие публичного исследования, не подтверждённое число экспонентов/компаний. Исходные JSON базы сохраняют первый срез из 12 профилей. Неопределённость сопоставления брендов указана в расширенном исследовании.'},'records':records}
(ROOT/'data/research-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
for lang in ['en','ru']:
    en=lang=='en';lines=['# '+('Complete public candidate roster' if en else 'Полный публичный реестр кандидатов'),'','[English](../../research/en/roster.md) · [Русский](../../research/ru/roster.md)','',
    (f"**{len(baseline_ids)} candidate organization labels · {len(covered)} with public profiles · {len(baseline_ids-covered)} not yet profiled.**" if en else f"**{len(baseline_ids)} названий кандидатов-организаций · {len(covered)} с публичными профилями · {len(baseline_ids-covered)} пока без профилей.**"),'',
    (f"The initial batch contains {len(initial_by_id)} profiles. The expanded study covers {len(expanded_by_id)} candidates, including {len(set(expanded_by_id)-set(initial_by_id))} additional candidates; these counts overlap and must not be added." if en else f"Первоначальная выборка содержит {len(initial_by_id)} профилей. Расширенное исследование охватывает {len(expanded_by_id)} кандидатов, включая {len(set(expanded_by_id)-set(initial_by_id))} новых; выборки пересекаются, их нельзя складывать.") if expanded_by_id else '',
    '',('This is not a verified legal-company count. A public profile can include an uncertain brand-to-site match; inspect its identity caveat. Stands come from the public floorplan observed 2026-10-26 03:30:39 UTC.' if en else 'Это не подтверждённое число юридических компаний. Публичный профиль может содержать неоднозначное сопоставление бренда и сайта; проверяйте оговорку об идентичности. Стенды взяты с публичного плана, наблюдавшегося 26.10.2026 в 03:30:39 UTC.'),'',
    '[Floorplan](https://dubaiaifestival.com/floorplan/) · [Method / Метод](../../docs/'+lang+'/public-baseline.md) · [Initial profiles / Первые профили](companies.md) · [Coverage JSON / Покрытие](../../data/research-coverage.json)',
    *(['','[Expanded study / Расширенное исследование](value-chains.md)'] if expanded_by_id else []),'',
    ('| # | Public label | Stand(s) | Current research coverage | Official source |' if en else '| № | Публичное название | Стенды | Текущее покрытие исследования | Официальный источник |'),'|---:|---|---|---|---|']
    for i,c in enumerate(records,1):
        cid=c['company_id']
        if c['expanded_profile_available']:
            text=('Initial + expanded' if c['initial_profile_available'] else 'Added in expanded study') if en else ('Первичный + расширенный' if c['initial_profile_available'] else 'Добавлен в расширенном исследовании')
            status=f"[{text}](value-chains.md#{c['report_anchor']})"
        elif c['initial_profile_available']:status='[Initial profile](companies.md)' if en else '[Первичный профиль](companies.md)'
        else:status='Not profiled' if en else 'Нет профиля'
        source=f"[{'Official source' if en else 'Официальный источник'}]({c['official_source_url']})" if c['official_source_url'] else '—'
        lines.append(f"| {i} | {c['floorplan_name'].replace('|','&#124;')} | {', '.join(c['stands'])} | {status} | {source} |")
    (ROOT/f'research/{lang}/roster.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(counts,ensure_ascii=False))
