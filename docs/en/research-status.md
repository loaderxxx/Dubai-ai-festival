# Research status and coverage

[Home](../../README.md) · [Field guide](../../research/en/README.md) · [Русский](../ru/research-status.md)

**Research snapshot: 26 October 2026. Partial coverage, not a completed census.**

## The numbers are different layers, not competing totals

| Layer | Included | Remaining / unresolved |
|---|---|---|
| Original public floorplan | 264 populated rows; 262 distinct normalized display labels | Live plan can change after capture |
| Candidate research universe | 248 organization labels | Unique legal-company count is **not established** |
| Original structured evidence batch | 12 profiles; 37 facts; 23 official sources; 14 typed edges | 236 candidates had no original profile |
| Expanded value-chain study | 18 selected companies; 21 typed relationships; 61 claim records; 38 official sources | **230 of 248 candidates are outside the expanded study** |

The public floorplan was captured at **2026-10-26 03:30:39 UTC**. That timestamp establishes when the labels were observed, not when an exhibitor's attendance was verified. [Original provenance and counting rules](public-baseline.md) · [Current machine-readable coverage](../../data/research-coverage.json)

## What changed in the expansion

The original 12-company group is **AWS, Alibaba Cloud, Atlan, ClickUp, Elastic, ElevenLabs, Snowflake, Haptik, ONLYOFFICE, Applause, PlaceOS and XenonStack**.

The six additions are **Apgar Group, DataCamp, Macgence, Sia Partners, Smart Spaces and Watergate**. Their floorplan labels and stand assignments are preserved in the [company directory](../../research/en/README.md#company-directory). They broaden the role map to include more data-services, skills, training-data and smart-building perspectives; this is a selection rationale, not a representativeness claim.

[Read the expanded study](../../research/en/value-chains.md) · [Inspect its registers](../../data/value-chain/README.md)

## How to read a research status

| View | Meaning |
|---|---|
| [Current roster](../../research/en/roster.md) | Combined reading view: original profiles, expanded-study coverage and not-yet-covered candidates |
| [Current coverage register](../../data/research-coverage.json) | Derived union of the two layers, joined by candidate identity rather than stand code |
| [Original company records](../../data/companies.json) | The original 12-profile checkpoint; `not_started` here does **not** override a later expanded brief |
| [Original profile dataset](../../data/company-profiles.json) | The original structured evidence schema and 12 bilingual profiles |
| [Expanded company register](../../data/value-chain/companies.json) | Additional company-level analysis for the selected 18-company study |

Do not add **12 + 18**: the original 12 are included within the expanded 18. Do not add source totals across registers without deduplicating URLs and distinguishing source documents from factual claims.

## Known limits

- **Coverage:** 230 candidates remain outside the expanded study. Even the 18 selected companies are not exhaustively researched.
- **Identity:** name-level normalization is not legal-entity verification. Co-branded labels and collective exhibits remain unresolved where the evidence does not justify a split.
- **Presence:** a public label and stand are not an onsite attendance check.
- **Capabilities:** official product descriptions are vendor claims, not independent benchmarks or production acceptance tests.
- **Relationships:** documented connectors, ecosystem entries and one-sided product claims have narrower meanings than a confirmed commercial partnership.
- **Intent:** budgets, buying interest, willingness to partner, decision makers and purchase timing are not established.
- **Freshness:** a dated public-source review is not live monitoring; local rebuilds do not refresh the web.

## What completion would require

For each remaining candidate: resolve its official identity, capture an offering and a real use case, identify supported integration surfaces, record public proof and limits, compare its role with other companies, and formulate a question that could disconfirm the proposed fit.

For each proposed combination: verify product-specific compatibility, permissions and data boundaries, delivery ownership, acceptance criteria and the relevant parties' actual interest. **A hypothesis is not promoted to fact because it sounds commercially attractive.**

## Verification scope

[Local validation](../../scripts/README.md) checks structural integrity, coverage consistency, provenance references, bilingual fields and navigation. It does not verify physical attendance, legal identity, vendor performance or commercial intent. Use the [source policy](source-policy.md) when extending the work.
