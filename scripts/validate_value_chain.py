#!/usr/bin/env python3
"""Validate the expanded public study and its join to historical baseline evidence.

Checks local consistency only. It does not test integrations or validate vendor performance.
"""
import csv,json,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def J(name):return json.loads((ROOT/name).read_text())
def bilingual(value):
    assert isinstance(value,dict) and {'en','ru'}<=set(value)
    assert all(isinstance(value[k],str) and value[k].strip() for k in ['en','ru'])
baseline=J('data/companies.json');base={c['id']:c for c in baseline['records']}
initial=J('data/company-profiles.json');initial_ids={c['company_id'] for c in initial['profiles']}
company_doc=J('data/value-chain/companies.json');companies=company_doc['companies'];byid={c['company_id']:c for c in companies}
source_doc=J('data/value-chain/sources.json');sources=source_doc['sources'];source_byid={s['id']:s for s in sources}
ledger=J('data/value-chain/evidence-ledger.json');claims=ledger['claims'];claim_byid={c['claim_id']:c for c in claims}
relationship_doc=J('data/value-chain/relationships.json');relations=relationship_doc['relationships']
coverage=J('data/research-coverage.json')
relation_byid={r['id']:r for r in relations}
def resolved_claim(claim):
    if 'claim' in claim:return claim['claim']
    ref=claim['claim_ref']
    if ref['file']=='companies.json':
        assert ref['company_id'] in byid and ref['field'] in {'offering','integration_surface'}
        return byid[ref['company_id']][ref['field']]
    assert ref['file']=='relationships.json' and ref['field']=='statement'
    assert ref['relationship_id'] in relation_byid
    return relation_byid[ref['relationship_id']]['statement']
assert company_doc['public_only'] is True and company_doc['private_app_data_used'] is False
assert company_doc['performance_benchmarks_run'] is False and company_doc['commercial_quotes_obtained'] is False
assert len(byid)==len(companies)==company_doc['sample_size']==18
assert len(base)==company_doc['baseline_organization_candidates']==248
assert initial_ids<=set(byid)
assert len(set(byid)-initial_ids)==company_doc['additional_profiles']==6
assert company_doc['outside_sample']==248-18==230
assert len(source_byid)==len(sources)==ledger['source_count']==38
assert source_byid=={s['id']:s for s in ledger['sources']}
assert len(claim_byid)==len(claims)==ledger['claim_count']==61
assert all(s['url'].startswith('https://') and s['accessed_on']=='2026-10-26' for s in sources)
assert all(s['source_type'].startswith('official') for s in sources)
for c in companies:
    cid=c['company_id'];assert cid in base
    assert c['floorplan_name']==base[cid]['name'] and c['stands']==base[cid]['stands']
    assert c['event_evidence']['source_url']==base[cid]['source_url']
    assert c['event_evidence']['observed_at_utc']==base[cid]['observed_at_utc']
    assert c['identity_match']['legal_entity_verified'] is False
    assert c['identity_match']['event_website_binding_verified'] is False
    assert c['buyer_intent_verified'] is False and c['partnership_intent_verified'] is False
    assert c['report_anchor'] and c['official_website'].startswith('https://')
    for field in ['commercial_model','offering','integration_surface','not_equivalent_to','procurement_questions','unknowns']:bilingual(c[field])
    assert c['source_ids'] and set(c['source_ids'])<=set(source_byid)
    for field in ['offering','integration_surface']:
        claim=claim_byid[cid+'-'+field]
        assert resolved_claim(claim)['en']==c[field]['en'] and resolved_claim(claim)['ru']==c[field]['ru']
        assert cid in claim['company_ids']
for claim in claims:
    bilingual(resolved_claim(claim))
    assert claim['company_ids'] and set(claim['company_ids'])<=set(byid)
    assert claim['source_ids'] and set(claim['source_ids'])<=set(source_byid)
    assert claim['retrieved_on']=='2026-10-26' and claim['evidence_class']
counts=Counter(r['relation_type'] for r in relations)
expected_counts={'documented_connector':1,'documented_inference_adapter':2,'vendor_documented_partner_integration':1,'vendor_named_alliance_listing':2,'advertised_integration_offering':1,'analyst_hypothesis':7,'analyst_overlap':7}
assert dict(counts)==relationship_doc['counts']==expected_counts
assert len(relations)==len({r['id'] for r in relations})==21
for r in relations:
    assert len(r['companies'])==2 and set(r['companies'])<=set(byid)
    bilingual(r['statement']);bilingual(r['evidence_boundary'])
    assert r['source_ids'] and set(r['source_ids'])<=set(source_byid)
    assert r['deployed_by_research_team'] is False
    claim=claim_byid[r['id']]
    assert resolved_claim(claim)['en']==r['statement']['en'] and resolved_claim(claim)['ru']==r['statement']['ru']
    assert claim['evidence_class']==r['relation_type']
    assert set(claim['company_ids'])==set(r['companies'])
assert {s for c in claims for s in c['source_ids']}==set(source_byid)
assert coverage['counts']['unique_candidates_with_public_profiles']==18 and coverage['counts']['candidates_not_profiled']==230
assert coverage['counts']['initial_profile_batch']==12 and coverage['counts']['additional_in_expanded_study']==6
coverage_byid={c['company_id']:c for c in coverage['records']}
assert len(coverage_byid)==248
for cid,c in byid.items():assert coverage_byid[cid]['expanded_profile_available'] is True and coverage_byid[cid]['report_anchor']==c['report_anchor']
texts={lang:(ROOT/f'research/{lang}/value-chains.md').read_text() for lang in ['en','ru']}
urlsets={}
for lang,body in texts.items():
    headings=re.findall(r'^### (.+)$',body,flags=re.M)
    for c in companies:
        assert c['display_name'] in headings,f'Missing {lang} company heading: '+c['display_name']
        assert headings.count(c['display_name'])==1
    urlsets[lang]=set(re.findall(r'\]\((https?://[^)]+)\)',body))
    assert {s['url'] for s in sources}<=urlsets[lang]
assert urlsets['en']==urlsets['ru'],'EN/RU report source URL sets differ'
rows=list(csv.DictReader((ROOT/'data/value-chain/company-comparison.csv').open()))
assert len(rows)==18 and {r['company_id'] for r in rows}==set(byid)
for row in rows:
    c=byid[row['company_id']]
    for field,key in [('commercial_model','commercial_model'),('offering','offering'),('integration_surface','integration_surface'),('not_equivalent_to','not_equivalent_to'),('procurement_questions','procurement_questions'),('unknowns','unknowns')]:
        for lang in ['en','ru']:
            assert row[field+'_'+lang]==c[key][lang],f'CSV text mismatch: {row["company_id"]}/{field}_{lang}'
report={'result':'PASS','scope':'Local public baseline joins, coverage union, claim/source/edge integrity, EN/RU fields and report sources, CSV parity; not live web or integration testing.',
'counts':{'companies':18,'used_official_sources':38,'claim_records':61,'relationship_records':21,'documented_integration_links':4,'vendor_named_alliances':2,'advertised_offering_links':1,'analyst_hypotheses':7,'analyst_overlaps':7,'current_unprofiled_candidates':230}}
print(json.dumps(report,ensure_ascii=False,indent=2))
