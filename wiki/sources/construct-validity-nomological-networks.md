# Establishing Construct Validity In LLM Capability Benchmarks Requires Nomological Networks

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/extra/Establishing Construct Validity in LLM Capability Benchmarks Requires Nomological Networks.md>)
- **Оригинал:** [arXiv HTML](https://arxiv.org/html/2603.15121v1)
- **Полнота raw:** clipped Markdown

## Ключевая мысль
> **Нельзя просто назвать benchmark “reasoning benchmark” и считать, что construct уже измерен.** Нужно еще показать, как этот construct связан с задачами, другими способностями и ожидаемыми эмпирическими отношениями.

## Зачем источник в базе
Это самый философски нагруженный, но содержательно полезный extra-text недели. Он нужен, чтобы придать week-03 более глубокий язык для разговора о capability claims: почему слова вроде `reasoning`, `theory of mind` или `morality` сами по себе создают сильные интерпретации и требуют более строгой validity framework.

## Эпистемический статус и как на него смотреть
Это exploratory theoretical paper, который заимствует язык psychometrics и philosophy of measurement для LLM benchmarks. Его полезно читать как попытку поднять планку capability claims, а не как уже settled doctrine для всего поля.

## На какие вопросы источник помогает отвечать
- Почему capability labels вроде `reasoning` не стоит принимать за сами измеренные constructs?
- Что такое `nomological network` и зачем она нужна benchmark interpretation?
- Чем nomological account of construct validity отличается от causal и inferential alternatives?
- Как более строгий validity language может ограничивать слишком свободные capability claims?

## Краткое содержание
Paper начинает с критики распространенной практики: researchers приписывают LLM human-like capabilities на основании benchmark results без достаточной теории того, что benchmark вообще измеряет. Затем автор сравнивает три account of construct validity — causal, inferential и nomological — и утверждает, что для текущего LLM research лучше всего подходит именно `nomological account`, потому что она не требует слишком сильных онтологических обязательств, но при этом дает substantive framework. Во второй части paper автор применяет эту рамку к reasoning capability: обсуждает task benchmarks, content validity, convergent и discriminant analysis, а также риск `theoretical–empirical mismatch`, когда observed benchmark relations плохо согласуются с заявленной network of capabilities. Итоговый вывод: capability benchmarks требуют не только scores, но и richer theoretical web, которая ограничивает допустимые интерпретации.

## Структура материала
- `1 Introduction`: почему capability benchmarks требуют более сильной теории validity.
- `2 The nomological account is the best available framework for conceptualizing LLM capabilities`: сравнение causal, inferential и nomological accounts.
- `3 Implications of the nomological account for LLM benchmark design`: design of nomological networks, validation, convergent / discriminant analysis и theory–measurement conflict.
- `4 Conclusion`: сжатое сведение argument.

## Как читать источник быстро
- Если нужен main claim, читай `1 Introduction` и затем `2 The nomological account...`.
- Если важен application layer, основной раздел — `3 Implications of the nomological account for LLM benchmark design`.
- Если статья кажется слишком abstract, заходи в `2.3 Nomological Networks as a middle ground...`, а затем в `3.1–3.3`: там theory быстрее цепляется за benchmark practice.

## Что источник утверждает прямо
- Capability labels вроде `reasoning` не становятся валидными автоматически только потому, что benchmark так назван.
- Автор сравнивает causal, inferential и nomological accounts of construct validity и утверждает, что для LLM capability benchmarks сейчас особенно полезен именно nomological account.
- Более сильный construct claim требует evidence from relations between tasks, constructs, convergent and discriminant patterns, not just one benchmark score.
- `Theoretical–empirical mismatch` выступает как важный warning sign: observed relations могут плохо поддерживать заявленную capability story.

## Что здесь особенно важно
- **Construct labels** автоматически тянут за собой сильные человеческие интерпретации.
- **Task score** сам по себе не равен capability claim.
- **Nomological network** задает более строгий язык для связи benchmark'ов и capability vocabulary.
- **Theoretical–empirical mismatch** — полезная идея для критики слишком смелых capability claims.

## Интерпретация для курса
Для курса этот paper полезен как способ ужесточить язык вывода. Он помогает различать “benchmark показал performance on tasks of type X” и “мы получили evidence for capability Y”, то есть прямо повышает требовательность к тому, что именно benchmark score вообще лицензирует.

## Что это добавляет к теме недели
Источник углубляет week-03 до уровня language of claims. HELM, ECBD и Benchmark Lottery в основном обсуждают benchmark design и ecosystem design, а этот paper добавляет еще один вопрос: что вообще нужно, чтобы слова про “capability” и “reasoning” были хоть сколько-то научно оправданными.

## Что стоит запомнить при повторении
- **Назвать capability легче, чем валидно ее измерить.**
- **Benchmark design и construct validity тесно связаны.**
- **Номологическая сеть — это попытка ограничить слишком свободные интерпретации benchmark scores.**

## Связанные концепты
- [concepts/construct-validity](../concepts/construct-validity.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/evidence-centered-benchmark-design](../concepts/evidence-centered-benchmark-design.md)

## Что осталось неясным / спорным
- Насколько сама психометрическая традиция достаточно зрелая, чтобы быть сильным ориентиром для LLM evaluation?
- Можно ли practically строить такие nomological networks в быстро меняющемся benchmark ecosystem?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/evidence-centered-benchmark-design-nlp](evidence-centered-benchmark-design-nlp.md)
- [sources/benchmarkcards-llm-benchmarks](benchmarkcards-llm-benchmarks.md)
