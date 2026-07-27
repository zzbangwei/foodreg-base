# FoodReg Base — Schema 规范

> **版本**: v2.2 | **最后更新**: 2026-07-27
> **范围**: 中国食品法规标准 + 新食品原料 + 药食同源 + 地方特色
> **原则**: 规范先行，务实演进——存量兼容，增量从严

---

## 一、三层架构（基石）

```
foodreg-base/
├── raw/     ← 原始资料，用户负责，LLM 只读
├── wiki/    ← 编译知识，LLM 维护，用户只读
└── SCHEMA.md ← 本文件，规则约束
```

### 读写边界（最高优先级）

```
用户永远不改 wiki/
LLM 永远不改 raw/
```

违反此规则 = 数据污染。raw/ 是真相源，wiki/ 是编译产物，互不越界。

### 完整目录

```
foodreg-base/
├── raw/
│   ├── new-food-ingredients/      新食品原料公告（50 份）
│   ├── standard-interpretations/  标准解读与问答（43 份）
│   ├── common-food-ingredients/   普通食品原料复函（11 份）
│   ├── medicine-food-homology/    药食同源公告（8 份）
│   ├── regulatory-documents/      法规原文与提案答复（36 份）
│   └── edible-strains/            可食用菌种公告（3 份）
│
├── wiki/
│   ├── entities/
│   │   ├── new-food-ingredients/     新食品原料（173）
│   │   ├── additives/                食品添加剂（359）
│   │   ├── medicine-food-homology/   药食同源（107）
│   │   ├── edible-strains/           可食用菌种（47）
│   │   ├── nutrition-fortifiers/     营养强化剂（76）
│   │   ├── local-specialty-food/     地方特色食品（189）
│   │   ├── terminated-reviews/       终止审查（82）
│   │   ├── food-product-standards/   食品产品标准（283）
│   │   ├── contact-materials/        食品接触材料（148）
│   │   ├── food-allergens/           食品过敏原（11）
│   │   ├── consultation-list/        征求意见（8）
│   │   └── acceptance-list/          申报受理（5）
│   ├── tables/              关联表（20 张）
│   ├── concepts/            概念页
│   └── comparisons/         对比分析页
│
├── SCHEMA.md
├── index.md
├── log.md
├── README.md
└── LICENSE
```

---

## 二、命名规范

### 原则
**有标准英译用英文，无英译用拼音，地方品种用中文，标准号用标准号。** 不搞一刀切。

### 各模块约定

| 模块 | 命名方式 | 示例 |
|------|---------|------|
| 新食品原料 | 英文名+连字符 | `corn-oligopeptides-powder.md` |
| 食品添加剂 | 中文名 | `苯甲酸及其钠盐.md` |
| 药食同源 | 拼音+连字符 | `dang-shen.md` |
| 可食用菌种 | 拉丁学名转连字符 | `lactobacillus-plantarum-299v.md` |
| 营养强化剂 | 中文名 | `维生素 C.md` |
| 地方特色食品 | 中文名 | `紫皮石斛.md` |
| 终止审查 | 中文名 | `玉米低聚肽粉.md` |
| 食品产品标准 | `GB_xxxx-20xx.md` | `GB_7718-2011.md` |
| 食品接触材料 | 中文名 | `聚乙烯.md` |
| 概念页 | 英文+连字符 | `protein-hydrolysate-rule.md` |
| 对比页 | `comparison-{主题}.md` | `comparison-2760-2014-vs-2024.md` |
| raw/ 公告 | `日期-关键词.md` | `2010-15-zhetangjuzhi.md` |

### 通用规则
- 全小写（英文/拼音部分）
- 连字符分隔，无空格、无下划线
- 不出现 `.` 号（除扩展名和标准号中的 `.`）
- GB 产品标准例外：`GB_` 前缀 + 下划线（与其他模块视觉区分）

---

## 三、YAML Frontmatter（必填字段）

每个实体页开头必须包含。这是查询加速和索引生成的基石。

### 共用字段

```yaml
---
title: "玉米低聚肽粉"
type: entity                         # entity | concept | comparison | table
module: 新食品原料                   # 必填，枚举见下文
status: 普通食品                     # 必填，枚举见下文
created: 2026-06-22
updated: 2026-06-25
tags: [新食品原料, 蛋白]
sources: [raw/new-food-ingredients/2010-15-zhetangjuzhi.md]
---
```

