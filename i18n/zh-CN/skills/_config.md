---
description: 所有 Skills 共享的全局配置文件。Claude 在执行任何 Skill 之前必须先读取本文件。
---

# 🔧 全局配置 (所有 Skill 共享)

## 根目录
所有 Skill 中的相对路径（如 `01-Clients/...`）均基于以下根目录解析：
```
ROOT: ./Obsidian-Vault
```

## 系统标准目录树 (全局向导)
当需要在系统中创建新文件或目录时，**必须严格遵守以下目录架构**：
```
ROOT/
├── 00-RawData/       # [前端/原始] 各类脱敏前的原始音视频、问卷数据
├── 01-Clients/       # [个案管理] 按儿童代号拆分，存储核心档案、评估、FBA、IEP、转衔
├── 02-Sessions/      # [日常记录] 按儿童代号拆分，存储课后记录、行为 ABC 日志
├── 03-Staff/         # [师资管理] 教师成长档案、听课反馈、实操单、组织架构、胜任力评估
├── 04-Supervision/   # [公共基建] 督导复盘、灵感库、系统变更日志、督导会简报
├── 05-Communication/ # [对外沟通] 面向家长的阶段报告、周报家书、战前简报
├── 06-Templates/     # [模板库] 督导要求一线人员填写的各类空白表单模板
├── 07-Curriculum/    # [课程开发] 团体课/社交课/专注力/学习困难等课程大纲、教案、评估
└── 08-Knowledge/     # [知识库] 原子化核心概念文档、参考教材、循证数据库
    ├── _知识库索引.md   # 全库 MOC
    ├── 教材/           # 教科书章节摘录、核心理论
    ├── 概念库/         # 原子化概念卡片（一个概念一个文件）
    ├── 教案库/         # 经过实践验证的历史教案
    └── 会议纪要/       # 督导会、家长会、团队培训的总结文档
```
任何未被定义在此目录树中的顶级文件夹都视为违规建立。

## Obsidian CLI 全局优先声明
所有 Skill 对 Vault 的操作**必须优先使用 obsidian-cli 命令**，而非 Claude Code 内置的 Read/Write/Glob/Grep 工具。obsidian-cli 保持与 Obsidian 的索引、缓存、插件联动一致性。

### 操作映射表
| 操作类型 | obsidian-cli 命令 | 说明 |
|:---|:---|:---|
| **读取文件** | `obsidian read file="文件名"` | wikilink 式解析，无需完整路径 |
| **按路径读取** | `obsidian read path="01-Clients/Client-[代号]/Client-[代号] - 核心档案.md"` | 精确路径 |
| **新建文件** | `obsidian create name="文件名" content="..." silent` | silent 阻止自动打开 |
| **覆盖文件** | `obsidian create name="文件名" content="..." overwrite silent` | 需配合 diff 预览 |
| **追加内容** | `obsidian append file="文件名" content="..."` | 追加到文件末尾 |
| **前置内容** | `obsidian prepend file="文件名" content="..."` | 插入到文件开头 |
| **搜索内容** | `obsidian search query="关键词" path="08-Knowledge" limit=10` | 替代 Glob/Grep |
| **带上下文搜索** | `obsidian search:context query="关键词" path="08-Knowledge"` | 返回匹配行上下文 |
| **读取属性** | `obsidian property:read name="status" file="文件名"` | 精准读 frontmatter |
| **设置属性** | `obsidian property:set name="status" value="执行中" file="文件名"` | 精准改 frontmatter |
| **查看反向链接** | `obsidian backlinks file="文件名"` | 验证谁引用了该文件 |
| **查看出链** | `obsidian links file="文件名"` | 验证该文件引用了谁 |
| **检测断链** | `obsidian unresolved` | 列出所有未解析的 `[[]]` 链接 |
| **列出目录文件** | `obsidian files folder="01-Clients/Client-[代号]"` | 替代 ls/Glob |
| **列出子文件夹** | `obsidian folders folder="01-Clients"` | 替代 ls 目录 |
| **查看文件信息** | `obsidian file file="文件名"` | 文件元数据 |
| **列出标签** | `obsidian tags file="文件名"` | 查看文件标签 |
| **搜索标签** | `obsidian tags sort=count counts` | 全库标签统计 |

### 回退规则
仅在以下情况可回退使用 Claude Code 内置工具：
1. Obsidian 未运行（obsidian-cli 不可用）
2. 需要操作 Vault 外的文件（如 `skills/references/` 下的参考文件）
3. 需要精确行号定位的 Edit 操作（obsidian-cli 无行级编辑能力，此时用 Claude Code Edit 工具）

