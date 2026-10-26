#!/usr/bin/env python3
"""Generate bilingual initial research from manually reviewed public official sources."""
import json,csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
D='2026-10-26'
sources=[];profiles=[]
def S(id,url,title,section,method='public_official_page_read'):
    sources.append({'id':id,'url':url,'title':title,'accessed_on':D,'source_type':'official_vendor','retrieval_method':method,'evidence_locator':section,'caution':'Vendor descriptions are evidence of the advertised offering, not independent performance validation.'});return id
def L(en,ru): return {'en':en,'ru':ru}
def F(id,category,en,ru,ss): return {'id':id,'category':category,'statement':L(en,ru),'evidence_kind':'official_vendor_statement','source_ids':ss,'accessed_on':D}
def P(id,name,site,tags,facts,angle,question,buyers):
    profiles.append({'company_id':id,'display_name':name,'official_website':site,'reviewed_on':D,'research_status':'initial_public_profile','tags':tags,
    'identity_basis':L('Floorplan brand label matched to an official brand site; legal exhibitor entity and onsite attendance are not independently confirmed.','Название бренда на плане сопоставлено с официальным сайтом; юридическое лицо экспонента и фактическое присутствие отдельно не подтверждены.'),
    'facts':facts,'analyst_hypotheses':[{'type':'integration_or_partnership_discussion','statement':angle,'status':'unvalidated','not_a_claim_of_company_interest':True}],
    'target_buyer_roles_to_validate':{'statement':buyers,'status':'analyst_inference_not_confirmed_buyer'},'discovery_question':question,
    'unknowns':L('Current buyer, budget, regional delivery, data-residency terms, integration acceptance and willingness to partner are unknown.','Неизвестны конкретный покупатель, бюджет, региональная доступность, условия хранения данных, приемлемость интеграции и готовность к партнёрству.'),
    'lead_priority':None,'buying_intent_verified':False,'partnership_intent_verified':False})
