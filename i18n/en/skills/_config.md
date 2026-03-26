---
description: Global configuration file shared by all Skills. Claude must read this file before executing any Skill.
---

# 🔧 Global Configuration (Shared by All Skills)

## Root Directory
All relative paths in Skills (e.g., `01-Clients/...`) are resolved relative to the following root directory:
```
ROOT: ./Obsidian-Vault
```

## Standard Directory Tree (Global Guide)
When creating new files or directories in the system, **the following directory structure must be strictly followed**:
```
ROOT/
├── 00-RawData/       # [Frontend/Raw] Raw audio/video and questionnaire data before de-identification
├── 01-Clients/       # [Case Management] Split by child code, stores master profiles, assessments, FBA, IEP, transitions
├── 02-Sessions/      # [Daily Records] Split by child code, stores post-session notes, behavioral ABC logs
├── 03-Staff/         # [Staff Management] Growth records, observation feedback, teaching guides, org charts, competency evaluations
├── 04-Supervision/   # [Shared Infrastructure] Supervision debriefs, idea bank, system change logs, supervision briefings
├── 05-Communication/ # [External Communication] Parent-facing milestone reports, weekly letters, pre-session briefings
├── 06-Templates/     # [Template Library] Blank form templates required by supervisors for frontline staff
├── 07-Curriculum/    # [Curriculum Development] Group/social/attention/learning difficulty course outlines, lesson plans, assessments
└── 08-Knowledge/     # [Knowledge Base] Atomized core concept documents, reference textbooks, evidence-based database
    ├── _knowledge-index.md   # Full library MOC
    ├── textbooks/             # Textbook chapter excerpts, core theories
    ├── concepts/              # Atomized concept cards (one concept per file)
    ├── lesson-plans/          # Historically validated lesson plans
    └── meeting-notes/         # Summaries from supervision meetings, parent meetings, team trainings
```
Any top-level folder not defined in this directory tree is considered an unauthorized creation.

## Obsidian CLI Global Priority Declaration
All Skills **must prioritize obsidian-cli commands** for Vault operations, rather than Claude Code's built-in Read/Write/Glob/Grep tools. obsidian-cli maintains consistency with Obsidian's index, cache, and plugin integrations.

### Operation Mapping Table
| Operation Type | obsidian-cli Command | Description |
|:---|:---|:---|
| **Read file** | `obsidian read file="filename"` | Wikilink-style resolution, no full path needed |
| **Read by path** | `obsidian read path="01-Clients/Client-[Code]/Client-[Code] - Master Profile.md"` | Exact path |
| **Create file** | `obsidian create name="filename" content="..." silent` | silent prevents auto-opening |
| **Overwrite file** | `obsidian create name="filename" content="..." overwrite silent` | Requires diff preview |
| **Append content** | `obsidian append file="filename" content="..."` | Append to end of file |
| **Prepend content** | `obsidian prepend file="filename" content="..."` | Insert at beginning of file |
| **Search content** | `obsidian search query="keyword" path="08-Knowledge" limit=10` | Replaces Glob/Grep |
| **Search with context** | `obsidian search:context query="keyword" path="08-Knowledge"` | Returns matching line context |
| **Read property** | `obsidian property:read name="status" file="filename"` | Precise frontmatter read |
| **Set property** | `obsidian property:set name="status" value="in-progress" file="filename"` | Precise frontmatter edit |
| **View backlinks** | `obsidian backlinks file="filename"` | Verify who references this file |
| **View outlinks** | `obsidian links file="filename"` | Verify what this file references |
| **Detect broken links** | `obsidian unresolved` | List all unresolved `[[]]` links |
| **List directory files** | `obsidian files folder="01-Clients/Client-[Code]"` | Replaces ls/Glob |
| **List subdirectories** | `obsidian folders folder="01-Clients"` | Replaces ls for directories |
| **View file info** | `obsidian file file="filename"` | File metadata |
| **List tags** | `obsidian tags file="filename"` | View file tags |
| **Search tags** | `obsidian tags sort=count counts` | Full vault tag statistics |

### Fallback Rules
Built-in Claude Code tools may only be used as fallback in the following situations:
1. Obsidian is not running (obsidian-cli unavailable)
2. Need to operate on files outside the Vault (e.g., reference files under `skills/references/`)
3. Need line-level Edit operations with precise line number targeting (obsidian-cli lacks line-level editing; use Claude Code Edit tool)