### 章节级编辑的混合策略
obsidian-cli 不支持行级替换，因此**章节级 Edit 操作**采用混合策略：
1. 用 `obsidian read file="文件名"` 读取全文
2. 在 Claude 内存中定位章节锚点并计算新内容
3. 用 Claude Code 的 `Edit` 工具执行精确替换（old_string → new_string）
4. 用 `obsidian property:set` 更新 frontmatter 字段（如 `last_updated`）

## 知识库检索规范 (Skills 通用)
多个 Skill 在执行时会先检索 `08-Knowledge/` 获取循证依据。统一遵循以下规则：
1. **检索方式**：用 `obsidian search query="[关键词]" path="08-Knowledge/概念库" limit=10` 按关键词搜索，或用 `obsidian search query="domain: 行为管理" path="08-Knowledge"` 按 frontmatter 字段搜索。需要匹配行上下文时用 `obsidian search:context`
2. **引用标注**：在输出中用 `> [!tip] 循证依据：[[概念卡片名]]` callout 标注引用来源
3. **无结果容错**：如知识库中无匹配内容，跳过检索步骤，不影响后续执行，不报错
4. **索引入口**：`obsidian read file="_知识库索引"` 为全库 MOC，可作为快速定位起点

## 文件命名规范 (全系统强制)
所有个案相关文件，**文件名中连字符前后必须加空格**，与 Obsidian 双链保持一致：
```
✅ 正确：Client-[代号] - 能力评估.md
❌ 错误：Client-[代号]-能力评估.md

✅ 正确：Client-[代号] - FBA 分析.md
❌ 错误：Client-[代号]-FBA分析.md
```

### 标准文件名对照表
| 文件类型 | 标准文件名格式 |
|:---|:---|
| 核心档案 | `Client-[代号] - 核心档案.md` |
| 初访信息表 | `Client-[代号] - 初访信息表.md` |
| 能力评估 | `Client-[代号] - 能力评估.md` |
| FBA 分析 | `Client-[代号] - FBA 分析.md` |
| IEP 方案 | `Client-[代号] - IEP.md` |
| 强化物评估 | `Client-[代号] - 强化物评估.md` |
| 里程碑报告 | `Client-[代号] - 里程碑报告.md` |
| 沟通记录 | `Client-[代号] - 沟通记录.md` |
| 学期总结 | `Client-[代号] - 学期总结 -YYYY 上/下.md` |
| 日志库文件夹 | `Client-[代号] - 日志库/` |
| 沟通记录文件夹 | `Client-[代号] - 沟通记录/` |
| 教师文件夹 | `教师 - [姓名]/` |
| 教师成长档案 | `督导 - [姓名] - 成长档案.md`（放在 `03-Staff/教师 - [姓名]/` 内） |
| 实操单 | `实操单 - Client-[代号] - [姓名].md` |
| 课题变更追踪 | `Client-[代号] - 课题变更追踪.md` |
| 课题变更单 | `Client-[代号] - 课题变更单-YYYY-MM-DD.md` |
| 胜任力评估 | `[姓名] - 胜任力评估 - YYYY-MM.md` |
| 组织架构总表 | `03-Staff/_组织架构.md` |
| 晋升路线参考 | `skills/references/competency_matrix.md` |
| 课程大纲 | `07-Curriculum/[课型]/[课型] - 课程大纲 - YYYY[季].md` |
| 课程教案 | `07-Curriculum/[课型]/[课型] - 第XX课教案.md` |
| 课程评估报告 | `07-Curriculum/[课型]/[课型] - 课程评估报告.md` |
| 团体课过程记录 | `07-Curriculum/[课型]/记录/[课型] - 第XX课记录 - YYYY-MM-DD.md` |
| 督导会简报 | `04-Supervision/督导会简报 - YYYY-MM-DD.md` |
| 每日速览 | `04-Supervision/每日速览 - YYYY-MM-DD.md` |
| 个案研讨材料 | `05-Communication/个案研讨/研讨 - Client-[代号] - YYYY-MM-DD.md` |

### Wikilink 双链命名
文件名中的空格和连字符都保留原样写入 `[[ ]]`：
```
[[Client-[代号] - 核心档案]]
[[Client-[代号] - IEP]]
[[Client-[代号] - FBA 分析]]
```

### 路径模糊匹配规则
由于历史文件可能存在命名不一致（有的带空格有的不带），Claude 在 Read 步骤遇到文件不存在时，**必须先用 `obsidian search query="Client-[代号] 能力评估" limit=5` 搜索匹配**，找到实际文件再用 `obsidian read` 读取，而不是直接报错。

## 占位符解析规则
- **`[代号]`**：完整格式为 `A-昵称`，用于路径时为 `Client-A-昵称`
  - 如用户只说"昵称"，先列出 `{{ROOT}}/01-Clients/` 下所有目录，匹配含该昵称的目录
  - 如有多个匹配，列出候选请用户确认
