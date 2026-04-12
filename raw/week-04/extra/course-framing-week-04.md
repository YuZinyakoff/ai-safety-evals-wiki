# Неделя 4. Оценка агентов

Источник: заметка от организаторов курса.  
Роль в базе: `course framing` для четвертой недели, включая переход от week-03, предварительные вопросы, карту чтения и вопросы для обсуждения.

## Переход от предыдущей недели

На предыдущей неделе речь шла о том, что benchmark'и не являются нейтральными измерительными приборами.

- обсуждалось, как дизайн benchmark'а влияет на выводы о модели;
- разбиралось, что вообще считать свидетельством о способностях модели;
- подчеркивалось, что выбор задач, метрик и способов агрегирования уже является содержательным решением;
- отдельно проговаривалось, что решения по оценке влияют не только на локальный вывод о модели, но и на направление прогресса в ML.

## Описание модуля

На этой неделе фокус смещается с benchmark design для одиночных моделей на оценку `LLM agents`.

Агент может:
- планировать;
- вызывать инструменты;
- взаимодействовать со средой;
- вести многошаговое решение;
- ошибаться на промежуточных этапах;
- по-разному вести себя при повторных запусках;
- по-разному реагировать на изменения условий.

Из-за этого усложняется и сама оценка. В центре оказывается не только вопрос "справился ли агент", но и вопрос "что именно мы узнали о нем из этой оценки".

Структура недели:
- первый текст отвечает на вопрос, как устроена область оценки агентов;
- второй показывает, чего не хватает обычным benchmark scores;
- третий предлагает руководство по проведению оценки так, чтобы меньше недооценивать реальные способности агентской системы и меньше портить результат плохой процедурой оценки.

## Предварительные вопросы

В духе идеи Фейнмана Notebook of Things I Don’t Know About полезно начать с честной фиксации своих пробелов в понимании. Это делает чтение целеориентированным. Фокус на конкретных вопросах помогает лучше замечать, какие именно ответы дает текст.

Перед чтением полезно честно ответить себе на несколько вопросов. Не стоит пытаться дать правильный ответ; лучше зафиксировать, что вы уже думаете сейчас и почему.

1. Какие свойства агентской системы, по вашему ощущению, вообще труднее всего измерять корректно?
2. Как рамка `evaluation strategy` (`what to measure`, `how to measure it`, `what the result means`) переносится на оценку агентов? Что в ней может поменяться именно из-за специфики агентских систем?

## Ссылки недели

- Обязательный список чтения: <https://t.me/c/3895961953/258/1722>
- Дополнительные материалы: <https://t.me/c/3895961953/258/1723>
- Задания: <https://t.me/c/3895961953/258/2026>

## Обязательный список чтения

### Evaluation and Benchmarking of LLM Agents: A Survey — SAP Labs

SAP позиционирует себя как глобального лидера в enterprise applications и business AI, а SAP Labs описывает как сеть глобальных R&D-центров, развивающих ключевые решения компании.

Текст раскладывает всю область оценки агентов на два вопроса: `what to evaluate` и `how to evaluate`. Авторы делят `evaluation objectives` на `behavior`, `capabilities`, `reliability`, `safety`, а `evaluation process` — на `interaction modes`, `datasets and benchmarks`, `metrics` и `tooling`.

Этот текст полезнее всего читать как карту поля, а не как законченный стандарт.

Из текста можно вынести:
- какие измерения вообще входят в оценку агентов, кроме `task success`;
- как раскладывать evaluation process на `interaction mode`, `benchmark`, `metric` и `tooling`;
- в чем agent evaluation до сих пор остается фрагментированной и методологически недостроенной областью.

Ссылка: <https://arxiv.org/abs/2507.21504>

### Towards a Science of AI Agent Reliability

Статья от исследователей Princeton University.

Если первый текст показывает, что у агентов много важных свойств, то этот текст предлагает мерить часть из них отдельно и явно. Авторы вводят `holistic reliability profile`: 12 concrete metrics, распределенных по четырем измерениям — `consistency`, `robustness`, `predictability`, `safety`. Затем эта рамка применяется к 14 agentic models, и авторы показывают, что capability gains опережают reliability gains.

