# Expanded research registers / Реестры расширенного исследования

[Data guide](../README.md) · [English study](../../research/en/value-chains.md) · [Исследование на русском](../../research/ru/value-chains.md)

| File | Purpose / Назначение |
|---|---|
| [companies.json](companies.json) | Selected-company analysis for the 18-company expansion / Анализ 18 выбранных компаний |
| [evidence-ledger.json](evidence-ledger.json) | Public-source evidence trail and claim boundaries / Путь к открытым источникам и границы утверждений |
| [relationships.json](relationships.json) | Typed cross-company connections and hypotheses / Типизированные связи и гипотезы между компаниями |
| [sources.json](sources.json) | Standalone copy of the 38-source register embedded in the evidence ledger / Отдельная копия реестра 38 источников из evidence ledger |
| [company-comparison.csv](company-comparison.csv) | Flat comparison table for spreadsheet use / Плоская сравнительная таблица для работы в электронных таблицах |

**Inventory:** 18 company records · 61 claim records · 38 official source documents · 21 typed relationships. / **Состав:** 18 компаний · 61 запись утверждений · 38 официальных документов · 21 типизированная связь.

The 21 relationships comprise 4 documented integration links, 2 named alliance listings, 1 advertised integration offering, 7 analyst hypotheses and 7 overlap comparisons. These classes must not be flattened into “21 partnerships.” / В 21 связь входят 4 документированные интеграционные связи, 2 заявления об альянсах, 1 рекламируемое интеграционное предложение, 7 гипотез и 7 конкурентных пересечений. Нельзя превращать эти классы в «21 партнёрство».

This layer **includes the original 12 companies and adds 6**, rather than creating 18 additional profiles. It does not imply all 248 candidate labels have been researched. Use [current coverage](../research-coverage.json) for the unified view and the [original profile dataset](../company-profiles.json) for the preserved 12-profile evidence schema.

Этот уровень **включает исходные 12 компаний и добавляет 6**, а не создаёт ещё 18 профилей. Он не означает, что исследованы все 248 кандидатов. Объединённый взгляд — в [текущем покрытии](../research-coverage.json); сохранённая структура исходных 12 профилей — в [исходном наборе](../company-profiles.json).

## Record pointers / Указатели записей

- `companies.json` → `companies[]` → `company_id`: joins to the public candidate inventory; `report_anchor` links to the corresponding company card. / Связь с публичным кандидатом; `report_anchor` ведёт к карточке.
- `evidence-ledger.json` → `claims[]`: `claim_id`, `claim_ref`, `source_ids`, `evidence_class` and `limits` preserve the evidence trail. / ID, ссылка на утверждение, источники, класс и границы сохраняют проверяемость.
- `relationships.json` → `relationships[]`: `companies`, `relation_type`, `source_ids` and `evidence_boundary` define the pair and the strength of the statement. / Пара компаний, тип, источники и граница определяют смысл связи.

Source and claim counts belong to this study and overlap the original baseline. Do not add them into a combined unique total. / Источники и утверждения пересекаются с исходной базой; их нельзя складывать в уникальный итог.

**Keep the relationship type when exporting.** A source-backed integration, a vendor ecosystem entry, a complementarity hypothesis and competitive overlap have different meanings. None establishes new buying intent or willingness to partner.

**При экспорте сохраняйте тип связи.** Документированная интеграция, запись в экосистеме, гипотеза взаимодополнения и конкурентное пересечение имеют разный смысл. Они не устанавливают новый покупательский интерес или желание сотрудничать.

[Evidence rules](../../docs/en/source-policy.md) · [Правила доказательности](../../docs/ru/source-policy.md)
