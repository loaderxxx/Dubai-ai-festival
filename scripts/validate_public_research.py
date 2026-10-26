#!/usr/bin/env python3
"""Local integrity checks; not a claim of current web or factual re-verification."""
import csv,json,re
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def J(p):return json.loads((root/p).read_text())
e=J('data/entities.json');c=J('data/companies.json');r=J('data/floorplan-rows.json');p=J('data/company-profiles.json');x=J('data/crossresearch.json');raw=J('data/floorplan-source-2026-10-26.json')
assert len(raw['rows'])==len(r['records'])==264
assert len(e['records'])==262
assert len(c['records'])==248
assert len(p['profiles'])==12
assert len(x['edges'])==14
ids=[a['id'] for a in e['records']];assert len(ids)==len(set(ids))
assert Counter(a['record_type'] for a in e['records'])=={'organization_candidate':248,'amenity_or_event_service':12,'pavilion':1,'unknown':1}
assert sum(a['source_row_count'] for a in e['records'])==264
assert sorted(v for a in e['records'] for v in a['source_row_numbers'])==list(range(1,265))
for rr,source in zip(r['records'],raw['rows']):
    assert rr['stand']==source['stand'] and rr['name']==source['name'] and rr['entity_id'] in ids
byid={a['id']:a for a in e['records']}
assert byid['aecendir']['stands']==['G103','S174']
assert byid['grid-studio']['stands']==['G105','G104']
assert byid['press-media-zone']['stands']==[]
assert byid['rsvd']['record_type']=='unknown'
assert byid['india-pavilion']['record_type']=='pavilion'
assert e['counts']['verified_unique_legal_company_count'] is None
assert e['counts']['initial_public_profiles']==12
assert e['counts']['organization_candidates_not_profiled']==236
sourceids={s['id'] for s in p['sources']};assert len(sourceids)==len(p['sources'])==23
for s in p['sources']:
    assert s['url'].startswith('https://') and s['accessed_on']=='2026-10-26'
profileids={a['company_id'] for a in p['profiles']};assert len(profileids)==12
factids=set()
for a in p['profiles']:
    assert a['company_id'] in byid and a['stands']==byid[a['company_id']]['stands']
    assert a['lead_priority'] is None and not a['buying_intent_verified'] and not a['partnership_intent_verified']
    assert byid[a['company_id']]['research_status']=='initial_public_profile'
    for f in a['facts']:
        assert f['id'] not in factids;factids.add(f['id'])
        assert set(f['statement'])=={'en','ru'} and all(f['statement'].values())
        assert set(f['source_ids'])<=sourceids and f['source_ids']
    assert a['target_buyer_roles_to_validate']['status']=='analyst_inference_not_confirmed_buyer'
    assert a['analyst_hypotheses'][0]['status']=='unvalidated'
for edge in x['edges']:
    assert edge['company_a'] in profileids and edge['company_b'] in profileids
    assert set(edge['supporting_fact_ids'])<=factids
    assert set(edge['source_ids'])<=sourceids
    assert not edge['commercial_partnership_confirmed'] and not edge['company_interest_confirmed']
    assert set(edge['statement'])=={'en','ru'}
for stem,n in [('entities',262),('companies',248),('floorplan-rows',264),('crossresearch',14)]:
    assert len(list(csv.DictReader((root/f'data/{stem}.csv').open())))==n
for md in root.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)',md.read_text()):
        if '://' in link or link.startswith('#'): continue
        target=(md.parent/link.split('#')[0]).resolve()
        assert target.exists(),f'Broken relative link in {md}: {link}'
report={'result':'PASS','checked_on':'2026-10-26','scope':'Local data integrity, bilingual fields, provenance references, exact row conservation, classifications, CSV parity and relative links; not live web verification.',
'counts':{'floorplan_rows':264,'labels':262,'organization_candidates':248,'initial_profiles':12,'not_profiled':236,'official_sources':23,'facts':len(factids),'crossresearch_edges':14},
'private_attendee_data_used':False,'legal_company_count_established':False}
(root/'data/validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