S('aws-agentcore','https://aws.amazon.com/bedrock/agentcore/','Amazon Bedrock AgentCore','Overview; Connect across your stack; Debug faster')
S('aws-classic','https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html','Amazon Bedrock Agents documentation','Maintenance-mode notice at top')
P('aws','AWS','https://aws.amazon.com/',['agent-runtime','enterprise-integration','identity-and-security'],[
F('aws-offering','offering','AgentCore provides infrastructure for deploying and operating production AI agents across models and frameworks.','AgentCore предоставляет инфраструктуру для развёртывания и эксплуатации AI-агентов с разными моделями и фреймворками.',['aws-agentcore']),
F('aws-integration','integration_surface','Its documented integration scope includes MCP servers, internal APIs, knowledge bases and Lambda, with authentication and access controls.','Документированы подключения MCP-серверов, внутренних API, баз знаний и Lambda с аутентификацией и управлением доступом.',['aws-agentcore']),
F('aws-users','advertised_users','The page addresses developers moving agents from prototypes into production.','Страница адресована разработчикам, переводящим агентов из прототипа в промышленную эксплуатацию.',['aws-agentcore']),
F('aws-caveat','availability_caveat','The separate Bedrock Agents Classic documentation says it is closed to new customers and directs them to AgentCore.','Документация отдельного Bedrock Agents Classic сообщает о закрытии для новых клиентов и направляет их к AgentCore.',['aws-classic'])],
L('Explore a governed business-system agent pilot; choose the current service before architecture work.','Обсудить пилот агента для бизнес-систем с контролем доступа; сначала выбрать актуальный сервис.'),
L('Which regional deployment, tool-permission and evaluation requirements must a pilot meet?','Какие требования к региону развёртывания, правам инструментов и оценке должен выполнить пилот?'),
L('Platform engineering or enterprise AI leaders.','Руководители платформенной разработки или корпоративного AI.'))
S('alibaba-genai','https://www.alibabacloud.com/en/solutions/generative-ai','Alibaba Cloud for Generative AI','Overview; GenAI Development; Model Studio')
S('alibaba-qwen-api','https://docs.modelstudio.console.alibabacloud.com/en/model-studio/first-api-call-to-qwen','Make your first API call to Qwen','Opening description; API compatibility','official_documentation_search_extract')
P('alibaba-cloud','Alibaba Cloud','https://www.alibabacloud.com/',['model-platform','cloud-ai','enterprise-integration'],[
F('alibaba-offering','offering','Alibaba Cloud describes infrastructure, model development and deployment services; Model Studio hosts Qwen models and supports application development.','Alibaba Cloud описывает инфраструктуру, разработку и развёртывание моделей; Model Studio предоставляет модели Qwen и средства разработки приложений.',['alibaba-genai']),
F('alibaba-integration','integration_surface','Official Qwen documentation describes OpenAI-compatible APIs and the DashScope SDK.','Официальная документация Qwen описывает OpenAI-совместимые API и DashScope SDK.',['alibaba-qwen-api']),
F('alibaba-users','advertised_users','The generative-AI solution targets businesses building or customizing models and AI applications.','Решение предназначено для компаний, разрабатывающих или адаптирующих модели и AI-приложения.',['alibaba-genai'])],
L('Evaluate Qwen as a candidate model backend for a document or workflow product; compatibility still needs testing.','Проверить Qwen как возможный модельный бэкенд документооборота или автоматизации; совместимость требует тестов.'),
L('Which model, region and API features are available for our exact workflow?','Какие модель, регион и функции API доступны для конкретного процесса?'),
L('AI application engineering or cloud-platform owners.','Руководители разработки AI-приложений или облачной платформы.'))
S('atlan-home','https://atlan.com/','Atlan','Enterprise Context Layer; business systems; enterprise customers')
S('atlan-connectors','https://atlan.com/connectors/','Atlan connectors','Connector setup; App Framework; FAQ listing Snowflake')
P('atlan','Atlan','https://atlan.com/',['data-context','governance','connectors'],[
F('atlan-offering','offering','Atlan offers an enterprise context layer combining data structure, business semantics, lineage and organizational knowledge for AI use.','Atlan предлагает корпоративный слой контекста: структуру данных, бизнес-семантику, происхождение данных и знания организации для AI.',['atlan-home']),
F('atlan-integration','integration_surface','Its connector documentation names Snowflake and describes custom connectors through the App Framework and SDK.','В описании коннекторов указаны Snowflake и создание собственных коннекторов через App Framework и SDK.',['atlan-connectors']),
F('atlan-users','advertised_users','The product addresses enterprise data and AI teams, including developers, partners and system integrators extending connectors.','Продукт адресован корпоративным командам данных и AI, включая разработчиков, партнёров и интеграторов, расширяющих коннекторы.',['atlan-connectors'])],
L('Explore governed context for a Snowflake-based business assistant rather than assuming the connector solves end-user authorization.','Обсудить управляемый контекст для бизнес-ассистента на Snowflake, не предполагая, что коннектор решает авторизацию конечных пользователей.'),
L('How are business definitions, freshness and end-user permissions exposed to downstream agents?','Как агентам передаются бизнес-определения, актуальность данных и права конечного пользователя?'),
L('Data platform, governance or enterprise AI leaders.','Руководители платформы данных, управления данными или корпоративного AI.'))
S('clickup-brain','https://clickup.com/brain','ClickUp Brain','AI tasks, projects and workspace context')
S('clickup-api','https://developer.clickup.com/','ClickUp developer portal','Public API; MCP; webhooks; OAuth')
S('clickup-webhooks','https://developer.clickup.com/docs/webhooks','ClickUp webhooks','Scope; signature; task events')
P('clickup','ClickUp','https://clickup.com/',['work-management','workflow-automation','business-system'],[
F('clickup-offering','offering','ClickUp combines work-management features with contextual AI for tasks, projects and team collaboration.','ClickUp сочетает управление работой с контекстным AI для задач, проектов и командной работы.',['clickup-brain']),
F('clickup-integration','integration_surface','The developer portal provides a public API, MCP server, OAuth and event webhooks.','Портал разработчика предлагает публичный API, MCP-сервер, OAuth и вебхуки событий.',['clickup-api']),
F('clickup-control','implementation_caveat','Webhook subscriptions are tied to the creating user; documentation specifies signed events and task-related event types.','Подписки вебхуков связаны с создавшим их пользователем; документация описывает подпись событий и события задач.',['clickup-webhooks'])],
L('Test conversation-to-task automation with explicit approvals, deduplication and an auditable write path.','Проверить создание задач из диалогов с явным подтверждением, устранением дублей и журналируемой записью.'),
L('Which task actions may an external agent perform, and who owns its OAuth and webhook lifecycle?','Какие действия с задачами разрешены внешнему агенту и кто управляет OAuth и жизненным циклом вебхуков?'),
L('Operations, project-management or workspace platform owners.','Руководители операций, проектного управления или корпоративной рабочей платформы.'))
S('elastic-product','https://www.elastic.co/elasticsearch','Elasticsearch','Search; observability; security; deployment options')
S('elastic-ecosystem','https://www.elastic.co/partners/ai-ecosystem','Elastic AI Ecosystem','Meet the ecosystem: AWS and Alibaba Cloud named')
P('elastic','Elastic','https://www.elastic.co/',['retrieval','observability','security'],[
F('elastic-offering','offering','Elastic offers search and vector retrieval, observability and security capabilities built around Elasticsearch.','Elastic предлагает поиск и векторное извлечение, наблюдаемость и средства безопасности на базе Elasticsearch.',['elastic-product']),
F('elastic-integration','integration_surface','Elastic publicly lists AWS and Alibaba Cloud in its AI ecosystem. This alone does not establish a specific deployed integration.','Elastic публично указывает AWS и Alibaba Cloud в AI-экосистеме. Само по себе это не подтверждает конкретную работающую интеграцию.',['elastic-ecosystem']),
F('elastic-users','advertised_users','Its advertised use cases include search applications, customer support search, infrastructure monitoring and security operations.','Среди заявленных сценариев — поисковые приложения, поиск для поддержки, мониторинг инфраструктуры и операции безопасности.',['elastic-product'])],
L('Explore an access-controlled retrieval and observability layer for an enterprise agent.','Обсудить слой извлечения знаний и наблюдаемости корпоративного агента с контролем доступа.'),
L('Which connector, permission model and retrieval-quality benchmark apply to the proposed data sources?','Какие коннектор, модель прав и критерий качества поиска подходят для выбранных источников данных?'),
L('Search engineering, SRE or security-platform leaders.','Руководители поисковой разработки, SRE или платформы безопасности.'))
S('eleven-agents','https://elevenlabs.io/agents','ElevenLabs Agents','Support, sales and operational use cases; configuration and testing')
S('eleven-tools','https://elevenlabs.io/docs/eleven-agents/customization/tools','ElevenLabs tools','Client, webhook, code, MCP and system tools')
P('eleven-labs','ElevenLabs','https://elevenlabs.io/',['voice-agents','customer-experience','tool-integration'],[
F('eleven-offering','offering','ElevenLabs offers conversational agents for customer support, sales and operational workflows.','ElevenLabs предлагает разговорных агентов для поддержки клиентов, продаж и операционных процессов.',['eleven-agents']),
F('eleven-integration','integration_surface','Its agent tools include external API webhooks, client actions and MCP integrations.','Инструменты агентов включают вебхуки внешних API, клиентские действия и интеграции MCP.',['eleven-tools']),
F('eleven-testing','quality_surface','The product describes agent simulations, automated behavioral tests and monitoring.','В продукте описаны симуляции, автоматические тесты поведения агентов и мониторинг.',['eleven-agents'])],
L('Prototype a voice front end that proposes approved actions in a business system rather than unrestricted writes.','Создать прототип голосового интерфейса, предлагающего подтверждаемые действия в бизнес-системе вместо неограниченной записи.'),
L('How are identity, human handoff, tool authorization and measurable task completion implemented?','Как реализованы идентификация, передача человеку, авторизация инструментов и измерение выполнения задачи?'),
L('Customer-experience, operations or application-platform leaders.','Руководители клиентского опыта, операций или платформы приложений.'))
S('snowflake-ai','https://www.snowflake.com/en/product/ai/','Snowflake for AI','Data agents; unstructured data; ML workflows')
S('snowflake-search','https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview','Cortex Search documentation','Overview; use cases; REST API example')
P('snowflake','Snowflake','https://www.snowflake.com/',['data-platform','enterprise-ai','retrieval'],[
F('snowflake-offering','offering','Snowflake offers data agents, unstructured-data analysis and ML workflows within its governed data platform.','Snowflake предлагает агентов для данных, анализ неструктурированных данных и ML-процессы в своей управляемой платформе данных.',['snowflake-ai']),
F('snowflake-integration','integration_surface','Cortex Search supports hybrid retrieval for RAG and enterprise search; documentation includes REST API queries.','Cortex Search поддерживает гибридное извлечение для RAG и корпоративного поиска; документация содержит запросы через REST API.',['snowflake-search']),
F('snowflake-users','advertised_users','The offerings target enterprises building applications and analytical workflows on their existing data.','Предложения адресованы компаниям, создающим приложения и аналитические процессы на своих данных.',['snowflake-ai'])],
L('Evaluate a governed knowledge backend for business assistants, with an explicit permission and freshness test.','Проверить управляемый бэкенд знаний для бизнес-ассистентов с явной проверкой прав и актуальности.'),
L('Which datasets, retrieval scopes and region-specific AI services are allowed in the pilot?','Какие наборы данных, области поиска и региональные AI-сервисы разрешены в пилоте?'),
L('Data platform, analytics or enterprise AI leaders.','Руководители платформы данных, аналитики или корпоративного AI.'))
S('haptik-home','https://www.haptik.ai/','Jio Haptik','Support, sales, booking and lead qualification agents; industries')
S('haptik-integrations','https://www.haptik.ai/platform/integrations','Haptik integrations','CRM and live chat; API integration; Salesforce, HubSpot and Zendesk')
P('haptik-ai','Haptik AI / Jio Haptik','https://www.haptik.ai/',['conversational-ai','customer-service','crm-integration'],[
F('haptik-offering','offering','Haptik markets agents for customer service, sales, bookings and lead qualification across conversational channels.','Haptik предлагает агентов для обслуживания, продаж, бронирования и квалификации лидов в разговорных каналах.',['haptik-home']),
F('haptik-integration','integration_surface','Its integration catalog names Salesforce, HubSpot and Zendesk, and describes connections to API-enabled software.','В каталоге интеграций указаны Salesforce, HubSpot и Zendesk; описано подключение ПО с API.',['haptik-integrations']),
F('haptik-users','advertised_users','The integration page addresses support, sales, marketing and customer-engagement teams.','Страница интеграций адресована командам поддержки, продаж, маркетинга и взаимодействия с клиентами.',['haptik-integrations'])],
L('Explore CRM-connected service automation; compare overlap with other voice-agent platforms before assuming partnership fit.','Обсудить автоматизацию обслуживания с CRM; проверить пересечение с другими платформами голосовых агентов, прежде чем предполагать партнёрство.'),
L('Which integrations are native, how does human handoff work, and what is the required deployment model?','Какие интеграции нативные, как работает передача человеку и какая модель развёртывания требуется?'),
L('Customer service, CX or revenue-operations leaders.','Руководители клиентского обслуживания, CX или коммерческих операций.'))
S('onlyoffice-developer','https://www.onlyoffice.com/for-developers','ONLYOFFICE Docs Developer','Embedded editing; APIs; connectors; AI-ready')
P('only-office','ONLYOFFICE','https://www.onlyoffice.com/',['document-workflows','embedded-software','business-system'],[
F('onlyoffice-offering','offering','ONLYOFFICE provides embeddable collaborative editors for documents, spreadsheets, presentations, forms and PDF.','ONLYOFFICE предоставляет встраиваемые совместные редакторы документов, таблиц, презентаций, форм и PDF.',['onlyoffice-developer']),
F('onlyoffice-integration','integration_surface','The developer offering lists JavaScript and REST APIs, WOPI, connectors and integrations with custom language models.','Предложение для разработчиков включает JavaScript- и REST-API, WOPI, коннекторы и интеграции с собственными языковыми моделями.',['onlyoffice-developer']),
F('onlyoffice-users','advertised_users','It targets developers embedding editing into their own applications.','Продукт адресован разработчикам, встраивающим редактирование в собственные приложения.',['onlyoffice-developer'])],
L('Test an AI-assisted document workflow with a selected model backend; API compatibility is not a verified integration.','Проверить AI-сценарий работы с документами с выбранным модельным бэкендом; совместимость API не равна подтверждённой интеграции.'),
L('What deployment, licensing and document-permission boundaries apply to embedding and AI calls?','Какие условия развёртывания, лицензирования и права документов действуют для встраивания и AI-вызовов?'),
L('Software product or document-platform owners.','Руководители программного продукта или платформы документооборота.'))
S('applause-eval','https://www.applause.com/ai-evaluation-and-benchmarking/','Applause AI Evaluation & Benchmarking','Evaluation service; enterprise QA; domain experts')
S('applause-agentic','https://www.applause.com/agentic-ai-testing/','Applause Agentic AI Testing','Trace, tool-call, retrieval and task-completion evaluation')
P('applause','Applause','https://www.applause.com/',['ai-evaluation','quality-assurance','agent-safety'],[
F('applause-offering','offering','Applause provides managed AI evaluation combining automated assessment and human/domain-expert review.','Applause предоставляет управляемую оценку AI, сочетая автоматическую проверку с участием людей и отраслевых экспертов.',['applause-eval']),
F('applause-evaluation','evaluation_scope','Its agent-testing service describes trace assessment, tool-call correctness, retrieval relevance and end-to-end task completion.','Услуга тестирования агентов включает оценку трасс, корректности вызовов инструментов, релевантности поиска и полного выполнения задач.',['applause-agentic']),
F('applause-users','advertised_users','The evaluation program is presented for enterprise AI and quality-assurance teams.','Программа оценки адресована корпоративным командам AI и обеспечения качества.',['applause-eval'])],
L('Explore independent acceptance testing for a voice or business-system agent pilot.','Обсудить независимые приёмочные испытания пилота голосового агента или агента бизнес-систем.'),
L('Can the program measure task success and unsafe-action rates using consented, non-sensitive test cases?','Можно ли измерять успешность задач и частоту небезопасных действий на согласованных несекретных тестовых сценариях?'),
L('AI product, quality engineering or responsible-AI owners.','Руководители AI-продукта, качества разработки или ответственного AI.'))
S('placeos-home','https://www.placeos.com/','PlaceOS','Platform overview; products; drivers and APIs')
P('placeos','PlaceOS','https://www.placeos.com/',['building-automation','physical-systems','integration-platform'],[
F('placeos-offering','offering','PlaceOS offers integration and automation for workplaces, rooms, buildings and digital displays.','PlaceOS предлагает интеграцию и автоматизацию рабочих пространств, комнат, зданий и цифровых экранов.',['placeos-home']),
F('placeos-integration','integration_surface','Its drivers connect AV, HVAC, access control, sensors and calendars; APIs expose configured integrations and actions.','Драйверы подключают AV, HVAC, контроль доступа, датчики и календари; API предоставляют настроенные интеграции и действия.',['placeos-home']),
F('placeos-users','advertised_users','The site supports teams building their own workplace applications and delivery through PlaceOS partners.','Сайт предлагает создание собственных приложений рабочего пространства командами и реализацию через партнёров PlaceOS.',['placeos-home'])],
L('Explore a voice-assisted room-booking or facilities workflow with safety-gated actions.','Обсудить голосовое бронирование комнат или заявки эксплуатации с безопасным подтверждением действий.'),
L('Which actions are read-only, approval-gated or prohibited, and how is occupancy data minimized?','Какие действия только читают данные, требуют подтверждения или запрещены, и как минимизируются данные о присутствии?'),
L('Workplace technology, facilities or smart-building platform owners.','Руководители технологий рабочего пространства, эксплуатации или платформы умного здания.'))
S('xenon-home','https://www.xenonstack.com/','XenonStack','Foundry; domains; integration list')
S('xenon-snowflake','https://www.xenonstack.com/ai-agents/snowflake-ai-agents/','XenonStack Snowflake AI Agents','Integration offering; use cases; not a verified performance benchmark')
P('xenonstack','XenonStack','https://www.xenonstack.com/',['systems-integration','agentic-operations','security-and-governance'],[
F('xenon-offering','offering','XenonStack markets agent orchestration, analytics, infrastructure automation and security/governance offerings.','XenonStack предлагает оркестрацию агентов, аналитику, автоматизацию инфраструктуры и решения безопасности и управления.',['xenon-home']),
F('xenon-integration','integration_surface','Its site advertises Snowflake AI Agents and lists ServiceNow, SAP, Jira and Oracle-oriented agent integrations.','Сайт предлагает Snowflake AI Agents и перечисляет интеграции агентов с ServiceNow, SAP, Jira и Oracle.',['xenon-home','xenon-snowflake']),
F('xenon-users','advertised_users','Advertised domains include IT operations, finance, risk, analytics and security.','Заявленные области включают IT-операции, финансы, риски, аналитику и безопасность.',['xenon-home'])],
L('Explore an implementation or co-delivery discussion for a narrowly scoped enterprise-agent workflow.','Обсудить внедрение или совместную реализацию узкого процесса корпоративного агента.'),
L('Which production references, connector ownership and support responsibilities can be demonstrated?','Какие промышленные референсы, владение коннекторами и обязанности поддержки можно подтвердить?'),
L('Enterprise transformation, IT operations or data-platform leaders.','Руководители корпоративной трансформации, IT-операций или платформы данных.'))
# Join only public floorplan labels. Brand normalization is explicit, not legal-identity verification.
base=json.loads((root/'data/companies.json').read_text());byid={c['id']:c for c in base['records']}
for p in profiles:
    c=byid[p['company_id']];p['floorplan_name']=c['name'];p['stands']=c['stands'];p['event_source_url']=c['source_url']
