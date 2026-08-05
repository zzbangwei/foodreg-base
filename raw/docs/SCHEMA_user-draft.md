# 食规智库 FoodReg Base — Wiki 规则配置

> **版本**: v1.1
> **范围**: 中国食品法规标准（GB 体系）
> **最后更新**: 2026-06-25

---

## 1. 目录结构

```
食规智库FoodReg Base/
├── raw/                    ← 原始资料（只读不可修改）
│   ├── gb-xxx.md           ← GB 标准原文/摘要
│   ├── notice-xxx.md       ← 卫健委/市监局公告
│   ├── paper-xxx.md        ← 学术论文/研究报告
│   ├── article-xxx.md      ← 行业文章/解读
│   └── notes-xxx.md        ← 会议纪要/笔记
├── wiki/                   ← LLM 编译维护的知识层
│   ├── index.md            ← 内容总目录
│   ├── log.md              ← 变更时间线
│   ├── entities/           ← 实体页
│   │   ├── standard-xxx.md ← 标准/法规实体（GB 2760, GB 2761...）
│   │   ├── org-xxx.md      ← 组织/机构（卫健委, CFSA, 市监局...）
│   │   └── substance-xxx.md← 物质（苯甲酸, 山梨酸, 铅...）
│   ├── concepts/           ← 概念页
│   │   ├── concept-xxx.md  ← 理论/概念（ADI, HACCP, MRL...）
│   │   └── method-xxx.md   ← 检测方法（GB 5009系列, GB 4789系列）
│   └── topics/             ← 主题综述页
│       ├── topic-xxx.md    ← 主题综述
│       └── comparison-xxx.md← 对比分析页（跨标准/新旧版本/跨类别）
└── SCHEMA.md               ← 本配置文件
```

## 2. 命名规范

| 前缀 | 适用类型 | 示例 |
|------|---------|------|
| `standard-` | GB 标准实体页 | `standard-gb-2760` |
| `org-` | 组织机构 | `org-nhc`（卫健委）、`org-cfsa`（风险评估中心） |
| `substance-` | 物质 | `substance-benzoic-acid` |
| `concept-` | 概念 | `concept-adi` |
| `method-` | 检测方法 | `method-gb-5009-28` |
| `topic-` | 主题综述 | `topic-preservatives` |
| `comparison-` | 对比分析 | `comparison-gb2760-vs-gb14880` |

规则：
- 全部使用 **kebab-case**（小写 + 连字符）
- 英文命名优先，中文可做别名
- raw/ 中：GB 标准文件用 `gb-{编号}-{年份}.md`，公告用 `notice-{部门}-{年份}-{编号}.md`
- 对比页命名规范：`comparison-{主题1}-vs-{主题2}`

## 3. 元数据规范（YAML Frontmatter）

每个 Wiki 页面必须在开头包含以下 frontmatter：

```yaml
---
title: "{中文标题}"
type: entity | concept | method | topic | comparison
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/gb-xxx.md, raw/notice-xxx.md]
tags: [标签1, 标签2]
standard_type: 基础标准 | 产品标准 | 检验方法 | 生产规范 | 标签标识 | 特殊食品 | 公告
food_category: [乳及乳制品, 饮料类]
substance_type: [防腐剂, 污染物]
status: current | draft | outdated | needs-review
replaces: {被替代的标准号}
replaced_by: {替代本标准的版本}
---
```

### 标准实体页额外字段

```yaml
standard_id: "GB 2760-2024"
issuing_body: 国家卫生健康委员会
effective_date: 2025-02-08
replaces: "GB 2760-2014"
```

### 物质页额外字段

```yaml
cas: "65-85-0"
einecs: "200-618-2"
synonyms: [苯甲酸钠, E210]
```

## 4. 领域分类体系

### 4.1 标准类型（standard_type 字段）

