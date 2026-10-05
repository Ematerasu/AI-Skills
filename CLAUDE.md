# Code explanations, larger changes, and code quality

Use these preferences when you explain code, architecture, bugs, changes, or technical choices.

For a substantial refactor, larger implementation, new subsystem, or change to shared interfaces, use `brainstorm-design` before substantial implementation. Ground the design in the existing code and use visual comparisons when they help. Routine edits and explanations do not need a design process.

## Implementation and review

Use `mindful-code` when writing, refactoring, or reviewing code in any language. Match the repository's language version, runtime, conventions, libraries, and error and missing-value rules. Prefer simple execution paths and abstractions that solve an existing problem.

- Prefer immutable data. Do not expose mutable internal collections or assume that a read-only binding makes its referenced data immutable.
- Give mutable state and resources an explicit owner. For concurrency changes, identify shared state and its synchronization mechanism.
- Make I/O, argument mutation, and other side effects apparent in the API. Preserve error and missing-value contracts.
- Retry requires an explicit idempotency decision, attempt limit, per-attempt timeout, and total deadline. Account for existing retries in other layers.
- An authorization failure must not trigger an authorization bypass.
- Add fallback, cache, or default values only when requirements or an existing contract justify them.

Use project tools for formatting. These instructions concern behavior and design.

For all code changes, add comments only when they explain a necessary reason, invariant, constraint, or contract that clear code cannot express well. First consider clearer names, control flow, or function boundaries. Do not narrate obvious operations, record chat history, or refer to the agent conversation. Keep necessary comments brief and maintainable.

## Communication

- Answer in Polish or English, as requested. Otherwise use the language of the user's latest request.
- Write in a practical ASD-STE100-inspired style. Treat Polish as an adaptation, not formal STE compliance.
- Use one canonical name for each code object or concept across prose, diagrams, and HTML. Preserve exact code identifiers.
- Keep facts, uncertainty, conditions, and requirement strength intact when you simplify.
- Prefer a focused visual plus a short explanation for architecture, interacting components, data flow, branches, or state changes. Create the visual without waiting for a separate request.
- Use short prose for a single fact or simple edit. Use HTML when interaction or animation helps explain the mechanism.
- Let visuals replace redundant text. Give the main result first and keep supporting detail easy to scan.
- Inspect relevant code before explaining actual behavior. Keep observed behavior, inference, and illustrative simulation distinct.

## Skills

Use the installed skill with the matching name. Read its SKILL.md before using it.

- `clear-writing`: simple Polish or English, consistent terminology, and the "80% ASD-STE100" style.
- `explain-diagram`: architecture, relationships, call sequences, states, and data flow.
- `explain-webpage`: interactive HTML explanations, including useful HTML animations.
- `brainstorm-design`: scope, alternatives, and a reviewable design for larger implementations and refactors, with visual HTML when useful.
- `mindful-code`: pragmatic code quality across languages, ownership, mutation, resource lifetime, and distributed-system behavior.

For project installation, the bundled source files are under `skills/<name>/SKILL.md` when this package is kept together. After installation, use the host's discovered skill locations. If a skill is unavailable, follow the preferences above using the available tools.

These preferences guide explanations and authorized code changes. They do not request unrelated code renames, changes to repository documentation, or publication of artifacts.
