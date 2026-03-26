---
description: Skill 调度索引。当用户请求不明确时，Claude 应参考本文件判断应该调用哪个 Skill。
---

# 📋 Skill 调度索引

## 关键词 → Skill 映射表

### 个案临床线
| 用户关键词 | 应触发的 Skill | 说明 |
|:---|:---|:---|
| 原始资料、脱敏、真实姓名、隐私 | `privacy-filter` | 处理含真实姓名的原始数据 |
| 初访、新个案、建档、新来的孩子 | `intake-interview` | 新个案的首次处理 |
| 核心档案、完善档案、Master File | `profile-builder` | 深化核心档案内容 |
| 评估、VB-MAPP、ABLLS、得分 | `assessment-logger` | 录入专业评估结果 |
| 行为分析、ABC、功能分析、FBA、问题行为原因 | `fba-analyzer` | 分析问题行为功能 |
| 强化物、偏好、饱和、奖励没用了 | `reinforcer-tracker` | 更新强化物偏好清单 |
| 方案、IEP、BIP、目标制定、计划 | `plan-generator` | 制定干预方案 |
| 拆解、切片、教学步骤、PT、DI、怎么教 | `program-slicer` | 将目标拆解为教学切片 |
| 课题升级、达标、掌握了、换课题、下一个目标、课题变更、通过了 | `curriculum-updater` | 课题达标确认+下一课题决策+变更单 |
| 课后卡、课后记录、老师填的表 | `session-reviewer` | 处理老师的课后记录 |
| 听课、观察老师、督导反馈、看了老师上课 | `staff-supervision` | 处理督导听课观察 |
| 实操单、实操小抄、准备下节课 | `teacher-guide` | 生成老师实操指引 |
| 家书、家长反馈、家长沟通、微光信 | `parent-update` | 生成家长周反馈 |
| 里程碑、阶段报告、结业、喜报 | `milestone-report` | 生成阶段性报告 |
| 简报、开会前、家长会、速览 | `quick-summary` | 生成战前电梯简报 |
| 复盘、周总结、本周回顾 | `clinical-reflection` | 每周临床复盘 |
| 转衔、移交、换老师、换机构 | `transfer-protocol` | 生成移交协议 |

### 组织管理线
| 用户关键词 | 应触发的 Skill | 说明 |
|:---|:---|:---|
| 新老师、新员工、入职、师资建档 | `staff-onboarding` | 新老师入职，初始化教师档案及目录 |
| 组织架构、人员分配、caseload、谁管谁 | `org-manager` | 维护三级组织架构和人员-个案分配 |
| 考核、晋升、胜任力、能不能升、KPI | `staff-evaluation` | 教师晋升路线管理和胜任力评估 |
| 督导会、周会、信息同步、团队简报 | `supervisor-sync` | 生成跨团队督导会简报和信息级联包 |
| 每日总结、今天怎么样、下班前看一眼 | `daily-digest` | 生成每日运营速览 |
| 个案研讨、case conference、讨论会 | `case-conference` | 生成个案研讨会全套材料包 |

### 课程开发线
| 用户关键词 | 应触发的 Skill | 说明 |
|:---|:---|:---|
| 课程设计、课程大纲、团体课、社交课、专注力课、学习困难 | `curriculum-builder` | 设计结构化课程大纲 |
| 教案、写教案、备课、某一课怎么上 | `lesson-planner` | 生成单节课详细教案 |
| 团体课记录、课程追踪、课程评估、前后测 | `group-tracker` | 团体课过程追踪和结局评估 |

## ⚠️ 易混淆场景澄清

### "实操单"相关 — 三个 Skill 都能生成
| 场景 | 正确 Skill | 判断依据 |
|:---|:---|:---|
| 督导说"帮我给张老师准备下节课的实操单" | `teacher-guide` | 无新输入，纯基于已有 IEP 生成 |
| 督导说"我刚看完张老师上课，帮我整理反馈和实操单" | `staff-supervision` | 有新的督导观察随笔作为输入 |
| 督导说"帮我把 IEP 的目标3拆解成教学步骤" | `program-slicer` | 有新的 IEP 目标需要拆解 |

