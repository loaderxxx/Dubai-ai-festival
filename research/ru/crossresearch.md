# Кросс-ресёрч компаний

[English](../../research/en/crossresearch.md) · [Русский](../../research/ru/crossresearch.md)

Ребро графа не означает подтверждённые коммерческие отношения. Документированные связи поставщиков, гипотезы взаимодополнения и конкурентное пересечение имеют разные типы.

Дата проверки: 2026-10-26.

## x01 · Atlan ↔ Snowflake

**documented_vendor_integration**

Atlan указывает коннектор Snowflake. Это документированная продуктовая связь, а не доказательство новой совместной коммерческой возможности.

Вопрос для проверки: Какие требования к метаданным, происхождению данных и авторизации остаются для сценария агента?

Ограничение: Коннектор метаданных не равен сквозной авторизации на уровне строк.

Основание: `atlan-integration`, `snowflake-offering`. [Atlan connectors](https://atlan.com/connectors/); [Snowflake for AI](https://www.snowflake.com/en/product/ai/) (2026-10-26).

## x02 · Elastic ↔ AWS

**documented_vendor_ecosystem_listing**

Elastic указывает AWS в AI-экосистеме; конкретная интеграция и условия совместного внедрения требуют отдельного подтверждения.

Вопрос для проверки: Какая поддерживаемая интеграция поиска и наблюдаемости подходит AgentCore в выбранном регионе?

Ограничение: Не выводить наличие конкретного коннектора, сертификации или договора из записи в списке.

Основание: `elastic-integration`, `aws-offering`. [Elastic AI Ecosystem](https://www.elastic.co/partners/ai-ecosystem); [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) (2026-10-26).

## x03 · Elastic ↔ Alibaba Cloud

**documented_vendor_ecosystem_listing**

Elastic указывает Alibaba Cloud в AI-экосистеме; архитектура поиска с Qwen остаётся отдельной технической гипотезой.

Вопрос для проверки: Какие поддерживаемые конечная точка модели, путь эмбеддингов и регион развёртывания применимы?

Ограничение: Доступность моделей и инфраструктуры может различаться по регионам.

Основание: `elastic-integration`, `alibaba-offering`. [Elastic AI Ecosystem](https://www.elastic.co/partners/ai-ecosystem); [Alibaba Cloud for Generative AI](https://www.alibabacloud.com/en/solutions/generative-ai) (2026-10-26).

## x04 · XenonStack ↔ Snowflake

**vendor_advertised_integration_offering**

XenonStack предлагает агентов для Snowflake. Это одностороннее описание предложения, а не подтверждение формального партнёрства.

Вопрос для проверки: Могут ли они показать промышленный референс и определить владельцев коннекторов, управления и поддержки?

Ограничение: Маркетинговые возможности и показатели результатов независимо не проверены.

Основание: `xenon-integration`, `snowflake-offering`. [XenonStack](https://www.xenonstack.com/); [XenonStack Snowflake AI Agents](https://www.xenonstack.com/ai-agents/snowflake-ai-agents/); [Snowflake for AI](https://www.snowflake.com/en/product/ai/) (2026-10-26).

## x05 · ElevenLabs ↔ ClickUp

**complementarity_hypothesis**

Голосовой агент может предлагать или создавать подтверждённые рабочие задачи через интерфейсы ClickUp. Нативная связка не подтверждена.

Вопрос для проверки: Может ли демонстрация в песочнице создать одну разрешённую задачу, отклонить запрещённую запись и исключить дубли при повторах?

Ограничение: Нужно явно спроектировать область OAuth, жизненный цикл пользователя вебхуков, согласие и идемпотентность.

Основание: `eleven-integration`, `clickup-integration`, `clickup-control`. [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools); [ClickUp developer portal](https://developer.clickup.com/); [ClickUp webhooks](https://developer.clickup.com/docs/webhooks) (2026-10-26).

## x06 · ElevenLabs ↔ PlaceOS

**complementarity_hypothesis**

Голосовой интерфейс может запрашивать бронирование комнат или действия эксплуатации через API PlaceOS.

Вопрос для проверки: Можно ли ограничить пилот бронированием и заявками, требуя подтверждения человеком для изменений физических систем?

Ограничение: Физический доступ и управление зданием критичны для безопасности; не предоставлять широкие права управления.

Основание: `eleven-integration`, `placeos-integration`. [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools); [PlaceOS](https://www.placeos.com/) (2026-10-26).

## x07 · Applause ↔ ElevenLabs

**complementarity_hypothesis**

Независимое тестирование с участием людей может дополнить встроенную оценку голосовых агентов.

Вопрос для проверки: Могут ли команды согласовать критерии успешности задач, правильного вызова инструментов, передачи человеку и небезопасных действий?

Ограничение: Партнёрство и готовность передавать тестовые данные клиентов не установлены.

Основание: `applause-evaluation`, `eleven-testing`. [Applause Agentic AI Testing](https://www.applause.com/agentic-ai-testing/); [ElevenLabs Agents](https://elevenlabs.io/agents) (2026-10-26).

## x08 · Applause ↔ Haptik AI / Jio Haptik

**complementarity_hypothesis**

Пилот сервисного агента с CRM может использовать внешнюю программу приёмочных испытаний.

Вопрос для проверки: Можно ли тестировать сценарии поддержки на синтетических данных при смене каналов и передаче человеку?

Ограничение: Охват тестов должен соответствовать конкретному внедрению; это не универсальная сертификация безопасности.

Основание: `applause-evaluation`, `haptik-offering`. [Applause Agentic AI Testing](https://www.applause.com/agentic-ai-testing/); [Jio Haptik](https://www.haptik.ai/) (2026-10-26).

## x09 · ONLYOFFICE ↔ Alibaba Cloud

**complementarity_hypothesis**

В документообороте с собственной моделью можно проверить Qwen как один из бэкендов. Прямая интеграция не подтверждена.

Вопрос для проверки: Сохраняет ли минимальный документный сценарий права, форматирование и требования к местонахождению данных?

Ограничение: OpenAI-совместимый API не гарантирует полную совместимость приложения или локализацию данных.

Основание: `onlyoffice-integration`, `alibaba-integration`. [ONLYOFFICE Docs Developer](https://www.onlyoffice.com/for-developers); [Make your first API call to Qwen](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/first-api-call-to-qwen) (2026-10-26).

## x10 · Elastic ↔ ElevenLabs

**complementarity_hypothesis**

Пользовательский инструмент агента может обращаться к корпоративному поиску для ответов с опорой на данные.

Вопрос для проверки: Может ли поиск учитывать личность вызывающего, возвращать источники и укладываться в задержку диалога?

Ограничение: Релевантность поиска не равна авторизации; индексируемые документы могут содержать недоверенные инструкции.

Основание: `elastic-offering`, `eleven-integration`. [Elasticsearch](https://www.elastic.co/elasticsearch); [ElevenLabs tools](https://elevenlabs.io/docs/eleven-agents/customization/tools) (2026-10-26).

## x11 · Atlan ↔ XenonStack

**complementarity_hypothesis**

Интегратор может использовать управляемый контекст при внедрении агентов бизнес-систем.

Вопрос для проверки: Ясно ли распределена ответственность за качество метаданных, логику агента и авторизацию?

Ограничение: Обе стороны могут выполнять пересекающиеся интеграционные работы; коммерческая совместимость и ответственность не определены.

Основание: `atlan-integration`, `xenon-offering`. [Atlan connectors](https://atlan.com/connectors/); [XenonStack](https://www.xenonstack.com/) (2026-10-26).

## x12 · Snowflake ↔ Haptik AI / Jio Haptik

**complementarity_hypothesis**

Сценарий клиентского обслуживания может проверить управляемый корпоративный поиск как бэкенд.

Вопрос для проверки: Можно ли предоставлять только разрешённые знания без непреднамеренной утечки клиентских записей?

Ограничение: Нативный коннектор Snowflake–Haptik или промышленная архитектура не подтверждены.

Основание: `snowflake-integration`, `haptik-integration`. [Cortex Search documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview); [Haptik integrations](https://www.haptik.ai/platform/integrations) (2026-10-26).

## x13 · ElevenLabs ↔ Haptik AI / Jio Haptik

**competitive_overlap_inference**

Обе компании предлагают разговорных агентов обслуживания; сначала сравнить их как возможные альтернативы, не предполагая взаимодополнение.

Вопрос для проверки: Чем различаются охват каналов, развёртывание, контроль инструментов и требования передачи человеку?

Ограничение: Общая категория не доказывает равенство возможностей, цен или взаимозаменяемость.

Основание: `eleven-offering`, `haptik-offering`. [ElevenLabs Agents](https://elevenlabs.io/agents); [Jio Haptik](https://www.haptik.ai/) (2026-10-26).

## x14 · Snowflake ↔ Elastic

**competitive_overlap_inference**

Обе платформы поддерживают корпоративный поиск; это повод сравнить архитектуры, а не автоматически объединять их.

Вопрос для проверки: Оставить поиск рядом с данными или использовать отдельный индекс с учётом прав, актуальности, задержки и стоимости?

Ограничение: Пересечение в поиске не делает платформы полностью эквивалентными.

Основание: `snowflake-integration`, `elastic-offering`. [Cortex Search documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview); [Elasticsearch](https://www.elastic.co/elasticsearch) (2026-10-26).

