# Enterprise AI is a value chain, not a vendor category

### An evidence-backed, 18-company research showcase for Dubai AI Festival 2026

[Repository home](../../README.md) · [Русская версия](../ru/value-chains.md) · [Public roster](roster.md) · [Machine-readable evidence](../../data/value-chain/evidence-ledger.json)

**Research date: 26 October 2026. Public sources only.** This is a purposeful sample of **18 of 248 organization-candidate labels** in the public floorplan baseline: the original 12 profiles plus six additions. **230 candidates remain outside this study.** It is not a census, ranking, buying-intent list or verification of 18 legal exhibitors.

**The useful conclusion:** choose companies by the boundary they own in a workflow, not by whether they call themselves an “AI platform.” A model endpoint, a governed data source, a voice interface, a document editor, an implementation team and an acceptance-test service solve different problems. Sometimes they complement one another; sometimes they compete for the same portion of a project.

## Findings in 90 seconds

1. **Four cross-company integration links have specific public documentation.** Atlan–Snowflake has technical connector instructions; Elastic has inference adapters for Amazon Bedrock and AlibabaCloud AI Search; Smart Spaces names Watergate as an API integration partner. These are stronger than logo adjacency, but none was deployed or benchmarked by this research. [Atlan](https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake), [Elastic–Bedrock](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-amazonbedrock), [Elastic–Alibaba](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-alibabacloud), [Smart Spaces–Watergate](https://www.smartspaces.app/our-partners/watergate/).
2. **The authorization boundary deserves more attention than the demo.** Cortex Search runs searches with owner’s rights. Therefore, a connected catalog or an attractive assistant UI does not by itself prove that each caller sees only their permitted data. This is an architectural inference from a documented behavior, not an allegation of a vendor vulnerability. [Snowflake documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview).
3. **Build, buy and commission are three different decisions.** Cloud/runtime platforms are not interchangeable with work applications; implementation services are not equivalent to a software subscription. Apgar, Sia and XenonStack combine services with packaged offerings, so a proposal should separate licenses, engineering, operations and ownership. [Apgar](https://apgar-group.com/), [Sia AI](https://www.sia-partners.com/en/about-us/siaai), [XenonStack](https://www.xenonstack.com/).
4. **Overlap is workload-specific.** Elastic/Snowflake overlap in retrieval; ElevenLabs/Haptik in voice-agent workflows; PlaceOS/Smart Spaces in building orchestration. This analysis identifies comparison sets, not winners. See the comparison questions below.
5. **Small operational details can change the design.** A ClickUp webhook stops triggering if its creator is disabled; the documented Elastic–Bedrock adapter requires endpoint recreation to change its key pair. Ownership, offboarding and rotation belong in the acceptance plan. [ClickUp](https://developer.clickup.com/docs/webhooks), [Elastic](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-amazonbedrock).
6. **Training, data preparation and evaluation are separate workstreams.** DataCamp, Macgence and Applause illustrate these roles. Course completion, an annotated dataset and a successful agent task are different deliverables and should have different acceptance criteria. [DataCamp](https://www.datacamp.com/business/), [Macgence](https://macgence.com/our-company/about-us/), [Applause](https://www.applause.com/agentic-ai-testing/).

### Read this in the order you need

- **Business owner:** [layer map](#the-layer-map) → [workflow examples](#three-workflows-to-make-the-map-useful) → [procurement checklist](#before-a-pilot-or-purchase).
- **Technical evaluator:** [relationship ledger](#documented-links-and-their-limits) → [overlap comparisons](#where-companies-complement-or-compete) → company-specific questions.
- **Festival visitor:** use stand codes in the [company cards](#company-cards) as a conversation aid; recheck the live floorplan before walking. They are observed labels, not a guarantee of onsite presence.

## The layer map

**Analyst segmentation, not vendor certification.** Roles are nonexclusive; a company can span several layers. Rows describe the decision in scope, not the entirety of each vendor’s portfolio.

| Layer | What it contributes | Companies in this sample | Boundary to settle |
|---|---|---|---|
| ☁️ Build and run | Models, compute, agent runtime | AWS; Alibaba Cloud | Region, identities, runtime/model billing, observability |
| 🗂️ Govern and retrieve | Data, metadata, meaning, search | Snowflake; Atlan; Elastic; Apgar | Source permissions, lineage, freshness, index location |
| ⚙️ Deliver business work | Tasks, documents, engineered processes | ClickUp; ONLYOFFICE; XenonStack; Sia | System of record, approval, write ownership, IP |
| 🎙️ Converse | Voice and customer-dialogue interfaces | ElevenLabs; Haptik | Consent, caller identity, handoff, tool correctness |
| 🏢 Act in physical spaces | Building orchestration and connected hardware | PlaceOS; Smart Spaces; Watergate | Commissioning, fail-safe design, local control |
| 🧪 Assure and enable | Testing, data preparation, workforce capability | Applause; Macgence; DataCamp | Test/data ownership, reviewer quality, measurable learning |

The map suggests a **workflow-first assembly method**: define a business result → identify the system of record → choose the access and execution boundary → select only the components required → measure end-to-end success. It does **not** imply that all six layers need a separate vendor or that every pair integrates.

## Documented links and their limits

“Documented” means a named capability appears in a primary vendor source, not that we reproduced it. A partner-directory statement is distinguished from technical setup documentation.

| Pair | Evidence level | Supported conclusion | What cannot be inferred |
|---|---|---|---|
| Atlan ↔ Snowflake | Technical connector documentation | Metadata/catalog and lineage integration has a documented setup. [Source](https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake) | Every asset is captured; every downstream user inherits source permissions. |
| Elastic ↔ AWS | Technical inference API documentation | An Amazon Bedrock adapter is documented. [Source](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-amazonbedrock) | AgentCore is integrated by this adapter; all models/regions work; a customer deployment exists. |
| Elastic ↔ Alibaba Cloud | Technical inference API documentation | AlibabaCloud **AI Search** is supported through a specific inference service. [Source](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-alibabacloud) | Universal compatibility with Model Studio, every Qwen endpoint or every region. |
| Smart Spaces ↔ Watergate | Named vendor integration-partner page | Watergate water-management data/control is described as API-integrated into Smart Spaces. [Source](https://www.smartspaces.app/our-partners/watergate/) | A particular installation works, savings are proven, or the floorplan legal identities are resolved. |
| XenonStack ↔ Snowflake | Advertised integration offering | XenonStack markets Snowflake AI Agents and pre-built connectors. [Source](https://www.xenonstack.com/ai-agents/snowflake-ai-agents/) | Same evidentiary strength as a tested connector, formal partner status or validated customer outcome. |

**Two additional named alliances:** Sia publicly lists AWS and ElevenLabs among its strategic technology alliances. This is a vendor relationship statement, not a connector specification or a promise of local delivery. [Current Sia AI page](https://www.sia-partners.com/en/about-us/siaai).

**Seven proposed combinations and seven overlap relationships** are separately labelled in [relationships.json](../../data/value-chain/relationships.json). Examples such as ElevenLabs → ClickUp, ElevenLabs → PlaceOS, ONLYOFFICE → Qwen and Apgar → Atlan are **analyst hypotheses**, not announced integrations or partnerships. The existence of APIs on both sides is a reason to test, not a proof of compatibility.

## Where companies complement or compete

The same pair can be complementary in one architecture and alternatives in another. The following judgments are **analyst interpretations of documented scopes**, not market-share analysis.

| Comparison | Where overlap exists | Useful decision question |
|---|---|---|
| AWS / Alibaba Cloud | Cloud, models and application-platform spend | Which exact workload, region, model, security boundary and total operating cost fits? Do not compare brand-level feature counts. |
| Elastic / Snowflake | Retrieval for AI assistants | Is the corpus already governed inside Snowflake, spread across systems, or both? Test entitlement filtering, update/delete latency, relevance and cost on the same corpus. |
| ElevenLabs / Haptik | Customer-facing voice and tool-using conversations | Are voice control and programmable tools decisive, or is the requirement a particular channel/CRM/human-handoff combination? Evaluate the complete journey. |
| PlaceOS / Smart Spaces | Workplace and building orchestration | Which installed devices, drivers, commissioning obligations and local/offline behaviors match the site? Watergate may complement either conceptually, but only the Smart Spaces link is documented here. |
| Applause / Macgence | Human-supported evaluation and data services | Are we buying dataset production, model feedback, adversarial testing, application QA or release acceptance? Require a separate scope and acceptance test for each. |
| Apgar / Sia / XenonStack | Portions of data/AI implementation and transformation | Which team actually delivers, what is product versus custom code, who owns IP, and who operates the result? |
| ClickUp / ONLYOFFICE | Some document collaboration and work-context needs | Is the primary requirement managing work or embedding a document editor? Limited overlap is not evidence that the products are substitutes. |

Use the linked sources in the company cards for each comparison. **Unknown across the sample:** comparable pricing, negotiated terms, current implementation capacity, local support, actual buyer budget, readiness to partner and performance on the same workload.

## Three workflows to make the map useful

All three are **illustrative reference designs, not customer case studies**. No outcome, savings figure or deployment success is claimed. Products joined by a proposed step still require integration testing, contractual review and explicit authorization for real actions.

### 1. A governed operations assistant

**Question:** “Which delivery commitments are at risk, and can we prepare follow-up tasks?”

1. Start with a narrowly approved operational dataset in **Snowflake**. Define which user may access which records before adding a conversational interface.
2. Use **Atlan** for catalog/meaning/lineage where justified. Its Snowflake connector is documented; the authorization design of the final assistant is still your responsibility.
3. Choose a retrieval path: **Cortex Search** for an appropriate Snowflake-centric design, or **Elastic** for a design that warrants a separate search index. Do not install both merely because both are in the map.
4. If Elastic is chosen, evaluate a documented **Bedrock** or **AlibabaCloud AI Search** inference adapter. This does not require, or prove, an AgentCore combination.
5. Produce a cited answer and a **draft** follow-up task. A custom backend may write to **ClickUp** only after the chosen approval/permission checks. This cross-product workflow is hypothetical.

**Evidence required before release:** a two-user entitlement test; relevant/irrelevant retrieval cases; stale and deleted source records; unsupported questions that trigger abstention; duplicate webhook delivery; a disabled integration owner; and replayable action logs. Measure answer grounding, authorized-task completion, unauthorized-action attempts, latency and cost per successful task. Agree thresholds with the business owner; none were benchmarked here.

**Why this chain matters:** catalog meaning, retrieval quality and action permission are three different responsibilities. Buying one does not remove the other two.

### 2. A conversation that produces usable work

**Question:** “Can a caller report a service problem without losing details between conversation and operations?”

1. Select **ElevenLabs or Haptik** against the actual language, channel, interruption and handoff requirements. Treat them initially as alternatives, not an assumed voice-engine/platform partnership.
2. Connect an approved backend to the chosen conversation platform. The backend validates required fields and checks identity; it does not trust a spoken instruction as authorization by itself.
3. Create a draft **ClickUp** task, optionally with an **ONLYOFFICE** document for structured review. These connections are proposed custom work, not verified native integrations in this study.
4. Ask **Applause** or another qualified evaluator to quote a scoped acceptance program if external validation is needed. **Macgence** may fit a separate consented data/annotation requirement. Avoid buying the same evaluation scope twice.
5. Use **DataCamp** or a suitable internal program for role-specific enablement, while retaining a separate operational adoption measure.

**Evidence required:** synthetic or properly consented conversations, ambiguous requests, wrong identity, accents/languages, interruption, unavailable backend, repeated submissions and successful human escalation. Count completed/correct tasks, harmful or unauthorized actions, missing information and manual rework—not simply call duration or a pleasant voice.

**Why this chain matters:** the value is an accepted operational record and a recoverable exception path, not a conversation that merely sounds successful.

### 3. A water incident in a connected building

**Question:** “Can facilities staff see a water incident, identify the affected area and coordinate a response?”

1. **Watergate** supplies the water-system component; **Smart Spaces** documents an API relationship that can expose water intelligence within the broader building interface.
2. First pilot read-only incident visibility, data freshness and operator acknowledgment. Treat notification-to-task creation as a separate integration to prove.
3. **PlaceOS** is an alternative building-orchestration comparison point. A PlaceOS–Watergate connector was **not** established by this research.
4. If a voice front end is later added, begin with read-only status and routing. Do not give a generative agent unrestricted valve, HVAC or access-control authority.

**Evidence required:** correct asset mapping, stale/lost telemetry behavior, sensor faults, network and power loss, manual override, operator escalation and a documented commissioning/sign-off process. Preserve vendor-engineered protective behavior; do not make essential protection depend on an LLM deciding correctly.

**Why this chain matters:** real-time hardware control has a different risk and support model from text generation. No water-saving or damage-prevention result is asserted for this proposed design.

## Before a pilot or purchase

Use this checklist with any combination above. These are proposed evaluation requirements, not claims that a vendor lacks the capability.

- **Outcome:** What specific action or decision improves, for whom, against what baseline?
- **System of record:** Which system owns the final state? Can a failed action be retried safely and reversed where appropriate?
- **Data boundary:** Which content, metadata, transcripts and logs leave each system? Where are they processed, retained and deleted?
- **Identity:** Is access evaluated as the user, a service account or an owner? How are revoked access and employee departures handled?
- **Integration ownership:** Who maintains schemas, API versions, drivers, secrets, rate limits and vendor changes?
- **Human control:** Which actions are read-only, approval-gated, reversible or prohibited? Who handles exceptions?
- **Acceptance:** Which ordinary, ambiguous, adversarial and failure-mode cases must pass? Who can block release?
- **Commercial boundary:** Separate license, cloud/model usage, implementation, data preparation, testing, training and ongoing operations.
- **Evidence of delivery:** Request a demonstration on a consented sample, clear architecture, a support model and relevant references—not only a partner logo.
- **Exit:** Can you export data, prompts/configuration, evaluation sets, logs and custom code under the proposed contract?

## Company cards

The cards compare **advertised capabilities, integration surfaces and buying questions**, not scores. **All 18 names/stands come from the public floorplan baseline.** Website matching is a separate analyst judgment: 16 high-confidence brand matches and two medium-confidence generic-name matches (Smart Spaces, Watergate). **No legal exhibitor entity, contractual relationship with the organizer or onsite presence was independently verified.**

### AWS

**Floorplan label:** AWS · **stand:** H40 · **Website match:** high brand match.

**Commercial form:** Managed cloud platform.

- **Advertised/documented:** Bedrock AgentCore supplies infrastructure for deploying and operating agents across models and frameworks.

- **Integration surface:** Advertised connections include internal APIs, MCP, knowledge bases and Lambda. Elastic separately documents a Bedrock inference endpoint.

- **Analyst boundary:** Not a ready-made company workflow: domain logic, permissions and acceptance tests still need an owner.

- **Ask before buying:** Which AgentCore components and regions meet the workload? Who pays for model calls, runtime, logs and network traffic?

- **Unknown / caveat:** Regional availability and commercial fit not assessed. Agents Classic is closed to new customers; do not design a new pilot around that legacy service.

**Primary sources:** [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/); [Amazon Bedrock Agents documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html); [Create an Amazon Bedrock inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-amazonbedrock).



### Alibaba Cloud

**Floorplan label:** Alibaba Cloud · **stand:** F30 · **Website match:** high brand match.

**Commercial form:** Cloud infrastructure and model platform.

- **Advertised/documented:** Generative-AI infrastructure and Model Studio support model customization and application development around Qwen and other offerings.

- **Integration surface:** Qwen documentation describes OpenAI-compatible APIs and DashScope. Elastic documents AlibabaCloud AI Search, a specific service path.

- **Analyst boundary:** OpenAI compatibility is not proof that every tool-call, streaming or schema behavior is interchangeable.

- **Ask before buying:** Which exact endpoint, model, region and data-processing terms apply? Does the desired Elastic task type exist there?

- **Unknown / caveat:** Region-specific availability, latency, residency and a native integration with ONLYOFFICE remain unverified.

**Primary sources:** [Alibaba Cloud for Generative AI](https://www.alibabacloud.com/en/solutions/generative-ai); [Make your first API call to Qwen](https://www.alibabacloud.com/help/en/model-studio/first-api-call-to-qwen); [Create an AlibabaCloud AI Search inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-alibabacloud).



### Atlan

**Floorplan label:** Atlan · **stand:** H76 · **Website match:** high brand match.

**Commercial form:** Metadata/context software platform.

- **Advertised/documented:** Atlan organizes metadata, business meaning and lineage as enterprise context.

- **Integration surface:** The Snowflake crawler catalogs data assets and mines query history for lineage; direct and self-deployed extraction are documented.

- **Analyst boundary:** A context catalog is not the warehouse, nor proof that an external agent inherits each user’s row-level access.

- **Ask before buying:** What metadata, SQL text and previews leave the source? Who owns definitions and stale-context alerts?

- **Unknown / caveat:** The downstream authorization design and completeness of lineage for this environment are unknown.

**Primary sources:** [Atlan](https://atlan.com/); [How to crawl Snowflake in Atlan](https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake).



### Snowflake

**Floorplan label:** Snowflake · **stand:** G76 · **Website match:** high brand match.

**Commercial form:** Managed data and AI platform.

- **Advertised/documented:** Snowflake combines enterprise data with AI services; Cortex Search supplies hybrid retrieval and reranking.

- **Integration surface:** Atlan has a documented Snowflake connector. Cortex Search exposes a governed service, but searches run with owner’s rights.

- **Analyst boundary:** A warehouse-native search service is not automatically equivalent to application search across many external sources.

- **Ask before buying:** Which data may the service owner read, and how will caller-specific restrictions be enforced and tested?

- **Unknown / caveat:** No entitlement design, region fit, cost model or quality benchmark was validated.

**Primary sources:** [Snowflake for AI](https://www.snowflake.com/en/product/ai/); [Cortex Search documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview); [How to crawl Snowflake in Atlan](https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake).



### Elastic

**Floorplan label:** Elastic · **stand:** G86 · **Website match:** high brand match.

**Commercial form:** Search/observability/security software platform.

- **Advertised/documented:** Elasticsearch provides search and vector retrieval within Elastic’s wider search, observability and security offering.

- **Integration surface:** Official inference APIs document Amazon Bedrock and AlibabaCloud AI Search endpoints and supported task types.

- **Analyst boundary:** A documented model connection does not supply the application’s access-control policy or prove answer quality.

- **Ask before buying:** Where are documents indexed, how are deletions/ACL changes propagated, and which model credentials must rotate?

- **Unknown / caveat:** Corpus-specific relevance, licensing, deployment topology and end-to-end latency remain untested.

**Primary sources:** [Elasticsearch](https://www.elastic.co/elasticsearch); [Create an Amazon Bedrock inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-amazonbedrock); [Create an AlibabaCloud AI Search inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-alibabacloud).



### ClickUp

**Floorplan label:** ClickUp · **stand:** H65 · **Website match:** high brand match.

**Commercial form:** Work-management SaaS.

- **Advertised/documented:** ClickUp combines tasks, projects, collaboration and workspace-context AI.

- **Integration surface:** The developer surface includes API, OAuth, MCP and webhooks; webhook operation depends on the creating user.

- **Analyst boundary:** A destination for operational work, not a replacement for upstream data governance or all document-editing requirements.

- **Ask before buying:** Can a service identity own integration lifecycle? How are duplicate writes, approvals and employee offboarding handled?

- **Unknown / caveat:** A native ElevenLabs–ClickUp connection was not established by this research.

**Primary sources:** [ClickUp Brain](https://clickup.com/brain); [ClickUp developer portal](https://developer.clickup.com/); [ClickUp webhooks](https://developer.clickup.com/docs/webhooks).



### ONLYOFFICE

**Floorplan label:** ONLY OFFICE · **stand:** G82 · **Website match:** high brand match.

**Commercial form:** Embeddable document software.

- **Advertised/documented:** Collaborative editors cover documents, spreadsheets, presentations, forms and PDF.

- **Integration surface:** The developer offering describes JavaScript/REST APIs, WOPI and custom-model integration options.

- **Analyst boundary:** An embedded editor is not the same buying decision as a project-management workspace or model-hosting platform.

- **Ask before buying:** Which license covers embedding? What document content may be sent to the model, and who controls versioning?

- **Unknown / caveat:** Provider-specific compatibility, deployment configuration and custom integration effort were not tested.

**Primary sources:** [ONLYOFFICE Docs Developer](https://www.onlyoffice.com/for-developers).



### ElevenLabs

**Floorplan label:** Eleven Labs · **stand:** H70 · **Website match:** high brand match.

**Commercial form:** Voice/agent software platform.

- **Advertised/documented:** ElevenLabs offers conversational agents as well as voice capabilities.

- **Integration surface:** Tools include webhook, client, code, MCP and system tools; they can connect an agent to external actions.

- **Analyst boundary:** High-quality voice is not by itself proof of correct task execution, human handoff or business-system permissions.

- **Ask before buying:** How are identity, consent, handoff, interruptions, tool failures and multilingual task success evaluated?

- **Unknown / caveat:** Native Haptik, ClickUp or PlaceOS integrations were not verified; custom composition remains a hypothesis.

**Primary sources:** [ElevenLabs Agents](https://elevenlabs.io/agents); [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools).



### Haptik

**Floorplan label:** Haptik AI · **stand:** G77 · **Website match:** high brand match.

**Commercial form:** Customer-conversation platform and services.

- **Advertised/documented:** Haptik advertises service and sales agents, voice and messaging channels.

- **Integration surface:** Its integration directory names CRM, helpdesk, knowledge-base and messaging systems, including human-agent handoff paths.

- **Analyst boundary:** Overlap with ElevenLabs is real at voice-agent workflows; neither is assumed to be merely the other’s component.

- **Ask before buying:** Which channel and CRM combination is native, what requires services, and can handoff preserve state?

- **Unknown / caveat:** Connector editions, write scopes, local channel constraints and comparative voice quality are unknown.

**Primary sources:** [Jio Haptik](https://www.haptik.ai/); [Haptik integrations](https://www.haptik.ai/platform/integrations).



### PlaceOS

**Floorplan label:** PlaceOS · **stand:** S51 · **Website match:** high brand match.

**Commercial form:** Workplace integration/automation platform.

- **Advertised/documented:** PlaceOS connects workplace and building systems for room, space and device workflows.

- **Integration surface:** Drivers and APIs cover AV, HVAC, access, sensors and calendars.

- **Analyst boundary:** Workplace orchestration does not replace the installed field devices, commissioning or physical safety controls.

- **Ask before buying:** Which installed hardware/firmware is certified, what runs locally, and who maintains each driver?

- **Unknown / caveat:** A Watergate or ElevenLabs connector, offline behavior and site-specific support have not been verified.

**Primary sources:** [PlaceOS](https://www.placeos.com/).



### Smart Spaces

**Floorplan label:** Smart Spaces · **stand:** S157 · **Website match:** medium brand match.

**Commercial form:** Building/workplace platform plus integration services.

- **Advertised/documented:** Smart Building OS combines building-system data, operational interfaces and digital-twin functions.

- **Integration surface:** Smart Spaces documents Watergate as an API integration partner; it also offers software-systems integration services.

- **Analyst boundary:** A building-wide orchestration layer overlaps PlaceOS, while Watergate is a more specific water-control component.

- **Ask before buying:** What is included in software versus commissioning? Which controls need local fail-safe behavior?

- **Unknown / caveat:** Generic floorplan name: brand identity is a medium-confidence match, not an organizer-linked website verification.

**Primary sources:** [Smart Building OS](https://www.smartspaces.app/smart-building-os/); [Software Systems Integrator](https://www.smartspaces.app/software-systems-integrator/); [Watergate: Integration Partner](https://www.smartspaces.app/our-partners/watergate/).



### Watergate

**Floorplan label:** Watergate · **stand:** S159 · **Website match:** medium brand match.

**Commercial form:** Connected water hardware and software.

- **Advertised/documented:** Sonic water valves, a server, mobile app and dashboard support leak detection and water-management workflows.

- **Integration surface:** Cloud and local APIs are documented; the local API includes reading and changing valve state. Smart Spaces names an API integration.

- **Analyst boundary:** A water-control component is not a general enterprise agent, and physical actions need a different safety boundary from task creation.

- **Ask before buying:** Which valve sizes and installation constraints fit the site? What happens on network loss, power failure and manual override?

- **Unknown / caveat:** Medium-confidence brand match from the generic label; local procurement, approvals and measured savings are unverified.

**Primary sources:** [Watergate: Smart water leak detection](https://watergate.ai/); [Watergate developer documentation](https://docs.watergate.ai/home/); [Sonic local API](https://docs.watergate.ai/api/local/); [Watergate: Integration Partner](https://www.smartspaces.app/our-partners/watergate/).



### Applause

**Floorplan label:** Applause · **stand:** G112 · **Website match:** high brand match.

**Commercial form:** Managed testing and evaluation services.

- **Advertised/documented:** Applause describes human/domain-expert AI evaluation and agent testing.

- **Integration surface:** Agent testing covers traces, tool calls, retrieval relevance and end-to-end completion.

- **Analyst boundary:** Buying evaluation is not buying a guarantee of safety; the agreed test distribution and independence matter.

- **Ask before buying:** Who defines failure categories, owns the test set, adjudicates disputed results and approves release?

- **Unknown / caveat:** No independent quality result, local testing coverage or quote was obtained.

**Primary sources:** [Applause AI Evaluation & Benchmarking](https://www.applause.com/ai-evaluation-and-benchmarking/); [Applause Agentic AI Testing](https://www.applause.com/agentic-ai-testing/).



### Macgence

**Floorplan label:** Macgence · **stand:** S63 · **Website match:** high brand match.

**Commercial form:** AI data and human-in-the-loop services.

- **Advertised/documented:** Macgence offers sourcing, annotation, validation, RLHF, language services and model evaluation.

- **Integration surface:** The service portfolio describes dataset preparation and human expertise, not a verified connector to every platform in this map.

- **Analyst boundary:** Useful overlap with Applause exists in evaluation; data-production and application acceptance are different scopes to contract.

- **Ask before buying:** What consent, provenance, licensing, reviewer qualifications and adjudication process accompany each dataset?

- **Unknown / caveat:** Accuracy and workforce-scale marketing claims were not validated or used as comparative scores.

**Primary sources:** [AI training data services](https://macgence.com/); [About Macgence](https://macgence.com/our-company/about-us/).



### DataCamp

**Floorplan label:** DataCamp · **stand:** H62 · **Website match:** high brand match.

**Commercial form:** Learning platform plus enablement services.

- **Advertised/documented:** DataCamp for Business supplies role-based data/AI learning, custom curricula and training delivery options.

- **Integration surface:** Official pages describe SSO, LMS/LXP/HRMS integration and a reporting Data Connector; some integrations require selected enterprise plans.

- **Analyst boundary:** Training completion is not evidence of safe production-agent performance or organizational adoption.

- **Ask before buying:** What baseline skill assessment, role-specific exercise and post-training task outcome will count as success?

- **Unknown / caveat:** Actual learner outcomes, integration entitlement and customer-specific content controls were not assessed.

**Primary sources:** [DataCamp for Business](https://www.datacamp.com/business/); [LMS, SSO and Enterprise Integrations](https://www.datacamp.com/business/integration).



### Apgar Group

**Floorplan label:** Apgar Group · **stand:** G71 · **Website match:** high brand match.

**Commercial form:** Data/AI advisory and implementation; packaged solutions.

- **Advertised/documented:** Apgar offers data quality, master/metadata management, integration and AI services; its portfolio also includes ApgarIA solutions.

- **Integration surface:** Integration services cover architecture, vendor assessment, implementation and platform operation.

- **Analyst boundary:** Implementation expertise complements platform products but is not proof of a named Atlan/Snowflake partnership.

- **Ask before buying:** Which deliverables are consulting, licensed software and ongoing operations? Who owns data rules and integration IP?

- **Unknown / caveat:** Named-company delivery references, staffing, support terms and a compatible packaged SKU are unverified.

**Primary sources:** [Apgar: Data and AI partner](https://apgar-group.com/); [Data Quality Management](https://apgar-group.com/our-expertise/data-quality/); [Data Integration](https://apgar-group.com/our-expertise/data-integration/).



### Sia Partners

**Floorplan label:** SIA Partners · **stand:** H84 · **Website match:** high brand match.

**Commercial form:** Consulting, engineering and packaged AI solutions.

- **Advertised/documented:** Sia Applied Intelligence and Sia Forward combine enterprise-AI design, engineering and change management; the site also describes an Agent Store.

- **Integration surface:** Sia publicly lists AWS and ElevenLabs among strategic technology alliances; no specific joint connector is documented on that page.

- **Analyst boundary:** Services, accelerators and deployable products need separate acceptance and ownership terms.

- **Ask before buying:** Which asset is deployable in our environment, who owns source/IP, and how is success measured beyond a workshop?

- **Unknown / caveat:** The floorplan says SIA Partners; the official legacy Heka URL redirects to Sia AI. Legal exhibitor identity remains unverified.

**Primary sources:** [Sia AI](https://www.sia-partners.com/en/about-us/siaai).



### XenonStack

**Floorplan label:** Xenonstack · **stand:** G91 · **Website match:** high brand match.

**Commercial form:** Engineering/managed services and agent-platform offerings.

- **Advertised/documented:** XenonStack advertises orchestration, analytics, infrastructure automation and governance offerings.

- **Integration surface:** Its Snowflake AI Agents page advertises pre-built connectors; this is a vendor offering, not a reproduced integration test.

- **Analyst boundary:** A service/accelerator proposal should not be compared to a cloud-service unit price without delivery scope.

- **Ask before buying:** Can a working connector, production reference and clear support/IP split be demonstrated for the exact workflow?

- **Unknown / caveat:** Partner status, connector maturity, installation process and customer results were not independently verified.

**Primary sources:** [XenonStack](https://www.xenonstack.com/); [XenonStack Snowflake AI Agents](https://www.xenonstack.com/ai-agents/snowflake-ai-agents/).


## Method and evidence rules

1. **Start with the public baseline.** The [official floorplan page](https://dubaiaifestival.com/floorplan/) embeds a [public interactive plan](https://floorplan.live/interactive/shows/4608/views/2/plan). The baseline captured labels/stands at **2026-10-26 03:30:39 UTC** and classified 248 organization candidates. Candidate count is not a count of verified legal companies.
2. **Select for decision value.** Retain the 12 seed profiles; add Apgar, DataCamp, Macgence, Sia, Smart Spaces and Watergate to expose implementation, skills, data services and a specific building-integration chain. Selection favors evidence-rich examples, so it is not representative of the full startup/exhibitor population.
3. **Match brands separately.** An official vendor website establishes that vendor’s offering; a floorplan label establishes a label. They do not jointly prove the exhibitor’s legal identity. Generic names receive lower match confidence. No private app, attendee list, messages or contact data was used.
4. **Use primary sources.** Technical documentation supports a documented interface; a product page supports an advertised capability; a partner page supports a named vendor relationship. None alone validates performance, availability for a specific customer or a successful deployment.
5. **Label interpretation.** Segmentation, competitive overlap, buyer questions and proposed workflows are analysis. A missing confirmation means “not established in this review,” not “does not exist.”
6. **Preserve limits.** No pricing comparison, hands-on benchmark, security audit, legal/compliance conclusion, contract review or customer reference check was performed. All regional, licensing, residency, support and safety requirements need workload-specific validation.
7. **Handle changing pages.** Sources were retrieved on 26 October 2026. The Sia legacy redirect and direct page differed; final claims use the direct current page. The Qwen console documentation exceeded the fetch limit and Macgence’s home-page direct fetch timed out; official search extracts and alternate official pages are explicitly noted in the ledger.

### Evidence classes

| Label | Meaning | Do not upgrade it to |
|---|---|---|
| Public floorplan observation | A named label/stand was visible | Legal entity, attendance, interest or endorsement |
| Technical documentation | A connector/API behavior is specified | Reproduced integration or deployment success |
| Vendor integration / alliance listing | A vendor names a relationship | Full feature coverage or local commercial commitment |
| Advertised offering | A vendor says it supplies something | Independently validated quality, ROI or maturity |
| Analyst hypothesis / overlap | A reasoned possible combination or comparison | Existing partnership, integration or buyer demand |

### Reusable research assets

- [18 structured bilingual company cards](../../data/value-chain/companies.json)
- [Company comparison CSV](../../data/value-chain/company-comparison.csv)
- [21 classified relationship records](../../data/value-chain/relationships.json)
- [Claim/source evidence ledger](../../data/value-chain/evidence-ledger.json)
- [Source register](../../data/value-chain/sources.json)

The ledger uses stable claim IDs and JSON references to the company/relationship text, so claims can be checked without treating a repeated paraphrase as separate evidence.

## Source register

All links below were retrieved or rechecked on **2026-10-26**. Most were read directly; search-extract exceptions and inherited-baseline provenance are recorded in JSON. Source count is not a quality score.

| Source ID | Official page | Evidence locator |
|---|---|---|
| `aws-agentcore` | [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) | Overview; Connect across your stack; Debug faster |
| `aws-classic` | [Amazon Bedrock Agents documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) | Maintenance-mode notice at top |
| `alibaba-genai` | [Alibaba Cloud for Generative AI](https://www.alibabacloud.com/en/solutions/generative-ai) | Overview; GenAI Development; Model Studio |
| `alibaba-qwen-api` | [Make your first API call to Qwen](https://www.alibabacloud.com/help/en/model-studio/first-api-call-to-qwen) | Opening description; API compatibility |
| `atlan-home` | [Atlan](https://atlan.com/) | Enterprise Context Layer; business systems; enterprise customers |
| `clickup-brain` | [ClickUp Brain](https://clickup.com/brain) | AI tasks, projects and workspace context |
| `clickup-api` | [ClickUp developer portal](https://developer.clickup.com/) | Public API; MCP; webhooks; OAuth |
| `clickup-webhooks` | [ClickUp webhooks](https://developer.clickup.com/docs/webhooks) | Scope; signature; task events |
| `elastic-product` | [Elasticsearch](https://www.elastic.co/elasticsearch) | Search; observability; security; deployment options |
| `eleven-agents` | [ElevenLabs Agents](https://elevenlabs.io/agents) | Support, sales and operational use cases; configuration and testing |
| `eleven-tools` | [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools) | Client, webhook, code, MCP and system tools |
| `snowflake-ai` | [Snowflake for AI](https://www.snowflake.com/en/product/ai/) | Data agents; unstructured data; ML workflows |
| `snowflake-search` | [Cortex Search documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview) | Overview; use cases; REST API example |
| `haptik-home` | [Jio Haptik](https://www.haptik.ai/) | Support, sales, booking and lead qualification agents; industries |
| `haptik-integrations` | [Haptik integrations](https://www.haptik.ai/platform/integrations) | CRM and live chat; API integration; Salesforce, HubSpot and Zendesk |
| `onlyoffice-developer` | [ONLYOFFICE Docs Developer](https://www.onlyoffice.com/for-developers) | Embedded editing; APIs; connectors; AI-ready |
| `applause-eval` | [Applause AI Evaluation & Benchmarking](https://www.applause.com/ai-evaluation-and-benchmarking/) | Evaluation service; enterprise QA; domain experts |
| `applause-agentic` | [Applause Agentic AI Testing](https://www.applause.com/agentic-ai-testing/) | Trace, tool-call, retrieval and task-completion evaluation |
| `placeos-home` | [PlaceOS](https://www.placeos.com/) | Platform overview; products; drivers and APIs |
| `xenon-home` | [XenonStack](https://www.xenonstack.com/) | Foundry; domains; integration list |
| `xenon-snowflake` | [XenonStack Snowflake AI Agents](https://www.xenonstack.com/ai-agents/snowflake-ai-agents/) | Integration offering; use cases; not a verified performance benchmark |
| `atlan-snowflake-crawl` | [How to crawl Snowflake in Atlan](https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake) | Opening description; Provide credentials; Configure connection; Configure crawler |
| `elastic-bedrock-api` | [Create an Amazon Bedrock inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-amazonbedrock) | Endpoint overview; required authorization; task_type; key rotation note |
| `elastic-alibaba-api` | [Create an AlibabaCloud AI Search inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-alibabacloud) | Endpoint overview; task_type; request examples |
| `apgar-home` | [Apgar: Data and AI partner](https://apgar-group.com/) | Expertise; Business Solutions; ApgarIA |
| `apgar-quality` | [Data Quality Management](https://apgar-group.com/our-expertise/data-quality/) | Data Quality Management: Build Trusted Data Across Your Organization |
| `apgar-integration` | [Data Integration](https://apgar-group.com/our-expertise/data-integration/) | How we can help you; Functional Architecture; Software Architecture |
| `datacamp-business` | [DataCamp for Business](https://www.datacamp.com/business/) | Enterprise-wide learning; custom curriculum; blended learning |
| `datacamp-integration` | [LMS, SSO and Enterprise Integrations](https://www.datacamp.com/business/integration) | SSO; LMS/LXP/HRMS integrations; Data Connector; FAQ plan limitation |
| `macgence-home` | [AI training data services](https://macgence.com/) | AI Training Data; Language Services; Build AI |
| `macgence-about` | [About Macgence](https://macgence.com/our-company/about-us/) | AI Data Services, Language Services, AI Engineering; human-in-the-loop |
| `sia-ai` | [Sia AI](https://www.sia-partners.com/en/about-us/siaai) | Sia Applied Intelligence; Agent Store; Sia Forward; Our Tech accelerators. Direct /siaai read used over the older /heka redirect snapshot. |
| `smartspaces-os` | [Smart Building OS](https://www.smartspaces.app/smart-building-os/) | Facility Management; Analytics; Digital Twin; Master Systems Integrator |
| `smartspaces-ssi` | [Software Systems Integrator](https://www.smartspaces.app/software-systems-integrator/) | What is an SSI?; Validating your building networks |
| `smartspaces-watergate` | [Watergate: Integration Partner](https://www.smartspaces.app/our-partners/watergate/) | Integration Partner; Technical compatibility: API; integration description |
| `watergate-home` | [Watergate: Smart water leak detection](https://watergate.ai/) | Products: Sonic, Server, Mobile App, Dashboard; integrations navigation |
| `watergate-docs` | [Watergate developer documentation](https://docs.watergate.ai/home/) | Cloud API; Local API; reference materials |
| `watergate-local` | [Sonic local API](https://docs.watergate.ai/api/local/) | Get valve state; Set valve state |