### "处理老师提交的内容" vs "督导自己观察"
| 输入来源 | 正确 Skill |
|:---|:---|
| **老师**填的《课后记录与求助卡》 | `session-reviewer` |
| **督导**自己的听课随笔/观察记录 | `staff-supervision` |

### "看孩子情况" — 三个 Skill 可能相关
| 场景 | 正确 Skill |
|:---|:---|
| 开会前快速了解全貌（只读不写） | `quick-summary` |
| 老师刚交课后记录，需要分析+反馈 | `session-reviewer` |
| 要开正式研讨会，需要全套讨论材料 | `case-conference` |

### "给家长发消息"
| 场景 | 正确 Skill |
|:---|:---|
| 常规周反馈家书 | `parent-update` |
| 达到里程碑/结业的喜报 | `milestone-report` |

### "课题达标" — 三个 Skill 易混淆
| 场景 | 正确 Skill | 判断依据 |
|:---|:---|:---|
| 老师交了课后记录，需要分析数据 | `session-reviewer` | 输入是课后记录卡，重点是反馈而非课题决策 |
| 数据显示课题达标，需要决定下一个教什么 | `curriculum-updater` | 重点是"达标确认+替换决策+生成变更单" |
| 新课题已确定，需要拆解教学步骤 | `program-slicer` | 重点是"怎么教"而非"教什么" |

### "课程" vs "个案教学"
| 场景 | 正确 Skill |
|:---|:---|
| 设计一套8周的社交团体课程 | `curriculum-builder` |
| 在已有课程内写某一节课的教案 | `lesson-planner` |
| 为某个孩子的 IEP 目标拆解教学步骤 | `program-slicer` |
| 记录团体课上各学员的表现 | `group-tracker` |

### "老师考核" vs "老师日常督导"
| 场景 | 正确 Skill |
|:---|:---|
| 观察老师上课后给反馈 | `staff-supervision` |
| 季度/年度正式胜任力考核 | `staff-evaluation` |
| 查看老师能不能晋升 | `staff-evaluation` |
| 给新老师建档 | `staff-onboarding` |

## 🔗 标准工作流链路

```
=== 组织管理线 ===
A. org-manager (架构维护/人员分配/caseload)
       ↓
B. staff-onboarding (新师入职建档)
       ↓
C. staff-evaluation (定期考核/晋升评估)
       ↓
D. supervisor-sync (督导会信息级联)

=== 个案临床主线 ===
1. privacy-filter (脱敏原始资料)
       ↓
2. intake-interview (建档+目录初始化)
       ↓
3. profile-builder (深化核心档案)
       ↓
4. assessment-logger (录入评估) + fba-analyzer (行为分析)
       ↓
5. plan-generator (制定 IEP/BIP)
       ↓
6. program-slicer (拆解教学切片) → teacher-guide (生成实操单)
       ↓
   ┌──────────── 日常循环 ────────────┐
   │  session-reviewer (课后记录)          │
   │      ↕                               │
   │  staff-supervision (听课反馈)         │
   │      ↓                               │
   │  curriculum-updater (课题达标→升级)   │
   │      ↓                               │
   │  program-slicer (新课题拆解)          │
   │      ↓                               │
   │  teacher-guide (更新实操单)           │
   └───────────────────────────────────────┘
       ↓
7. parent-update (每周家书)
8. reinforcer-tracker (每双周强化物评估)
9. clinical-reflection (每周复盘)
       ↓
10. milestone-report (阶段报告/结业)
       ↓
11. transfer-protocol (转衔移交)

=== 课程开发线 ===
I.  curriculum-builder (课程大纲设计)
       ↓
II. lesson-planner (单课教案生成)
       ↓
III. group-tracker (过程追踪+结局评估)

=== 效率工具线 ===
• daily-digest (每日速览)
• case-conference (个案研讨材料包)
• supervisor-sync (督导会简报)
```
