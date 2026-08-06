# FoodReg Base（食规智库）

中国食品法规结构化开放知识库，覆盖 **1,583 条目**。

## 简介

FoodReg Base 是一个面向中国食品安全法规的结构化知识库，系统整理了中国食品领域的核心法规信息，包括食品添加剂、新食品原料、药食同源目录、营养强化剂、食品接触材料、食品产品标准、地方特色食品等类别。

知识库采用 Markdown + Wiki 链接的格式组织，适合 LLM / AI Agent 检索和人类阅读，便于快速查询和交叉引用。

## 知识库结构

```
foodreg-base/
├── index.md                          # 总目录索引
├── SCHEMA.md                         # 数据结构 schema 说明
├── log.md                            # 变更日志
├── wiki/
│   ├── concepts/                     # 概念解释（3 页）
│   ├── comparisons/                  # 对比分析（1 页）
│   ├── tables/                       # 关联表（20 张）
│   └── entities/
│       ├── additives/                # 食品添加剂 GB 2760（368 页）
│       ├── food-product-standards/   # 食品产品标准 GB/GB/T（367 页）
│       ├── local-specialty-food/     # 地方特色食品（189 页）
│       ├── new-food-ingredients/     # 新食品原料（173 页）
│       ├── contact-materials/        # 食品接触材料 GB 9685（152 页）
│       ├── medicine-food-homology/   # 药食同源目录（107 页）
│       ├── nutrition-fortifiers/     # 营养强化剂 GB 14880（86 页）
│       ├── terminated-reviews/       # 终止审查（82 页）
│       ├── edible-strains/           # 可食用菌种（48 页）
│       ├── food-allergens/           # 食品过敏原（11 页）
│       ├── consultation-list/        # 征求意见（8 页）
│       └── acceptance-list/          # 申报受理（5 页）
└── raw/                              # 原始公告、解读、答复原文（199 份）
    ├── announcements-standards/      # 标准发布公告（12 份）
    ├── articles/                     # 法规解读文章（50 份）
    ├── articles-common-food/         # 普通食品原料相关（12 份）
    ├── articles-medfood/             # 药食同源相关（10 份）
    ├── docs/                         # 源文档（9 份）
    ├── interpretations/              # 法规解读（67 份）
    ├── regulations/                  # 法规原文（36 份）
    │   ├── proposal-replies/         # 建议/提案答复
    │   └── labeling-replies/         # 标签标识答复
    └── strains/                      # 菌种相关（3 份）
```

## 数据来源

知识库内容整理自中国国家卫生健康委员会（NHC）、国家市场监督管理总局（SAMR）、国家食品安全风险评估中心（CFSA）等官方发布的公告、标准和解读文件。

## 协议

本知识库采用 [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) 许可协议。

你可以自由地：

- **共享** — 在任何媒介以任何形式复制、发行本作品
- **改编** — 修改、转换或以本作品为基础进行创作

但必须遵循以下条件：

- **署名** — 必须给出适当的署名，提供指向本许可协议的链接
- **相同方式共享** — 如果你对本作品进行了改编，你必须基于相同的许可协议分发你的贡献

## 免责声明

本知识库内容**仅供参考**，不构成法律建议。虽然我们尽力确保信息的准确性和时效性，但法规会不断更新变化，请以官方发布的最新版本为准。使用者应自行核实信息的准确性，并在做出任何法律或商业决策前咨询专业法律顾问。

知识库作者不对因使用本知识库信息而产生的任何直接或间接损失承担责任。
