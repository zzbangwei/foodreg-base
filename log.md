# FoodReg Base 操作日志

## 2026-07-27 — raw/ 目录重组 + 仓库开源

### 执行

**raw/ 目录重组**
- 8 个旧子目录重组为 6 个，按内容类型对齐 wiki/ 分类命名
- `articles/` → `new-food-ingredients/`（50 份）
- `articles-common-food/` → `common-food-ingredients/`（11 份）
- `articles-medfood/` → `medicine-food-homology/`（8 份）
- `interpretations/` + `pdfs/` → `standard-interpretations/`（43 份）
- `regulations/` → `regulatory-documents/`（36 份，扁平化子目录）
- `strains/` → `edible-strains/`（3 份）
- 删除空目录 `docs/` `announcements-standards/` `interpretations-standards/` `standards-pdf/`
- 所有文件名规范化：全英文小写 + 连字符

**文档同步**
- README.md、index.md、SCHEMA.md 目录树和数字全部同步更新
- 实体页合计 1,476 → 1,488，raw/ 由 444 份重算为 151 份（纯 md）

**开源**
- 仓库公开至 GitHub: [github.com/zzbangwei/foodreg-base](https://github.com/zzbangwei/foodreg-base)
- 协议: CC BY-SA 4.0

---

## 2026-07-04 — 营养成分数据全库归拢

### 执行

**新食品原料质量规格（12→68）**
- 扫描 wiki/entities/new-food-ingredients/ 172页 + raw/new-food-ingredients/ 50份公告
- 提取蛋白质/脂肪/膳食纤维/多糖/EPA/DHA/水分/灰分质量规格（≥/≤ 限量）
- 从 12 种扩展到 68 种，覆盖 40% 新食品原料

**药食同源扩展**
- 旧版 nutrition-data-mfh.md（37种，含糖/纤维/钠）vs 完整版（105种）
- 仅奇亚籽不在完整表中（非药食同源），无遗漏
- 新增 生地黄 + 熟地黄 完整数据（矿物质/维生素/氨基酸/脂肪酸/植物化合物），表规模 103→105

**交叉引用（152页）**
- 106 药食同源实体页 → 加 [[营养成分总表]] 链接
- 46 新食品原料实体页 → 加 [[质量规格表]] 链接

### 最终状态

| 数据表 | 条目 | 字段 |
|--------|------|------|
| nutrition-data-mfh-complete.md | 105 | 能量/蛋白/脂肪/碳水/饱和脂肪 + 地黄扩展 |
| nutrition-data-nfi.md | 68 | 蛋白/脂肪/纤维/多糖/EPA/DHA 质量规格 |
| 实体页交叉引用 | 152页 | mfh 106 + nfi 46 |

---

## 2026-07-04 — Knowledge层 阶段三：条款完整性加固

### 执行

**实体页推迟修复（3页）**：二氧化硫（61条）、脱氢乙酸（36条）、司盘类（60条）原为"详见 GB 2760 表A.1"的空壳，从 additive-category-cross.md 反向拉取完整限量数据写入实体页。

**关联表上下文外套**：additive-category-cross.md 表头补标准信息块（标准号、发布方、faid→附录映射规则），确保 RAG 切到此表时每个 chunk 都知道来自 GB 2760-2024。

### 最终状态

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| "详见"推迟模式 | 3 页 | 0 页 |
| 有完整使用数据 | 232 | 356/357 |
| 关联表上下文 | 无标准号 | 有标准号+附录映射 |

唯一未覆盖：enzyme-index.md（索引页）。

### Knowledge层 最终状态

| 检查项 | 状态 |
|--------|------|
| ③ 显式关系 | ✅ |
| ④ 元数据过滤 | ✅ |
| ⑥ 统一别名 | ✅ |
| ⑤ 上下文外套 | ✅ |
| ① 一句话摘要 | ✅ |
| ② 按条款切分 | ✅ |

**全 6 项达标。**

---

## 2026-07-04 — Knowledge层 阶段二：一句话摘要（812页全覆盖）

### 执行

**添加剂（357页）**：模板化生成，基于阶段一的 frontmatter 元数据：
"{中文名}（{英文名}），是{功能}，CNS {cns} / INS {ins}，GB 2760-2024 {section}中{用途描述}。"
表A.1/A.2/C.2/C.3 各有对应的用途描述模板。

**产品标准（283页）**：从正文"1 范围"条款提取第一句作为范围描述（107页有范围文本），无范围的用 "规定{产品名}的术语定义、技术要求、检验方法等"。

**新食品原料（172页）**：从现有 `## 概述` 段提取第一句（全部都有概述）。

**修复**：16个添加剂 summary 的 INS/CNS 噪音修复；103个产品标准范围文本格式修复；2个标准目录点线误提取修复。

### 最终状态

| 模块 | 覆盖率 |
|------|--------|
| 添加剂 | 357/357 (100%) |
| 产品标准 | 283/283 (100%) |
| 新食品原料 | 172/172 (100%) |
| **合计** | **812/812 (100%)** |

### Knowledge层 总体进度

| 检查项 | 状态 |
|--------|------|
| ③ 显式关系 | ✅ 已有 |
| ④ 元数据过滤 | ✅ 已有 |
| ⑥ 统一别名（INS/EN/E编号） | ✅ 阶段一完成 |
| ⑤ 上下文外套（standard/section） | ✅ 阶段一完成 |
| ① 一句话摘要 | ✅ 阶段二完成 |
| ② 按条款切分 | 🔲 待阶段三 |

---

## 2026-07-04 — Knowledge层 阶段一：元数据补全（上下文外套+统一别名）

### 背景
Knowledge 层 6 项检查中 ③ 显式关系 和 ④ 元数据过滤 已达标，但 ⑤ chunk上下文外套 和 ⑥ 统一别名 缺失严重：
- 添加剂实体页仅 3% 提及 GB 2760（孤岛 chunk）
- INS号覆盖率 81%（65 酶制剂缺）、英文名 78%
- E编号全库零覆盖

### 执行过程

**Step 1: 解析权威源**
- additive-list.md (290条) → 提取 CNS/INS/英文名/功能/faid
- enzyme-list.md (71条) → 提取 酶制剂信息
- processing-aid-list.md (119条) → 提取 加工助剂信息
- additive-category-cross.md (27,328条) → faid → 表A.1/A.2 分类（180/110）

**Step 2: 批量补齐实体页**
- Python 脚本逐页匹配中文名 → 写入 frontmatter（standard/section/en_name/functions）
- Body 添加「所属标准」行（GB 2760-2024 表A.1/A.2/C.2/C.3）
- 补齐 INS号、功能字段（此前为「—」的）
- 多轮边缘案例修复（5'-核苷酸类、β-胡萝卜素类、司盘/吐温类）

**Step 3: 去重处理**
- 修复 59 个文件中「所属标准」重复插入问题
- 跳过 enzyme-index.md（索引页，非实体）
- 跳过 3 个重复文件名实体页

**Step 4: E编号交叉映射**
- 建 tables/e-number-crosswalk.md（290条 INS↔E编号）
- 208 个添加剂实体页 frontmatter 写入 e_number

### 最终状态

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| frontmatter standard | 0% | 357/358 (99.7%) |
| frontmatter section | 0% | 357/358 (99.7%) |
| frontmatter en_name | 78% | 357/358 (99.7%) |
| frontmatter functions | 0% | 357/358 (99.7%) |
| frontmatter e_number | 0% | 208/358 (58%) |
| body 所属标准 | 3% | 357/358 (99.7%) |
| new 关联表 | 18 张 | 19 张 (+e-number-crosswalk) |

唯一未覆盖：enzyme-index.md（索引页，设计如此）。65个酶制剂 INS=— 系 GB 2760 表C.2 实际无 INS 编号，正确标记。

---

## 2026-07-03 — 食品产品标准全库补完

### 背景
食品产品标准模块 282 个实体页中 268 个仅为骨架（无标准正文），覆盖率 17.5%。

### 执行过程

**Phase 1: gov.cn 批量下载（来宝）**
- 从 fzmq.gov.cn、jckspj.customs.gov.cn 等政府站点批量搜索+下载
- 63 个 PDF 入库 raw/standards-pdf/

**Phase 2: 用户手动下载（三言）**
- 用户 Windows 端编写 CFSA 平台 + foodmate 爬虫脚本
- 221 个标准全覆盖下载（含 6 个清单编号错误更正）
- 分 6 批 zip（s1-s6）通过飞书传输到服务器
- 另发 interpretations.zip（21 份标准解读）、announcements.zip（18 份公告）
- 最终 295 个 PDF 入库

**Phase 3: 终止审查补充**
- 用户提供 CFSA 完整终止审查意见原文（80+ 产品条目）
- Python 脚本自动匹配实体页 → 写入审查意见
- 81/81 终止审查实体页全部补全

**Phase 4: 个别补发**
- 8 个硬骨头标准逐个飞书发送，实时 pymupdf 提取+入库

**Phase 5: 批量 PDF→MD 转换**
- pymupdf 批量提取文字型 PDF → 136 标准写入实体页
- vision_analyze 逐页 OCR 扫描型 PDF → 86 标准写入实体页
- 3 路子代理并行处理

**Phase 6: 全系整理**
- 更新 index.md 数据规模、模块列表、raw/ 结构
- 更新 log.md
- wikilink 断裂扫描修复（1724 → 322）
- 残余断裂均为实体页间引用缺少年份/缺失实体

### 最终状态

| 指标 | 数量 |
|------|------|
| 实体页总计 | 1,476 |
| 食品产品标准 PDF | 295 个 |
| 标准实体页有正文 | 280/283 (99%) |
| 标准官方解读 | 21 份 |
| 标准发布公告 | 18 份 |
| 终止审查有审查意见 | 81/81 |
| 残余 wikilink 断裂 | 322（缺失实体/年号差异） |

---
*来宝 · 食规智库*
