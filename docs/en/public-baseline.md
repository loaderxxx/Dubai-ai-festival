# Public company baseline and research method

[Русский](../ru/public-baseline.md)

## What is actually counted

Public event source: [Dubai AI Festival floorplan](https://dubaiaifestival.com/floorplan/), embedding the [live floorplan](https://floorplan.live/interactive/shows/4608/views/2/plan). The public displayed table was observed on **2026-10-26 at 03:30:39 UTC**. Company sites were reviewed on **2026-10-26**.

| Measure | Count |
|---|---:|
| Populated floorplan table rows | 264 |
| Distinct normalized labels | 262 |
| Candidate organization labels | 248 |
| Amenities and event-service labels | 12 |
| Collective pavilion | 1 |
| Unknown / possible placeholder | 1 |
| Initial official-site company profiles | 12 |
| Candidate labels still without a profile | 236 |
| Independently verified unique legal companies | **Not established** |

**Do not present 264, 262 or 248 as a verified company count.** A label can name a brand, product, institution, collective or co-branded exhibit. Public-floorplan membership does not establish legal identity, physical attendance, a live booth, purchase intent or interest in a partnership. The organizers may revise the live plan.

The site wrapper was rechecked and exposes the live floorplan iframe; some wrapper navigation still refers to 2025. The captured map itself identifies the 2026 event. The underlying public-table capture is preserved with its provenance; no private attendee app, account-only exhibitor directory or personal attendee information was used.

## Normalization and classification

- Normalize Unicode with NFKC, collapse whitespace and casefold only for exact label grouping. Preserve original names.
- **Aecendir** appears at **G103 and S174**; **Grid Studio** at **G105 and G104**. Each becomes one label record with both stand assignments. This is name-level deduplication, not a legal-entity merge.
- Never use booth number as a company ID. **G103** is shared by Aecendir, Handover AI, RSVD and TOTL Resource International LLC (TRI). **G104** lists Grid Studio and Jalubro; **G105** lists ATELIC AI and Grid Studio.
- Preserve co-branded labels such as **Habytat / Realm9** and **Exordium – BugLoud** until evidence resolves the underlying entities. Do not split or infer separate companies.
- **India Pavilion** is a collective exhibit, not a single company. Its constituent entities remain unresolved.
- **RSVD** is retained as an unknown, possible reserved placeholder, pending organizer confirmation.
- These 12 labels are classified as amenities/event services: Activation Zone; Cafe. Food Trucks; Dubai AI Festival 2027 Sales Stand; Helpdesk; INNOVATION STAGE; Investors Lounge; MOU Signing Stage; Photo Op; PLENARY; PREMIUM LOUNGE; Press & Media Zone; START-UP STAGE.
- **Press & Media Zone has no stand code** in the source; preserve null rather than invent a location.
- Academic institutions and media brands remain organization candidates. The `companies` filename is a practical research inventory, not a claim that every row is a commercial legal company.

## Evidence standard

1. **Event presence evidence:** public floorplan label and stand assignment, with original row numbers and observation time.
2. **Identity evidence:** independently resolve the official brand site. Record ambiguity; never guess a domain from a common company name. A brand-site match is not legal-exhibitor verification.
3. **Offering evidence:** concise paraphrases of official product/documentation pages, each with source ID, URL, access date and locator. Vendor statements are not independently verified performance results.
4. **Target users versus buyers:** explicitly advertised user groups may be recorded as facts; suggested buyer roles remain analyst hypotheses until confirmed.
5. **Integration surface versus interest:** APIs, SDKs, connectors and public ecosystem listings can be factual. Willingness to integrate, partner, buy or co-sell is **unknown** unless separately evidenced.
6. **Crossresearch:** separate documented vendor links, proposed complementarity and competitive overlap. Each edge points to supporting fact IDs, a validation question and an implementation boundary. An edge does not mean a partnership.
7. **No fabricated prioritization:** this first batch is a relevance-based research selection, not scored or qualified sales leads. No budgets, decision makers, ROI, purchase timing or readiness scores are inferred.

The 12-profile batch covers AWS, Alibaba Cloud, Atlan, ClickUp, Elastic, ElevenLabs, Snowflake, Haptik, ONLYOFFICE, Applause, PlaceOS and XenonStack. English and Russian have equivalent facts, hypotheses and source references.

## Remaining work

For the remaining **236 candidate labels**, resolve the public identity first, then apply the same fact/hypothesis structure. Shared stands, generic names and co-branded labels should be resolved before expanding the entity count. Full research of all candidates is **not complete**.

For every candidate, the next evidence gate is: official website → offer and customer use case → integration surfaces → public proof → overlap/complementarity → questions to validate. The user's historical exhibition-research method has not been independently reconstructed in this bundle; this is an explicit evidence-first baseline, not a claim to have recovered that method.

## Data and reproducibility

- `data/floorplan-source-2026-10-26.json`: original public capture with provenance.
- `data/floorplan-rows.{json,csv}`: all 264 rows with entity references.
- `data/entities.{json,csv}`: all 262 labels with record type.
- `data/companies.{json,csv}`: 248 candidate organizations, research/identity status and verified brand-site links where researched.
- `data/company-profiles.json`, `data/sources.json`: initial bilingual evidence and source registry.
- `data/crossresearch.{json,csv}`: typed cross-company edges.
- `research/en/roster.md`, `research/ru/roster.md`: full candidate roster.

From the bundle root:

```sh
python scripts/normalize_floorplan.py
python scripts/build_initial_profiles.py
python scripts/normalize_floorplan.py
python scripts/build_crossresearch.py
python scripts/build_rosters.py
python scripts/validate_public_research.py
```

The scripts regenerate local files only; they do not scrape private systems, contact companies or make authenticated requests. Website evidence was manually reviewed; rebuilding files does not recheck the current web.
