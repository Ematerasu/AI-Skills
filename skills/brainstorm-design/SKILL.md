---
name: brainstorm-design
description: Develop a reviewable design before substantial refactors, larger implementations, new subsystems, or shared-interface changes. Compare approaches with diagrams or interactive HTML in Polish or English. Excludes routine edits and explanations of existing code.
---

# Brainstorm larger changes with visual designs

Adapted from Jesse Vincent's `obra/superpowers` brainstorming skill. Turn an intended outcome into a concrete design the user can inspect and correct. Scale the process to the decisions that matter.

## When to use

Use for substantial refactors, larger implementations, new subsystems, and changes to interfaces other components depend on. Judge scope by affected behavior and dependencies, not line count alone.

For a local fix, obvious small edit, or explanation of existing code, proceed with the normal workflow. Do not turn those tasks into a design exercise. If a small task reveals significant architectural choices, explain the discovery and apply this skill to those choices.

## Establish the brief

1. Inspect relevant code, existing architecture, tests, and project instructions before proposing changes.
2. Identify the intended outcome, constraints, and observable success criteria. Reuse information the user has already supplied.
3. Write back a short brief. Distinguish stated requirements from assumptions. For a refactor, state the behavior that must remain the same and any requested behavior changes.
4. Ask only about missing information that materially changes the design. Prefer one focused question at a time. Continue independent inspection while awaiting an answer.
5. If the task contains independent subsystems, propose a sensible decomposition and implementation order. Keep the current design focused.

Use simple Polish or English according to the request. Keep one canonical name for each concept across the brief, design, diagrams, and HTML. Preserve exact code identifiers. Follow the user's glossary. Define specialist terms instead of replacing them with rotating synonyms.

## Compare approaches

Present 2–3 viable approaches when a real choice exists. Lead with the recommended approach and its reason. If only one sensible approach exists, explain it without manufacturing alternatives.

Show the trade-offs that affect this task: complexity, dependencies, compatibility, migration effort, testability, and maintenance. Identify assumptions. Do not invent measurements or imply that illustrative numbers came from the repository.

For each main component, explain its purpose, interface, and dependencies. Follow existing patterns when they fit. Keep unrelated refactors and speculative features outside the design.

## Use visuals to make decisions easier

Create a visual when it reduces the effort needed to compare designs. The user has a standing preference for visual explanations; do not request separate permission just to create a local diagram or HTML artifact.

- Use a diagram for the current structure and the proposed structure.
- Use a table for a small set of trade-offs.
- Use HTML for switching between designs, inspecting affected components, stepping through a request, or comparing a migration sequence.
- Use animation when movement, order, or state is part of the decision. Include pause, restart, and manual stepping where useful.

Use the available `explain-diagram` and `explain-webpage` skills when installed. Read [references/visual-design.md](references/visual-design.md) when a visual design page is useful. If those skills are unavailable, create a focused local diagram or self-contained HTML using the same naming and language rules. No Superpowers server or `writing-plans` skill is required.

Keep observed current behavior, proposed behavior, and fictional simulation clearly labeled. A design preview does not need working product logic. It must make the decisions visible and understandable.

## Present a concrete design

Keep the design proportional to the task. Include only relevant items:

- Goal, scope, exclusions, and success criteria.
- Current structure and proposed components, interfaces, and data flow.
- Recommended approach, alternatives, and trade-offs.
- Important errors, compatibility requirements, and concurrency behavior.
- For code changes, owners of mutable state and resources, visible effects, and any retry, authorization, cache, fallback, or default-value decisions. Use `mindful-code` when available.
- For a refactor, behavior to preserve and the migration sequence.
- Validation that can distinguish a successful change from a broken one.
- Open decisions and assumptions that still matter.

For a larger design, save a short Markdown design note and the useful visual artifact in the workspace's designated output location. Cross-link them. Keep the design note as the record of decisions; use HTML to inspect those decisions. Update both when the design changes.

For a simpler major change, a concise design in chat plus one diagram can be sufficient. Do not produce duplicate documents merely to satisfy a template. Follow repository rules for documentation and commits. This skill does not request an automatic commit or changes under `manual/`.

## Review and implementation handoff

Before substantial implementation, make the concrete design available for review. Check existing conversation context for approval of that design and its material decisions. Do not ask the user to authorize the same scope again.

If a material design decision is unresolved, ask the user to choose or approve the concrete proposal. While it is unresolved, continue work that does not depend on it. Respect any explicit request to stop after planning.

When the design is accepted or the user has explicitly delegated those decisions, record the choice and proceed with the authorized implementation. For a large change, use a concise implementation sequence with checks after meaningful stages. A separate plan review is needed only when the user requests it or a genuinely new decision appears.

If new evidence changes the agreed scope or interfaces, update the design and surface the material decision. Do not restart the whole process for ordinary implementation details.

Before handoff, check for contradictory requirements, undefined terms, missing error paths, and unverified assumptions. State remaining uncertainty. Report implementation results against the original success criteria.
