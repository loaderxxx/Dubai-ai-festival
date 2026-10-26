# ImposterHunter — краткий публичный разбор

[Полный профиль](profile.ru.md) · [English version](brief.en.md) · [Реестр доказательств](sources.json)

Проверено **26 октября 2026, Asia/Dubai**. Независимое исследование; функции не тестировались.

**Что продаёт — ЗАЯВЛЕНИЕ ВЕНДОРА:** LLM Shield — API классификации входа для prompt injection, jailbreak и обмана на уровне разговора. Один движок обслуживает шесть заявленных live-поверхностей: chat, voice transcripts, agents, MCP, RAG, memory. Возвращаются score, цитируемое доказательство и рекомендация; политику исполняет приложение клиента. Заявлены hosted, VPC, on-premises и air-gapped. [IH03](https://imposterhunter.com/llm-shield)

**Жёсткие границы:** voice работает с расшифровкой, не аудио. MCP-screening не доказывает полную авторизацию протокола. Memory проверяет recall; записи можно направлять через API, но существующее хранилище продукт не очищает. Это важно для предмета пилота. [IH05](https://imposterhunter.com/llm-shield/voice-agents) · [IH07](https://imposterhunter.com/llm-shield/mcp) · [IH09](https://imposterhunter.com/llm-shield/memory)

**Идентичность — ФАКТ о раскрытии:** глобальный контрагент ImposterHunter AI LTD, DIFC **13635 / CL13635**; основатели **Dragos Balhui, CEO**, и **Cristina Balhui, Chief Threat Methodology Officer**. Датированная выгрузка официального плана содержит **Imposter Hunter, G113**, наблюдение **26 октября 2026, 03:30:39 UTC**. Уровень спонсорства **НЕИЗВЕСТЕН**; одна надпись на плане не подтверждает юрлицо и присутствие. [IH02](https://imposterhunter.com/company) · [IH27](https://dubaiaifestival.com/floorplan/) · [IH28](https://floorplan.live/interactive/shows/4608/views/2/plan)

**Доказательства — ЗАЯВЛЕНИЕ ВЕНДОРА:** сентябрьский API-прогон: **7 084 запроса**, **1 700 атак**, **99,78% ROC AUC**, все атаки non-PASS; PDF уточняет **99,59% BLOCK**, остальные flagged. False positives: **0,86%** обычного и **3,43%** сложного доброкачественного трафика. Корпус/методика/latency не опубликованы; независимое воспроизведение и названный клиентский результат не установлены. [IH10](https://imposterhunter.com/trust) · [IH13](https://imposterhunter.com/resources/imposterhunter-best-defence-in-depth-ai-security-platform-overview.pdf)

**До закупки:** уточнить схему разговора, лимиты, политику ошибок/действий, sizing, latency и цену. SOC 2 готовится; ISO 27001 планируется на **2027**. До production-данных согласовать обработчиков, retention запросов/логов и подписанный DPA вместо необязывающего проекта. [IH10](https://imposterhunter.com/trust) · [IH14](https://imposterhunter.com/dpa) · [IH16](https://imposterhunter.com/privacy)

**Публичный следующий шаг:** предлагаются **30-минутное техническое демо** и маршрут к evaluation key; цены не опубликованы. Полезная ограниченная оценка — синтетические сценарии покупателя с раздельным измерением false positives и фактического исполнения политики приложением. Это **ГИПОТЕЗА**, не договорённость и не выполненный тест. [IH18](https://imposterhunter.com/demo) · [IH11](https://imposterhunter.com/resources)