### Hybrid Strategy for Section-Level Editing
obsidian-cli does not support line-level replacement, so **section-level Edit operations** use a hybrid strategy:
1. Use `obsidian read file="filename"` to read the full text
2. Locate section anchors in Claude's memory and compute new content
3. Use Claude Code's `Edit` tool for precise replacement (old_string → new_string)
4. Use `obsidian property:set` to update frontmatter fields (e.g., `last_updated`)

## Knowledge Base Search Specification (Shared by Skills)
Multiple Skills search `08-Knowledge/` for evidence-based references before execution. Follow these unified rules:
1. **Search method**: Use `obsidian search query="[keyword]" path="08-Knowledge/concepts" limit=10` for keyword search, or `obsidian search query="domain: behavior management" path="08-Knowledge"` for frontmatter field search. Use `obsidian search:context` when matching line context is needed
2. **Citation format**: Mark sources in output with `> [!tip] Evidence basis: [[Concept Card Name]]` callout
3. **No-result tolerance**: If no matches found in the knowledge base, skip the search step without affecting subsequent execution or raising errors
4. **Index entry point**: `obsidian read file="_knowledge-index"` serves as the full library MOC and can be used as a quick navigation starting point

## File Naming Convention (System-Wide Mandatory)
For all case-related files, **hyphens in filenames must be surrounded by spaces**, consistent with Obsidian wikilinks:
```
✅ Correct: Client-[Code] - Skill Assessment.md
❌ Wrong:   Client-[Code]-Skill Assessment.md

✅ Correct: Client-[Code] - FBA Report.md
❌ Wrong:   Client-[Code]-FBA Report.md
```

### Standard Filename Reference Table
| File Type | Standard Filename Format |
|:---|:---|
| Master Profile | `Client-[Code] - Master Profile.md` |
| Intake Form | `Client-[Code] - Intake Form.md` |
| Skill Assessment | `Client-[Code] - Skill Assessment.md` |
| FBA Report | `Client-[Code] - FBA Report.md` |
| IEP Plan | `Client-[Code] - IEP.md` |
| Reinforcer Assessment | `Client-[Code] - Reinforcer Assessment.md` |
| Milestone Report | `Client-[Code] - Milestone Report.md` |
| Communication Log | `Client-[Code] - Communication Log.md` |
| Semester Summary | `Client-[Code] - Semester Summary -YYYY H1/H2.md` |
| Session logs folder | `Client-[Code] - session-logs/` |
| Communication Log folder | `Client-[Code] - Communication Log/` |
| Teacher folder | `Teacher - [Name]/` |
| Growth Record | `Supervision - [Name] - Growth Record.md` (placed in `03-Staff/Teacher - [Name]/`) |
| Teaching Guide | `Teaching Guide - Client-[Code] - [Name].md` |
| Curriculum Change Tracker | `Client-[Code] - Curriculum Change Tracker.md` |
| Curriculum Change Order | `Client-[Code] - Curriculum Change Order-YYYY-MM-DD.md` |
| Competency Evaluation | `[Name] - Competency Evaluation - YYYY-MM.md` |
| Org Chart Master | `03-Staff/_org-chart.md` |
| Promotion Path Reference | `skills/references/competency_matrix.md` |
| Course Outline | `07-Curriculum/[CourseType]/[CourseType] - Course Outline - YYYY[Season].md` |
| Course Lesson Plan | `07-Curriculum/[CourseType]/[CourseType] - Lesson Plan XX.md` |
| Course Evaluation Report | `07-Curriculum/[CourseType]/[CourseType] - Course Evaluation Report.md` |
| Group Session Record | `07-Curriculum/[CourseType]/records/[CourseType] - Session XX Record - YYYY-MM-DD.md` |
| Supervision Briefing | `04-Supervision/Supervision Briefing - YYYY-MM-DD.md` |
| Daily Digest | `04-Supervision/Daily Digest - YYYY-MM-DD.md` |
| Case Conference Materials | `05-Communication/case-conference/Conference - Client-[Code] - YYYY-MM-DD.md` |

### Wikilink Naming
Spaces and hyphens in filenames are preserved as-is inside `[[ ]]`:
```
[[Client-[Code] - Master Profile]]
[[Client-[Code] - IEP]]
[[Client-[Code] - FBA Report]]
```

### Path Fuzzy Matching Rules
Due to historical naming inconsistencies (some with spaces, some without), when Claude encounters a file-not-found during the Read step, **it must first search using `obsidian search query="Client-[Code] Skill Assessment" limit=5`** to find the actual file, then read it with `obsidian read`, rather than reporting an error directly.

## Placeholder Resolution Rules
- **`[Code]`**: Full format is `A-Nickname`, used in paths as `Client-A-Nickname`
  - If the user only says "nickname", first list all directories under `{{ROOT}}/01-Clients/` and match the directory containing that nickname
  - If multiple matches exist, list candidates and ask the user to confirm
