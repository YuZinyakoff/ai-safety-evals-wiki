# Judging LLM-As-A-Judge With MT-Bench And Chatbot Arena

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/extra/Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.md>), [PDF](<../../raw/week-03/extra/2306.05685v4.pdf>), [TeX source](<../../raw/week-03/extra/arXiv-2306.05685v4.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2306.05685)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **LLM judge может быть масштабируемой заменой части human preference evaluation, но только если учитывать его собственные biases и тщательно проектировать judge prompt.**

## Зачем источник в базе
Это один из канонических текстов про `LLM-as-a-judge`. Он нужен, чтобы week-03 не сводилась к критике benchmark'ов на уровне dataset design, а включала еще и разговор о judge-based evaluation для open-ended tasks, где обычные closed-form benchmarks уже слишком слабы.

## Эпистемический статус и как на него смотреть
Это canonical proposal-and-validation paper for `LLM-as-a-judge` in preference-heavy chat settings. Его лучше читать как сильный case for judge-based evaluation in a particular regime, а не как универсальную лицензию заменять human judgment everywhere.

## На какие вопросы источник помогает отвечать
- Зачем вообще нужны `MT-Bench` и `Chatbot Arena` в мире open-ended assistant evaluation?
- Когда `LLM-as-a-judge` выглядит достаточно близким к human preference judgments?
- Какие judge biases authors обнаруживают и как пытаются их смягчать?
- Почему preference benchmarks и capability benchmarks не стоит смешивать?

## Краткое содержание
Статья начинается с постановки проблемы: обычные benchmarks плохо улавливают человеческое предпочтение в multi-turn и open-ended assistant settings. Затем авторы вводят два benchmark-like evaluation assets: `MT-Bench` как curated набор многоходовых вопросов и `Chatbot Arena` как crowdsourced platform с pairwise battles. После этого paper делает главный ход: предлагает использовать сильные LLMs как judges и систематически сравнивает их решения с human preferences. В средней части статьи авторы разбирают failure modes judge models: position bias, verbosity bias, self-enhancement bias и ограниченную reasoning ability, а затем показывают mitigation ideas вроде chain-of-thought и reference-guided judging. В финальной части paper сравнивает agreement judge models и humans и получает сильный результат для GPT-4 на preference-style evaluation, одновременно предлагая hybrid view: capability benchmarks и preference benchmarks нужны вместе.

## Как читать источник быстро
- Если нужен big picture, читай motivation for open-ended evaluation plus what `MT-Bench` and `Chatbot Arena` are for.
- Если вопрос про judge reliability, переходи к sections on biases and mitigation strategies.
- Если нужен final practical claim, смотри agreement-with-humans results and the hybrid conclusion about preference plus capability benchmarks.

## Что источник утверждает прямо
- Авторы предлагают `MT-Bench` и `Chatbot Arena` как preference-oriented evaluation assets для open-ended assistant settings, где обычные closed-form benchmarks слишком узки.
- В этих settings сильный judge model вроде GPT-4 может достигать высокого agreement with human preferences.
- Judge models демонстрируют систематические biases, включая position bias, verbosity bias, self-enhancement bias и limits in reasoning.
- Prompt design, chain-of-thought и reference-guided judging могут частично смягчать эти biases, но не делают judging neutral by default.

## Что здесь особенно важно
- **Preference evaluation** и обычные capability benchmarks измеряют разные вещи.
- **`LLM-as-a-judge`** не нейтрален: у judge есть собственные systematic biases.
- **Prompt design judge'а** сильно влияет на качество результата.
- **MT-Bench / Chatbot Arena** важны не только как datasets, но и как новые формы evaluation practice.

## Интерпретация для курса
Для курса это не “доказательство, что judge solved evaluation”, а сильный best-case paper для preference-heavy regime. Его полезно читать как scoped success case: judge-based evaluation действительно работает лучше в некоторых open-ended settings, но только вместе с явным учетом judge design и failure modes.

## Что это добавляет к теме недели
Источник делает week-03 шире. Он показывает, что как только benchmark'и выходят в open-ended regime, design problem сдвигается: теперь важно не только выбрать dataset и metric, но и продумать judge, reference, comparison mode и format of interaction. Это важный мост между benchmark design и современными evaluation pipelines.

## Что стоит запомнить при повторении
- **Judge-based evaluation** полезна там, где closed-form benchmark уже мало что говорит о user utility.
- **Высокий agreement judge'а с людьми не отменяет необходимость понимать его biases.**
- **Judge prompt — часть benchmark design, а не техническая мелочь.**

## Связанные концепты
- [concepts/llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Насколько устойчивы эти выводы за пределами preference-heavy chat settings?
- Можно ли judge-based evaluation расширять на correctness-heavy и high-stakes domains без human grounding?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/limits-scalable-evaluation-frontier](limits-scalable-evaluation-frontier.md)
- [sources/no-free-labels-llm-as-a-judge](no-free-labels-llm-as-a-judge.md)
- [sources/inspect-ai-tutorial-week-03](inspect-ai-tutorial-week-03.md)