### 扩展字段（按模块按需）

| 字段 | 适用模块 | 说明 | 示例 |
|------|---------|------|------|
| `dosage` | 新食品原料/添加剂/强化剂 | 食用量/限量 | `≤4.5g/d` |
| `unsuitable` | 新食品原料/药食同源 | 不适宜人群 | `婴幼儿` |
| `scope` | 新食品原料/菌种 | 使用范围 | `不限 / 保健食品原料` |
| `announcements` | 新食品原料/菌种 | 公告列表 | `[2010年第15号, 2013年第3号]` |
| `keywords` | 全部 | 检索别名 | `[玉米肽, 玉米蛋白肽]` |
| `standard_id` | 食品产品标准 | 标准号 | `GB 7718-2011` |
| `issuing_body` | 食品产品标准 | 发布机构 | `国家卫健委` |
| `effective_date` | 食品产品标准 | 实施日期 | `2012-04-20` |
| `replaces` | 食品产品标准 | 替代标准 | `GB 7718-2004` |
| `replaced_by` | 食品产品标准 | 被替代为 | `GB 7718-2025` |
| `quality` | 全部 | 质量标记 | `✅已验证 / 📌待验证` |
| `contradictions` | 全部 | 矛盾标记 | `[页面名]` |

### 枚举值

**module**：
```
新食品原料 | 药食同源 | 可食用菌种 | 营养强化剂 | 食品添加剂
食品产品标准 | 地方特色食品 | 终止审查 | 食品接触材料
食品过敏原 | 征求意见 | 申报受理
```

**status**：
```
现行有效 | 即将实施 | 已废止 | 修订中
普通食品 | 保健食品原料 | 终止审查
```

**quality**：
```
✅已验证 — 关键数据已对照原文确认
📌待验证 — AI 推理或非官方来源，需人工核对
⚠️矛盾   — 不同来源数据冲突
🔄草稿   — 页面未完成
```

---

## 四、查询体系

### 四级索引

| 层级 | 位置 | 作用 | 响应 |
|------|------|------|------|
| L1 | `index.md` | 模块入口 + 统计 | 1 次 read_file |
| L2 | 各模块 master-list.md | 模块内清单 | 1 次 read_file |
| L3 | 实体页正文 | 详情/公告原文/批准历程 | 1-2 次 read_file |

### 查询路径

| 问题类型 | 路径 |
|---------|------|
| "XX 能不能用作食品原料" | L1 index.md → 搜 title/keywords → 读实体页 → 多源合规排查 |
| "XX 的食用量上限" | master-list → 搜 dosage → 读实体页 |
| "XX 标准的最新版本" | master-list → module=食品产品标准 → 读 standard_id |
| "乳制品相关所有标准" | L2 → 食品产品标准 master-list → 筛选 |
| "XX 添加剂能用在哪类食品" | tables/additive-category-cross.md |
| "XX 和 YY 有什么区别" | comparisons/ 目录 → 无则当场生成并归档 |

### 高频查询 → 预计算归档

被问 ≥2 次的对比/分析，立即生成 `comparisons/` 或 `concepts/` 页面，后续秒出。

---

## 五、页面模板

### 5.1 新食品原料实体页

```markdown
---
title: "{名称}"
type: entity
module: 新食品原料
status: {现行有效|普通食品|保健食品原料|终止审查}
created: YYYY-MM-DD
updated: YYYY-MM-DD
dosage: "{食用量}"
unsuitable: "{不适宜人群}"
scope: "{使用范围}"
announcements: [{公告列表}]
keywords: [{别名}]
quality: {✅已验证|📌待验证}
tags: [新食品原料, ...]
sources: [raw/new-food-ingredients/xxx.md]
---

# {名称}

## 概述
{一句话 + 当前管理状态}

## 基本信息
| 项目 | 内容 |
|------|------|
| 中文名称 | ... |
| 英文/拉丁名 | ... |
| 生产工艺 | ... |
| 推荐食用量 | ... |
| 不适宜人群 | ... |
| 使用范围 | ... |

## 批准历程
| 公告 | 日期 | 发布机构 | 说明 |
|------|------|---------|------|
| ... | ... | ... | ... |

## 质量要求（如适用）
| 指标 | 要求 |
|------|------|
| ... | ... |

## 相关条目
- [[wiki/entities/xxx]]
- [[wiki/concepts/xxx]]

> 公告引用原文
```

