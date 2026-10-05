---
name: explain-diagram
description: Explain code, architecture, data flow, call order, or states with a focused diagram and short Polish or English prose. Use proactively for interacting components or branching behavior, and when the user requests a diagram.
---

# Explain with a diagram

Adapted from Ashrya Agrawal's `karpathy-output-style`. A diagram should make the answer easier to see.

## Plan the explanation

1. Identify the reader's main question. Inspect relevant code before drawing actual behavior.
2. Use the requested language, or the language of the latest request. Support Polish and English. Keep labels short and sentences direct.
3. Use one canonical name for each object or concept in the diagram and prose. Preserve exact code identifiers. Define a necessary translated term once.
4. Choose the smallest useful representation:
   - Flowchart for components, data flow, or decisions.
   - Sequence diagram for calls, messages, asynchronous work, or order.
   - State diagram for states and transitions.
   - Table for a simple comparison or mapping.
5. Keep one question per diagram. Aim for 3–7 main nodes. Split a large system into an overview and focused details.

## Render with available tools

Use Mermaid for a compact diagram that the host can render. Use Excalidraw when an editable drawing or spatial layout helps. Use SVG when a standalone rendered diagram fits better. A local image can help when the subject needs spatial detail.

If an Excalidraw MCP tool is available, read its current instructions and follow its schema. With the upstream Excalidraw server, the workflow is `read_me`, then `create_view`. Do not assume those tools exist on every Claude or Codex host.

If Excalidraw MCP is unavailable, use Mermaid or local SVG. Create native `.excalidraw` JSON only when you can check its schema. If the host cannot render Mermaid, provide a readable text diagram or a local rendered artifact.

## Preserve the mechanism

- Give each shape one idea. Use explicit arrow directions and labels such as "calls", "reads", or "writes" and their Polish equivalents.
- Distinguish call order, data flow, and ownership. Label decisions, feedback loops, and important error paths.
- Preserve uncertainty and concurrency. Do not draw a sequential guarantee for concurrent code.
- Label assumptions, fictional examples, and omitted steps when they affect interpretation.
- Use color only when it has meaning. Also use text or line styles so color is not the only signal.

## Inspect and deliver

Read the result as a newcomer. When rendering is available, check text size, overlap, arrow endpoints, and whether the main path is obvious. Correct the rendered result. State any rendering check you could not perform.

Return the diagram with a brief explanation of how to read it. Cite the useful source files separately when labels would become crowded. Avoid repeating each arrow in prose.

Save editable or rendered files in the workspace's designated output directory when useful. Link or preview the artifact. Do not claim that a file or share link exists until you have it. Use existing access rules for remote services; a local diagram is the default when no remote service is authorized.
