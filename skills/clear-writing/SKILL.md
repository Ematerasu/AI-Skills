---
name: clear-writing
description: Write or revise code explanations and technical prose in simple Polish or English, with ASD-STE100-inspired sentences and consistent names. Use for explanations, change summaries, and requests for plain language or 80% ASD-STE100.
---

# Clear writing

Adapted from Ashrya Agrawal's `karpathy-output-style`, inspired by Andrej Karpathy's post. Explain the subject so the reader can understand it without decoding the prose.

## Language and style

1. Use the user's requested language. Otherwise follow the language of the latest request. Support both Polish and English.
2. Identify the reader's question and the facts that answer it. Give the main result, then build the explanation in a useful order.
3. Use common words, concrete subjects, and active verbs. Name the actor. Define necessary technical terms at first use.
4. Keep one main idea per sentence. Aim for 15–20 words. Treat 25 words per explanation and 20 per instruction as useful upper targets, not reasons to lose meaning.
5. Keep one topic per paragraph. Prefer 2–4 sentences. Split paragraphs longer than six sentences.
6. Give one instruction per sentence, unless actions must happen together. Put prerequisites before actions. Use numbered steps for sequences.
7. Break long noun groups into phrases that show relationships. Remove decorative synonyms, stock phrases, idioms, and unnecessary words.
8. Preserve facts, numbers, units, uncertainty, exceptions, conditions, and the user's intended meaning. Read the result again for meaning.

In Polish, use natural grammar and normal inflection. Prefer direct sentences such as "`OrderService` sprawdza zamówienie." Do not force English grammar onto Polish.

## One object, one name

- Use exact code identifiers in backticks. Use the same identifiers in visual labels.
- Select one canonical term for each concept. Follow an existing repository glossary when available.
- Reuse that term across the explanation, table, diagram, and HTML. Do not alternate between "manager", "service", and "handler" for one object.
- Define a Polish term once when useful: `JobQueue` means "kolejka zadań". Do not later call `JobQueue` "bufor" or "scheduler". Normal inflection of "kolejka zadań" is allowed.
- Distinguish different objects that share a short name. Add a module or path when needed.
- Map an existing alias to the canonical name once. Continue with the canonical name.
- Show a small glossary for a longer explanation only when it reduces ambiguity. Do not rename code to make the explanation easier.

## Accuracy before compression

Inspect relevant code before describing actual behavior. Cite the useful symbol, file, or line. Mark inferences and fictional examples.

Keep "may", "must", "should", and their Polish equivalents at the same strength. "Może powodować błąd" must not become "powoduje błąd". Do not add a cause or guarantee just to make a sentence clearer.

For ordinary explanations, aim for a first view of about 150–250 words, excluding code and visuals. Expand when requested or required for accuracy. A diagram should replace repeated prose.

## ASD-STE100 and the "80%" mode

Default to practical STE-inspired writing. "80% ASD-STE100" means a style preference, not a measured conformity score. Allow necessary specialist terms and more complex sentences when they preserve accuracy. Define the term or follow a difficult idea with a simple example. Canonical names remain mandatory in this mode.

Polish uses the same clarity principles as a local adaptation. Do not claim formal ASD-STE100 compliance for Polish.

If the user asks for strict English ASD-STE100, read [references/asd-ste100.md](references/asd-ste100.md). Use the official rules and dictionary for the requested issue, plus the relevant technical glossary. If those sources are unavailable, return a clearly labeled STE-inspired draft and identify unverified checks. Do not claim compliance from short sentences or model memory.

## Example

Fictional example, not a description of an inspected repository:

- Polish: "`OrderService` sprawdza zamówienie. Następnie `OrderService` wywołuje `OrderRepository`. `OrderRepository` zapisuje zamówienie w bazie danych."
- English: "`OrderService` validates the order. Then `OrderService` calls `OrderRepository`. `OrderRepository` saves the order in the database."

Return the explanation or revised text. Discuss edits only when useful or requested. Before sending, check actor clarity, canonical names, preserved meaning, and removable repetition.
