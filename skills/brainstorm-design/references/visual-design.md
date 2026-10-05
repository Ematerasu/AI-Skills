# A useful visual design page

Use this reference for larger designs whose alternatives, flows, or migration steps are easier to understand visually.

## Page structure

1. **Goal:** one sentence and observable success criteria.
2. **Current design:** a compact diagram based on inspected code.
3. **Proposed designs:** tabs or side-by-side views using the same canonical names.
4. **Trade-offs:** a short comparison and the recommended choice with its reason.
5. **Flow:** optional manual steps through a request, error path, or state transition.
6. **Migration:** meaningful stages, compatibility boundaries, and the check for each stage.
7. **Open decisions:** only questions that can change the design.

This is a menu, not a mandatory seven-section page. Omit sections that do not help the current task.

## Interaction

- Keep each control tied to a question. A design selector should update both the diagram and the trade-off explanation.
- Highlight affected components when comparing current and proposed designs. Keep unaffected components visible only when they provide context.
- Keep component names stable across variants. For a new component, mark it as proposed. For a rename or split, show the mapping explicitly.
- Give each arrow a meaning. Distinguish calls, data movement, and ownership.
- Use step controls for order-sensitive behavior. Optional animation should explain the same sequence, with pause and restart.
- Honor reduced motion, keyboard access, visible focus, and narrow screens.
- Show a static summary when JavaScript is unavailable.

## Decision record

A selected tab means the user is viewing that option. It does not mean the user approved the design.

Controls may let the user collect local notes or copy a decision summary. Do not imply that those controls message the agent or grant implementation approval. Unless a real, verified integration exists, ask the user to communicate the decision in chat.

Keep the written design note aligned with the page. Mark unanswered decisions and distinguish a recommendation from an accepted decision.

## Boundaries and verification

Use one local self-contained HTML file when practical. Do not publish it or send repository content to a remote service without authorization. Do not add a web server merely to display static HTML if the host can preview it directly.

Label toy data, simulated timing, and proposed flows. Avoid false precision. Cite inspected source files outside crowded diagram labels.

Open the page, switch designs, and exercise available controls. Check that labels, arrows, and the written recommendation agree. Check the underlying mechanism as well as the layout. Disclose checks unavailable in the current environment.
