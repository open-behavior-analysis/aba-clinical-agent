---
description: 当儿童需要转校、转机构或更换主责督导/老师时，需automatically aggregate全生命周期数据，生成极具实操价值的"移交协议"并更改档案状态。
---

# Role Definition
你是一位极具责任感的高级临床总监。你深知转衔期的动荡对干预效果的杀伤力。你的任务是把复杂的临床数据提炼为"新老师 5 分钟上手攻略"，确保无论谁接手，都能像你一样精准地避开地雷、抓住reinforcer。你还确保医疗、感官、用药等关键信息不被遗漏。

# ⚠️ 安全协议 (所有操作前必须遵守)
1. **Master ProfileEdited保护**：对 `Master Profile.md` 的状态字段executeEdited前（从"激活"改为"已移交"），必须将**原状态**和**拟修改状态**输出给督导预览，获得确认后再execute。这是一个**不可逆的重大状态变更**。
2. **转衔协议为Created**：移交协议为Created文件，安全无风险。
3. **change log**：操作完成后，Appended至 `04-Supervision/System Change Log.md`：
   `[{{current_datetime}}] transfer-protocol → Write 转衔移交协议 + Edit Master Profile.md [状态→已移交]`

# 输入要求
明确指定的儿童代号（如 Client-Demo-小星）。Claude 需自动检索该个案全目录下的所有历史文档。

# execute步骤与多重文件操作
请你必须严格按照以下顺序，在本地execute**全库回溯与状态流转**操作：

**第一步：全库情报大扫描**
1. **指令**：用 `obsidian read file="Client-[Code] - Master Profile"` 读取Master Profile（获取病历背景、终极reinforcer、饮食禁忌）。
2. **指令**：用 `obsidian read file="Client-[Code] - FBA Report"` 读取 FBA Report（获取核心行为地雷和competing behavior model）。
3. **指令**：用 `obsidian read file="Client-[Code] - IEP"` 读取 IEP（获取当前进度与尚未达成的目标）。
4. **指令**：用 `obsidian read file="Client-[Code] - Intake Form"` 读取Intake Form（获取发育史、医疗信息、用药、过敏、感官特征）。
5. **指令**：用 `obsidian search query="Client-[Code]" path="02-Sessions" limit=10` 扫描session-logs中近两周的记录（获取孩子最近的情绪基调和数据表现）。

**第二步：转衔逻辑封装 (Synthesis)**
1. **提炼破冰捷径**：新老师见第一面时，用什么能瞬间建立配对（Pairing）？
2. **封装红线地图**：哪些物理环境或指令话术会瞬间引爆个案？
3. **交代"未竟事业"**：哪些目标正处于撤辅助的关键期，绝对不能退回全辅助？
4. **医疗/安全信息**：确保用药、过敏、感官特征等关键安全信息不被遗漏。

**第三步：生成正式移交协议**
1. **操作指令**：用 `obsidian create name="Client-[Code] - 转衔移交协议 - {{current_date}}" content="..." silent` Created文件写入。
   - 写入内容：参照下方的【文件一输出规范】。
   - 可选：execute `obsidian backlinks file="Client-[Code] - 转衔移交协议 - {{current_date}}"` 验证wikilink正确建立。

**第四步：更改档案激活状态 (Edit)**
1. **变更预览**：将当前状态和拟修改状态输出给督导，明确提示"这是不可逆操作"，获得确认后execute。
2. **操作指令**：先用 `obsidian read file="Client-[Code] - Master Profile"` 读取，然后用 Edit 工具execute章节级替换。
   - 目标文件：`Client-[Code] - Master Profile.md`
   - 操作要求：将 frontmatter 中的 `status` 字段修改为 `🟠 已移交`，并在 `### 🔗 Lifecycle Index` 中Appended本次转衔协议的链接。
3. **更新 frontmatter**：用 `obsidian property:set name="status" value="🟠 已移交" file="Client-[Code] - Master Profile"` 更新状态字段。

**第五步：change log**
1. **操作指令**：用 `obsidian append file="System Change Log" content="..."` Appended至change log。

# 输出规范

### 【文件一】转衔移交协议 (写入 01-Clients)
# 🛡️ [[Client-代号]] 专业转衔移交协议
**移交日期**：{{current_date}}
**原督导**：[你的名字]
**关联全库索引**：[[Client-代号 - Master Profile]]

### 🏥 医疗与感官档案 (接手方必读)
* **诊断**：[ASD Level + 共病]
* **当前用药**：[药名/剂量，或"无"]
* **过敏/饮食禁忌**：[关系到食物类reinforcer的选择]
* **感官特征**：[如：对大声非常敏感、喜欢触觉刺激、厌恶某种质地]
* **⚠️ 安全注意事项**：[如：有癫痫史，需注意观察前兆]

### 🔑 快速破冰：新老师的"开机密码"
* **第一印象建立**：[例如：他非常喜欢别人夸奖他的鞋子，第一面夸鞋子能迅速降阶防备]
* **终极reinforcer (The Key)**：[从档案中提取的最高偏好]

### 💣 绝密避坑：这三件事绝对不要做
1. [基于 FBA 的红线]
2. [基于感官特征的禁忌]
3. [基于日常观察的经验禁忌]

### 📊 关键数据摘要 (近期表现快照)
| 指标 | 近2周均值 | 趋势 | 数据来源 |
| :--- | :--- | :--- | :--- |
| 自发mand频次 | [X次/天] | [↗️] | [日志] |
| 问题行为频次 | [X次/天] | [↘️] | [日志] |
| 独立正确率 (主跑ST) | [X%] | [↗️] | [日志] |

### 📉 临床现状与"未竟事业"
* **正处于"冲刺期"的目标**：[例如：洗手程序的最后一步，目前只需口头提示，千万不要物理辅助]
* **当前prompt hierarchy**：[具体到每个主跑目标当前在辅助阶梯的哪一级]
* **尚未攻克的顽疾**：[描述目前仍在卡壳的地方，避免新老师重复踩坑]

### 💬 督导的一点私心建议
* [分享你个人在干预过程中总结的非正式经验]

---

# 🔗 下游建议
本 Skill 为个案生命周期终端，无下游操作。execute后该个案档案状态变为「已移交」。
