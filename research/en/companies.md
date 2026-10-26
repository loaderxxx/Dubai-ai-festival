# Initial company research

[English](../../research/en/companies.md) · [Русский](../../research/ru/companies.md)

First research batch selected for visible relevance to business-system integration, automation, data infrastructure and enterprise AI assurance. Not a ranked lead list or validated sales pipeline.

Reviewed: 2026-10-26.

Facts below summarize official vendor claims. They do not validate performance, legal exhibitor identity, attendance, buying intent or partnership interest. Target buyer roles and collaboration angles are explicitly hypotheses.

## AWS

Floorplan: **AWS — H40**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **aws-offering**: AgentCore provides infrastructure for deploying and operating production AI agents across models and frameworks. ([Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/); 2026-10-26).
- **aws-integration**: Its documented integration scope includes MCP servers, internal APIs, knowledge bases and Lambda, with authentication and access controls. ([Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/); 2026-10-26).
- **aws-users**: The page addresses developers moving agents from prototypes into production. ([Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/); 2026-10-26).
- **aws-caveat**: The separate Bedrock Agents Classic documentation says it is closed to new customers and directs them to AgentCore. ([Amazon Bedrock Agents documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html); 2026-10-26).

### Hypotheses — validate in discussion

- Explore a governed business-system agent pilot; choose the current service before architecture work.
- Buyer roles to verify: Platform engineering or enterprise AI leaders.
- Question: Which regional deployment, tool-permission and evaluation requirements must a pilot meet?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## Alibaba Cloud

