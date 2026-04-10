# What AI Evaluations For Preventing Catastrophic Risks Can And Cannot Do

- Тип источника: theory
- Неделя: week-01
- Raw: `raw/week-01/theory/Barnett-Thiergart-What+AI+evals+for+preventing+catastroph+risks+can+and+cannot+do-arX2412v1.pdf`
- Оригинал: https://arxiv.org/abs/2412.08653
- Полнота raw: PDF статьи

## Зачем источник в базе
Это самый систематичный текст недели о границах evals. Он нужен как опорная страница, когда хочется не просто помнить, что у evals есть ограничения, а аккуратно различать, какие именно claims о risk и safety они поддерживают.

## Краткое содержание
Систематический разбор того, какие claims о catastrophic risk можно и нельзя опирать на современные AI evals. Текст отделяет полезные функции evals от фундаментальных ограничений behavior-based paradigm и завершает обсуждение предварительными governance и safety recommendations. Если Apollo дает словарь, то этот источник дает более строгую дисциплину вывода: он все время спрашивает не "полезен ли eval вообще?", а "какой тип вывода из него действительно оправдан?".

## Ключевые идеи
- Evals могут надежно установить lower bounds на наблюдаемые capabilities.
- Для current models они в принципе могут помогать оценивать misuse risk, но только при сильных предпосылках о capability elicitation и превосходстве evaluators над attackers.
- Evals полезны для науки, preparedness и policy coordination.
- В текущей парадигме evals не могут дать upper bounds на capabilities.
- Evals не умеют надежно forecast future capabilities через precursor signals.
- Evals не дают robust assessment для misalignment, autonomy и unknown unknown risks.

## Опорные тезисы из источника
- Текст утверждает, что evaluations надежно показывают только то, что система уже сумела продемонстрировать, то есть lower bounds.
- Для misuse evaluations evaluators должны уметь находить threat vectors лучше потенциальных attackers и иметь преимущества, которые недоступны злоумышленникам.
- Авторы подчеркивают, что current evaluations с высокой вероятностью under-elicit dangerous capabilities.
- Отсутствие выявленной способности не доказывает ее отсутствия, потому что новые scaffolds, fine-tuning, post-training improvements и in-context learning могут резко поднять результат.
- Подходы с precursor capabilities и safety buffers опираются на слабые предпосылки о порядке появления опасных способностей.
- Для autonomous and misaligned systems проблема усложняется из-за sandbagging, unknown propensities и отсутствия методов, которые могли бы надежно проверять alignment в novel situations.
- Авторы отдельно выделяют unknown unknown risks как фундаментальное ограничение любого threat modeling.
- В preliminary recommendations входят third-party audits, conservative red lines, defense in depth for cybersecurity, monitoring for signs of misalignment и investment in research.

## Что это добавляет к теме недели
Этот источник наиболее четко разводит полезность evals и границы того, что на них можно навешивать в safety case. По сути он усиливает оговорку из Apollo: evals нужны для decision-making, но их нельзя превращать в главный и тем более единственный механизм гарантии безопасности. Для повторения недели это, вероятно, самый полезный текст, если нужно снова собрать в голове именно логику ограничений, а не отдельные примеры.

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