- **`[Teacher Name]`**: Used in paths as `Teacher - [Name]`, e.g., `Teacher - Ms. Smith`
  - If the user only says "Ms. Smith", first list all directories under `{{ROOT}}/03-Staff/` and match the directory containing that name
- **On resolution failure**: List existing directories and ask the user to confirm. Never guess.

## Date Format Specification
- **`{{current_date}}`** → `YYYY-MM-DD` format, e.g., `2026-03-06`
- **`{{current_datetime}}`** → `YYYY-MM-DD HH:mm` format, e.g., `2026-03-06 19:00`
- **Dates in filenames** → Always use `YYYY-MM-DD`
- **In body text / parent letters** → May use friendlier formats: `March 6, 2026`
- Note: `{{date}}` and `{{current_date}}` are equivalent

## Frontmatter Metadata Standard (Mandatory for All File Types)
All `.md` files generated or edited by Skills **must include YAML frontmatter**. Obsidian CLI and Claude Code rely on frontmatter for structured search (e.g., `obsidian-cli search --property status:active`).

### Master Profile frontmatter
```yaml
---
type: master-profile
status: 🟢 Active - Intervention in Progress   # 🟢 Active - Intervention in Progress | 🟡 New Case - Baseline Assessment | 🟠 Plan in Execution | 🔴 Paused | ⚪ Graduated | 🔵 Transition
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: [case]
aliases: [Nickname, Client-Code]    # e.g., [Star, Client-Demo]
linked_staff: [Teacher Name]        # Currently assigned teachers
supervisor: Supervisor Name          # Assigned sub-supervisor/lead supervisor
---
```
- `status` field is updated by `milestone-report` and `transfer-protocol`
- `last_updated` field is automatically updated to `{{current_date}}` by any Skill that edits this file
- `linked_staff` field is maintained by `org-manager`

### Growth Record frontmatter
```yaml
---
type: staff-profile
level: L1              # L1-Intern | L2-Junior | L3-Mid | L4-Senior | L5-Sub-Supervisor | L6-Lead Supervisor
status: active          # active | probation | departed
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: [staff]
aliases: [Name]
supervisor: Supervising Supervisor Name
caseload: [Client-Code1, Client-Code2]
---
```
- `level` field is updated after promotion approval by `staff-evaluation`
- `caseload` field is maintained by `org-manager`

### IEP Plan frontmatter
```yaml
---
type: IEP
status: in-progress     # draft | in-progress | archived
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
client: Client-Code
tags: [IEP]
---
```

### Curriculum Change Order frontmatter
```yaml
---
type: curriculum-change-order
client: Client-Code
date: YYYY-MM-DD
teacher: Implementing Teacher Name
supervisor: Supervisor Name
status: pending          # pending | in-progress | completed
created: YYYY-MM-DD
tags: [curriculum-change]
---
```
- `status` field is set to "pending" by `curriculum-updater` at creation; can be manually updated afterward

### Other File Types frontmatter (Minimum Set)
```yaml
---
type: [file-type]        # intake-form | skill-assessment | fba-report | reinforcer-assessment | milestone-report | communication-log | semester-summary | course-outline | lesson-plan | supervision-briefing | daily-digest | competency-evaluation
created: YYYY-MM-DD
client: Client-Code      # Required for case-related files, omitted for shared files
tags: []
---
```

### Frontmatter Update Rules
1. **New file**: Skill must generate complete frontmatter
2. **Edit file**: Skill must update `last_updated` to `{{current_date}}`
3. **Query scenarios**: Use `obsidian search query="status: active" path="01-Clients"` for batch file lookup, or `obsidian property:read name="status" file="filename"` for precise single-file queries

## Preview Confirmation Standard Procedure
When a Skill's safety protocol requires "preview confirmation", Claude must follow this procedure:
1. Wrap preview content in a `> [!NOTE] 📋 Change Preview` callout
2. For **Edit operations** (replacing existing sections), use side-by-side comparison format:
   - `**Original content:**` + original text
   - `**Proposed replacement:**` + new text
3. For **Write operations** (creating new files), display the full text directly
4. If preview content exceeds 50 lines, provide a summary first (key changes), then ask whether to view the full content
5. After preview, must explicitly ask: **"Do you confirm the above changes? (confirm/modify/cancel)"**
6. Only execute the write after receiving a clear affirmative response (e.g., "confirm", "ok", "y", "go ahead")