| 代码 | 含义 | 典型标准 |
|------|------|----------|
| `基础标准` | 通用限量/要求 | GB 2760, GB 2761, GB 2762, GB 2763, GB 14880, GB 29921 |
| `产品标准` | 具体食品产品 | GB 19644（乳粉）, GB 10765（婴儿配方）, GB 7101（饮料） |
| `检验方法` | 检测方法标准 | GB 5009 系列（理化）, GB 4789 系列（微生物） |
| `生产规范` | GMP/HACCP | GB 14881, GB 12693 |
| `标签标识` | 标签与声称 | GB 7718, GB 28050, GB 13432 |
| `包装材料` | 食品接触材料 | GB 4806 系列, GB 9685 |
| `特殊食品` | 保健食品/特膳 | GB 16740, GB 24154 |
| `公告` | 部门公告/通知 | 新食品原料、添加剂增补等 |
| `通则` | 术语/分类/导则 | GB/T 15091, GB/T 23586 |

### 4.2 食品类别（food_category 字段）

采用 GB 2760-2024 附录 E 食品分类系统，一级分类：

```yaml
01.0: 乳及乳制品
02.0: 脂肪、油和乳化脂肪制品
03.0: 冷冻饮品
04.0: 水果、蔬菜、豆类、食用菌、藻类等
05.0: 可可制品、巧克力和巧克力制品及糖果
06.0: 粮食和粮食制品
07.0: 焙烤食品
08.0: 肉及肉制品
09.0: 水产及其制品
10.0: 蛋及蛋制品
11.0: 甜味料
12.0: 调味品
13.0: 特殊膳食用食品
14.0: 饮料类
15.0: 酒类
16.0: 其他类
```

> 子类（如 01.01 巴氏杀菌乳）按 GB 2760 附录 E 完整编号引用。

### 4.3 物质类型（substance_type 字段）

```yaml
食品添加剂类:
  - 防腐剂
  - 着色剂
  - 甜味剂
  - 乳化剂
  - 增稠剂
  - 抗氧化剂
  - 酸度调节剂
  - 膨松剂
  - 抗结剂
  - 消泡剂
  - 面粉处理剂
  - 被膜剂
  - 水分保持剂
  - 稳定剂和凝固剂
  - 食品用香料

限量物:
  - 农药残留
  - 兽药残留
  - 真菌毒素
  - 污染物
  - 重金属
  - 致病菌

其他:
  - 营养强化剂
  - 新食品原料
  - 加工助剂
  - 酶制剂
```

### 4.4 标签（tags 字段，自由维度）

```yaml
建议标签:
  - 中国食品安全国家标准
  - GB体系
  - 最大使用量
  - 最大残留限量
  - 不得检出
  - 婴幼儿食品
  - 出口合规
  - 高风险物质
```

## 5. 页面模板

### 5.1 标准/法规实体页

```markdown
---
title: "{标准名称}"
type: entity
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/gb-xxx.md]
tags: [标签1, 标签2]
standard_type: 基础标准
food_category: [乳及乳制品]
substance_type: [防腐剂, 着色剂]
status: current
standard_id: "GB XXXX-YYYY"
issuing_body: 国家卫生健康委员会
effective_date: YYYY-MM-DD
replaces: "GB XXXX-20YY"
replaced_by: null
---

# {标准名称}

## 基本信息
| 项目 | 内容 |
|------|------|
| 标准号 | GB XXXX-YYYY |
| 发布机构 | 国家卫生健康委员会 / 国家市场监督管理总局 |
| 实施日期 | YYYY-MM-DD |
| 替代标准 | GB XXXX-20YY |
| 标准类型 | {standard_type} |

## 版本历史
| 版本 | 实施日期 | 状态 |
|------|----------|------|
| GB XXXX-YYYY | YYYY-MM-DD | ✅ 现行 |
| GB XXXX-20YY | 20YY-MM-DD | 🔔 已废止 |

## 核心内容摘要
{关键条款和数据}

## 关联标准
- 引用: [[standard-xxx]]
- 被引用: [[standard-yyy]]

## 管控物质
- [[substance-xxx]] — 限量值/使用条件

## 引用来源
- [1] [[raw/gb-xxx.md]] — 标准摘要/全文

## 变更记录
- YYYY-MM-DD: 初始创建
```

### 5.2 物质页（核心查询入口）

