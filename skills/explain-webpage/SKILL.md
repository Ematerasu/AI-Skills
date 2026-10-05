---
name: explain-webpage
description: Explain code or compare proposed designs with focused interactive HTML in Polish or English, including useful animations. Use for step-by-step flows, changing inputs, comparing scenarios, visual brainstorming, and requested HTML explanations.
---

# Explain in HTML

Adapted from Ashrya Agrawal's `karpathy-output-style`. A small interactive page can make a mechanism easier to understand.

## Choose the teaching example

1. Find the reader's main question. Use HTML when changing inputs, revealing steps, comparing scenarios, or animation makes the answer clearer.
2. Inspect relevant code before explaining its behavior. Keep facts, assumptions, unknowns, and illustrative simulations distinct.
3. Use the requested language, or the language of the latest request. Support Polish and English in headings, labels, controls, and explanations. Do not build a language switch unless it helps or is requested.
4. Select one concrete example. Keep the main result visible. Put supporting detail in expandable sections.
5. Keep one canonical name for each object or concept across prose, diagrams, controls, and animations. Preserve exact code identifiers. Define necessary terms once.

For visual brainstorming, distinguish current and proposed designs. Keep names stable across variants and show how the selected option changes dependencies or behavior. A selected tab is a viewing choice, not approval to implement. Link the page to the written design note when one exists.

## Build the page

Create one complete HTML file with embedded CSS and JavaScript unless the user already has an app or needs separate assets. Prefer no external dependencies.

Use readable type, clear hierarchy, short sentences, and a focused visual. Prefer active verbs and explicit actors. Preserve facts, uncertainty, exceptions, and requirement strength when simplifying English or Polish.

Add interaction only where it teaches. Examples: change an input, reveal a step, show an error path, compare two scenarios, or change queue size. Show what changed and why. Avoid decorative controls.

Give controls labels, keyboard access, and visible focus. Support narrow screens. Use color as an extra signal, with labels or symbols as well. Include a static summary so the main explanation remains understandable without interaction.

## HTML animations

Use CSS, SVG, canvas, or JavaScript animations when they explain movement, order, state, or timing. Examples include a request moving between components, a queue being processed, and a state transition.

- Keep steps slow enough to inspect. Provide pause and restart controls for ongoing playback. Offer manual stepping when order matters.
- Respect `prefers-reduced-motion`. Show a static or step-based equivalent when reduced motion is enabled.
- Keep canonical names visible during transitions. Explain the meaning of movement and timing.
- Label illustrative speed, sample data, and simplified behavior. An animation is not a runtime trace unless it uses verified trace data.
- Keep animation optional when the same view can show the result directly.

This skill creates browser-based explanations. Rendering MP4 files, narrated videos, and audio production are outside its scope.

## Verify and deliver

Open the page and exercise its controls. Check a narrow viewport, keyboard operation, and reduced-motion behavior when browser tools are available. Verify the underlying example as well as the appearance. Fix issues and disclose checks you could not perform.

Save the HTML in the workspace's designated output directory. Return a working link or preview and one short instruction for using the page. Do not publish the page unless the user requests publication.