- **`[教师姓名]`**：用于路径时为 `教师 - [姓名]`，如 `教师 - 张老师`
  - 如用户只说"张老师"，先列出 `{{ROOT}}/03-Staff/` 下所有目录，匹配含该姓名的目录
- **解析失败时**：列出已有目录，请用户确认。绝不猜测。

## 日期格式规范
- **`{{当前日期}}`** → `YYYY-MM-DD` 格式，如 `2026-03-06`
- **`{{当前日期时间}}`** → `YYYY-MM-DD HH:mm` 格式，如 `2026-03-06 19:00`
- **文件名中的日期** → 一律使用 `YYYY-MM-DD`
- **正文/家书中** → 可用更友好的格式：`YYYY年M月D日`
- 注意：`{{date}}` 和 `{{日期}}` 均等价于 `{{当前日期}}`

## Frontmatter 元数据标准 (全文件类型强制)
所有 Skill 生成或编辑的 `.md` 文件，**必须包含 YAML frontmatter**。Obsidian CLI 和 Claude Code 依赖 frontmatter 进行结构化检索（如 `obsidian-cli search --property status:活跃`）。

### 核心档案 frontmatter
```yaml
---
type: 核心档案
status: 🟢 激活 - 干预进行中   # 🟢 激活 - 干预进行中 | 🟡 新个案 - 基线评估期 | 🟠 方案执行中 | 🔴 暂停 | ⚪ 结业 | 🔵 转衔
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: [个案]
aliases: [昵称, Client-代号]    # 如 [小星, Client-Demo]
linked_staff: [教师姓名]        # 当前负责的老师列表
supervisor: 督导姓名             # 负责的分督导/总督导
---
```
- `status` 字段由 `milestone-report` 和 `transfer-protocol` 更新
- `last_updated` 字段由任何编辑该文件的 Skill 自动更新为 `{{当前日期}}`
- `linked_staff` 字段由 `org-manager` 维护

### 教师成长档案 frontmatter
```yaml
---
type: 教师档案
level: L1              # L1-实习 | L2-初级 | L3-中级 | L4-高级 | L5-分督导 | L6-总督导
status: 在职            # 在职 | 试用期 | 离职
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: [教师]
aliases: [姓名]
supervisor: 上级督导姓名
caseload: [Client-代号1, Client-代号2]
---
```
- `level` 字段由 `staff-evaluation` 晋升通过后更新
- `caseload` 字段由 `org-manager` 维护

### IEP 方案 frontmatter
```yaml
---
type: IEP
status: 执行中          # 草案 | 执行中 | 已归档
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
client: Client-代号
tags: [IEP]
---
```

### 课题变更单 frontmatter
```yaml
---
type: 课题变更单
client: Client-代号
date: YYYY-MM-DD
teacher: 执行老师姓名
supervisor: 督导姓名
status: 待执行          # 待执行 | 执行中 | 已完成
created: YYYY-MM-DD
tags: [课题变更]
---
```
- `status` 字段由 `curriculum-updater` 创建时设为"待执行"，后续可手动更新

### 其他文件类型 frontmatter（最小集）
```yaml
---
type: [文件类型]        # 初访信息表 | 能力评估 | FBA分析 | 强化物评估 | 里程碑报告 | 沟通记录 | 学期总结 | 课程大纲 | 教案 | 督导会简报 | 每日速览 | 胜任力评估
created: YYYY-MM-DD
client: Client-代号     # 个案相关文件必填，公共文件省略
tags: []
---
```

### Frontmatter 更新规则
1. **新建文件**：Skill 必须生成完整 frontmatter
2. **编辑文件**：Skill 必须更新 `last_updated` 为 `{{当前日期}}`
3. **查询场景**：用 `obsidian search query="status: 活跃" path="01-Clients"` 批量定位文件，或用 `obsidian property:read name="status" file="文件名"` 精确查询单个文件

## 预览确认标准流程
当 Skill 安全协议要求"预览确认"时，Claude 必须遵循以下流程：
1. 用 `> [!NOTE] 📋 变更预览` callout 包裹预览内容
2. 如果是 **Edit 操作**（替换已有章节），用并排对比格式：
   - `**原内容：**` + 原文
   - `**拟替换为：**` + 新文
3. 如果是 **Write 操作**（新建文件），直接展示全文
4. 如果预览内容超过 50 行，先给出摘要（核心变更点），询问是否查看完整内容
5. 预览后必须明确询问：**"以上变更是否确认执行？(确认/修改/取消)"**
6. 只有收到明确肯定回复（如"确认"、"好"、"y"、"执行"）后才执行写入

