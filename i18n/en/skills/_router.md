---
description: Skill dispatch index. When a user request is ambiguous, Claude should consult this file to determine which Skill to invoke.
---

# Skill Dispatch Index

## Keyword to Skill Mapping

### Clinical Pipeline
| User Keywords | Skill to Trigger | Description |
|:---|:---|:---|
| raw data, de-identify, real name, privacy | `privacy-filter` | Process raw data containing real names |
| intake, new client, create file, new child | `intake-interview` | First-time processing for a new case |
| master profile, build profile, master file | `profile-builder` | Deepen Master Profile content |
| assessment, VB-MAPP, ABLLS, scores | `assessment-logger` | Log professional assessment results |
| behavior analysis, ABC, functional analysis, FBA, why the behavior | `fba-analyzer` | Analyze problem behavior function |
| reinforcer, preference, satiation, rewards not working | `reinforcer-tracker` | Update reinforcer preference list |
| plan, IEP, BIP, goal setting, treatment plan | `plan-generator` | Develop intervention plans |
| break down, slice, teaching steps, PT, DI, how to teach | `program-slicer` | Break goals into discrete teaching programs |
| mastered, criterion met, next target, change program, passed | `curriculum-updater` | Mastery confirmation + next program decision + change order |
| session notes, post-session record, therapist form | `session-reviewer` | Process therapist post-session records |
| observation, watch therapist, supervision feedback | `staff-supervision` | Process supervisor observation notes |
| teaching guide, cheat sheet, prep next session | `teacher-guide` | Generate one-page teaching reference |
| family letter, parent update, parent feedback | `parent-update` | Generate weekly parent feedback letter |
| milestone, progress report, discharge, celebration | `milestone-report` | Generate milestone progress report |
| quick brief, pre-meeting, parent conference, overview | `quick-summary` | Generate pre-meeting elevator brief |
| reflection, weekly review, week in review | `clinical-reflection` | Weekly clinical reflection |
| transition, handover, change therapist, change agency | `transfer-protocol` | Generate transition protocol |

### Organization Management
| User Keywords | Skill to Trigger | Description |
|:---|:---|:---|
| new therapist, new staff, onboarding, staff setup | `staff-onboarding` | New therapist onboarding and profile init |
| org chart, staff assignment, caseload, who supervises whom | `org-manager` | Maintain 3-tier org structure and case assignments |
| competency, promotion, evaluation, KPI, ready to advance | `staff-evaluation` | Staff promotion pathway and competency assessment |
| team meeting, weekly meeting, info sync, team brief | `supervisor-sync` | Generate supervision meeting brief and info cascade |
| daily summary, how was today, end of day check | `daily-digest` | Generate daily operational dashboard |
| case conference, case discussion, team review | `case-conference` | Generate full case conference materials package |

### Curriculum Development
| User Keywords | Skill to Trigger | Description |
|:---|:---|:---|
| course design, course outline, group session, social skills, attention | `curriculum-builder` | Design structured course outline |
| lesson plan, write lesson plan, session prep | `lesson-planner` | Generate single-session detailed lesson plan |
| group session record, course tracking, course evaluation, pre-post test | `group-tracker` | Group session progress tracking and outcome evaluation |

## Disambiguation Guide

### "Teaching Guide" - Three Skills Can Generate One
| Scenario | Correct Skill | Rationale |
|:---|:---|:---|
| Supervisor says "prepare a teaching guide for next session" | `teacher-guide` | No new input, based on existing IEP |
| Supervisor says "I just observed the session, compile feedback and guide" | `staff-supervision` | New supervisor observation notes as input |
| Supervisor says "break down IEP goal 3 into teaching steps" | `program-slicer` | New IEP goal needs decomposition |

### "Processing Therapist Input" vs "Supervisor Observations"
| Input Source | Correct Skill |
|:---|:---|
| **Therapist**-completed Post-Session Record & Help Request Card | `session-reviewer` |
| **Supervisor** own observation notes from watching a session | `staff-supervision` |

### "Checking on a Child" - Three Skills May Apply
| Scenario | Correct Skill |
|:---|:---|
| Quick overview before a meeting (read-only) | `quick-summary` |
| Therapist submitted session notes, need analysis + feedback | `session-reviewer` |
| Formal case conference, need full discussion materials | `case-conference` |

### "Sending a Message to Parents"
| Scenario | Correct Skill |
|:---|:---|
| Routine weekly feedback letter | `parent-update` |
| Milestone achieved / discharge celebration | `milestone-report` |

### "Program Mastered" - Three Skills Easily Confused
| Scenario | Correct Skill | Rationale |
|:---|:---|:---|
| Therapist submitted session notes, need data analysis | `session-reviewer` | Input is session record, focus is feedback |
| Data shows mastery, need to decide what to teach next | `curriculum-updater` | Focus is mastery confirmation + replacement decision |
| New program confirmed, need teaching step breakdown | `program-slicer` | Focus is "how to teach" not "what to teach" |

### "Course" vs "Individual Teaching"
| Scenario | Correct Skill |
|:---|:---|
| Design an 8-week social skills group course | `curriculum-builder` |
| Write a lesson plan for one session in existing course | `lesson-planner` |
| Break down IEP goals into teaching steps for a child | `program-slicer` |
| Record student performance during a group session | `group-tracker` |

### "Staff Evaluation" vs "Daily Supervision"
| Scenario | Correct Skill |
|:---|:---|
| Observe a therapist session and give feedback | `staff-supervision` |
| Quarterly/annual formal competency evaluation | `staff-evaluation` |
| Check if therapist is ready for promotion | `staff-evaluation` |
| Set up profile for a new therapist | `staff-onboarding` |

## Standard Workflow Chains

```
=== Organization Management ===
A. org-manager (org structure / staff assignment / caseload)
       |
B. staff-onboarding (new therapist onboarding)
       |
C. staff-evaluation (periodic evaluation / promotion)
       |
D. supervisor-sync (meeting info cascade)

=== Clinical Pipeline ===
1. privacy-filter (de-identify raw data)
       |
2. intake-interview (create case + init directories)
       |
3. profile-builder (deepen Master Profile)
       |
4. assessment-logger (log assessments) + fba-analyzer (behavior analysis)
       |
5. plan-generator (develop IEP/BIP)
       |
6. program-slicer (teaching programs) -> teacher-guide (teaching guide)
       |
   +------------ Daily Cycle ----------------+
   |  session-reviewer (session notes)        |
   |      <->                                 |
   |  staff-supervision (observation feedback)|
   |      |                                   |
   |  curriculum-updater (mastery -> upgrade) |
   |      |                                   |
   |  program-slicer (new program breakdown)  |
   |      |                                   |
   |  teacher-guide (update teaching guide)   |
   +-----------------------------------------+
       |
7. parent-update (weekly family letter)
8. reinforcer-tracker (biweekly reinforcer assessment)
9. clinical-reflection (weekly reflection)
       |
10. milestone-report (progress report / discharge)
       |
11. transfer-protocol (transition handover)

=== Curriculum Development ===
I.  curriculum-builder (course outline design)
       |
II. lesson-planner (single lesson plan)
       |
III. group-tracker (progress tracking + outcome evaluation)

=== Efficiency Tools ===
- daily-digest (daily operational dashboard)
- case-conference (case conference materials)
- supervisor-sync (supervision meeting brief)
```
