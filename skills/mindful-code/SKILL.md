---
name: mindful-code
description: Write, refactor, or review code in any language with pragmatic function and abstraction design, explicit ownership of mutable state and resources, and deliberate retry, authorization, cache, fallback, and concurrency behavior. Formatting belongs to project tools.
---

# Mindful Code

Use clean-code principles as design questions, not universal laws. Borrow Rust's questions about ownership, sharing, and mutation. Apply those questions using the target language's guarantees and idioms. Distinguish compiler-enforced guarantees from conventions. Support conventions with API boundaries, encapsulation, synchronization, and focused checks; do not imitate Rust syntax or force its mechanisms onto another language.

Apply the relevant parts to the code being changed. Do not turn every small edit into a full design review or repeat this checklist in every answer.

## Start with the repository

- Inspect the affected code, callers, tests, language and runtime versions, framework lifecycle, and existing conventions.
- Reuse existing libraries and patterns. Add a new pattern or dependency only for a concrete need that existing tools do not meet.
- Follow the project's conventions for missing values, errors, transactions, dependency management, logging, and asynchronous execution. Use exceptions, result types, error returns, or optional values according to the language and existing API contracts.
- Preserve the requested scope. Improve nearby structure when it helps the task, without unrelated cleanup.

## Functions and abstractions

- Give a function a coherent purpose and a contract the caller can understand. Make important effects and failure modes apparent.
- Prefer a flow that can be traced directly. Use a loop, collection operation, or helper according to clarity and repository practice.
- Extract a function when it names a meaningful operation, separates effects, or makes a complex rule easier to inspect and test.
- Keep cohesive steps together when splitting them would scatter the flow or hide dependencies. Do not enforce a fixed line limit or one-line methods.
- Add an abstraction when it protects a real boundary, invariant, or variation. Do not add interfaces, factories, generic frameworks, or layers merely to satisfy a pattern.
- Share code when the domain rule is shared. Similar syntax alone is not evidence that two responsibilities belong in one abstraction.
- Avoid boolean mode flags or parameter bundles that conceal unrelated operations. Prefer an explicit contract when that makes callers clearer.
- Use names that distinguish real concepts. Keep names consistent with the repository and explanations.

## Comments must earn their place

- Before adding a comment, check whether the function is clear enough. Consider better names, a simpler flow, or a meaningful function boundary. Do not add abstractions merely to eliminate a useful comment.
- Add a comment only when it conveys necessary information that the code does not express clearly: a reason, invariant, resource-lifetime rule, concurrency constraint, external contract, or compatibility requirement.
- Do not narrate obvious operations, paraphrase a method name, or add a comment to every block. Do not add API documentation that merely repeats the signature.
- Do not put conversation history in code: no references to the user, agent, prompt, chat, or an earlier discussion. If the conversation reveals a lasting requirement, express the independently meaningful requirement only when a comment is actually needed.
- Keep comments short and close to the relevant code. Explain the important reason or constraint without overwhelming the execution flow.
- Do not use a comment to excuse confusing code or claim a guarantee the implementation does not enforce.
- Follow required public-API documentation conventions. Document non-obvious contracts and behavior instead of filling templates with redundant text.
- When changing code, update or remove affected comments that are now false or redundant. Do not perform unrelated comment cleanup.

## Ownership, mutation, and sharing

For changed mutable state, answer these questions:

1. Who creates and owns the object?
2. Who can change it, and through which API?
3. Who holds an alias or shares it across threads, tasks, or processes?
4. Which invariant must remain true during a change?
5. Who owns any resources associated with it, and when do those resources end?

Keep these answers in the API and implementation where possible. Add a short comment or explanation only when the contract is not apparent.

- Prefer immutable objects for data unless mutation serves a concrete need. Stay within the project's supported language, runtime, and framework constraints.
- A read-only binding or immutable wrapper does not necessarily make referenced data deeply immutable. Check the target language's actual guarantees, including nested values and interior mutation.
- Do not expose internal mutable collections, arrays, or mutable elements. Use a defensive copy, immutable value, or controlled API as the contract requires.
- An unmodifiable view can still reflect changes to its backing collection. A shallow copy may still share mutable elements. Choose deliberately.
- Be deliberate about both input aliases and returned values. A constructor can retain mutable state supplied by its caller.
- Keep necessary mutation local or behind an explicit owner. Do not change a caller's argument unless the API states that behavior.
- Framework-managed entities, buffers, or performance-sensitive data may need mutation. Preserve their invariants instead of forcing a disruptive immutable redesign.

## Resource lifetime

