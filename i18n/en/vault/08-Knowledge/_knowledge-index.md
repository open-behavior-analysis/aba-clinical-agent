---
type: MOC
created: 2026-03-15
last_updated: 2026-03-15
tags: [MOC, 知识库, 索引]
aliases: [知识库索引, Knowledge Base]
---

# 知识库索引 (Knowledge Base MOC)

> [!NOTE]
> 本文件是 `08-Knowledge/` 的全局索引。Skills 在执行时通过此索引或 frontmatter 标签检索相关知识。
> 新增文档后请在对应分类下追加wikilink。

---

## 按领域分类

### 行为原理 (Behavioral Principles)
> domain: 行为原理

⏳ 待导入概念卡片，如：[[reinforcement]]、[[消退]]、[[惩罚]]、[[Motivating Operation (MO)]]、[[刺激控制]]

### 教学技术 (Teaching Procedures)
> domain: 教学技术

⏳ 待导入概念卡片，如：[[DTT 回合式教学]]、[[NET 自然环境教学]]、[[prompt hierarchy]]、[[纠错程序]]

### 评估工具 (Assessment Tools)
> domain: 评估工具

⏳ 待导入，如：[[VB-MAPP]]、[[ABLLS-R]]、[[PEAK]]

### 行为管理 (Behavior Management)
> domain: 行为管理

⏳ 待导入概念卡片，如：[[functional analysis]]、[[competing behavior model]]、[[功能性沟通训练]]、[[区别reinforcement]]

### 沟通策略 (Communication)
> domain: 沟通策略

⏳ 待导入，如：[[家长沟通技巧]]、[[BST 培训框架]]

---

## lesson-plans (Proven Lesson Plans)

### 语言行为
⏳ 待导入历史教案

### 社交技能
⏳ 待导入历史教案

### 自理 / 生活技能
⏳ 待导入历史教案

### 学业 / 认知
⏳ 待导入历史教案

---

## 教材 (Textbooks & References)

⏳ 待导入教材章节摘录

---

## meeting-notes (Meeting Notes)

⏳ 待导入会议总结文档

---

## 知识库使用指南

### 文件命名规范
- 概念卡片：`概念名称.md`（如 `reinforcement.md`、`DTT 回合式教学.md`）
- 教案参考：`[教学目标] - [描述].md`（如 `提要求训练 - 经典教案.md`）
- 教材摘录：`[书名] - [章节].md`（如 `Cooper行为分析 - 第9章reinforcement.md`）
- meeting-notes：`YYYY-MM-DD - [主题].md`（如 `2026-03-10 - 团队培训会.md`）

### Frontmatter 标准
概念卡片：
```yaml
---
type: 概念卡片
domain: [行为原理]           # 行为原理 | 教学技术 | 评估工具 | 行为管理 | 沟通策略
tags: [reinforcement, 正reinforcement, ABA基础]
related: [[消退]], [[prompt hierarchy]]
difficulty: L2               # L1-L5 对应胜任力等级
---
```

教案参考：
```yaml
---
type: 教案参考
target_skill: [提要求, mand]
age_range: 3-6
teaching_format: [DTT, NET]
proven: true
---
```

教材摘录：
```yaml
---
type: 教材
source: 书名/作者
chapter: 章节号
domain: [行为原理]
---
```

meeting-notes：
```yaml
---
type: meeting-notes
date: YYYY-MM-DD
participants: [姓名列表]
topics: [主题标签]
---
```
