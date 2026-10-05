# Ematerasu-code-skills

Five skills and standing instructions for Claude Code, Codex, and Cursor. They support clear Polish and English explanations, visual design, and pragmatic code quality across languages.

| Skill | Purpose |
| --- | --- |
| [clear-writing](skills/clear-writing/SKILL.md) | Simple technical language, stable names, and practical ASD-STE100-inspired writing. |
| [explain-diagram](skills/explain-diagram/SKILL.md) | Focused architecture, data-flow, sequence, and state diagrams. |
| [explain-webpage](skills/explain-webpage/SKILL.md) | Interactive HTML and useful animations. |
| [brainstorm-design](skills/brainstorm-design/SKILL.md) | Reviewable designs for larger implementations and refactors. |
| [mindful-code](skills/mindful-code/SKILL.md) | Deliberate abstractions, ownership, mutation, resource lifetime, and distributed-system behavior. |

The [standing instructions](AGENTS.md) route tasks to the skills. [CLAUDE.md](CLAUDE.md) contains the same preferences. See the [Polish overview](docs/overview.pl.md) for examples and design choices.

## Install locally

Python 3.9 or later is sufficient. From this checkout, run:

```sh
python3 install.py
```

The installer:

- Copies the five skills and their license to `~/.codex/skills` and `~/.claude/skills`.
- Adds discovery symlinks under `~/.agents/skills`, the global skill location documented by current Codex versions.
- Merges a marked section into `~/.codex/AGENTS.md` and `~/.claude/CLAUDE.md`, preserving content outside that section.
- Backs up each existing instruction file before the first change, using a dedicated backup suffix.
- Checks destinations before writing. Conflicting skill files or discovery links stop installation. Identical installations can be run again.

The installer does not change credentials, plugins, or tool settings. If a skill has explicitly been disabled in your tool's configuration, enable it through that tool. If `AGENTS.override.md` exists in your Codex home, the installer stops so its instruction precedence can be resolved deliberately.

This installer uses the default home locations. For an isolated test home:

```sh
python3 install.py --home /path/to/test-home
```

For a custom `CODEX_HOME`, adapt the locations before installation. This package does not silently install into a different Codex profile.

Start a new session in each tool after installation. In Codex, inspect `/skills` or mention a skill with `$mindful-code`. In Claude Code, inspect `/context` for the global instructions and `/skills` if supported by your version, or invoke `/mindful-code`.

Global skills can activate when their descriptions match a task. Standing instructions make the user's preferences explicit; they do not provide compiler-enforced guarantees.

## Cursor

Local Cursor discovers the already-installed skills from `~/.agents/skills/`. Current versions also support the Claude and Codex skill directories. No extra skill copies are needed.

For standing preferences across projects, open **Customize → Rules → User Rules** and merge the contents of [CURSOR.md](CURSOR.md) with your existing rules. The installer does not change Cursor User Rules. A Markdown file in this checkout is a template, not an automatically loaded global rule.

Restart or reload Cursor, then check **Customize → Skills**. You can invoke a skill from Agent chat with `/mindful-code`, for example. Skills can activate when relevant; User Rules supply the persistent preferences.

For project-specific rules, use the project's `AGENTS.md` or `.cursor/rules/*.mdc`. A `~/.cursor/rules` directory is not the documented global User Rules mechanism.

This setup covers local Cursor Agent. Shared local skills are not automatically copied to Cloud Agents or remote sessions. Those environments need their own project installation or an explicitly configured supported sync.

Sources: [Cursor skills](https://cursor.com/docs/skills#skill-directories), [Cursor rules](https://cursor.com/docs/rules).

## Repository use

Keep the source in this checkout. Installed skills are copies, so editing a source file does not update installed copies automatically. The installer stops if a destination differs. Review and update those copies deliberately when publishing a new version.

The repository contains reusable prompts, references, and a local installer. Machine-specific instructions, configuration backups, credentials, and conversation transcripts do not belong here.

Run the installer checks with `python3 -m unittest discover -s tests`. They use temporary homes and do not modify your tool configuration.

## Sources and license

- The three explanation skills adapt [Ashrya Agrawal's karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style), inspired by [Andrej Karpathy's post](https://x.com/karpathy/status/2105819303471976479).
- `brainstorm-design` adapts [Jesse Vincent's Superpowers brainstorming skill](https://github.com/obra/superpowers/tree/main/skills/brainstorming).
- `mindful-code` and the additional preferences were written for this package.

The upstream MIT notices are retained in [LICENSE](LICENSE). The package does not include the tweet image, video production, or the full ASD-STE100 dictionary. Polish is an adaptation of the clarity principles; the package does not claim formal ASD-STE100 compliance.
