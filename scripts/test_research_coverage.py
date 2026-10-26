#!/usr/bin/env python3
"""Small offline regression tests for profile-union coverage and roster links."""
import json,shutil,subprocess,sys,tempfile,unittest
from pathlib import Path
SCRIPT=Path(__file__).with_name('build_rosters.py')
class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        for d in ['scripts','data/value-chain','research/en','research/ru']:(self.root/d).mkdir(parents=True,exist_ok=True)
        shutil.copyfile(SCRIPT,self.root/'scripts/build_rosters.py')
        self.write('data/companies.json',{'records':[
            {'id':'eleven-labs','name':'Eleven Labs','stands':['H70'],'official_website':'https://elevenlabs.io/'},
            {'id':'watergate','name':'Watergate','stands':['S159'],'official_website':None},
            {'id':'unresearched-example','name':'Unresearched Example','stands':['T1'],'official_website':None}]})
        self.write('data/company-profiles.json',{'profiles':[{'company_id':'eleven-labs'}]})
        self.expanded={'companies':[
            {'company_id':'eleven-labs','display_name':'ElevenLabs','report_anchor':'elevenlabs','source_ids':['voice'],'identity_match':{'confidence':'high_brand_match'}},
            {'company_id':'watergate','display_name':'Watergate','report_anchor':'watergate','source_ids':['water'],'identity_match':{'confidence':'medium_brand_match'}}]}
        self.write('data/value-chain/companies.json',self.expanded)
        self.write('data/value-chain/sources.json',{'sources':[{'id':'water','url':'https://example.test/official-water-product'}]})
    def tearDown(self):self.temp.cleanup()
    def write(self,path,obj):(self.root/path).write_text(json.dumps(obj))
    def run_generator(self):return subprocess.run([sys.executable,str(self.root/'scripts/build_rosters.py')],capture_output=True,text=True)
    def test_overlapping_profile_batches_are_not_added(self):
        p=self.run_generator();self.assertEqual(p.returncode,0,p.stderr)
        x=json.loads((self.root/'data/research-coverage.json').read_text());n=x['counts']
        self.assertEqual((n['initial_profile_batch'],n['expanded_study'],n['additional_in_expanded_study']),(1,2,1))
        self.assertEqual((n['unique_candidates_with_public_profiles'],n['candidates_not_profiled']),(2,1))
        for lang in ['en','ru']:
            md=(self.root/f'research/{lang}/roster.md').read_text()
            self.assertIn('value-chains.md#elevenlabs',md)
            self.assertNotIn('value-chains.md#eleven-labs',md)
            self.assertIn('https://example.test/official-water-product',md)
        self.assertEqual(x['records'][1]['brand_match_confidence'],'medium_brand_match')
    def test_unknown_expanded_id_rejected(self):
        self.expanded['companies'][0]['company_id']='outside-public-baseline'
        self.write('data/value-chain/companies.json',self.expanded)
        self.assertNotEqual(self.run_generator().returncode,0)
    def test_duplicate_expanded_id_rejected(self):
        self.expanded['companies'].append(self.expanded['companies'][0])
        self.write('data/value-chain/companies.json',self.expanded)
        self.assertNotEqual(self.run_generator().returncode,0)
    def test_original_batch_works_without_expanded_files(self):
        (self.root/'data/value-chain/companies.json').unlink()
        p=self.run_generator();self.assertEqual(p.returncode,0,p.stderr)
        x=json.loads((self.root/'data/research-coverage.json').read_text())
        self.assertEqual(x['counts']['unique_candidates_with_public_profiles'],1)
        self.assertEqual(x['counts']['candidates_not_profiled'],2)
if __name__=='__main__':unittest.main()
