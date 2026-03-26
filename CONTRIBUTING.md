# Contributing Guide

Thank you for your interest in ABA Clinical Agent! We welcome all forms of contribution.

## Types of Contributions Welcome

| Type | Description |
|:---|:---|
| **New Skills** | Develop new automated clinical skills |
| **Knowledge Base** | VB-MAPP/ABLLS-R concept cards, lesson plan templates, evidence-based literature indices |
| **Reference Dictionaries** | New developmental sequences, assessment tool mappings |
| **Translations** | Skill and documentation translations |
| **Bug Fixes** | Skill logic errors, path reference issues |
| **Documentation** | Tutorials, FAQ, architecture documentation |

## Skill Submission Requirements

New Skills must include:
1. A `SKILL.md` file following the existing frontmatter format
2. Safety protocols (data integrity, change log, preview confirmation)
3. Keyword mapping registered in `_router.md`
4. At least 2 test cases using fictional data

See the [Skill Development Guide](docs/skill-development.md) for details.

## Knowledge Base Contribution Standards

- Concept cards follow the atomic principle (one concept per file)
- Source literature must be cited
- Frontmatter must include `type` and `tags`

## Submission Process

1. Fork this repository
2. Create a feature branch: `feat/skill-xxx` or `docs/xxx`
3. Submit a PR describing changes and clinical rationale
4. Await review (technical + clinical dual review)

## Privacy Red Line

- **Never** include real case data in PRs
- Example data must be entirely fictional
- If you find real data remnants in the repository, immediately submit a [Security Issue](SECURITY.md)

## Development Environment

1. Clone the repository
2. Run `python scripts/setup.py --lang en` (or `--lang zh-CN`)
3. Install Claude Code (or Cursor/Cline)
4. Install Obsidian (recommended)
5. Install Python 3.8+ (if testing data analysis scripts)

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).
