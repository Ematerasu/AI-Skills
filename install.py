#!/usr/bin/env python3
"""Install the package without replacing unrelated local instructions or skills."""

import argparse
import os
from pathlib import Path
import shutil


SKILLS = (
    "clear-writing",
    "explain-diagram",
    "explain-webpage",
    "brainstorm-design",
    "mindful-code",
)
START = "<!-- ematerasu-code-skills:start -->"
END = "<!-- ematerasu-code-skills:end -->"


def skill_files(source):
    return {
        str(path.relative_to(source)): path.read_bytes()
        for path in source.rglob("*")
        if path.is_file()
    }


def merged_instructions(current, preferences):
    section = START + "\n" + preferences.rstrip() + "\n" + END
    if START not in current and END not in current:
        separator = "" if current.endswith("\n\n") else "\n" if current.endswith("\n") else "\n\n"
        return current + (separator if current else "") + section + "\n"
    if current.count(START) != 1 or current.count(END) != 1:
        raise ValueError("Instruction markers are incomplete or duplicated.")
    start = current.index(START)
    end = current.index(END)
    if end < start:
        raise ValueError("Instruction markers are out of order.")
    return current[:start] + section + current[end + len(END):]


def install(source, home):
    override = home / ".codex" / "AGENTS.override.md"
    if override.exists() and override.read_text().strip():
        raise ValueError("Codex AGENTS.override.md takes precedence. Resolve it before installation.")
    if override.is_symlink():
        raise ValueError("Review the symlinked Codex AGENTS.override.md before installation.")

    license_bytes = (source / "LICENSE").read_bytes()
    copies = []
    links = []
    instructions = []

    for name in SKILLS:
        origin = source / "skills" / name
        if not (origin / "SKILL.md").is_file():
            raise ValueError("Missing source skill: " + str(origin))
        expected = skill_files(origin)
        expected["LICENSE"] = license_bytes
        for tool in (".codex", ".claude"):
            destination = home / tool / "skills" / name
            if destination.is_symlink():
                raise ValueError("Review existing skill symlink: " + str(destination))
            if destination.exists():
                if not destination.is_dir() or skill_files(destination) != expected:
                    raise ValueError("Conflicting installed skill: " + str(destination))
            else:
                copies.append((destination, expected))
        link = home / ".agents" / "skills" / name
        target = home / ".codex" / "skills" / name
        if link.exists() or link.is_symlink():
            if not link.is_symlink() or link.resolve() != target.resolve():
                raise ValueError("Conflicting Codex discovery entry: " + str(link))
        else:
            links.append((link, target))

    for tool, filename in ((".codex", "AGENTS.md"), (".claude", "CLAUDE.md")):
        path = home / tool / filename
        backup = path.with_name(path.name + ".before-ematerasu-code-skills")
        if path.is_symlink() or backup.is_symlink():
            raise ValueError("Review existing instruction or backup symlink: " + str(path))
        current = path.read_text() if path.exists() else ""
        merged = merged_instructions(current, (source / filename).read_text())
        if merged != current:
            instructions.append((path, backup, current, merged, path.exists()))

    for destination, files in copies:
        destination.mkdir(parents=True)
        for relative, content in files.items():
            path = destination / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)

    for link, target in links:
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(target, target_is_directory=True)

    for path, backup, current, merged, existed in instructions:
        path.parent.mkdir(parents=True, exist_ok=True)
        if existed and not backup.exists():
            shutil.copy2(path, backup)
        path.write_text(merged)

    print("Installed five skills for Claude Code and Codex in " + str(home))
    print("Standing instructions merged. Start new sessions to verify discovery.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, help="Use an isolated home directory.")
    args = parser.parse_args()
    home = (args.home or Path.home()).expanduser().resolve()
    configured_home = os.environ.get("CODEX_HOME")
    if args.home is None and configured_home:
        if Path(configured_home).expanduser().resolve() != home / ".codex":
            parser.error("Custom CODEX_HOME detected. Adapt install locations before continuing.")
    try:
        install(Path(__file__).resolve().parent, home)
    except (OSError, ValueError) as error:
        parser.exit(1, "Installation stopped: " + str(error) + "\n")


if __name__ == "__main__":
    main()