- Define who releases files, streams, connections, transactions, subscriptions, and other resources. Use the target language's established lifetime mechanisms, such as scoped cleanup, context managers, RAII, or deferred cleanup, when appropriate. Garbage collection alone does not guarantee timely release of external resources.
- Do not close or dispose of a borrowed shared client, scheduler, or worker pool whose lifecycle belongs to the caller or framework.
- For asynchronous work, keep owned resources alive until dependent work finishes. Handle cleanup on success, failure, timeout, and cancellation.
- Follow the runtime's interruption and cancellation semantics. Do not swallow cancellation signals or convert them into ordinary success. Preserve or propagate the signal as the language and project require.
- Do not hide a primary failure behind a cleanup error. Preserve meaningful cause information.

## Side effects, errors, and absence

- Separate calculations from I/O when it simplifies the flow. Do not add layers solely to make every function pure.
- Make database writes, network calls, argument mutation, and publication of events visible through names, API contracts, and control flow.
- Keep transaction boundaries and the order of effects explicit. A remote effect is not rolled back by a local database transaction.
- Preserve the distinction between a valid empty result, missing data, and an operation that failed.
- Do not turn a failure into an empty collection, a missing value, a default value, or success unless the contract defines that behavior.
- Represent absence with the project's established mechanism, such as nullable values, option types, or explicit result variants. Do not introduce a new convention or force one representation into every field and parameter.
- Catch errors where the code can recover or translate them meaningfully. Avoid broad catches that hide programming failures.

## Distributed-system decisions

### Retry

Before adding or changing retries, identify:

- Whether the operation is idempotent and how that property is enforced. For side effects, identify any deduplication key, storage, scope, and lifetime needed by the contract.
- Which failures are retryable, including ambiguous outcomes where the remote operation may already have succeeded.
- The maximum number of total attempts, including the first attempt. State that meaning explicitly.
- The timeout for each attempt, the total deadline, and how cancellation stops further attempts.
- The backoff policy and whether jitter is needed to avoid synchronized load. Use existing retry infrastructure when available.
- Existing retries in clients, gateways, consumers, and callers. Avoid multiplying attempts across layers.

Do not assume that a timeout means no remote effect occurred. Do not add retries for an unsafe side effect merely because an error is transient. A local transaction or an in-memory flag does not establish distributed idempotency.

If required retry semantics cannot be determined from code or requirements, preserve existing behavior and raise the concrete missing decision before adding a retry policy. Do not invent attempt counts or deadlines as hidden defaults.

### Authorization

An authorization failure must not trigger an elevated identity, alternate unprotected endpoint, skipped check, or implicit anonymous access. Preserve denial according to the contract. Credential refresh may be used only through an existing authorized flow that preserves identity and access scope.

### Fallback, cache, and defaults

Derive these behaviors from requirements or an established contract. Do not silently add them to make a failing operation appear successful.

For a cache, define scope, keys, validity or invalidation, and required freshness. Include tenant and authorization boundaries where relevant. Cached data must not bypass required access checks.

For a fallback or default, identify the triggering condition, the changed meaning or quality of the result, and how callers can distinguish it when the contract requires that distinction. Do not equate unavailable data with an empty result.

### Concurrency

For a concurrency change, describe the shared state, its owner, the threads or tasks that access it, and the mechanism that protects the invariant.

- Prefer confinement or immutable snapshots when they meet the need.
- Use locks, atomic operations, concurrent collections, or message passing according to the actual invariant and runtime memory model. Do not infer compound-operation atomicity from visibility guarantees or a keyword's name.
- A concurrent collection does not make arbitrary multi-step or cross-object operations safe. Account for check-then-act races. A single-threaded event loop can also interleave tasks at suspension points.
- Check ordering, transaction context, asynchronous captures, and resource lifetime. Use managed execution and bounded work where appropriate to the contract.
- A local lock protects one process. It does not coordinate state across replicas. Identify the actual coordination boundary when correctness depends on it.
- Do not equate async functions, promises, futures, coroutines, lightweight threads, or parallel collection operations with safe access to shared state.

Read [references/decision-examples.md](references/decision-examples.md) when a concrete example helps clarify these decisions.

## Verify the changed behavior

Use the repository's relevant build checks and focused tests. Verify meaningful invariants rather than private implementation details. Depending on the change, check mutation aliases, error propagation, authorization denial, duplicate effects, timeout budgets, or concurrency races.

For retry and concurrency tests, prefer controlled clocks, synchronization, and deterministic failure injection over arbitrary sleeps. Do not invent a new test framework when the repository already supports the needed checks.

For a refactor, verify behavior that must remain the same. For a larger design, make these state and effect decisions part of `brainstorm-design` when that skill is available. A small task does not require that skill.

Explain material choices briefly in Polish or English, following the user's request. Use a diagram for complicated ownership, shared state, or effects when it helps. State what was checked and what remains unverified. Formatting and style enforcement stay with project tools.
