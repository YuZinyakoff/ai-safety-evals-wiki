# We Need A Science of Evals

- **Тип источника:** theory
- **Неделя:** week-05
- **Raw:** [clipped `.md`](<../../raw/week-05/theory/We Need A ‘Science of Evals’.md>)
- **Оригинал:** [Apollo Research](https://www.apolloresearch.ai/blog/we-need-a-science-of-evals/)
- **Полнота raw:** хороший web-clipped Markdown

## Ключевая мысль
> **Если evals используются как основание для deployment, policy и risk thresholds, поле не может оставаться набором локальных эвристик.** Нужна более зрелая дисциплина с ясными объектами измерения, достаточным coverage, воспроизводимыми процедурами и более сильной статистической культурой.

## Зачем источник в базе
Это самый удобный текст недели для перехода от critique отдельных benchmark practices к critique зрелости поля в целом. Он не дает готовый стандарт, но хорошо показывает, почему разговор об evals уже нельзя вести только как разговор о полезных инженерных трюках и benchmark recipes.

## Краткое содержание
Текст начинается с мотивации: evals уже участвуют в safety-related decisions и потенциально будут связаны с law and policy, а значит, их результатам придется выдерживать гораздо более сильную внешнюю проверку. Дальше Apollo показывает на примере prompt sensitivity и elicitation instability, почему нынешняя практика часто больше похожа на искусство, чем на зрелую научную дисциплину. После этого пост вводит идею `Science of Evals` через аналогию с maturation process других инженерных полей, особенно авиации: от exploratory phase к informal norms и дальше к standards that are ready for law. Затем текст формулирует вопросы, на которые должна уметь отвечать зрелая evaluation field: что именно измеряется, какое coverage у eval, насколько robust и replicable результаты, возможны ли статистические guarantees и как результаты current evals переносятся на future systems. Финальный блок уже работает как field-building memo: перечисляет ранние примеры полезных meta-evaluation работ и формулирует open questions вокруг conceptual clarity и trustworthiness of results.

## Что здесь особенно важно
- **Порог требований к evals поднимается из-за того, что они становятся policy-relevant.**
- **`Science of Evals` — это не "еще больше benchmark'ов", а более зрелая measurement discipline.**
- **Два центральных вопроса здесь очень простые и очень жесткие:** измеряем ли мы правильную величину и насколько вообще можно доверять результату?
- **Coverage, replicability и statistical guarantees** описаны как признаки зрелости поля, а не как nice-to-have дополнения.
- **Пост одновременно и диагностический, и организационный.** Он не только критикует состояние поля, но и пытается собрать research agenda и экосистему вокруг этого направления.

## Что это добавляет к теме недели
Если первый текст недели критикует именно safety benchmarks, то Apollo поднимает разговор на уровень всей дисциплины. Он помогает увидеть, что проблемы safety benchmarking — не локальная техническая неисправность, а частный случай более общей незрелости evals как поля.

## Что стоит запомнить при повторении
- **High-stakes evals требуют стандарта, близкого к engineering discipline, а не только к clever experimentation.**
- **Плохая conceptual clarity и слабая trustworthiness of results подрывают весь downstream use of evals.**
- **Если поле хочет быть "ready for law", оно должно уметь говорить на языке coverage, reproducibility и stronger statistical guarantees.**

## Связанные концепты
- [concepts/science-of-evals](../concepts/science-of-evals.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/risk-quantification](../concepts/risk-quantification.md)
- [concepts/measurement-validity](../concepts/measurement-validity.md)

## Что осталось неясным / спорным
- Насколько realistic и desirable делать сильные статистические guarantees для frontier safety evals, а не только для более узких benchmark settings?
- Где проходит граница между полезной field building rhetoric и реально operational research program?

## Связанные страницы
- [weeks/week-05](../weeks/week-05.md)
- [sources/how-should-ai-safety-benchmarks-benchmark-safety](how-should-ai-safety-benchmarks-benchmark-safety.md)
- [syntheses/reliable-ai-safety-evals](../syntheses/reliable-ai-safety-evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
