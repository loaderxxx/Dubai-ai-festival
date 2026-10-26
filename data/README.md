# Data guide / Путеводитель по данным

[Home](../README.md) · [Главная](../README.ru.md) · [Coverage / Покрытие](../docs/en/research-status.md)

**Public-source data only.** The complete inventory and research coverage are different things. / **Только открытые данные.** Полнота списка и глубина исследования — разные характеристики.

## Start with the question / Начните с вопроса

| Question / Вопрос | File / Файл | Scope / Границы |
|---|---|---|
| What was captured? / Что зафиксировано? | [Original floorplan capture](floorplan-source-2026-10-26.json) | Original rows and provenance / Исходные строки и происхождение |
| Where is every source row? / Где каждая строка? | [Rows JSON](floorplan-rows.json) · [CSV](floorplan-rows.csv) | 264 populated rows / 264 заполненные строки |
| Which labels are not companies? / Какие названия не компании? | [Entities JSON](entities.json) · [CSV](entities.csv) | 262 labels, explicitly typed / 262 названия с типами |
| What is the candidate universe? / Какова база кандидатов? | [Candidates JSON](companies.json) · [CSV](companies.csv) | 248 organization labels, original research-status checkpoint / 248 названий, исходные статусы |
| What is covered now? / Что охвачено сейчас? | [Current coverage](research-coverage.json) | Union of the original and expanded study / Объединение исходной и расширенной выборок |
| Where are the original facts? / Где исходные факты? | [Company profiles](company-profiles.json) | 12 bilingual profiles and their source-linked facts / 12 двуязычных профилей |
| Which sources support them? / Какие источники их подтверждают? | [Original source register](sources.json) | 23 official source documents / 23 официальных документа |
| What connects the original companies? / Что связывает исходную выборку? | [Edges JSON](crossresearch.json) · [CSV](crossresearch.csv) | 14 typed relationships; not 14 partnerships / 14 связей, не 14 партнёрств |
| Where is the richer study? / Где расширенное исследование? | [Expanded research registers](value-chain/README.md) | 18 selected companies, evidence and relationships / 18 компаний, доказательства и связи |
| What was checked locally? / Что проверено локально? | [Baseline validation report](validation-report.json) | Original data integrity; not fresh web verification / Целостность исходной базы, не проверка сайтов |
| How was the original universe counted? / Как посчитана исходная база? | [Baseline summary](baseline-summary.json) | Original normalization counts and limitations / Исходные числа и ограничения |

## Reading identities / Как читать идентичность

- The candidate `id` is the join key. **A stand code is not a company ID.** / Ключ связи — `id` кандидата. **Номер стенда не является ID компании.**
- Original spellings, row numbers and every stand assignment are preserved. / Исходные написания, номера строк и все стенды сохранены.
- Shared stands and duplicate labels are not legal-entity merges. / Общие стенды и повторяющиеся названия не доказывают тождество юридических лиц.
- Null and unknown fields are intentional; do not fill them with guessed domains, contacts or intent. / Пустые и неизвестные значения намеренны; не заменяйте их угаданными доменами, контактами или намерениями.

## Original versus current coverage / Исходное и текущее покрытие

`companies.json`, `entities.json`, `company-profiles.json`, `baseline-summary.json` and `validation-report.json` preserve the **original 12-profile checkpoint**. Six additional companies are covered in the expanded study without rewriting that original evidence batch.

`research-coverage.json` and the [current English roster](../research/en/roster.md) / [русский список](../research/ru/roster.md) reconcile the two layers. The expanded 18 **include**, rather than add to, the original 12. The current gap is 230 candidates; the original gap was 236.

Указанные исходные JSON сохраняют контрольную точку из **12 профилей**. Ещё 6 компаний рассмотрены в расширенном исследовании. Текущий реестр объединяет уровни: расширенные 18 **включают** исходные 12. Текущий пробел — 230 кандидатов; исходный составлял 236.

## Safe reuse / Корректное использование

Carry the source URL, review date, claim type and limitation into any derivative table or graph. Do not relabel hypotheses as partnerships or inventory labels as verified legal companies. No private dataset should be imported here.

При переносе данных сохраняйте URL, дату, тип утверждения и ограничение. Не превращайте гипотезы в партнёрства, а названия из списка — в проверенные юридические компании. Приватные данные сюда не переносятся.

[Source policy](../docs/en/source-policy.md) · [Правила источников](../docs/ru/source-policy.md) · [Rebuild and validation](../scripts/README.md)