Floorplan: **Alibaba Cloud — F30**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **alibaba-offering**: Alibaba Cloud describes infrastructure, model development and deployment services; Model Studio hosts Qwen models and supports application development. ([Alibaba Cloud for Generative AI](https://www.alibabacloud.com/en/solutions/generative-ai); 2026-10-26).
- **alibaba-integration**: Official Qwen documentation describes OpenAI-compatible APIs and the DashScope SDK. ([Make your first API call to Qwen](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/first-api-call-to-qwen); 2026-10-26).
- **alibaba-users**: The generative-AI solution targets businesses building or customizing models and AI applications. ([Alibaba Cloud for Generative AI](https://www.alibabacloud.com/en/solutions/generative-ai); 2026-10-26).

### Hypotheses — validate in discussion

- Evaluate Qwen as a candidate model backend for a document or workflow product; compatibility still needs testing.
- Buyer roles to verify: AI application engineering or cloud-platform owners.
- Question: Which model, region and API features are available for our exact workflow?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## Atlan

Floorplan: **Atlan — H76**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **atlan-offering**: Atlan offers an enterprise context layer combining data structure, business semantics, lineage and organizational knowledge for AI use. ([Atlan](https://atlan.com/); 2026-10-26).
- **atlan-integration**: Its connector documentation names Snowflake and describes custom connectors through the App Framework and SDK. ([Atlan connectors](https://atlan.com/connectors/); 2026-10-26).
- **atlan-users**: The product addresses enterprise data and AI teams, including developers, partners and system integrators extending connectors. ([Atlan connectors](https://atlan.com/connectors/); 2026-10-26).

### Hypotheses — validate in discussion

- Explore governed context for a Snowflake-based business assistant rather than assuming the connector solves end-user authorization.
- Buyer roles to verify: Data platform, governance or enterprise AI leaders.
- Question: How are business definitions, freshness and end-user permissions exposed to downstream agents?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## ClickUp

Floorplan: **ClickUp — H65**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **clickup-offering**: ClickUp combines work-management features with contextual AI for tasks, projects and team collaboration. ([ClickUp Brain](https://clickup.com/brain); 2026-10-26).
- **clickup-integration**: The developer portal provides a public API, MCP server, OAuth and event webhooks. ([ClickUp developer portal](https://developer.clickup.com/); 2026-10-26).
- **clickup-control**: Webhook subscriptions are tied to the creating user; documentation specifies signed events and task-related event types. ([ClickUp webhooks](https://developer.clickup.com/docs/webhooks); 2026-10-26).

### Hypotheses — validate in discussion

- Test conversation-to-task automation with explicit approvals, deduplication and an auditable write path.
- Buyer roles to verify: Operations, project-management or workspace platform owners.
- Question: Which task actions may an external agent perform, and who owns its OAuth and webhook lifecycle?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## Elastic

Floorplan: **Elastic — G86**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **elastic-offering**: Elastic offers search and vector retrieval, observability and security capabilities built around Elasticsearch. ([Elasticsearch](https://www.elastic.co/elasticsearch); 2026-10-26).
- **elastic-integration**: Elastic publicly lists AWS and Alibaba Cloud in its AI ecosystem. This alone does not establish a specific deployed integration. ([Elastic AI Ecosystem](https://www.elastic.co/partners/ai-ecosystem); 2026-10-26).
- **elastic-users**: Its advertised use cases include search applications, customer support search, infrastructure monitoring and security operations. ([Elasticsearch](https://www.elastic.co/elasticsearch); 2026-10-26).

### Hypotheses — validate in discussion

- Explore an access-controlled retrieval and observability layer for an enterprise agent.
- Buyer roles to verify: Search engineering, SRE or security-platform leaders.
- Question: Which connector, permission model and retrieval-quality benchmark apply to the proposed data sources?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## ElevenLabs

Floorplan: **Eleven Labs — H70**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **eleven-offering**: ElevenLabs offers conversational agents for customer support, sales and operational workflows. ([ElevenLabs Agents](https://elevenlabs.io/agents); 2026-10-26).
- **eleven-integration**: Its agent tools include external API webhooks, client actions and MCP integrations. ([ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools); 2026-10-26).
- **eleven-testing**: The product describes agent simulations, automated behavioral tests and monitoring. ([ElevenLabs Agents](https://elevenlabs.io/agents); 2026-10-26).

### Hypotheses — validate in discussion

- Prototype a voice front end that proposes approved actions in a business system rather than unrestricted writes.
- Buyer roles to verify: Customer-experience, operations or application-platform leaders.
- Question: How are identity, human handoff, tool authorization and measurable task completion implemented?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## Snowflake

Floorplan: **Snowflake — G76**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **snowflake-offering**: Snowflake offers data agents, unstructured-data analysis and ML workflows within its governed data platform. ([Snowflake for AI](https://www.snowflake.com/en/product/ai/); 2026-10-26).
- **snowflake-integration**: Cortex Search supports hybrid retrieval for RAG and enterprise search; documentation includes REST API queries. ([Cortex Search documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview); 2026-10-26).
- **snowflake-users**: The offerings target enterprises building applications and analytical workflows on their existing data. ([Snowflake for AI](https://www.snowflake.com/en/product/ai/); 2026-10-26).

### Hypotheses — validate in discussion

- Evaluate a governed knowledge backend for business assistants, with an explicit permission and freshness test.
- Buyer roles to verify: Data platform, analytics or enterprise AI leaders.
- Question: Which datasets, retrieval scopes and region-specific AI services are allowed in the pilot?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## Haptik AI / Jio Haptik

Floorplan: **Haptik AI — G77**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **haptik-offering**: Haptik markets agents for customer service, sales, bookings and lead qualification across conversational channels. ([Jio Haptik](https://www.haptik.ai/); 2026-10-26).
- **haptik-integration**: Its integration catalog names Salesforce, HubSpot and Zendesk, and describes connections to API-enabled software. ([Haptik integrations](https://www.haptik.ai/platform/integrations); 2026-10-26).
- **haptik-users**: The integration page addresses support, sales, marketing and customer-engagement teams. ([Haptik integrations](https://www.haptik.ai/platform/integrations); 2026-10-26).

### Hypotheses — validate in discussion

- Explore CRM-connected service automation; compare overlap with other voice-agent platforms before assuming partnership fit.
- Buyer roles to verify: Customer service, CX or revenue-operations leaders.
- Question: Which integrations are native, how does human handoff work, and what is the required deployment model?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## ONLYOFFICE

Floorplan: **ONLY OFFICE — G82**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **onlyoffice-offering**: ONLYOFFICE provides embeddable collaborative editors for documents, spreadsheets, presentations, forms and PDF. ([ONLYOFFICE Docs Developer](https://www.onlyoffice.com/for-developers); 2026-10-26).
- **onlyoffice-integration**: The developer offering lists JavaScript and REST APIs, WOPI, connectors and integrations with custom language models. ([ONLYOFFICE Docs Developer](https://www.onlyoffice.com/for-developers); 2026-10-26).
- **onlyoffice-users**: It targets developers embedding editing into their own applications. ([ONLYOFFICE Docs Developer](https://www.onlyoffice.com/for-developers); 2026-10-26).

### Hypotheses — validate in discussion

- Test an AI-assisted document workflow with a selected model backend; API compatibility is not a verified integration.
- Buyer roles to verify: Software product or document-platform owners.
- Question: What deployment, licensing and document-permission boundaries apply to embedding and AI calls?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## Applause

Floorplan: **Applause — G112**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **applause-offering**: Applause provides managed AI evaluation combining automated assessment and human/domain-expert review. ([Applause AI Evaluation & Benchmarking](https://www.applause.com/ai-evaluation-and-benchmarking/); 2026-10-26).
- **applause-evaluation**: Its agent-testing service describes trace assessment, tool-call correctness, retrieval relevance and end-to-end task completion. ([Applause Agentic AI Testing](https://www.applause.com/agentic-ai-testing/); 2026-10-26).
- **applause-users**: The evaluation program is presented for enterprise AI and quality-assurance teams. ([Applause AI Evaluation & Benchmarking](https://www.applause.com/ai-evaluation-and-benchmarking/); 2026-10-26).

### Hypotheses — validate in discussion

- Explore independent acceptance testing for a voice or business-system agent pilot.
- Buyer roles to verify: AI product, quality engineering or responsible-AI owners.
- Question: Can the program measure task success and unsafe-action rates using consented, non-sensitive test cases?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## PlaceOS

Floorplan: **PlaceOS — S51**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **placeos-offering**: PlaceOS offers integration and automation for workplaces, rooms, buildings and digital displays. ([PlaceOS](https://www.placeos.com/); 2026-10-26).
- **placeos-integration**: Its drivers connect AV, HVAC, access control, sensors and calendars; APIs expose configured integrations and actions. ([PlaceOS](https://www.placeos.com/); 2026-10-26).
- **placeos-users**: The site supports teams building their own workplace applications and delivery through PlaceOS partners. ([PlaceOS](https://www.placeos.com/); 2026-10-26).

### Hypotheses — validate in discussion

- Explore a voice-assisted room-booking or facilities workflow with safety-gated actions.
- Buyer roles to verify: Workplace technology, facilities or smart-building platform owners.
- Question: Which actions are read-only, approval-gated or prohibited, and how is occupancy data minimized?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

## XenonStack

Floorplan: **Xenonstack — G91**. [Public source](https://dubaiaifestival.com/floorplan/).

### Publicly documented offering and interfaces

- **xenon-offering**: XenonStack markets agent orchestration, analytics, infrastructure automation and security/governance offerings. ([XenonStack](https://www.xenonstack.com/); 2026-10-26).
- **xenon-integration**: Its site advertises Snowflake AI Agents and lists ServiceNow, SAP, Jira and Oracle-oriented agent integrations. ([XenonStack](https://www.xenonstack.com/); [XenonStack Snowflake AI Agents](https://www.xenonstack.com/ai-agents/snowflake-ai-agents/); 2026-10-26).
- **xenon-users**: Advertised domains include IT operations, finance, risk, analytics and security. ([XenonStack](https://www.xenonstack.com/); 2026-10-26).

### Hypotheses — validate in discussion

- Explore an implementation or co-delivery discussion for a narrowly scoped enterprise-agent workflow.
- Buyer roles to verify: Enterprise transformation, IT operations or data-platform leaders.
- Question: Which production references, connector ownership and support responsibilities can be demonstrated?

Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.

