#!/usr/bin/env python3
"""Process GB 14880 nutrition fortifier data and generate entity pages."""

import json
import os

BASE_DIR = '/home/ubuntu/wiki-foodreg/entities/nutrition-fortifiers'
os.makedirs(BASE_DIR, exist_ok=True)

# Load data
with open('/home/ubuntu/wiki-foodreg/nutrition_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data)} raw records")

# Deduplicate: merge same name, combine scopes and sources
merged = {}
for d in data:
    name = d['name']
    if name not in merged:
        merged[name] = {
            'name': name,
            'sources': set(),
            'scopes': set(),
            'remarks': set(),
        }
    if d['source'].strip():
        merged[name]['sources'].add(d['source'])
    merged[name]['scopes'].add(d['scope'])
    if d['remark'].strip():
        merged[name]['remarks'].add(d['remark'])

print(f"Unique names after merge: {len(merged)}")

# Classification maps
vitamins = [
    '维生素 A', '维生素 B1', '维生素 B2', '维生素 B6', '维生素 B12',
    '维生素 C', '维生素 D', '维生素 E', '维生素 K',
    '烟酸（尼克酸）', '泛酸', '叶酸', '生物素', '肌醇', '胆碱',
    'β-胡萝卜素', '叶黄素', '左旋肉碱（L-肉碱）', 'L-赖氨酸',
]

mineral_names = [
    '钙', '铁', '锌', '硒', '碘', '铜', '锰', '镁', '钾', '磷', '钠',
    '铬', '钼',
]

amino_acid_names = [
    '赖氨酸', '蛋氨酸', '色氨酸', '苯丙氨酸', '缬氨酸', '亮氨酸',
    '异亮氨酸', '苏氨酸', '组氨酸', '精氨酸', '谷氨酸', '谷氨酰胺',
    '天冬氨酸', '甘氨酸', '丙氨酸', '脯氨酸', '丝氨酸', '半胱氨酸',
    '胱氨酸', '酪氨酸', '牛磺酸', '鸟氨酸', '瓜氨酸', 'β-丙氨酸',
]

fatty_acid_names = [
    '二十二碳六烯酸（DHA）', '花生四烯酸（AA 或 ARA）', 'γ-亚麻酸',
    '1,3-二油酸 2-棕榈酸甘油三酯',
]

nucleotide_names = ['核苷酸']

prebiotic_names = [
    '低聚果糖', '低聚半乳糖', '多聚果糖', '棉子糖', '聚葡萄糖',
    '半乳甘露聚糖', '酵母β-葡聚糖', "2'-岩藻糖基乳糖", '乳糖-N-新四糖',
]

other_names = [
    '酪蛋白磷酸肽', '酪蛋白钙肽', '乳铁蛋白', "3'-唾液酸乳糖钠盐",
    'd-核糖', 'γ-亚麻酸',
]

# Build lookup
name_to_category = {}
for n in vitamins: name_to_category[n] = '维生素类'
for n in mineral_names: name_to_category[n] = '矿物质类'
for n in amino_acid_names: name_to_category[n] = '氨基酸类'
for n in fatty_acid_names: name_to_category[n] = '脂肪酸类'
for n in nucleotide_names: name_to_category[n] = '核苷酸类'
for n in prebiotic_names: name_to_category[n] = '益生元类'
for n in other_names: name_to_category[n] = '其他类'

categories = {
    '维生素类': [],
    '矿物质类': [],
    '氨基酸类': [],
    '脂肪酸类': [],
    '核苷酸类': [],
    '益生元类': [],
    '其他类': [],
}

uncertain = []
for name in merged:
    cat = name_to_category.get(name)
    if cat:
        categories[cat].append(name)
    else:
        uncertain.append(name)

print("\nClassification:")
for cat, names in categories.items():
    print(f"  {cat}: {len(names)}")
print(f"  Uncertain: {len(uncertain)}")
for u in uncertain:
    print(f"    - '{u}'")

# ========================
# Generate master list
# ========================
lines = []
lines.append("# GB 14880-2012 食品营养强化剂使用标准 — 营养强化剂总清单")
lines.append("")
lines.append("## 数据来源")
lines.append("- **标准**: GB 14880-2012 食品安全国家标准 食品营养强化剂使用标准")
lines.append("- **网站**: https://14880.foodvip.net/index/supple/index")
lines.append("- **数据提取日期**: 2026-06-22")
lines.append("- **原始记录**: {}条，去重后{}种营养强化剂".format(len(data), len(merged)))
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 目录")
lines.append("")
for cat, names in categories.items():
    if names:
        anchor = cat.replace('（', '-').replace('）', '-').replace(' ', '-')
        lines.append(f"- [{cat}](#{cat})（{len(names)}种）")
lines.append("")

# Write each category
for cat, names in categories.items():
    if not names:
        continue
    lines.append(f"## {cat}")
    lines.append("")
    lines.append("| 序号 | 营养强化剂名称 | 化合物来源 | 允许使用范围 | 增补公告 |")
    lines.append("|------|---------------|-----------|-------------|---------|")
    for i, name in enumerate(sorted(names), 1):
        info = merged[name]
        sources_str = "、".join(sorted(info['sources'])) if info['sources'] else "[待确认]"
        scopes = []
        if '允许用于普通食品' in info['scopes']:
            scopes.append('普通食品')
        if '允许用于特殊膳食用食品' in info['scopes']:
            scopes.append('特殊膳食用食品')
        scope_str = "、".join(scopes) if scopes else "[待确认]"

        remark_strs = []
        for r in sorted(info['remarks']):
            if len(r) > 100:
                r_short = r[:100] + "..."
            else:
                r_short = r
            remark_strs.append(r_short.replace('\n', '；'))
        remark_str = "；".join(remark_strs) if remark_strs else "—"

        if len(sources_str) > 120:
            sources_str = sources_str[:120] + "..."

        lines.append(f"| {i} | {name} | {sources_str} | {scope_str} | {remark_str} |")
    lines.append("")

# Add uncertain section if any
if uncertain:
    lines.append("## 待确认分类")
    lines.append("")
    for name in sorted(uncertain):
        info = merged[name]
        sources_str = "、".join(sorted(info['sources'])) if info['sources'] else "[待确认]"
        lines.append(f"- **{name}**: 来源={sources_str}, 范围={'/'.join(info['scopes'])}")
    lines.append("")

master_path = os.path.join(BASE_DIR, 'master-list.md')
with open(master_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f"\nWrote master list: {master_path}")

# ========================
# Generate entity pages
# ========================
entity_count = 0
for name, info in merged.items():
    safe_name = name.replace('/', '-').replace('\\', '-').replace("'", "-")
    entity_path = os.path.join(BASE_DIR, f'{safe_name}.md')

    scopes = []
    if '允许用于普通食品' in info['scopes']:
        scopes.append('允许用于普通食品')
    if '允许用于特殊膳食用食品' in info['scopes']:
        scopes.append('允许用于特殊膳食用食品')

    sources = sorted(info['sources']) if info['sources'] else ["[待确认]"]
    remarks = sorted(info['remarks']) if info['remarks'] else ["—"]

    cat = name_to_category.get(name, '未分类')

    content = []
    content.append(f"# {name}")
    content.append("")
    content.append(f"> 分类: {cat}")
    content.append("")
    content.append("## 基本信息")
    for src in sources:
        content.append(f"- 化合物来源: {src}")
    content.append(f"- 允许使用范围: {'、'.join(scopes) if scopes else '[待确认]'}")
    content.append(f"- 增补公告: {remarks[0]}")
    for r in remarks[1:]:
        content.append(f"  {r}")
    content.append("")
    content.append("## 数据来源")
    content.append("GB 14880-2012 食品安全国家标准 食品营养强化剂使用标准")
    content.append("")
    content.append(f"→ [返回总清单](master-list.md)")
    content.append("")

    with open(entity_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    entity_count += 1

print(f"Wrote {entity_count} entity pages to {BASE_DIR}/")
print("Done!")
