#!/usr/bin/env python3
"""Validate public atlas joins and coverage; not a factual or live-source audit."""
from pathlib import Path
from collections import Counter
import json
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_text())
c=read('research/company-atlas/roster.json');rows=c['records'];cov=read('research/company-atlas/coverage.json')
assert len(rows)==cov['organization_candidates']==248
assert len({r['id'] for r in rows})==len(rows)
assert dict(Counter(r['depth'] for r in rows))==cov['depth_counts']
assert cov['private_app_data_used'] is False and cov['complete_deep_research'] is False
sources=read('research/company-atlas/sources.json')['sources'];source_ids={s['id'] for s in sources}
assert len(source_ids)==len(sources)
for r in rows:
 assert set(r['source_ids'])<=source_ids, r['id']
 assert (R/'research/company-atlas/profiles'/f"{r['id']}.md").exists()
 assert r['partnership_confirmed'] is False
 for field in ('offering','integration_surface','collaboration_hypothesis'):assert all(r[field].get(l) for l in ('en','ru'))
sp=read('research/speakers/speakers.json');ss=read('research/speakers/sessions.json');pp=read('research/speakers/startup-pitches.json');sc=read('research/speakers/coverage.json')
assert len(sp)==sc['public_directory_cards']
assert dict(Counter(s['date'] for s in ss))==sc['conference_sessions']
assert len(pp)==sc['startup_pitch_table_rows']
assert len({s['id'] for s in sp})==len(sp)
assert len({s['id'] for s in ss})==len(ss)
spi={s['id'] for s in sp};ssi={s['id'] for s in ss};links=0
for s in ss:
 assert not s['delivery_verified']; assert s['recording_url'] is None and s['transcript_url'] is None
 for person in s['people']:
  assert person['speaker_id'] in spi;links+=1
for p in pp:assert not p['delivery_verified']
for s in sp:assert set(s['sessions'])<=ssi
assert links==sc['speaker_session_links']
for topic in read('research/speakers/topics.json'):assert set(topic['session_ids'])<=ssi
assert sc['authenticated_app_data_used'] is False
print(json.dumps({'result':'PASS','scope':'Local public-company/source/profile and speaker/session/topic joins; no web verification or completeness certification','company_candidates':len(rows),'depth_counts':cov['depth_counts'],'speakers':len(sp),'sessions':len(ss),'speaker_session_links':links,'startup_pitch_rows':len(pp)},ensure_ascii=False,indent=2))
org=read('research/organizers-sponsors/directory.json')
assert len(org)==36 and len({r['id'] for r in org})==36
for r in org:
 assert r['public_source_only'] is True
 assert r['role_source'].startswith('https://') and r['contact_source'].startswith('https://')
 assert r['contact'] and r['contact_purpose']
print(json.dumps({'organizer_sponsor_records':len(org),'result':'PASS','limitation':'Official public routes may be general support or switchboards, not direct event contacts.'}))
