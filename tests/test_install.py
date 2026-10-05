import contextlib
import io
from pathlib import Path
import tempfile
import unittest

import install as installer


SOURCE = Path(__file__).resolve().parents[1]


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.home = Path(self.temporary.name)

    def run_install(self):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(SOURCE, self.home)

    def test_existing_instructions_survive_and_are_backed_up(self):
        for tool, filename in ((".codex", "AGENTS.md"), (".claude", "CLAUDE.md")):
            path = self.home / tool / filename
            path.parent.mkdir()
            path.write_text("# Existing rules\n\nKeep my workflow.\n")
        self.run_install()
        for tool, filename in ((".codex", "AGENTS.md"), (".claude", "CLAUDE.md")):
            path = self.home / tool / filename
            original = "# Existing rules\n\nKeep my workflow.\n"
            self.assertTrue(path.read_text().startswith(original))
            backup = path.with_name(filename + ".before-dbudzki-code-skills")
            self.assertEqual(backup.read_text(), original)
        for name in installer.SKILLS:
            for tool in (".codex", ".claude"):
                installed = self.home / tool / "skills" / name
                self.assertEqual((installed / "SKILL.md").read_bytes(), (SOURCE / "skills" / name / "SKILL.md").read_bytes())
                self.assertEqual((installed / "LICENSE").read_bytes(), (SOURCE / "LICENSE").read_bytes())
            discovery = self.home / ".agents" / "skills" / name
            self.assertEqual(discovery.resolve(), (self.home / ".codex" / "skills" / name).resolve())

    def test_repeat_installation_is_identical(self):
        self.run_install()
        before = {str(p.relative_to(self.home)): p.read_bytes() for p in self.home.rglob("*") if p.is_file()}
        self.run_install()
        after = {str(p.relative_to(self.home)): p.read_bytes() for p in self.home.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_conflicting_skill_stops_before_other_changes(self):
        path = self.home / ".claude" / "skills" / "mindful-code" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("Local custom skill")
        with self.assertRaisesRegex(ValueError, "Conflicting installed skill"):
            self.run_install()
        self.assertEqual(path.read_text(), "Local custom skill")
        self.assertFalse((self.home / ".codex").exists())

    def test_override_stops_before_installing(self):
        path = self.home / ".codex" / "AGENTS.override.md"
        path.parent.mkdir()
        path.write_text("Use different global instructions.")
        with self.assertRaisesRegex(ValueError, "takes precedence"):
            self.run_install()
        self.assertFalse((self.home / ".claude").exists())

    def test_incomplete_managed_section_stops_before_installing(self):
        path = self.home / ".claude" / "CLAUDE.md"
        path.parent.mkdir()
        path.write_text("Existing instructions\n" + installer.START)
        with self.assertRaisesRegex(ValueError, "incomplete or duplicated"):
            self.run_install()
        self.assertFalse((self.home / ".codex").exists())


if __name__ == "__main__":
    unittest.main()