## 文件不存在时的处理策略
当 Skill 的 Read 步骤中需要读取的文件不存在或为空占位文件时：
1. **不要报错终止**：基于已有数据继续执行 Skill
2. **标记为"待完善"**：在输出中用 `⏳ [待XX完成后补充]` 占位，绝不编造数据
3. **执行完成后提醒**：汇报中注明"建议先执行 [缺失的skill名] 来补全数据"

**⚠️ 特殊情况：公共基建文件的 Append 容错**
当向 `04-Supervision/系统变更日志.md` 或 `04-Supervision/督导灵感与SOP迭代库.md` 追加内容时，**如果该文件不存在，Claude 必须主动进行无中生有（Create）**：
1. 建立具有对应 `# 标题` 的 Markdown 框架。
2. 再执行追加写入。
**绝对不允许因为“找不到变更日志文件”而中断 Skill 执行。**

## 核心档案标准章节结构
以下为核心档案的完整章节结构。`intake-interview` 建骨架、`profile-builder` 填血肉时，必须包含所有章节（内容可留 `[待补充]`）：

```markdown
# [[Client-代号 - 核心档案]]
### 📊 基线数据汇总              ← profile-builder 填写
### 👤 基本背景与病历摘要          ← intake-interview 初建，profile-builder 深化
### 🧸 强化物偏好清单              ← reinforcer-tracker 更新
### 🧩 核心能力画像               ← assessment-logger 更新
### 🚨 历史问题行为备忘            ← fba-analyzer 更新
### 📋 当前干预目标索引            ← plan-generator 更新
### 🔗 全生命周期索引              ← 多个 Skill 追加链接
```

### 章节锚点 (用于 Edit 定位)
Edit 操作时通过这些关键词定位。匹配时**忽略 emoji 和首尾空格**，仅匹配中文关键词：

| 章节关键词 | 被哪个 Skill 编辑 |
|:---|:---|
| "基线数据汇总" | `profile-builder` |
| "核心能力画像" | `assessment-logger` |
| "强化物偏好清单" | `reinforcer-tracker` |
| "历史问题行为备忘" 或 "问题行为预警" | `fba-analyzer` |
| "当前干预目标索引" | `plan-generator` |
| "全生命周期索引" | 多个 Skill 追加链接 |
| "累计掌握项目" | `curriculum-updater`（课题变更追踪表格） |
| "当前执行课题" | `curriculum-updater`（核心档案教学项目清单） |
| frontmatter `status` 字段 | `milestone-report`, `transfer-protocol` |

## Append 操作精确位置
- **核心档案 (`核心档案.md`)**：追加到 `### 🔗 全生命周期索引` 章节**之前**（所有 Skill 统一遵守此规则，包括 `session-reviewer` 和 `parent-update` 的沟通记录追加）
- **教师成长档案 (`督导 - * - 成长档案.md`)**：追加到文件**最末尾**
- **变更日志 (`系统变更日志.md`)**：追加到文件**最末尾**
- **课题变更追踪 (`课题变更追踪.md`)**：累计掌握项目表追加**新行到表尾**，变更历史追加**新日期段落到章节末**
- **IEP (`IEP.md`)**：追加到对应目标章节**末尾**
- **灵感库 (`督导灵感与SOP迭代库.md`)**：追加到文件**最末尾**

## 双链完整性维护
每个 Skill 在执行完成后，可选执行以下双链健康检查：
1. `obsidian unresolved` — 检测是否有新产生的断链（`[[]]` 指向不存在的文件），应为 0
2. `obsidian backlinks file="Client-[代号] - 核心档案"` — 验证核心档案的反向链接完整
3. `obsidian links file="Client-[代号] - 核心档案"` — 验证核心档案的出链指向正确文件

### IEP 版本双链注意事项
IEP 文件带日期后缀（如 `Client-[代号] - IEP-2026-03-18`），在核心档案的 `### 🔗 全生命周期索引` 中**必须使用完整文件名**（含日期），不要用无日期的 `[[Client-代号 - IEP]]`。多版本 IEP 应全部保留在索引中：
```markdown
- [x] **个别化方案 v2**：[[Client-[代号] - IEP-2026-03-18]]
- [x] **个别化方案 v1**：[[Client-[代号] - IEP-2026-01-15]]
```

## 执行完成汇报格式
每个 Skill 执行完毕后，Claude 必须用以下格式向用户汇报：

```
✅ **[Skill名称] 执行完成**
📄 本次操作的文件：
- ✏️ 新建：[文件路径]
- 📝 编辑：[文件路径] > [章节名]
- ➕ 追加：[文件路径]
📋 变更日志已更新

🔗 建议下一步：[下游 Skill 建议]
```