Из текста можно вынести:
- почему оценку безопасности нельзя усреднять, если речь идет о `tail risks`;
- почему single success metric скрывает operationally important failures;
- как reliability framework меняет сам вопрос интерпретации результатов.

Ссылка: <https://arxiv.org/html/2602.16666v1>

### METR: Guidelines for capability elicitation

[METR](https://metr.org/) — независимая исследовательская организация, занимающаяся оценкой фронтирных моделей и catastrophic-risk-relevant capabilities.

Это пример методического руководства для autonomy-focused agent evals. Главная идея в том, что evaluation должен измерять не только способности модели "как есть", но и способности, которые могут быть разумно достигнуты через `post-training enhancement`, prompting, tooling и scaffolding. `Elicitation protocol` нужен как защита от сильного занижения capabilities из-за слабого scaffolding, неудачного промптинга или других легко устранимых bottlenecks.

Из текста можно вынести:
- почему agent evaluation может систематически занижать реальные возможности модели;
- как использовать dev set не только для улучшения агента, но и для классификации типов провалов;
- чем `spurious failure` отличается от `real failure` и `tradeoff`;
- какие red flags стоит проверять, прежде чем интерпретировать итоговый score как meaningful.

Важно: сам METR пишет, что это `beta`, `early working draft` и `current best guess`, а не завершенный стандарт.

Ссылка: <https://evaluations.metr.org/elicitation-protocol/>

## Примечание составителей курса

Смысл недели в том, чтобы перестать смотреть на агентские evals как на простое продолжение model benchmarking. Агентская система делает больше, чем один ответ на один prompt, а значит и claims по результатам ее оценки должны быть аккуратнее, богаче и сильнее привязаны к процедуре.

## Вопросы для обсуждения

1. Должен ли хороший evaluation protocol пытаться измерить "максимально достижимые" возможности агента через elicitation, или полезнее оценивать агента в более естественном `product-like setup`? Какие риски у каждого из вариантов?
2. Как соотносятся два измерения из первого текста (`what to evaluate` и `how to evaluate`) с процедурой elicitation у METR и с reliability dimensions из второй статьи?
3. Что в этих статьях относится к третьему шагу `evaluation strategy` — `what the result means`?

## Дополнительные материалы

### Подробнее про концепции и инструменты из ноутбука

1. `ReAct: Synergizing Reasoning and Acting in Language Models`
   - Текст про подход, где модель чередует рассуждение и действия, чтобы решать задачи с инструментами и внешней средой.
   - Ссылка: <https://openreview.net/forum?id=WE_vluYUL-X>

2. `Measuring Mathematical Problem Solving With the MATH Dataset`
   - Исторический контекст к `MATH-500`, который используется в notebook. Полезен, чтобы понимать, на каком типе benchmark оптимизируется агент.
   - Ссылка: <https://arxiv.org/abs/2103.03874>

### Про агентов и методы их создания

1. `Large Language Model Agent: A Survey on Methodology, Applications and Challenges`
   - Широкий обзор того, как вообще устроены агенты, какие design choices существуют и почему они ведут к разным типам поведения.
   - Ссылка: <https://arxiv.org/abs/2503.21460>

### Подробнее о практике оценки агентов

1. `Measuring AI agent autonomy in practice`
   - Anthropic о том, как они пытаются измерять автономность агентов в реальном использовании на данных из миллионов human-agent interactions.
   - Ссылка: <https://www.anthropic.com/research/measuring-agent-autonomy>

2. `SWE-bench: Can Language Models Resolve Real-World GitHub Issues`
   - Канонический benchmark для software engineering tasks на реальных GitHub issues.
   - Ссылка: <https://arxiv.org/abs/2310.06770>

3. `Introducing SWE-bench Verified`
   - Текст о human-verified subset SWE-bench и о том, как сам benchmark тоже нуждается в критической проверке.
   - Ссылка: <https://openai.com/index/introducing-swe-bench-verified/>

4. `Resources | METR’s Autonomy Evaluation Resources`
   - Главная страница-индекс всего набора METR-ресурсов по автономным evals: task suite, elicitation protocol, task standard and workbench, example protocol и research block про impact of elicitation.
   - Ссылка: <https://evaluations.metr.org/>