### 5.2 食品产品标准实体页

```markdown
---
title: "{标准名称}"
type: entity
module: 食品产品标准
status: {现行有效|即将实施|已废止|修订中}
standard_id: "GB xxxx-20xx"
standard_type: {产品标准|基础标准|标签标识|生产规范|检验方法|通用标准}
issuing_body: {发布机构}
effective_date: YYYY-MM-DD
replaces: "{旧标准号}"
replaced_by: null
quality: ✅已验证
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [...]
sources: []
---

# {标准名称}

## 基本信息
| 项目 | 内容 |
|------|------|
| 标准号 | GB xxxx-20xx |
| 标准类别 | GB 强制性 |
| 发布日期 | YYYY-MM-DD |
| 实施日期 | YYYY-MM-DD |
| 代替标准 | ... |
| 当前状态 | ... |

## 版本历史
| 版本 | 实施日期 | 状态 |
|------|----------|------|
| ... | ... | ... |

## 过渡期信息（如适用）
- 过渡期：YYYY-MM-DD 至 YYYY-MM-DD
- 备注：...

## 关联模块
- [[GB 2760-2024]]
- [[GB 7718-2025]]

## 引用来源

## 变更记录
```

### 5.3 概念页

```markdown
---
title: "{概念名}"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [...]
sources: [raw/xxx.md]
---

# {概念名}

## 定义

## 法规依据
> 原文引用

## 适用范围/判定条件

## 关联页面
- [[wiki/entities/xxx]]
```

### 5.4 对比页

```markdown
---
title: "{对比主题}"
type: comparison
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [对比]
sources: []
---

# {对比主题}

## 对比表
| 维度 | A | B |
|------|---|---|
| ... | ... | ... |

## 关键差异

## 关联页面
```

---

## 六、质量体系

### 质量标记（写入 frontmatter `quality` 字段）

| 标记 | 含义 | 触发条件 |
|------|------|----------|
| `✅已验证` | 关键数据已对照原文 | NHC 公告原文 / GB 标准原文核对过 |
| `📌待验证` | 需人工核对 | 第三方转载、AI 推理、间接引用 |
| `⚠️矛盾` | 不同来源冲突 | 两处原始资料数据不一致 |
| `🔄草稿` | 页面未完成 | 信息不完整 |

### 矛盾处理流程
1. 检查日期，新来源通常取代旧来源
2. 若确实矛盾，保留两方观点并注日期和来源
3. frontmatter 标 `contradictions: [页面名]`

### Lint 巡检（每次全系整理时执行）
- 状态一致性：`status` 与实施日期是否对齐（运行 `verify-standard-status.py`）
- 断裂 wikilink：`[[ ]]` 目标是否存在
- 孤立页面：零入链的实体页
- 版本链：`replaces`/`replaced_by` 双向闭合
- frontmatter 完整性：必填字段是否缺失

---

## 七、操作流程

### Ingest（入库）
1. 用户放入 raw/
2. LLM 读取 → 提取关键字段
3. 创建/更新 wiki/ 对应页面
4. 写入 frontmatter（必填字段 + quality 标记）
5. 建立 wikilink 交叉引用
6. 更新 index.md 和 log.md

### Query（查询）
1. L1 `index.md` 定位模块
2. L2 `master-list.md` 定位实体页
3. L3 读实体页提取详情
4. 综合回答
5. 高价值问答归档 → `comparisons/` 或更新实体页

### Periodic Ingest（全系整理）
1. 更新 index.md 统计数据
2. 更新 log.md 终态表
3. 修复断裂 wikilink（三类：.md 后缀 / 尾反斜杠 / ../ 相对路径）
4. 运行 Lint 巡检 → 修正
5. 打包交付（仅用户要求时）

---

## 八、关联表规范

所有 tables/ 下的双向关联表遵循统一格式：

- 文件名：`{主题}-cross.md`
- 必须含生成日期和数据源声明
- 添加剂关联表字段：添加剂名称 → 食品分类号 → 食品类别 → 最大使用量

---

> 💡 本 SCHEMA 随知识库演进持续更新。发现新的管理需求时，更新本文件并同步 index.md。
