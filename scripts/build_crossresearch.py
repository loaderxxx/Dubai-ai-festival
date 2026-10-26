#!/usr/bin/env python3
import csv,json
from pathlib import Path
root=Path(__file__).resolve().parents[1];D='2026-10-26'
p=json.loads((root/'data/company-profiles.json').read_text());companies={c['company_id']:c for c in p['profiles']}
facts={f['id']:f for c in p['profiles'] for f in c['facts']};sources={s['id']:s for s in p['sources']};edges=[]
def L(en,ru):return {'en':en,'ru':ru}
def E(id,a,b,kind,basis,statement,question,risk):
    ss=list(dict.fromkeys(s for f in basis for s in facts[f]['source_ids']))
    edges.append({'id':id,'company_a':a,'company_b':b,'relationship_type':kind,'statement':statement,'supporting_fact_ids':basis,'source_ids':ss,'source_urls':[sources[s]['url'] for s in ss],'accessed_on':D,'validation_question':question,'risk_or_boundary':risk,'company_interest_confirmed':False,'commercial_partnership_confirmed':False})
E('x01','atlan','snowflake','documented_vendor_integration',['atlan-integration','snowflake-offering'],
L('Atlan names a Snowflake connector. This is a documented product connection, not proof of a new joint commercial opportunity.','Atlan указывает коннектор Snowflake. Это документированная продуктовая связь, а не доказательство новой совместной коммерческой возможности.'),
L('Which metadata, lineage and authorization requirements remain for the proposed agent use case?','Какие требования к метаданным, происхождению данных и авторизации остаются для сценария агента?'),
L('A metadata connector is not end-to-end row-level authorization.','Коннектор метаданных не равен сквозной авторизации на уровне строк.'))
E('x02','elastic','aws','documented_vendor_ecosystem_listing',['elastic-integration','aws-offering'],
L('Elastic lists AWS in its AI ecosystem; the exact integration and joint-delivery terms require separate confirmation.','Elastic указывает AWS в AI-экосистеме; конкретная интеграция и условия совместного внедрения требуют отдельного подтверждения.'),
L('Which supported retrieval and observability integration fits AgentCore in the selected region?','Какая поддерживаемая интеграция поиска и наблюдаемости подходит AgentCore в выбранном регионе?'),
L('Do not infer a specific connector, certification or commercial agreement from a list entry.','Не выводить наличие конкретного коннектора, сертификации или договора из записи в списке.'))
E('x03','elastic','alibaba-cloud','documented_vendor_ecosystem_listing',['elastic-integration','alibaba-offering'],
L('Elastic lists Alibaba Cloud in its AI ecosystem; a Qwen-backed retrieval design is a separate technical hypothesis.','Elastic указывает Alibaba Cloud в AI-экосистеме; архитектура поиска с Qwen остаётся отдельной технической гипотезой.'),
L('Which supported model endpoint, embedding path and deployment region apply?','Какие поддерживаемые конечная точка модели, путь эмбеддингов и регион развёртывания применимы?'),
L('Model and infrastructure availability may vary by region.','Доступность моделей и инфраструктуры может различаться по регионам.'))
E('x04','xenonstack','snowflake','vendor_advertised_integration_offering',['xenon-integration','snowflake-offering'],
L('XenonStack advertises Snowflake-oriented agents. This is unilateral offering evidence, not a verified formal partnership.','XenonStack предлагает агентов для Snowflake. Это одностороннее описание предложения, а не подтверждение формального партнёрства.'),
L('Can they demonstrate a production reference and define ownership of connectors, governance and support?','Могут ли они показать промышленный референс и определить владельцев коннекторов, управления и поддержки?'),
L('Marketing capabilities and outcome figures are not independently validated.','Маркетинговые возможности и показатели результатов независимо не проверены.'))
E('x05','eleven-labs','clickup','complementarity_hypothesis',['eleven-integration','clickup-integration','clickup-control'],
L('A voice agent could propose or create approved work items through ClickUp interfaces. No native pairing was verified.','Голосовой агент может предлагать или создавать подтверждённые рабочие задачи через интерфейсы ClickUp. Нативная связка не подтверждена.'),
L('Can a sandbox demonstration create one authorized task, reject unauthorized writes and avoid duplicate retries?','Может ли демонстрация в песочнице создать одну разрешённую задачу, отклонить запрещённую запись и исключить дубли при повторах?'),
L('OAuth scope, webhook-user lifecycle, consent and idempotency need explicit design.','Нужно явно спроектировать область OAuth, жизненный цикл пользователя вебхуков, согласие и идемпотентность.'))
E('x06','eleven-labs','placeos','complementarity_hypothesis',['eleven-integration','placeos-integration'],
L('A voice interface could request room bookings or facilities actions through PlaceOS APIs.','Голосовой интерфейс может запрашивать бронирование комнат или действия эксплуатации через API PlaceOS.'),
L('Can the pilot restrict actions to booking or requests, with human approval for physical-control changes?','Можно ли ограничить пилот бронированием и заявками, требуя подтверждения человеком для изменений физических систем?'),
L('Physical access and building control are safety-sensitive; do not grant broad actuation privileges.','Физический доступ и управление зданием критичны для безопасности; не предоставлять широкие права управления.'))
E('x07','applause','eleven-labs','complementarity_hypothesis',['applause-evaluation','eleven-testing'],
L('Independent human-led testing could complement platform-native voice-agent evaluations.','Независимое тестирование с участием людей может дополнить встроенную оценку голосовых агентов.'),
L('Can both teams agree on task-success, correct tool-use, handoff and unsafe-action acceptance criteria?','Могут ли команды согласовать критерии успешности задач, правильного вызова инструментов, передачи человеку и небезопасных действий?'),
L('No partnership or willingness to share customer test data was established.','Партнёрство и готовность передавать тестовые данные клиентов не установлены.'))
E('x08','applause','haptik-ai','complementarity_hypothesis',['applause-evaluation','haptik-offering'],
L('A CRM-connected service-agent pilot could use an external acceptance-testing program.','Пилот сервисного агента с CRM может использовать внешнюю программу приёмочных испытаний.'),
L('Can support scenarios be tested with synthetic data across channel transitions and human handoffs?','Можно ли тестировать сценарии поддержки на синтетических данных при смене каналов и передаче человеку?'),
L('Testing coverage must match the actual deployment; it is not a general safety certification.','Охват тестов должен соответствовать конкретному внедрению; это не универсальная сертификация безопасности.'))
E('x09','only-office','alibaba-cloud','complementarity_hypothesis',['onlyoffice-integration','alibaba-integration'],
L('A custom-model document workflow could evaluate Qwen as one candidate backend. Direct integration was not verified.','В документообороте с собственной моделью можно проверить Qwen как один из бэкендов. Прямая интеграция не подтверждена.'),
L('Does a minimal document workflow preserve permissions, formatting and data-location requirements?','Сохраняет ли минимальный документный сценарий права, форматирование и требования к местонахождению данных?'),
L('OpenAI-compatible APIs do not guarantee full application compatibility or data residency.','OpenAI-совместимый API не гарантирует полную совместимость приложения или локализацию данных.'))
E('x10','elastic','eleven-labs','complementarity_hypothesis',['elastic-offering','eleven-integration'],
L('A custom agent tool could query an enterprise search service for grounded responses.','Пользовательский инструмент агента может обращаться к корпоративному поиску для ответов с опорой на данные.'),
L('Can retrieval enforce the caller identity, return citations and meet the conversation latency budget?','Может ли поиск учитывать личность вызывающего, возвращать источники и укладываться в задержку диалога?'),
L('Search relevance is not authorization; indexed documents may contain untrusted instructions.','Релевантность поиска не равна авторизации; индексируемые документы могут содержать недоверенные инструкции.'))
E('x11','atlan','xenonstack','complementarity_hypothesis',['atlan-integration','xenon-offering'],
L('An implementation provider could use governed context when delivering business-system agents.','Интегратор может использовать управляемый контекст при внедрении агентов бизнес-систем.'),
L('Is the proposed division of responsibility clear for metadata quality, agent logic and authorization?','Ясно ли распределена ответственность за качество метаданных, логику агента и авторизацию?'),
L('Both may provide overlapping integration work; commercial fit and ownership are unresolved.','Обе стороны могут выполнять пересекающиеся интеграционные работы; коммерческая совместимость и ответственность не определены.'))
E('x12','snowflake','haptik-ai','complementarity_hypothesis',['snowflake-integration','haptik-integration'],
L('A customer-service workflow could evaluate governed enterprise retrieval as a backend.','Сценарий клиентского обслуживания может проверить управляемый корпоративный поиск как бэкенд.'),
L('Can only approved knowledge be exposed, with no unintended customer-record leakage?','Можно ли предоставлять только разрешённые знания без непреднамеренной утечки клиентских записей?'),
L('No native Snowflake–Haptik connector or production architecture was verified.','Нативный коннектор Snowflake–Haptik или промышленная архитектура не подтверждены.'))
E('x13','eleven-labs','haptik-ai','competitive_overlap_inference',['eleven-offering','haptik-offering'],
L('Both advertise conversational customer-service agents; evaluate as potential alternatives before assuming complementarity.','Обе компании предлагают разговорных агентов обслуживания; сначала сравнить их как возможные альтернативы, не предполагая взаимодополнение.'),
L('Where do channel coverage, deployment, tool controls and human-handoff requirements differ?','Чем различаются охват каналов, развёртывание, контроль инструментов и требования передачи человеку?'),
L('Shared category does not prove equal capabilities, pricing or substitutability.','Общая категория не доказывает равенство возможностей, цен или взаимозаменяемость.'))
E('x14','snowflake','elastic','competitive_overlap_inference',['snowflake-integration','elastic-offering'],
L('Both support enterprise retrieval use cases, creating an architectural comparison rather than automatic synergy.','Обе платформы поддерживают корпоративный поиск; это повод сравнить архитектуры, а не автоматически объединять их.'),
L('Should retrieval stay with existing data or use a separate index, given permissions, freshness, latency and cost?','Оставить поиск рядом с данными или использовать отдельный индекс с учётом прав, актуальности, задержки и стоимости?'),
L('Overlap in retrieval does not make the full platforms equivalent.','Пересечение в поиске не делает платформы полностью эквивалентными.'))
meta={'schema_version':'1.0','accessed_on':D,'public_only':True,'edge_count':len(edges),'note':L('A graph edge is not a confirmed commercial relationship. Documented vendor links, analyst complementarity hypotheses and competitive overlap are separate types.','Ребро графа не означает подтверждённые коммерческие отношения. Документированные связи поставщиков, гипотезы взаимодополнения и конкурентное пересечение имеют разные типы.')}
(root/'data/crossresearch.json').write_text(json.dumps({**meta,'edges':edges},ensure_ascii=False,indent=2)+'\n')
with (root/'data/crossresearch.csv').open('w',newline='') as f:
    fields=['id','company_a','company_b','relationship_type','statement_en','statement_ru','supporting_fact_ids','source_urls','accessed_on','validation_question_en','validation_question_ru','company_interest_confirmed','commercial_partnership_confirmed'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for e in edges:w.writerow({'id':e['id'],'company_a':e['company_a'],'company_b':e['company_b'],'relationship_type':e['relationship_type'],'statement_en':e['statement']['en'],'statement_ru':e['statement']['ru'],'supporting_fact_ids':';'.join(e['supporting_fact_ids']),'source_urls':';'.join(e['source_urls']),'accessed_on':D,'validation_question_en':e['validation_question']['en'],'validation_question_ru':e['validation_question']['ru'],'company_interest_confirmed':False,'commercial_partnership_confirmed':False})
for lang in ['en','ru']:
    en=lang=='en';lines=['# '+('Cross-company research' if en else 'Кросс-ресёрч компаний'),'','[English](../../research/en/crossresearch.md) · [Русский](../../research/ru/crossresearch.md)','',meta['note'][lang],'',('Reviewed: ' if en else 'Дата проверки: ')+D+'.','']
    for e in edges:
        lines+=['## '+e['id']+' · '+companies[e['company_a']]['display_name']+' ↔ '+companies[e['company_b']]['display_name'],'','**'+e['relationship_type']+'**','',e['statement'][lang],'',('Validation question: ' if en else 'Вопрос для проверки: ')+e['validation_question'][lang],'',('Boundary: ' if en else 'Ограничение: ')+e['risk_or_boundary'][lang],'',('Evidence: ' if en else 'Основание: ')+', '.join('`'+f+'`' for f in e['supporting_fact_ids'])+'. '+ '; '.join(f"[{sources[s]['title']}]({sources[s]['url']})" for s in e['source_ids'])+f' ({D}).','']
    (root/f'research/{lang}/crossresearch.md').write_text('\n'.join(lines)+'\n')
print(f'Generated {len(edges)} cross-research edges; 4 documented vendor links, 8 complementarity hypotheses, 2 overlap inferences.')
