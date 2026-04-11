# What AI Evaluations For Preventing Catastrophic Risks Can And Cannot Do

- **Тип источника:** theory
- **Неделя:** week-01
- **Raw:** [HTML-clipped `.md`](<../../raw/week-01/theory/What AI evaluations for preventing catastrophic risks can and cannot do.md>), [PDF](<../../raw/week-01/theory/Barnett-Thiergart-What+AI+evals+for+preventing+catastroph+risks+can+and+cannot+do-arX2412v1.pdf>), [TeX source](<../../raw/week-01/theory/arXiv-2412.08653v1.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2412.08653)
- **Полнота raw:** сильный raw-набор: clipped HTML, PDF и TeX source

## Ключевая мысль
> **Главная польза evals в safety-контексте не бесконечна: они хорошо показывают то, что система уже сумела продемонстрировать, но плохо поддерживают сильные отрицательные и дальние прогнозные claims.**

## Зачем источник в базе
Это самый систематичный текст недели о границах evals. Он нужен как опорная страница, когда хочется не просто помнить, что у evals есть ограничения, а аккуратно различать, **какие именно claims о risk и safety они поддерживают**, а какие нет.

## Краткое содержание
Статья устроена как систематический разбор роли evals внутри более широкого `safety case`. Сначала авторы задают рамку вопроса: какие именно catastrophic-risk claims мы вообще хотим поддерживать с помощью evaluations. Затем они раскладывают обсуждение по двум осям — `existing vs future models` и `misuse vs autonomous / misaligned risks` — и на этой матрице показывают, где современные behavior-based evals действительно дают полезный сигнал. В средней части paper подробно разбираются ограничения: `under-elicitation`, зависимость от threat modeling, невозможность надежно получить **upper bounds** на capabilities, слабость precursor-style forecasting и особые трудности для autonomy / misalignment scenarios, где становятся важны sandbagging, hidden propensities и unknown unknowns. Финал текста важен тем, что он не остается на уровне критики: авторы обсуждают, какие compensating measures и governance moves вроде audits, conservative red lines и defense in depth имеют смысл даже при признании фундаментальных limits evals.

## Что здесь особенно важно
- **Lower bounds сильнее upper bounds.** Это, возможно, самый важный запоминающийся тезис всей статьи.
- **Misuse risk и misalignment risk не симметричны.** Для misuse evals иногда могут быть practically useful, но только при сильных условиях; для misalignment и autonomy limits гораздо серьезнее.
- **Future capability forecasting очень хрупок.** `Precursor signals` и `safety buffers` не дают надежной опоры без сильных предпосылок.
- **Threat modeling ограничено неизвестным неизвестным.** Авторы отдельно подчеркивают, что часть risk landscape не попадает в eval по определению.
- **Evals не отменяются, а встраиваются в larger safety stack.** Это важная часть дисциплины: инструмент полезен, но не самодостаточен.

## Что это добавляет к теме недели
Если Apollo задает язык области, то Barnett-Thiergart задает **дисциплину вывода**. После этой статьи week-01 перестает быть просто “неделей про limits of evals” и становится неделей про то, **какой тип evidence действительно способен поддерживать какой тип claim**. Для повторения курса это, вероятно, самая полезная source page, когда нужно восстановить именно структуру ограничений.

## Что стоит запомнить при повторении
- **“Не нашли”** не равно **“этого нет”**, особенно для dangerous capabilities.
- **Misuse, autonomy и misalignment** требуют разных ожиданий от evals.
- **Хороший safety case** не строится только на score; ему нужны и другие защитные слои.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/understanding-based-evals](../concepts/understanding-based-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)

## Что осталось неясным / спорным
- Можно ли радикально улучшить capability elicitation так, чтобы practical value evals выросла без ложного чувства надежности?
- Какие дополнительные safety mechanisms должны компенсировать пределы behavior-based evaluations?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