meta={'schema_version':'1.0','public_only':True,'accessed_on':D,'count':len(profiles),'selection_basis':L('First research batch selected for visible relevance to business-system integration, automation, data infrastructure and enterprise AI assurance. Not a ranked lead list or validated sales pipeline.','Первая исследовательская выборка по видимой связи с интеграцией бизнес-систем, автоматизацией, инфраструктурой данных и проверкой корпоративного AI. Не рейтинг лидов и не подтверждённая воронка продаж.'),'sources':sources}
(root/'data/company-profiles.json').write_text(json.dumps({**meta,'profiles':profiles},ensure_ascii=False,indent=2)+'\n')
(root/'data/sources.json').write_text(json.dumps({'accessed_on':D,'sources':sources},ensure_ascii=False,indent=2)+'\n')
lookup={s['id']:s for s in sources}
for lang in ['en','ru']:
    en=lang=='en'; lines=['# '+('Initial company research' if en else 'Первичный ресёрч компаний'),'','[English](../../research/en/companies.md) · [Русский](../../research/ru/companies.md)','',meta['selection_basis'][lang],'',('Reviewed: ' if en else 'Дата проверки: ')+D+'.', '',('Facts below summarize official vendor claims. They do not validate performance, legal exhibitor identity, attendance, buying intent or partnership interest. Target buyer roles and collaboration angles are explicitly hypotheses.' if en else 'Факты ниже пересказывают официальные заявления поставщиков. Они не подтверждают эффективность, юридическое лицо экспонента, присутствие, намерение купить или интерес к партнёрству. Роли покупателей и темы сотрудничества — явно обозначенные гипотезы.'),'']
    for p in profiles:
        lines+=['## '+p['display_name'],'',('Floorplan: ' if en else 'План: ')+f"**{p['floorplan_name']} — {', '.join(p['stands'])}**. [Public source]({p['event_source_url']}).",'',('### Publicly documented offering and interfaces' if en else '### Публично описанные предложение и интерфейсы'),'']
        for f in p['facts']:
            refs='; '.join(f"[{lookup[s]['title']}]({lookup[s]['url']})" for s in f['source_ids'])
            lines+=[f"- **{f['id']}**: {f['statement'][lang]} ({refs}; {D})."]
        lines+=['',('### Hypotheses — validate in discussion' if en else '### Гипотезы — проверить в разговоре'),'','- '+p['analyst_hypotheses'][0]['statement'][lang],'- '+('Buyer roles to verify: ' if en else 'Роли покупателей для проверки: ')+p['target_buyer_roles_to_validate']['statement'][lang],'- '+('Question: ' if en else 'Вопрос: ')+p['discovery_question'][lang],'',p['unknowns'][lang],'']
    (root/f'research/{lang}/companies.md').write_text('\n'.join(lines)+'\n')
print(f'Generated {len(profiles)} bilingual profiles using {len(sources)} official sources.')
