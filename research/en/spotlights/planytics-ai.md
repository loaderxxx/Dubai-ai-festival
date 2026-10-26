# Planytics AI and VERA™ — independent public-source deep dive

[Research Atlas](../../../README.md) · [English guide](../README.md) · [Русская версия](../../ru/spotlights/planytics-ai.md) · [Source policy](../../../docs/en/source-policy.md)

[Machine-readable evidence supplement](../../../data/research-supplements/planytics-ai.json)

**Review date:** 26 October 2026 · **Event candidate:** Planytics AI · **Public floorplan stand:** S69 · **Candidate ID:** `planytics-ai`

**Scope:** A standalone company deep dive **outside** the original 12-profile dataset and the selected 18-company value-chain study. The 18-company study's denominators and original machine-readable evidence have not been rewritten. This is not a lead assessment, collaboration announcement, independent product audit, or a verified record of the founder's personal interactions. Public sources only.

## Executive finding

Planytics AI is an India-based enterprise supply-chain intelligence vendor with a production inventory-planning SaaS foundation and a newer AI agent layer. **VERA™ (Virtual Enterprise Resolution Agent)** is positioned as the semantic decision layer between operational data and modular agents: ingest signals → model relationships/trade-offs → propose or dispatch actions subject to enterprise-set confidence thresholds. The meaningful distinction is its **operations-specific context and action loop**, not the marketing label "AI agent." The vendor describes active SaaS operations; the public evidence does **not** independently prove that every VERA agent is deployed in production or that the system is accessible to outside agents.

## 1. Identity and festival attribution

