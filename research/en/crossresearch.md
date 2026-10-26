# Cross-company research

[English](../../research/en/crossresearch.md) · [Русский](../../research/ru/crossresearch.md)

A graph edge is not a confirmed commercial relationship. Documented vendor links, analyst complementarity hypotheses and competitive overlap are separate types.

Reviewed: 2026-10-26.

## x01 · Atlan ↔ Snowflake

**documented_vendor_integration**

Atlan names a Snowflake connector. This is a documented product connection, not proof of a new joint commercial opportunity.

Validation question: Which metadata, lineage and authorization requirements remain for the proposed agent use case?

Boundary: A metadata connector is not end-to-end row-level authorization.

Evidence: `atlan-integration`, `snowflake-offering`. [Atlan connectors](https://atlan.com/connectors/); [Snowflake for AI](https://www.snowflake.com/en/product/ai/) (2026-10-26).

## x02 · Elastic ↔ AWS

**documented_vendor_ecosystem_listing**

Elastic lists AWS in its AI ecosystem; the exact integration and joint-delivery terms require separate confirmation.

Validation question: Which supported retrieval and observability integration fits AgentCore in the selected region?

Boundary: Do not infer a specific connector, certification or commercial agreement from a list entry.

Evidence: `elastic-integration`, `aws-offering`. [Elastic AI Ecosystem](https://www.elastic.co/partners/ai-ecosystem); [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) (2026-10-26).

## x03 · Elastic ↔ Alibaba Cloud

**documented_vendor_ecosystem_listing**

Elastic lists Alibaba Cloud in its AI ecosystem; a Qwen-backed retrieval design is a separate technical hypothesis.

Validation question: Which supported model endpoint, embedding path and deployment region apply?

Boundary: Model and infrastructure availability may vary by region.

Evidence: `elastic-integration`, `alibaba-offering`. [Elastic AI Ecosystem](https://www.elastic.co/partners/ai-ecosystem); [Alibaba Cloud for Generative AI](https://www.alibabacloud.com/en/solutions/generative-ai) (2026-10-26).

## x04 · XenonStack ↔ Snowflake

**vendor_advertised_integration_offering**

XenonStack advertises Snowflake-oriented agents. This is unilateral offering evidence, not a verified formal partnership.

Validation question: Can they demonstrate a production reference and define ownership of connectors, governance and support?

Boundary: Marketing capabilities and outcome figures are not independently validated.

Evidence: `xenon-integration`, `snowflake-offering`. [XenonStack](https://www.xenonstack.com/); [XenonStack Snowflake AI Agents](https://www.xenonstack.com/ai-agents/snowflake-ai-agents/); [Snowflake for AI](https://www.snowflake.com/en/product/ai/) (2026-10-26).

## x05 · ElevenLabs ↔ ClickUp

**complementarity_hypothesis**

A voice agent could propose or create approved work items through ClickUp interfaces. No native pairing was verified.

Validation question: Can a sandbox demonstration create one authorized task, reject unauthorized writes and avoid duplicate retries?

Boundary: OAuth scope, webhook-user lifecycle, consent and idempotency need explicit design.

Evidence: `eleven-integration`, `clickup-integration`, `clickup-control`. [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools); [ClickUp developer portal](https://developer.clickup.com/); [ClickUp webhooks](https://developer.clickup.com/docs/webhooks) (2026-10-26).

## x06 · ElevenLabs ↔ PlaceOS

**complementarity_hypothesis**

A voice interface could request room bookings or facilities actions through PlaceOS APIs.

Validation question: Can the pilot restrict actions to booking or requests, with human approval for physical-control changes?

Boundary: Physical access and building control are safety-sensitive; do not grant broad actuation privileges.

Evidence: `eleven-integration`, `placeos-integration`. [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools); [PlaceOS](https://www.placeos.com/) (2026-10-26).

## x07 · Applause ↔ ElevenLabs

**complementarity_hypothesis**

Independent human-led testing could complement platform-native voice-agent evaluations.

Validation question: Can both teams agree on task-success, correct tool-use, handoff and unsafe-action acceptance criteria?

Boundary: No partnership or willingness to share customer test data was established.

Evidence: `applause-evaluation`, `eleven-testing`. [Applause Agentic AI Testing](https://www.applause.com/agentic-ai-testing/); [ElevenLabs Agents](https://elevenlabs.io/agents) (2026-10-26).

## x08 · Applause ↔ Haptik AI / Jio Haptik

**complementarity_hypothesis**

A CRM-connected service-agent pilot could use an external acceptance-testing program.

Validation question: Can support scenarios be tested with synthetic data across channel transitions and human handoffs?

Boundary: Testing coverage must match the actual deployment; it is not a general safety certification.

Evidence: `applause-evaluation`, `haptik-offering`. [Applause Agentic AI Testing](https://www.applause.com/agentic-ai-testing/); [Jio Haptik](https://www.haptik.ai/) (2026-10-26).

## x09 · ONLYOFFICE ↔ Alibaba Cloud

**complementarity_hypothesis**

A custom-model document workflow could evaluate Qwen as one candidate backend. Direct integration was not verified.

Validation question: Does a minimal document workflow preserve permissions, formatting and data-location requirements?

Boundary: OpenAI-compatible APIs do not guarantee full application compatibility or data residency.

Evidence: `onlyoffice-integration`, `alibaba-integration`. [ONLYOFFICE Docs Developer](https://www.onlyoffice.com/for-developers); [Make your first API call to Qwen](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/first-api-call-to-qwen) (2026-10-26).

## x10 · Elastic ↔ ElevenLabs

**complementarity_hypothesis**

A custom agent tool could query an enterprise search service for grounded responses.

Validation question: Can retrieval enforce the caller identity, return citations and meet the conversation latency budget?

Boundary: Search relevance is not authorization; indexed documents may contain untrusted instructions.

Evidence: `elastic-offering`, `eleven-integration`. [Elasticsearch](https://www.elastic.co/elasticsearch); [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools) (2026-10-26).

## x11 · Atlan ↔ XenonStack

**complementarity_hypothesis**

An implementation provider could use governed context when delivering business-system agents.

Validation question: Is the proposed division of responsibility clear for metadata quality, agent logic and authorization?

Boundary: Both may provide overlapping integration work; commercial fit and ownership are unresolved.

Evidence: `atlan-integration`, `xenon-offering`. [Atlan connectors](https://atlan.com/connectors/); [XenonStack](https://www.xenonstack.com/) (2026-10-26).

## x12 · Snowflake ↔ Haptik AI / Jio Haptik

**complementarity_hypothesis**

A customer-service workflow could evaluate governed enterprise retrieval as a backend.

Validation question: Can only approved knowledge be exposed, with no unintended customer-record leakage?

Boundary: No native Snowflake–Haptik connector or production architecture was verified.

Evidence: `snowflake-integration`, `haptik-integration`. [Cortex Search documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview); [Haptik integrations](https://www.haptik.ai/platform/integrations) (2026-10-26).

## x13 · ElevenLabs ↔ Haptik AI / Jio Haptik

**competitive_overlap_inference**

Both advertise conversational customer-service agents; evaluate as potential alternatives before assuming complementarity.

Validation question: Where do channel coverage, deployment, tool controls and human-handoff requirements differ?

Boundary: Shared category does not prove equal capabilities, pricing or substitutability.

Evidence: `eleven-offering`, `haptik-offering`. [ElevenLabs Agents](https://elevenlabs.io/agents); [Jio Haptik](https://www.haptik.ai/) (2026-10-26).

## x14 · Snowflake ↔ Elastic

**competitive_overlap_inference**

Both support enterprise retrieval use cases, creating an architectural comparison rather than automatic synergy.

Validation question: Should retrieval stay with existing data or use a separate index, given permissions, freshness, latency and cost?

Boundary: Overlap in retrieval does not make the full platforms equivalent.

Evidence: `snowflake-integration`, `elastic-offering`. [Cortex Search documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview); [Elasticsearch](https://www.elastic.co/elasticsearch) (2026-10-26).

