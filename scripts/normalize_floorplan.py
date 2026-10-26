#!/usr/bin/env python3
"""Rebuild conservative public baseline. Never merge by stand number."""
import csv, hashlib, json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
root=Path(__file__).resolve().parents[1]
src=Path(sys.argv[1]) if len(sys.argv)>1 else root/'data/floorplan-source-2026-10-26.json'
x=json.loads(src.read_text())
accessed='2026-10-26'
amenities={
'Activation Zone':'event_activity_zone',
'Cafe. Food Trucks':'food_service',
'Dubai AI Festival 2027 Sales Stand':'organizer_sales_stand',
'Helpdesk':'helpdesk',
'INNOVATION STAGE':'stage',
'Investors Lounge':'lounge',
'MOU Signing Stage':'stage',
'Photo Op':'photo_area',
'PLENARY':'stage',
'PREMIUM LOUNGE':'lounge',
'Press & Media Zone':'media_area',
'START-UP STAGE':'stage'}
def key(name): return ' '.join(unicodedata.normalize('NFKC',name).split()).casefold()
def slug(name): return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',name).encode('ascii','ignore').decode().casefold()).strip('-')
byname={}
for idx,row in enumerate(x['rows'],1):
    k=key(row['name'])
    byname.setdefault(k,{'name':row['name'],'rows':[]})['rows'].append((idx,row['stand']))
stand_names=defaultdict(set)
for r in x['rows']:
    if r['stand']: stand_names[r['stand']].add(key(r['name']))
profiles_path=root/'data/company-profiles.json'
profiles={p['company_id']:p for p in json.loads(profiles_path.read_text())['profiles']} if profiles_path.exists() else {}
entities=[]; raw=[]
for k,g in byname.items():
    name=g['name']; entity_id=slug(name); stands=list(dict.fromkeys(s for _,s in g['rows'] if s))
    kind='organization_candidate'; subtype=None; status='unresolved_public_label'
    if name in amenities: kind='amenity_or_event_service';subtype=amenities[name];status='label_classified'
    elif name=='India Pavilion': kind='pavilion';subtype='collective_exhibit';status='constituents_unresolved'
    elif name=='RSVD': kind='unknown';subtype='possible_reserved_placeholder';status='requires_organizer_confirmation'
    e={'id':entity_id,'name':name,'normalized_name':k,'record_type':kind,'record_subtype':subtype,'stands':stands,
       'source_row_numbers':[i for i,_ in g['rows']], 'source_row_count':len(g['rows']),
       'shared_stand_codes':[s for s in stands if len(stand_names[s])>1], 'identity_status':status,
       'official_website':None,'research_status':'not_started' if kind=='organization_candidate' else 'not_applicable',
       'source_url':x['source_url'],'embedded_source_url':x['embedded_source_url'],'observed_at_utc':x['observed_at_utc'],
       'accessed_on':accessed,'evidence_scope':'Public floorplan label and stand assignment only; not legal-entity, onsite-presence, buying-intent, or partnership verification.'}
    if entity_id in profiles:
        e['official_website']=profiles[entity_id]['official_website']
        e['research_status']='initial_public_profile'
        e['identity_status']='brand_matched_legal_entity_unverified'
    entities.append(e)
    for row_no,stand in g['rows']:
        raw.append({'row_number':row_no,'stand':stand,'name':name,'entity_id':entity_id,'record_type':kind,'source_url':x['source_url'],'observed_at_utc':x['observed_at_utc']})
raw.sort(key=lambda r:r['row_number'])
counts=Counter(e['record_type'] for e in entities)
summary={'raw_populated_rows':len(raw),'distinct_normalized_labels':len(entities),'organization_candidates':counts['organization_candidate'],
'amenity_or_event_service_labels':counts['amenity_or_event_service'],'pavilion_labels':counts['pavilion'],'unknown_labels':counts['unknown'],
'duplicate_label_extra_rows':len(raw)-len(entities),'unique_nonempty_stand_codes':len(stand_names),'rows_without_stand':sum(r['stand'] is None for r in raw),
'shared_stand_codes':{s:[g['name'] for k,g in byname.items() if k in names] for s,names in stand_names.items() if len(names)>1},
'verified_unique_legal_company_count':None,'initial_public_profiles':len(profiles),'organization_candidates_not_profiled':counts['organization_candidate']-len(profiles)}
meta={'schema_version':'1.0','event':x['event'],'accessed_on':accessed,'source_url':x['source_url'],
'normalization':'NFKC; collapse whitespace; casefold for grouping. No fuzzy merge. Keep all stand assignments. Preserve raw spellings. Do not split co-branded labels without evidence.',
'public_only':True,'private_app_data_used':False,'counts':summary}
for name,records in [('entities',entities),('companies',[e for e in entities if e['record_type']=='organization_candidate']),('floorplan-rows',raw)]:
    (root/f'data/{name}.json').write_text(json.dumps({**meta,'records':records},ensure_ascii=False,indent=2)+'\n')
    fields=list(records[0]);
    with (root/f'data/{name}.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r in records:w.writerow({k:';'.join(map(str,v)) if isinstance(v,list) else v for k,v in r.items()})
(root/'data/baseline-summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