- The [IIT Madras Research Park startup directory](https://respark.iitm.ac.in/Planytics-AI) independently identifies **Planytics Solutions Private Limited**, incorporated in **2019**, located in **Chennai**, and associated with the **IITM Incubation Cell**. This is stronger third-party identity evidence than a booth label, but not a company registry extract.
- The same directory names **Badhrinath Kidambi**, **Ajay Iyer**, and **Emmanuel Albert** as founders. The [current company team page](https://planytics.ai/team) gives roles CEO, CTO, and CRO, respectively. The event badge supplied privately to the researcher is **not reproduced or relied on here**.
- The [public festival floorplan capture](../../../data/floorplan-source-2026-10-26.json) lists **Planytics AI at S69**. The [organizer's Startup Stage agenda](https://dubaiaifestival.com/start-up-agenda/) schedules Badhrinath Kidambi at **13:20 Dubai time on 26 October 2026**. These are event listings; neither by itself proves the talk took place.
- [Planytics' public company announcement](https://www.linkedin.com/company/planytics/) describes the team exhibiting at **S69** on 26–27 October 2026. It is a first-party statement, not independent attendance verification.

**Identity conclusion:** official domain `planytics.ai` matches the company name and IITM directory. Do **not** confuse it with `planytic.com`, a distinct similarly named project-management product.

## 2. Product stack: foundation, semantic layer and actions

| Layer | Reported mechanism | Public maturity / boundary |
|---|---|---|
| Planning SaaS foundation | Item-level forecasting, inventory buffers, dynamic reorder points, KPI cockpit and connections to existing HIS/ERP | **Live since 2023** per vendor; reported at **30+ customer locations**, **200+ business users**, **800K+ daily transactions** across India and Africa |
| VERA™ semantic decision layer | Maps SKUs, suppliers, sites, lead times, rules, exceptions and trade-offs via an ontology-based engine | Vendor architecture description; ontology schema, model training strategy and independent evaluation are **not** public in the reviewed sources |
| KPI Control Tower | Operational visibility and reasoned anomaly alerts | Base platform offering |
| Demand Forecasting | Probabilistic SKU-by-location predictions, potentially using transactions, weather and promotion signals | Advertised for healthcare/manufacturing; deployment boundaries not separately audited |
| Replenishment Agent | Generates purchase requests/orders from demand, buffer stock, lead-time and supplier signals | **Marked live** on the company site |
| Re-planning Agent | Resequences production and reallocates inventory on disruption | **Marked beta testing**, not production generally |
| ESG Agent | Optimises routes/sourcing versus environmental and compliance constraints | **In development** |
| Pricing Agent | Dynamic pricing versus margin and elasticity constraints | **In development** |

**Decision policy:** the vendor says high-confidence actions can execute within customer-set bands, while low-confidence cases are escalated with reasoning to a human planner. This is a design claim; it does not establish how approval, audit or rollback actually work at each client. [Primary source: product home](https://planytics.ai/).

**Important distinction:** existing SaaS transactions and customers must not be attributed automatically to VERA's autonomous agent layer. The marketing page combines these layers, but their production maturity differs.

## 3. Integrations and enterprise architecture

**Documented in the vendor's offering:** ERP coexistence rather than replacement; live manufacturing **SAP** integration; hospital HIS/pharmacy/ePharma links; and ingestion through APIs, files or database connections. The homepage also names Oracle, Dynamics, Tally and NetSuite as supported target families. That list is a capability claim, not independently verified, version-specific connector documentation. [Vendor product](https://planytics.ai/).

**Observed public gaps:** no public developer portal, authenticated endpoint list, external-agent tool contract, OpenAPI schema or MCP specification for VERA was established during this review. Absence from the reviewed pages does **not** prove no private API exists. Ask the team for a sandbox, data contract, sample payloads, webhook/event model, tenant-scoping model and execution authorization rules before proposing a connector.

**Potential workflow (HYPOTHESIS, not a partnership):**

1. A permissioned personal or enterprise assistant asks a narrowly scoped question about stockouts or replenishment.
2. VERA (if an approved API exists) returns a cited, structured read-only result with confidence and affected SKUs.
3. A human validates suggested action scope and business impact.
4. The operational write occurs only through a signed, limited-permission operation; audit and rollback are logged.

**Hard boundaries:** no uncontrolled transmission of supplier/customer or patient information; no externally triggered purchase-order writes without explicit delegated authority; separate identity, data residency, retention, incident response and human override.

## 4. Customer evidence and what it does not prove

| Published vendor case | Reported implementation and outcome | Evidence limit |
|---|---|---|
| **Arjas Steel** (India) | 12+ MRO stores, SAP integration and recalibrated reorder buffers twice weekly. Vendor reports **$90,000+ excess inventory cleared in Q1**. | **25% reduction on $8.2M inventory** and **100% machine service level** are **targets**, not completed results. Vendor-authored case; ask for dated customer-verifiable baseline and counterfactual. |
| **Apollo Hospitals** (India) | An 850-bed facility, four pharmacy stores, HIS/ERP integration. Vendor reports working capital **$1.5M → $1.1M** (~**$400K released**), inventory days **24 → 16**, indent fill rate **68% → 86%**, administration time **3h → under 1h**. | Vendor-authored case; measurements are not independently audited in the reviewed public sources. Do not imply that clinical outcomes were externally validated. |

References: [Arjas case](https://planytics.ai/case-study-arjas-steel) · [Apollo case](https://planytics.ai/case-study-healthcare) · [Customer overview](https://planytics.ai/customers).

The company additionally displays **Daimler India Commercial Vehicles** and **Arjas Steel** as manufacturing pilots, and **Apollo, Aster, Vijaya and Aga Khan University Hospital** as healthcare customers. The exact current contract or deployment scope for each displayed brand was not independently established. The site labels Google for Startups as a **Cloud Program 2024** association; this is **not evidence of Google equity investment**. IITM inclusion is separately supported by the IITM directory.

## 5. Commercial and security posture

- **Pricing:** no published tariff. Reported model: **fixed-fee 30-day pilot for one location**, including integration support and KPI Control Tower; production contracts scoped by site, agent and transactions. The same FAQ describes typical subsequent rollout as **4–8 weeks/location**, contingent on readiness. Price, minimum contract, resale rights and revenue share are **unknown**. [Pricing/FAQ](https://planytics.ai/pricing)
- **Security (vendor claims):** GCP hosting; encryption at rest/in transit; optional multi-region deployment and customer-chosen region; **ISO 27001:2022** and **ISO 42001:2023** certification. **SOC 2 Type II is a Q4 2026 target**, not a certified status as of this review. Certificate scope, issuing accreditation body, expiry, subprocessor inventory and data processing terms must be requested and inspected. [Security](https://planytics.ai/security)
- **Capital / economics:** public validated revenue, profitability, valuation and funding rounds were not established. **Google for Startups program participation must not be restated as investment.**
- **Company scale:** the [public LinkedIn company profile](https://www.linkedin.com/company/planytics/) lists a small private company headquartered in Chennai. Platform transaction volume is a vendor claim, not an audited ARR proxy.

## 6. Questions that would falsify a proposed integration or partnership

1. What exactly is **VERA** in production today, separate from the mature SaaS replenishment functions? Which agents can perform writes at a real site?
2. Is there a **documented customer-authorized external API** or MCP/tool gateway? Is it read-only, write-enabled or both? Which regions and tenants?
3. How does VERA express **confidence, evidence, constraints and explanations**? Can a third-party assistant receive machine-readable justifications?
4. What is the **approval chain** for purchase orders and re-planning; who can stop an action; how are reversals and duplicate actions handled?
5. Which security attestations and data-residency options cover **the VERA service**, not only the core SaaS?
6. Can the team demonstrate a **30-day test** with one bounded use case, agreed acceptance criteria and no access to protected data outside the test?
7. If a business partnership is discussed, what are **permitted integration scopes, support responsibilities and commercial/referral terms**? None are established by the present study.

## 7. Analytical synthesis — explicitly not a concluded partnership

**Complementarity hypothesis:** Planytics specializes in supply-chain decision intelligence and operational execution. A separate authorized human-facing assistant could offer multilingual natural-language exploration and briefing **if** Planytics exposes suitable controlled interfaces. Conversely, VERA is not described as a general personal assistant, and no public evidence demonstrates a direct agent-to-agent interface.

**Commercial fit to investigate:** UAE/GCC manufacturers, hospital pharmacies or distributors that already operate an ERP/HIS and face measurable planning/replenishment friction. A lead list, financing ability, willingness to partner, resale rights or specific customer need is **not** inferred here.

**Research judgment:** substantive enterprise-software evidence exists (independent IITM company identity plus internally documented customer examples). What remains unverified is the real-world autonomous behavior of each VERA agent, independent customer ROI, API openness, procurement attestations and partner intent.

## 8. Public source register (all reviewed 26 October 2026)

| ID | Public source | Supports / limits |
|---|---|---|
| P01 | [IIT Madras Research Park company page](https://respark.iitm.ac.in/Planytics-AI) | Independent company identity, incorporation year, founders, incubator |
| P02 | [Planytics product home](https://planytics.ai/) | VERA, agent maturity labels, integrations, company-stated usage metrics |
| P03 | [Planytics team](https://planytics.ai/team) | Founder roles |
| P04 | [Planytics case: Arjas](https://planytics.ai/case-study-arjas-steel) | Vendor-reported Q1 inventory outcome versus unachieved targets |
| P05 | [Planytics case: Apollo](https://planytics.ai/case-study-healthcare) | Vendor-reported hospital outcomes |
| P06 | [Planytics customers](https://planytics.ai/customers) | Named customer/recognition claims; not contracts |
| P07 | [Planytics pricing](https://planytics.ai/pricing) | Pilot/production pricing model, absence of posted figures |
| P08 | [Planytics security](https://planytics.ai/security) | Security assertions and SOC 2 target |
| P09 | [Festival startup stage](https://dubaiaifestival.com/start-up-agenda/) | Speaker name and scheduled slot |
| P10 | [Company LinkedIn](https://www.linkedin.com/company/planytics/) | First-party event announcement and public company profile |
| P11 | [Public floorplan snapshot](../../../data/floorplan-source-2026-10-26.json) | Name/stand capture only; no physical-attendance claim |

**Handling note:** No authenticated attendee records, personal contact details, private conversation logs, event-app screenshots, or claims of personal relationships entered this file. Each prospect of a collaboration remains an untested hypothesis.
