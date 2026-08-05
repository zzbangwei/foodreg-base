# FoodReg Base 目录

> 食规智库 Wiki 索引。来宝维护。
> 最后更新：2026-08-05 07:37

## 三层架构

```
raw/  → 原始资料（只读）
wiki/ → 编译知识（实体页 + 关联表 + 概念页）
  本文件 ← 规范约束
```

## 数据规模

| 模块 | 数量 |
|------|------|
| 食品添加剂 | 358 |
| 食品产品标准（GB/GB/T） | 285 |
| 地方特色食品 | 187 |
| 新食品原料 | 173 |
| 食品接触材料 | 147 |
| 药食同源 | 106 |
| 终止审查 | 81 |
| 营养强化剂 | 75 |
| 可食用菌种 | 46 |
| 食品过敏原 | 9 |
| 征求意见 | 7 |
| 申报受理 | 4 |
| 概念页 | 3 |
| 关联表 | 22 张 |
| raw/ 原始资料 | 444 份 |
| **实体页合计** | **1,478** |

## wiki/entities/ — 实体模块

- [[wiki/entities/additives/master-list|食品添加剂总清单]] — 358 种
- [[wiki/entities/food-product-standards/|食品产品标准]] — 285 页（GB 强制性 + GB/T 推荐性 + 生产经营规范，99% 有标准正文）
- [[wiki/entities/local-specialty-food/master-list|地方特色食品]] — 187 页
- [[wiki/entities/new-food-ingredients/master-ingredient-list|新食品原料总清单]] — 173 种
- [[wiki/entities/contact-materials/master-list|食品接触材料]] — 147 页
- [[wiki/entities/medicine-food-homology/master-list|药食同源]] — 106 页
- [[wiki/entities/terminated-reviews/master-list|终止审查]] — 81 页（全部含 CFSA 审查意见原文）
- [[wiki/entities/nutrition-fortifiers/master-list|营养强化剂]] — 75 页
- [[wiki/entities/edible-strains/master-list|可食用菌种]] — 46 页
- [[wiki/entities/food-allergens/master-list|食品过敏原]] — 9 页
- [[wiki/entities/consultation-list/_index|征求意见]] — 7 页
- [[wiki/entities/acceptance-list/_index|申报受理]] — 4 页

## wiki/tables/ — 关联表

- [[wiki/tables/additive-category-cross|添加剂×食品分类关联]] — GB 2760 使用量（27,328 条）
- [[wiki/tables/nutrition-fortifier-category-cross|强化剂×食品分类关联]] — GB 14880 使用量（824 条）
- [[wiki/tables/gb9685-additive-list|接触材料添加剂汇总]] — GB 9685
- [[wiki/tables/gb9685-category-cross|接触材料×材料类别关联]] — GB 9685
- [[wiki/tables/additive-list|添加剂总清单]]
- [[wiki/tables/common-food-ingredient-list|普通食品原料清单]]
- [[wiki/tables/prohibited-restricted-ingredient-list|禁用限用目录]]
- [[wiki/tables/prohibited-ingredient-list|负面清单]]
- [[wiki/tables/enzyme-list|酶制剂清单]]
- [[wiki/tables/processing-aid-list|加工助剂清单]]
- [[wiki/tables/natural-flavor-list|天然香料清单]]
- [[wiki/tables/synthetic-flavor-list|合成香料清单]]
- [[wiki/tables/category-list|食品分类表]]
- [[wiki/tables/gb-master-catalog|GB 总目录]]
- [[wiki/tables/nutrition-data-mfh-complete|药食同源营养成分总表]] — 110种
- [[wiki/tables/nutrition-data-nfi|新食品原料营养成分表]] — 68种（NHC公告质量规格）
- [[wiki/tables/nutrition-data-common-food|普通食品原料营养成分表]] — 513种（中国食物成分表第6版匹配）
- [[wiki/tables/e-number-crosswalk|E编号交叉映射表]] — INS ↔ E编号（290条）
- [[wiki/tables/nutrient-function-claims|营养成分功能声称标准用语]] — GB 28050 附录D

## wiki/concepts/ — 概念页

- [[wiki/concepts/new-resource-food|新资源食品/新食品原料/三新食品]]
- [[wiki/concepts/protein-hydrolysate-rule|蛋白质酶解产物按普通食品管理规则]]
- [[wiki/concepts/bone-collagen-naming|骨胶原蛋白粉命名规范]] — 配料表/产品名/企标三场景分析

## raw/ — 原始资料（只读）

- raw/interpretations-standards/ — 21 份 标准官方解读
- raw/announcements-standards/ — 18 份 标准发布公告
- raw/articles/ — 50 份 新食品原料公告原文
- raw/docs/ — 2 份 中国食物成分表第6版 Excel（第一册+第二册）
- raw/interpretations/ — 39 份 官方解读
- raw/articles-common-food/ — 12 份 普通食品复函
- raw/articles-medfood/ — 9 份 药食同源相关

## 最新更新

- 2026-07-29 — 新增 GB/T 29602-2026《固体饮料质量要求》（2026.07.02发布，2027.08.01实施，全部代替GB/T 29602-2013）+ GB/T 29602-2013 旧版实体页
- 2026-07-04 — 营养成分全库归拢：药食同源 110种（A43+B54+C13）、新食品原料 68种、普通食品 513种。中国食物成分表第6版入库。Knowledge层6项全部达标。
- 2026-07-03 — 食品产品标准全库补完：812页实体页 frontmatter 全部补齐 standard/section/en_name/e_number/functions/summary。新建 E编号交叉映射表。
- 2026-07-03 — 食品产品标准全库补完：285 PDF 入库 → pymupdf + vision OCR 提取正文 → 280/283 实体页覆盖（99%）。终止审查 81 个全部录入 CFSA 审查意见原文。
- 2026-06-29 — 新食品原料移入独立子目录
- 2026-06-24 — 新增营养成分数据表两张（药食同源106种+新食品原料框架）
- 2026-06-24 — 新增概念页「蛋白质酶解产物按普通食品管理规则」
