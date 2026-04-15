# Проблема Методологии Evals в Контексте AI Safety — Лекция 3

- **Тип источника:** extra
- **Неделя:** shared
- **Raw:** [`.pptx`](<../../raw/shared/Проблемы методолгии в эвалс 3.pptx>), [sidecar `.md`](<../../raw/shared/Проблемы методолгии в эвалс 3.pptx.md>)
- **Полнота raw:** `.pptx` + generated Markdown sidecar; для слайдового формата структура в целом сохранена

## Ключевая мысль
> **Улучшение методологии evals требует не только более аккуратных тестов, но и более сильной операционализации самих safety-целей: что считается целью системы, в какой онтологии мы это описываем и какие поведенческие паттерны вообще осмысленно измерять.**

## Зачем источник в базе
Это самая исследовательски-направленная часть цикла. Она полезна не как готовый standard, а как пример того, как проблема methodology может переводиться в более конкретную research agenda. В отличие от первых двух лекций, здесь центр тяжести уже не в critique current practice, а в попытке очертить возможный объект исследования.

## Эпистемический статус и как на него смотреть
Это exploratory research-framing lecture, а не settled theory of eval methodology. Ее лучше читать как источник hypotheses and research directions about ontology, goals and operationalization.

## На какие вопросы источник помогает отвечать
- Почему улучшение eval methodology может упираться не только в protocol quality, но и в object definition?
- Что значит говорить о цели ИИ как о pattern on outcomes?
- Почему benchmark and eval themselves encode ontology?
- Какие research questions появляются, если относиться к operationalization как к central bottleneck?

## Краткое содержание
Лекция сначала коротко собирает предпосылки: предпарадигмальное состояние AI safety и evals, значение эмпирики и общий потенциал evals для накопления знаний. Затем она сужает разговор до двух связок: `central alignment problem` и `ontology identification problem`. После этого появляется основная прикладная линия: если говорить о цели ИИ не как о loss function и не как о внутреннем представлении, а как о паттерне на исходах, то нужно понять, как такой паттерн операционализировать и что именно можно измерять как свидетельство goal-directedness или aimability. В финальных слайдах лекция уже напрямую переводит это в language of evals: `eval` как способ зафиксировать паттерн, `benchmark` как конкретная онтология, prompting/fine-tuning как интерфейс управления, и список исследовательских вопросов, которые из этого следуют.

## Как читать источник быстро
- Если нужен conceptual jump, читай slides on ontology identification and the different senses of “goal”.
- Если важен methodological claim, переходи к the move from patterns on outcomes to what evals can actually operationalize.
- Если нужен project-idea layer, смотри final slides where the lecture translates ontology questions into eval research questions.

## Что источник утверждает прямо
- Для прикладных исследований безопасности ИИ особенно важно не смешивать разные значения слова "цель": reward/loss, внутреннее представление цели и паттерн на исходах.
- Если цель понимать как паттерн на исходах, то ее нельзя обсуждать без онтологии, которая делает такие исходы различимыми.
- Benchmark и eval не нейтральны по отношению к онтологии: они задают, что именно считается наблюдаемым и измеримым.
- Улучшение методологии evals может требовать лучшей операционализации самих исследовательских constructs, а не только better protocols.

## Что здесь особенно важно
- **Лекция радикально поднимает ставку для benchmark design.** Benchmark здесь оказывается не просто task suite, а частью онтологии измерения.
- **Операционализация целей становится methodological bottleneck.** Это редкий, но полезный взгляд на связь evals и deeper alignment questions.
- **Текст явно исследовательский и exploratory.** Его полезно читать не как established doctrine, а как источник hypotheses и project directions.
- **Тут хорошо видно, что проблема methodology упирается в объект измерения, а не только в metric hygiene.**

## Интерпретация для курса
В логике всей базы эта лекция особенно ценна тем, что связывает разговор о eval methodology с более глубокими alignment questions. Если week-05 поднимает тему mature measurement discipline, то эта лекция показывает еще более ранний bottleneck: иногда проблема в том, что поле пока недостаточно хорошо понимает, что именно хочет operationalize.

## Что стоит запомнить при повторении
- **Плохая операционализация construct может испортить eval раньше, чем начнется статистика или benchmark design.**
- **Говорить о цели ИИ полезно только если не смешивать разные уровни этого слова.**
- **Benchmark можно понимать как конкретную онтологию измерения, а не просто набор задач.**

## Связанные концепты
- [concepts/eval-methodology](../concepts/eval-methodology.md)
- [concepts/measurement-validity](../concepts/measurement-validity.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/evals](../concepts/evals.md)

## Что осталось неясным / спорным
- Насколько tractable вообще делать полезные evals для constructs вроде goal-directedness и aimability без существенно более сильной теории интеллекта?
- Не приводит ли такой исследовательский фрейм к слишком ранней фиксации на speculative constructs, которые пока трудно валидировать?

## Связанные страницы
- [syntheses/eval-methodology-in-ai-safety](../syntheses/eval-methodology-in-ai-safety.md)
- [sources/slava-meriton-evals-methodology-lecture-01](slava-meriton-evals-methodology-lecture-01.md)
- [sources/slava-meriton-evals-methodology-lecture-02](slava-meriton-evals-methodology-lecture-02.md)
- [concepts/science-of-evals](../concepts/science-of-evals.md)
