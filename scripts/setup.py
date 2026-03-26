#!/usr/bin/env python3
"""
ABA Clinical Agent - Language Setup Script

Sets up the working environment by copying the selected language's
skills, vault template, and documentation into their active locations.

Usage:
    python scripts/setup.py --lang zh-CN    # Chinese (default)
    python scripts/setup.py --lang en        # English
"""

import argparse
import shutil
import sys
from pathlib import Path

SUPPORTED_LANGUAGES = {"zh-CN", "en"}
DEFAULT_LANGUAGE = "zh-CN"

LANGUAGE_LABELS = {
    "zh-CN": "Chinese (简体中文)",
    "en": "English",
}


def get_project_root() -> Path:
    """Return the project root directory (parent of scripts/)."""
    return Path(__file__).resolve().parent.parent


def copy_tree(src: Path, dst: Path) -> None:
    """Copy directory tree, removing destination first if it exists."""
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def setup_skills(root: Path, lang: str) -> None:
    """Copy language-specific skills + shared skill-creator into .claude/skills/."""
    src_skills = root / "i18n" / lang / "skills"
    dst_skills = root / ".claude" / "skills"
    shared_creator = root / "shared" / "skill-creator"

    if not src_skills.exists():
        print(f"  [ERROR] Skills not found: {src_skills}")
        sys.exit(1)

    copy_tree(src_skills, dst_skills)
    print(f"  [OK] Skills ({lang}) -> .claude/skills/")

    if shared_creator.exists():
        dst_creator = dst_skills / "skill-creator"
        if dst_creator.exists():
            shutil.rmtree(dst_creator)
        shutil.copytree(shared_creator, dst_creator)
        print(f"  [OK] skill-creator (shared) -> .claude/skills/skill-creator/")


def setup_vault(root: Path, lang: str) -> None:
    """Copy language-specific vault template into Obsidian-Vault/ (only if not exists)."""
    src_vault = root / "i18n" / lang / "vault"
    dst_vault = root / "Obsidian-Vault"

    if not src_vault.exists():
        print(f"  [SKIP] Vault template not found: {src_vault}")
        return

    if dst_vault.exists() and any(dst_vault.iterdir()):
        print(f"  [SKIP] Obsidian-Vault/ already exists (won't overwrite user data)")
        print(f"         To reset, delete Obsidian-Vault/ and run setup again.")
        return

    copy_tree(src_vault, dst_vault)
    print(f"  [OK] Vault template ({lang}) -> Obsidian-Vault/")


def setup_claude_md(root: Path, lang: str) -> None:
    """Copy language-specific CLAUDE.md to project root."""
    src = root / "i18n" / lang / "CLAUDE.md"
    dst = root / "CLAUDE.md"

    if not src.exists():
        print(f"  [SKIP] CLAUDE.md not found: {src}")
        return

    shutil.copy2(src, dst)
    print(f"  [OK] CLAUDE.md ({lang}) -> ./CLAUDE.md")


def setup_docs(root: Path, lang: str) -> None:
    """Copy language-specific docs into docs/."""
    src_docs = root / "i18n" / lang / "docs"
    dst_docs = root / "docs"

    if not src_docs.exists():
        print(f"  [SKIP] Docs not found: {src_docs}")
        return

    copy_tree(src_docs, dst_docs)
    print(f"  [OK] Docs ({lang}) -> docs/")


def main():
    parser = argparse.ArgumentParser(
        description="Set up ABA Clinical Agent for a specific language.",
        epilog="Example: python scripts/setup.py --lang en",
    )
    parser.add_argument(
        "--lang",
        choices=sorted(SUPPORTED_LANGUAGES),
        default=DEFAULT_LANGUAGE,
        help=f"Language to set up (default: {DEFAULT_LANGUAGE})",
    )
    parser.add_argument(
        "--force-vault",
        action="store_true",
        help="Overwrite existing Obsidian-Vault/ with demo data",
    )
    args = parser.parse_args()

    root = get_project_root()
    lang = args.lang
    label = LANGUAGE_LABELS.get(lang, lang)

    print(f"\n{'='*50}")
    print(f"  ABA Clinical Agent - Language Setup")
    print(f"  Language: {label}")
    print(f"{'='*50}\n")

    # Ensure .claude directory exists
    (root / ".claude").mkdir(exist_ok=True)

    setup_skills(root, lang)
    setup_claude_md(root, lang)
    setup_docs(root, lang)

    if args.force_vault:
        # Remove existing vault to force overwrite
        dst_vault = root / "Obsidian-Vault"
        if dst_vault.exists():
            shutil.rmtree(dst_vault)

    setup_vault(root, lang)

    print(f"\n{'='*50}")
    print(f"  Setup complete!")
    print(f"  Run `claude` to start using the system.")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