## File-Not-Found Handling Strategy
When a file that a Skill's Read step needs to access does not exist or is an empty placeholder:
1. **Do not error out and terminate**: Continue executing the Skill based on available data
2. **Mark as "pending"**: Use `⏳ [TBD after XX is completed]` as placeholder in output; never fabricate data
3. **Post-execution reminder**: Note in the report "Recommend running [missing skill name] first to complete the data"

**⚠️ Special Case: Append Tolerance for Shared Infrastructure Files**
When appending content to `04-Supervision/system-change-log.md` or `04-Supervision/supervision-ideas-and-sop-iterations.md`, **if the file does not exist, Claude must proactively create it from scratch**:
1. Establish a Markdown skeleton with the corresponding `# Title`.
2. Then perform the append write.
**It is absolutely forbidden to interrupt Skill execution because "the change log file cannot be found."**

## Master Profile Standard Section Structure
The following is the complete section structure for the Master Profile. When `intake-interview` builds the skeleton and `profile-builder` fills in details, all sections must be included (content may be left as `[TBD]`):

```markdown
# [[Client-Code - Master Profile]]
### 📊 Baseline Data Summary              ← profile-builder fills this
### 👤 Background & Medical History        ← intake-interview creates, profile-builder deepens
### 🧸 Reinforcer Preference List          ← reinforcer-tracker updates
### 🧩 Core Skill Profile                  ← assessment-logger updates
### 🚨 Historical Problem Behavior Memo    ← fba-analyzer updates
### 📋 Current Intervention Target Index   ← plan-generator updates
### 🔗 Full Lifecycle Index                ← multiple Skills append links
```

### Section Anchors (for Edit Targeting)
Edit operations locate sections by these keywords. When matching, **ignore emojis and leading/trailing spaces**; match only the English keywords:

| Section Keyword | Edited by Which Skill |
|:---|:---|
| "Baseline Data Summary" | `profile-builder` |
| "Core Skill Profile" | `assessment-logger` |
| "Reinforcer Preference List" | `reinforcer-tracker` |
| "Historical Problem Behavior Memo" or "Problem Behavior Alert" | `fba-analyzer` |
| "Current Intervention Target Index" | `plan-generator` |
| "Full Lifecycle Index" | Multiple Skills append links |
| "Cumulative Mastered Items" | `curriculum-updater` (Curriculum Change Tracker table) |
| "Current Active Programs" | `curriculum-updater` (Master Profile teaching item list) |
| frontmatter `status` field | `milestone-report`, `transfer-protocol` |

## Append Operation Precise Locations
- **Master Profile (`Master Profile.md`)**: Append **before** the `### 🔗 Full Lifecycle Index` section (all Skills follow this rule uniformly, including `session-reviewer` and `parent-update` communication log appends)
- **Growth Record (`Supervision - * - Growth Record.md`)**: Append to **end of file**
- **Change Log (`system-change-log.md`)**: Append to **end of file**
- **Curriculum Change Tracker (`Curriculum Change Tracker.md`)**: Cumulative mastered items table appends **new row to table end**; change history appends **new date section to section end**
- **IEP (`IEP.md`)**: Append to **end of corresponding target section**
- **Ideas Bank (`supervision-ideas-and-sop-iterations.md`)**: Append to **end of file**

## Wikilink Integrity Maintenance
Each Skill may optionally perform the following wikilink health checks after execution:
1. `obsidian unresolved` — Check for newly created broken links (`[[]]` pointing to non-existent files); should be 0
2. `obsidian backlinks file="Client-[Code] - Master Profile"` — Verify Master Profile backlinks are complete
3. `obsidian links file="Client-[Code] - Master Profile"` — Verify Master Profile outlinks point to correct files

### IEP Version Wikilink Notes
IEP files have date suffixes (e.g., `Client-[Code] - IEP-2026-03-18`). In the Master Profile's `### 🔗 Full Lifecycle Index`, **the full filename (including date) must be used**; do not use the dateless `[[Client-Code - IEP]]`. Multiple IEP versions should all be preserved in the index:
```markdown
- [x] **Individualized Plan v2**: [[Client-[Code] - IEP-2026-03-18]]
- [x] **Individualized Plan v1**: [[Client-[Code] - IEP-2026-01-15]]
```

## Execution Completion Report Format
After each Skill completes execution, Claude must report to the user in the following format:

```
✅ **[Skill Name] Execution Complete**
📄 Files affected:
- ✏️ Created: [file path]
- 📝 Edited: [file path] > [section name]
- ➕ Appended: [file path]
📋 Change log updated

🔗 Suggested next step: [downstream Skill recommendation]
```