```markdown
---
title: "{物质名称}（英文名）"
type: entity
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/gb-xxx.md]
tags: [标签1]
substance_type: 防腐剂
food_category: [乳及乳制品, 饮料类]
cas: "{CAS号}"
status: current
---

# {物质名称}

## 基本信息
| 项目 | 内容 |
|------|------|
| 中文名 | XX |
| 英文名 | XX |
| CAS | XX |
| 物质类型 | {substance_type} |
| 功能 | 防腐 / 着色 / 甜味... |

## 在各标准中的出现
- [[standard-gb-2760]] — 限量：{限量值}
- [[standard-gb-5009-xx]] — 检测方法：{方法名称}
- [[standard-gb-7718]] — 标签标注要求

## 产品应用速查表
| 食品类别 | 最大使用量 | 备注 |
|----------|-----------|------|
| 风味发酵乳(01.02.02) | 0.03 g/kg | 以苯甲酸计 |
| ... | ... | ... |

## 版本变更记录
- GB 2760-2024 vs 2014：{变更说明}

## 关联页面
- 相关物质: [[substance-xxx]]
- 参见: [[comparison-xxx]]

## 引用来源
- [1] [[raw/gb-2760.md]]
- [2] [[raw/gb-5009-28.md]]

## 变更记录
- YYYY-MM-DD: 初始创建
```

### 5.3 概念页

```markdown
---
title: "{概念名称}"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/xxx.md]
tags: [标签]
---

# {概念名称}

## 定义

## 在 GB 体系中的位置

## 相关标准
- [[standard-xxx]]
- [[standard-yyy]]

## 引用来源

## 变更记录
```

### 5.4 对比分析页

```markdown
---
title: "{对比主题}"
type: comparison
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/xxx.md, raw/yyy.md]
tags: [对比, 版本对比 | 跨标准对比]
---

# {对比主题}

> 对比类型：版本对比 | 跨标准对比 | 跨类别对比

## 对比表

| 维度 | A | B |
|------|---|---|
|      |   |   |

## 关键差异分析

## 关联页面
- [[standard-xxx]]
- [[standard-yyy]]

## 引用来源

## 变更记录
```

## 6. 交叉引用规则

- 所有页面间引用使用 `[[相对路径]]`，如 `[[entities/standard-gb-2760]]`
- `index.md` 中的引用不带路径前缀
- 创建新页面时，自动更新所有引用它的页面
- 每个 `substance-` 页必须包含"在各标准中的出现"区块，列出所有相关标准
- 相关标准 ≥3 个的 `substance-` 页应包含速查表
- 被引用 ≥3 次的概念/实体，若缺少独立页面，标记为"缺失引用"待补充

## 7. 操作流程

### 7.1 Ingest（灌入资料）
1. 用户将资料放入 `raw/` 目录
2. LLM 读取资料，提取关键信息（标准号、条款、限量值、物质列表）
3. 创建/更新对应的 Wiki 页面（standard- / substance- / concept-）
4. 更新 substance- 页的速查表
5. 建立交叉引用
6. 标注矛盾（如同一物质在不同标准中限量冲突）
7. 更新 `wiki/index.md` 和 `wiki/log.md`

### 7.2 Query（查询）
1. 读取 `wiki/index.md` 定位相关页面
2. 优先读 substance- 页（物质枢纽）
3. 必要时读 standard- 页获取原文细节
4. 综合回答
5. 有价值的回答归档为新的 Wiki 页面（特别是 comparison- 页）

### 7.3 Lint（健康巡检）
- 矛盾检查：同一物质在不同 GB 标准中的限量值是否冲突
- 时效性检查：标准是否已被替代/废止（`status: outdated`）
- 孤立页面检查：无入链的页面
- 缺失引用检查：被多次提及但无独立页面的概念
- 物质页完整性：substance- 页是否含速查表和标准关联
- 版本链完整性：replaces/replaced_by 字段是否双向闭合

## 8. 质量标记

| 标记 | 含义 | 使用场景 |
|------|------|----------|
| `⚠️ 矛盾标注` | 不同来源矛盾 | 如 GB 2760 与 GB 14880 对同一物质限量不一致 |
| `🔔 已废止` | 标准已被替代 | GB 新版本发布，旧版标记为 outdated |
| `📌 待验证` | 需人工确认 | AI 推理内容或非官方来源 |
| `🔄 草稿` | 页面未完成 | 信息不完整 |
| `✅ 已验证` | 经人工核对 | 关键数据已对照原文确认 |

---

> 💡 此 SCHEMA 是"活文档"，随着知识库的增长持续演进。当发现新的管理需求时，更新本文件并向用户说明变更。
