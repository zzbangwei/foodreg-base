#!/usr/bin/env python3
"""Generate entity pages for 2019-2021 food contact materials."""
import os

OUT = "/home/ubuntu/wiki-foodreg/entities/contact-materials"

def write_page(filename, title, en_name, notice_no, notice_date, notice_name,
               prod_type, usage, extra_sections=None):
    """Write a standard entity page."""
    content = f"""# {title}

## 基本信息
- **中文名称**：{title}
- **英文名称**：{en_name}
- **公告号**：{notice_no}
- **批准日期**：{notice_date}
- **来源公告**：{notice_name}

## 产品类型
{prod_type}

## 使用范围
{usage}
"""
    if extra_sections:
        content += extra_sections
    
    content += """## 质量规格
执行 GB 9685-2016 《食品安全国家标准 食品接触材料及制品用添加剂使用标准》

## 来源
"""
    # Add source links based on notice
    links = {
        "2019年第2号": "- 解读链接：https://zwfw.nhc.gov.cn/kzx/tzgg/xspylsp_225/201905/t20190529_1261.html",
        "2020年第4号": "- 解读链接：https://zwfw.nhc.gov.cn/kzx/tzgg/sptjjxpzsp_224/202006/t20200602_1671.html",
        "2020年第6号": "- 公告链接：https://www.nhc.gov.cn/sps/c100088/202008/38710d77a6dd431282999af5050fc62d.shtml\n- 解读链接：https://zwfw.nhc.gov.cn/kzx/tzgg/sptjjxpzsp_224/202101/t20210115_2014.html",
        "2020年第8号": "- 解读链接：https://zwfw.nhc.gov.cn/kzx/tzgg/sptjjxpzsp_224/202101/t20210115_2016.html",
        "2020年第9号": "- 公告链接：https://www.nhc.gov.cn/sps/c100088/202101/a677d9fc167241d4a49d4a22329d774e.shtml\n- 解读链接：https://zwfw.nhc.gov.cn/kzx/tzgg/xspylsp_225/202101/t20210108_1687.html",
        "2021年第2号": "- 解读链接：https://www.nhc.gov.cn/sps/c100087/202102/f0a4464207b843a0b355fbdcfbccd863.shtml",
        "2021年第9号": "- 解读链接：https://www.nhc.gov.cn/sps/c100088/202110/9b83696439ac4bd8b81353c8e5b3a5d9.shtml",
    }
    content += links.get(notice_no, "") + "\n"
    
    path = os.path.join(OUT, filename)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  Created: {filename}")


# ============================================================
# 2019年第2号 (15 items)
# ============================================================
N2019_2 = "2019年第2号"
D2019_2 = "2019-05-29"
NN2019_2 = "关于弯曲乳杆菌等24种\"三新食品\"的公告"

# --- 扩大使用范围的食品接触材料及制品用添加剂 (8 items) ---

write_page(
    "magnesium-sulfate-abs.md",
    "硫酸镁", "Magnesium sulfate",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "丙烯腈-丁二烯-苯乙烯共聚物（ABS）塑料",
    "\n## 最大使用量\n按需使用\n\n## 国际参考\n该物质常温下为白色固体粉末，作为添加剂用于ABS塑料的加工过程。\n"
)

write_page(
    "dimethylbenzylidene-glucitol-pb1.md",
    "1,3:2,4-双-O-[(3,4-二甲基苯基)亚甲基]-D-葡糖醇", 
    "1,3:2,4-Bis-O-[(3,4-dimethylphenyl)methylene]-D-glucitol",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "聚丁烯-1（PB-1）塑料",
    "\n## 最大使用量\n0.3%\n\n## CAS号\n135861-56-2\n\n## 国际参考\n该物质常温下为白色固体粉末，作为添加剂用于PB-1塑料的加工过程。\n"
)

write_page(
    "erucamide-pb1.md",
    "芥酸酰胺", "Erucamide",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "聚丁烯-1（PB-1）塑料",
    "\n## 最大使用量\n0.3%\n\n## CAS号\n112-84-5\n\n## 国际参考\n该物质常温下为白色固体粉末，作为添加剂用于PB-1塑料的加工过程。\n"
)

write_page(
    "calcium-stearate-pb1.md",
    "硬脂酸钙", "Calcium stearate",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "聚丁烯-1（PB-1）塑料",
    "\n## 最大使用量\n0.2%\n\n## CAS号\n1592-23-0\n\n## 国际参考\n该物质常温下为白色固体粉末，作为添加剂用于PB-1塑料的加工过程。\n"
)

write_page(
    "zinc-stearate-pmp.md",
    "硬脂酸锌", "Zinc stearate",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "聚甲基戊烯（PMP）塑料",
    "\n## 最大使用量\n0.04%\n\n## CAS号\n557-05-1\n\n## 国际参考\n该物质常温下为白色固体粉末，作为添加剂用于PMP塑料的加工过程。\n"
)

write_page(
    "pentaerythritol-tetrakis-pmp.md",
    "四[3-(3,5-二叔丁基-4-羟基苯基)丙酸]季戊四醇酯",
    "Pentaerythritol tetrakis[3-(3,5-di-tert-butyl-4-hydroxyphenyl)propionate]",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "聚甲基戊烯（PMP）塑料",
    "\n## 最大使用量\n0.13%\n\n## CAS号\n6683-19-8\n\n## 国际参考\n该物质常温下为白色固体粉末，作为抗氧化剂用于PMP塑料的加工过程。\n"
)

write_page(
    "tris-di-tert-butylphenyl-phosphite-pmp.md",
    "三(2,4-二叔丁基苯基)亚磷酸酯",
    "Tris(2,4-di-tert-butylphenyl) phosphite",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "聚甲基戊烯（PMP）塑料",
    "\n## 最大使用量\n0.08%\n\n## CAS号\n31570-04-4\n\n## 国际参考\n该物质常温下为白色固体粉末，作为抗氧化剂用于PMP塑料的加工过程。\n"
)

write_page(
    "butyl-acrylate-ethylhexyl-acrylate-copolymer.md",
    "2-丙烯酸丁酯与2-丙烯酸-2-乙基己基酯的聚合物",
    "Copolymer of butyl acrylate and 2-ethylhexyl acrylate",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "涂料及涂层",
    "\n## 最大使用量\n按需使用\n\n## CAS号\n171885-12-4\n\n## 国际参考\n该物质常温下为无色透明液体，作为添加剂用于涂料及涂层的加工过程。\n"
)

# --- 食品接触材料及制品用添加剂新品种 (1 item) ---

write_page(
    "distearoyl-ethylenediamine-azacyclotridecanone-isocyanate.md",
    "N,N'-二(十八酰基)-乙二胺与氮杂环十三烷-2-酮的均聚物和1-异氰酸根合十八碳烷的反应产物",
    "Reaction product of N,N'-distearoyl-ethylenediamine, azacyclotridecan-2-one homopolymer and 1-isocyanatooctadecane",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用添加剂（新品种）",
    "涂料及涂层",
    "\n## 最大使用量\n2%\n\n## CAS号\n338462-62-7\n\n## SML（特定迁移限量）\n- 5 mg/kg（氮杂环十三烷-2-酮）\n- ND（异氰酸根，检测限DL=0.01mg/kg）\n\n## 国际参考\n该物质常温下为固体，作为添加剂用于涂料及涂层的加工过程，改善涂层的性能。\n"
)

# --- 食品接触材料及制品用树脂新品种 (6 items) ---

poly10_usage = "涂料及涂层"
poly10_extra = "\n## 最大使用量\n30%\n\n## SML（特定迁移限量）\n- 7.5 mg/kg（1,4-苯二甲酸）\n- 5 mg/kg（1,4-丁二醇）\n- 5 mg/kg（偏苯三甲酸）\n"

write_page(
    "terephthalic-adipic-butanediol-trimellitic-polymer.md",
    "1,4-苯二甲酸与己二酸、1,4-丁二醇和偏苯三甲酸酐的聚合物",
    "Polymer of terephthalic acid, adipic acid, 1,4-butanediol and trimellitic anhydride",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用树脂（新品种）",
    poly10_usage,
    poly10_extra
)

write_page(
    "epichlorohydrin-methylenebis-dimethylphenol-hydroquinone-polymer.md",
    "氯甲基环氧乙烷与4,4'-亚甲基双(2,6-二甲基酚)和对苯二酚的聚合物",
    "Polymer of chloromethyloxirane, 4,4'-methylenebis(2,6-dimethylphenol) and hydroquinone",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用树脂（新品种）",
    "涂料及涂层",
    "\n## 最大使用量\n90%\n\n## SML（特定迁移限量）\n- 0.6 mg/kg（对苯二酚）\n- ND（氯甲基环氧乙烷，检测限DL=0.01mg/kg）\n"
)

write_page(
    "dimethylethanolamine-neutralized-bpa-epoxy-acrylate.md",
    "二甲基乙醇胺部分中和的缩水甘油封端双酚A/环氧氯丙烷共聚物与苯乙烯、甲基丙烯酸甲酯、丙烯酸2-乙基己酯、丙烯酸和甲基丙烯酸的反应产物",
    "Reaction product of dimethyl ethanolamine partially neutralized glycidyl-terminated bisphenol A/epichlorohydrin copolymer with styrene, methyl methacrylate, 2-ethylhexyl acrylate, acrylic acid and methacrylic acid",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用树脂（新品种）",
    "涂料及涂层",
    "\n## SML（特定迁移限量）\n- 6 mg/kg（甲基丙烯酸）\n- 0.05 mg/kg（丙烯酸2-乙基己酯）\n- ND（环氧氯丙烷，检测限DL=0.01mg/kg）\n- 0.6 mg/kg（双酚A）\n"
)

write_page(
    "isophthalic-terephthalic-butanediol-ethylene-glycol-adipic-polymer-2019.md",
    "1,3-苯二甲酸与1,4-苯二甲酸、1,4-丁二醇、1,2-乙二醇和己二酸的聚合物",
    "Polymer of isophthalic acid, terephthalic acid, 1,4-butanediol, 1,2-ethylene glycol and adipic acid",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用树脂（新品种）",
    "涂料及涂层",
    "\n## SML（特定迁移限量）\n- 5 mg/kg（1,3-苯二甲酸）\n- 7.5 mg/kg（1,4-苯二甲酸）\n- 5 mg/kg（1,4-丁二醇）\n- 30 mg/kg（乙二醇）\n"
)

write_page(
    "isocyanato-trimethylcyclohexyl-homopolymer-neopentyl-glycol-caprolactam.md",
    "5-异氰酸根合-1-(异氰酸根合甲基)-1,3,3-三甲基环己烷的均聚物与2,2-二甲基-1,3-丙二醇、二甘醇、1,4-二(羟甲基)环己烷、1,3-苯二甲酸、氢化二聚C18不饱和脂肪酸和ε-己内酰胺的反应产物",
    "Reaction product of 5-isocyanato-1-(isocyanatomethyl)-1,3,3-trimethylcyclohexane homopolymer with neopentyl glycol, diethylene glycol, 1,4-cyclohexanedimethanol, isophthalic acid, hydrogenated dimer C18 unsaturated fatty acid and ε-caprolactam",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用树脂（新品种）",
    "涂料及涂层",
    "\n## SML（特定迁移限量）\n- 5 mg/kg（1,3-苯二甲酸）\n- 0.05 mg/kg（新戊二醇）\n- 30 mg/kg（乙二醇）\n- 15 mg/kg（己内酰胺）\n- ND（异氰酸根，检测限DL=0.01mg/kg）\n"
)

write_page(
    "isophthalic-terephthalic-trimellitic-adipic-methylpropanediol-diglycol-polymer.md",
    "1,3-苯二甲酸与1,4-苯二甲酸、1,3-二氢-1,3-二氧代-5-异苯并呋喃羧酸、己二酸、2-甲基-1,3-丙二醇和2,2'-氧双[乙醇]的聚合物",
    "Polymer of isophthalic acid, terephthalic acid, trimellitic anhydride, adipic acid, 2-methyl-1,3-propanediol and 2,2'-oxybis[ethanol]",
    N2019_2, D2019_2, NN2019_2,
    "食品接触材料及制品用树脂（新品种）",
    "涂料及涂层",
    "\n## SML（特定迁移限量）\n- 5 mg/kg（1,3-苯二甲酸）\n- 7.5 mg/kg（1,4-苯二甲酸）\n- 5 mg/kg（偏苯三甲酸）\n- 5 mg/kg（2-甲基-1,3-丙二醇）\n- 30 mg/kg（乙二醇）\n"
)

# ============================================================
# 2020年第4号 (21 items, 辛酸锌/zinc-octoate already exists)
# ============================================================
N2020_4 = "2020年第4号"
D2020_4 = "2020-06-02"
NN2020_4 = "关于瑞士乳杆菌R0052等53种\"三新食品\"的公告"

# --- 添加剂新品种 (items 2-4, item 1 辛酸锌 already exists) ---

write_page(
    "neopentyl-glycol-ethylene-glycol-isophthalic-dimethyl-terephthalate-dimer-acid-trimellitic-copolymer.md",
    "2,2-二甲基-1,3-丙二醇，乙二醇，间苯二甲酸，对苯二酸二甲酯，二聚酸及偏苯三甲酸酐的共聚物",
    "Copolymer of neopentyl glycol, ethylene glycol, isophthalic acid, dimethyl terephthalate, dimer acid and trimellitic anhydride",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（新品种）",
    "涂料及涂层"
)

write_page(
    "trimellitic-anhydride-mdi-dimethyl-biphenyl-diisocyanate-copolymer.md",
    "1,2,4-苯三酸酐与4,4'-二苯基甲烷二异氰酸酯和3,3'-二甲基-4,4'-联苯二异氰酸酯的共聚物",
    "Copolymer of trimellitic anhydride, 4,4'-diphenylmethane diisocyanate and 3,3'-dimethyl-4,4'-biphenyl diisocyanate",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（新品种）",
    "涂料及涂层"
)

write_page(
    "trimethylpropanamide-benzene-paper.md",
    "1,3,5-三(2,2-二甲基丙酰胺)苯",
    "1,3,5-Tris(2,2-dimethylpropanamide)benzene",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（新品种，消泡剂）",
    "纸和纸板"
)

# --- 扩大使用范围的添加剂 (items 5-16, 12 items) ---

write_page(
    "neopentyl-glycol-ethylene-glycol-isophthalic-sebacic-terephthalic-trimellitic-polymer-rubber.md",
    "2,2-二甲基-1,3-丙二醇与乙二醇、1,3-苯二甲酸、癸二酸、1,4-苯二甲酸和偏苯三甲酸酐的聚合物",
    "Polymer of neopentyl glycol, ethylene glycol, isophthalic acid, sebacic acid, terephthalic acid and trimellitic anhydride",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（扩大使用范围，填料）",
    "扩大至橡胶材料及制品"
)

write_page(
    "neopentyl-glycol-ethylene-glycol-isophthalic-sebacic-terephthalic-trimellitic-polymer-pvc.md",
    "2,2-二甲基-1,3-丙二醇与乙二醇、1,3-苯二甲酸、癸二酸、1,4-苯二甲酸和偏苯三甲酸酐的聚合物",
    "Polymer of neopentyl glycol, ethylene glycol, isophthalic acid, sebacic acid, terephthalic acid and trimellitic anhydride",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（扩大使用范围，爽滑剂）",
    "扩大至聚氯乙烯（PVC）塑料"
)

write_page(
    "n-n-bis-tetramethyl-piperidinyl-isophthalamide-pps.md",
    "N,N'-双(2,2,6,6-四甲基-4-哌啶基)-1,3-苯二甲酰胺",
    "N,N'-Bis(2,2,6,6-tetramethyl-4-piperidinyl)-1,3-benzenedicarboxamide",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至聚苯硫醚（PPS）塑料"
)

write_page(
    "dimethyl-terephthalate-butanediol-ptmg-polymer-pet.md",
    "对苯二甲酸二甲酯与1,4-丁二醇和α-氢-ω-羟基聚(氧-1,4-丁烷二基)的聚合物",
    "Polymer of dimethyl terephthalate, 1,4-butanediol and α-hydro-ω-hydroxy poly(oxy-1,4-butanediyl)",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至聚对苯二甲酸乙二醇酯（PET）塑料"
)

write_page(
    "methacrylic-acid-ethyl-acrylate-acrylic-acid-copolymer-paper.md",
    "2-甲基-2-丙烯酸与2-丙烯酸乙酯和2-丙烯酸的聚合物",
    "Polymer of methacrylic acid, ethyl acrylate and acrylic acid",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大使用量至0.5%（纸和纸板）"
)

write_page(
    "methacrylic-acid-ethyl-acrylate-acrylic-acid-copolymer-adhesive.md",
    "2-甲基-2-丙烯酸与2-丙烯酸乙酯和2-丙烯酸的聚合物",
    "Polymer of methacrylic acid, ethyl acrylate and acrylic acid",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至粘合剂"
)

write_page(
    "ci-disperse-violet-26-as.md",
    "C.I.分散紫26",
    "C.I. Disperse Violet 26",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用着色剂（扩大使用范围）",
    "扩大至丙烯腈-苯乙烯共聚物（AS）塑料"
)

write_page(
    "glass-fiber-ptfe.md",
    "玻璃纤维",
    "Glass fiber",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至聚四氟乙烯（PTFE）塑料"
)

write_page(
    "methyl-methacrylate-styrene-ethylhexyl-acrylate-methyl-acrylate-copolymer.md",
    "2-甲基-2-丙烯酸甲酯与乙烯基苯、2-丙烯酸-2-乙基己基酯和2-丙烯酸甲酯的聚合物",
    "Polymer of methyl methacrylate, vinylbenzene, 2-ethylhexyl acrylate and methyl acrylate",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂/树脂（扩大使用范围）",
    "塑料材料及制品"
)

write_page(
    "methyl-methacrylate-butyl-acrylate-vinyl-acetate-ethylhexyl-acrylate-copolymer.md",
    "2-甲基丙烯酸甲酯与丙烯酸丁酯、乙酸乙烯酯和2-丙烯酸-2-乙基己基酯的聚合物",
    "Polymer of methyl methacrylate, butyl acrylate, vinyl acetate and 2-ethylhexyl acrylate",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂/树脂（扩大使用范围）",
    "塑料材料及制品"
)

write_page(
    "methyl-methacrylate-vinyl-acetate-ethylhexyl-acrylate-copolymer.md",
    "2-甲基-2-丙烯酸甲酯与乙酸乙烯酯和2-丙烯酸-2-乙基己基酯的聚合物",
    "Polymer of methyl methacrylate, vinyl acetate and 2-ethylhexyl acrylate",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂/树脂（扩大使用范围）",
    "塑料材料及制品"
)

write_page(
    "ethylhexyl-acrylate-vinyl-acetate-copolymer.md",
    "2-丙烯酸-2-乙基己基酯与乙酸乙烯酯的聚合物",
    "Polymer of 2-ethylhexyl acrylate and vinyl acetate",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用添加剂/树脂（扩大使用范围）",
    "塑料材料及制品"
)

# --- 树脂新品种 (items 17-21, 5 items) ---

write_page(
    "isophthalic-terephthalic-chdm-methylpropanediol-polymer.md",
    "1,3-苯二甲酸与1,4-苯二甲酸、1,4-二(羟甲基)环己烷和2-甲基-1,3-丙二醇的聚合物",
    "Polymer of isophthalic acid, terephthalic acid, 1,4-cyclohexanedimethanol and 2-methyl-1,3-propanediol",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用树脂（新品种，成膜物质）",
    "涂料及涂层"
)

write_page(
    "sorbic-acid-hydroquinone-epichlorohydrin-dimethylaminoethanol-polymer.md",
    "(2E,4E)-2,4-己二烯酸与对苯二酚、氯甲基环氧乙烷...的聚合物与二甲胺基乙醇的反应产物",
    "Reaction product of (2E,4E)-2,4-hexadienoic acid with hydroquinone and chloromethyloxirane polymer, reacted with dimethylaminoethanol",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用树脂（新品种）",
    "涂料及涂层"
)

write_page(
    "trimellitic-anhydride-ethylene-glycol-polymer.md",
    "1,3-二氢-1,3-二氧代-5-异苯并呋喃羧酸与1,2-乙二醇的聚合物",
    "Polymer of trimellitic anhydride and ethylene glycol",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用树脂（新品种）",
    "塑料、橡胶"
)

write_page(
    "methyl-methacrylate-multi-monomer-polymer-adhesive-coating-ink.md",
    "2-甲基-2-丙烯酸甲酯与多种单体的聚合物",
    "Polymer of methyl methacrylate with multiple monomers",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用基础树脂（新品种）",
    "粘合剂、涂料及涂层、油墨"
)

write_page(
    "terephthalic-acid-multi-monomer-polymer-adhesive-coating-ink.md",
    "1,4-苯二甲酸与多种单体的聚合物",
    "Polymer of terephthalic acid with multiple monomers",
    N2020_4, D2020_4, NN2020_4,
    "食品接触材料及制品用基础树脂（新品种）",
    "粘合剂、涂料及涂层、油墨"
)

# ============================================================
# 2020年第6号 (16 items)
# ============================================================
N2020_6 = "2020年第6号"
D2020_6 = "2020-08-10"
NN2020_6 = "关于蛋白质谷氨酰胺酶等21种\"三新食品\"的公告"

international_refs_2020_6 = {
    1: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用纸和纸板\n- 加拿大卫生部：允许用于食品接触用纸和纸板\n",
    2: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用涂料\n- 欧盟委员会（EU）：允许用于食品接触用涂料\n",
    3: "\n## 国际参考\n- 欧盟委员会（EU）：允许用于食品接触用塑料\n- 南方共同市场（MERCOSUR）：允许用于食品接触用塑料\n",
    4: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用PEEK塑料\n- 欧盟委员会（EU）：允许用于食品接触用塑料\n",
    5: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用PE和PP塑料\n- 欧盟委员会（EU）：允许用于食品接触用塑料\n",
    6: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用橡胶\n- 欧盟委员会（EU）：允许用于食品接触用橡胶\n",
    7: "\n## 国际参考\n- 法国卫生部：允许用于食品接触用AS塑料\n- 日本JHOSPA：允许用于食品接触用塑料\n",
    8: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用PB-1塑料\n- 欧盟委员会（EU）：允许用于食品接触用塑料\n",
    9: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用塑料\n- 欧盟委员会（EU）：允许用于食品接触用塑料\n",
    10: "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用塑料\n- 欧盟委员会（EU）：允许用于食品接触用塑料\n- 日本JHOSPA：允许用于食品接触用塑料\n",
}

ref = international_refs_2020_6.get

write_page(
    "microfibrillated-cellulose-pulp.md",
    "微纤化纤维素纸浆",
    "Microfibrillated cellulose pulp",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用纸和纸板干湿强度剂（新品种）",
    "有涂层及无涂层食品接触用纸和纸板",
    ref(1)
)

write_page(
    "dibutyl-fumarate-homopolymer.md",
    "富马酸二丁酯均聚物",
    "Dibutyl fumarate homopolymer",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用涂料添加剂（新品种）",
    "食品接触用涂料及涂层，用于调节表面张力，增强附着力",
    ref(2)
)

write_page(
    "ethyl-acrylate-methyl-acrylamide-copolymer-abs.md",
    "2-丙烯酸乙酯与2-甲基-2-丙烯酰胺的聚合物",
    "Polymer of ethyl acrylate and 2-methyl-2-acrylamide",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用塑料附聚助剂（新品种）",
    "ABS塑料（白色水性乳液，避免聚合物结块）",
    ref(3)
)

write_page(
    "calcium-stearate-peek.md",
    "硬脂酸钙",
    "Calcium stearate",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用脱模剂（扩大使用范围）",
    "扩大至聚醚醚酮（PEEK）塑料",
    ref(4)
)

write_page(
    "mono-alkenyl-dihydro-furandione-derivative-pe-pp.md",
    "单C15~C20烯基-二氢-2,5-呋喃二酮衍生物",
    "Mono C15~C20 alkenyl-dihydro-2,5-furandione derivative",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用碳酸钙表面处理剂（扩大使用范围）",
    "扩大至聚乙烯（PE）和聚丙烯（PP）塑料",
    ref(5)
)

write_page(
    "polyethylene-rubber.md",
    "聚乙烯",
    "Polyethylene",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用润滑/流动改善剂（扩大使用范围）",
    "扩大至橡胶材料及制品",
    ref(6)
)

write_page(
    "ci-solvent-violet-36-as.md",
    "C.I.溶剂紫36",
    "C.I. Solvent Violet 36",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用紫色着色剂（扩大使用范围）",
    "扩大至丙烯腈-苯乙烯共聚物（AS）塑料",
    ref(7)
)

write_page(
    "octadecyl-di-tert-butyl-hydroxyphenyl-propionate-pb1.md",
    "β-(3,5-二叔丁基-4-羟基苯基)丙酸十八醇酯",
    "Octadecyl β-(3,5-di-tert-butyl-4-hydroxyphenyl)propionate",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用抗氧化剂（扩大使用范围）",
    "扩大至聚丁烯-1（PB-1）塑料",
    ref(8)
)

# 9. C18-不饱和脂肪酸二聚体与己内酰胺和六亚甲基二胺的聚合物 - 基础树脂
write_page(
    "c18-dimer-acid-caprolactam-hexamethylenediamine-polymer.md",
    "C18-不饱和脂肪酸二聚体与己内酰胺和六亚甲基二胺的聚合物",
    "Polymer of C18 unsaturated fatty acid dimer, caprolactam and hexamethylenediamine",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用基础树脂（新品种）",
    "食品接触用塑料，熔点约200°C",
    ref(9)
)

# 10. 氢化的苯乙烯与2-甲基-1,3-丁二烯和1,3-丁二烯的嵌段聚合物
write_page(
    "hydrogenated-styrene-isoprene-butadiene-block-copolymer.md",
    "氢化的苯乙烯与2-甲基-1,3-丁二烯和1,3-丁二烯的嵌段聚合物",
    "Hydrogenated block polymer of styrene, isoprene and butadiene",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用基础树脂（新品种）",
    "食品接触用塑料，具有高抗拉强度和吸油性",
    ref(10)
)

# 11. 4,4'-(1-甲基亚乙基)二苯酚与2-(氯甲基)环氧乙烷苯甲酸酯的聚合物
write_page(
    "bisphenol-a-epichlorohydrin-benzoate-polymer.md",
    "4,4'-(1-甲基亚乙基)二苯酚与2-(氯甲基)环氧乙烷苯甲酸酯的聚合物",
    "Polymer of 4,4'-(1-methylethylidene)bisphenol and 2-(chloromethyl)oxirane benzoate",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用涂料树脂（新品种）",
    "食品接触用涂料及涂层（高硬度/耐化学性）",
    "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用涂料\n- 欧盟委员会（EU）：允许用于食品接触用涂料\n"
)

# 12. 1,4-二（羟甲基）环己烷与多种单体的聚合物
write_page(
    "chdm-multi-monomer-polymer-coating.md",
    "1,4-二（羟甲基）环己烷与多种单体的聚合物",
    "Polymer of 1,4-cyclohexanedimethanol with multiple monomers",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用涂料树脂（新品种）",
    "食品接触用涂料及涂层（良好附着力/抗腐蚀性）",
    "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用涂料\n- 欧盟委员会（EU）：允许用于食品接触用涂料\n"
)

# 13. 1,4-丁二醇与乙二醇等多种单体的聚合物
write_page(
    "butanediol-ethylene-glycol-multi-monomer-polymer-coating.md",
    "1,4-丁二醇与乙二醇等多种单体的聚合物",
    "Polymer of 1,4-butanediol, ethylene glycol and multiple monomers",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用涂料树脂（新品种）",
    "食品接触用涂料及涂层",
    "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用涂料\n- 欧盟委员会（EU）：允许用于食品接触用涂料\n"
)

# 14. 1,3-苯二甲酸与1,4-苯二甲酸和1,2-乙二醇的聚合物
write_page(
    "isophthalic-terephthalic-ethylene-glycol-polymer.md",
    "1,3-苯二甲酸与1,4-苯二甲酸和1,2-乙二醇的聚合物",
    "Polymer of isophthalic acid, terephthalic acid and ethylene glycol",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用涂料树脂（新品种）",
    "食品接触用涂料及涂层",
    "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用涂料\n- 欧盟委员会（EU）：允许用于食品接触用涂料\n"
)

# 15. 甲基丙烯酸与多种单体的聚合物与二甲氨基乙醇反应产物
write_page(
    "methacrylic-acid-multi-monomer-dimethylaminoethanol-polymer.md",
    "甲基丙烯酸与多种单体的聚合物与二甲氨基乙醇反应产物",
    "Reaction product of methacrylic acid multi-monomer polymer with dimethylaminoethanol",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用水性涂料成膜物（新品种）",
    "食品接触用涂料及涂层"
)

# 16. 1,3-苯二甲酸与1,4-苯二甲酸、1,4-丁二醇、癸二酸和乙二醇的聚合物
write_page(
    "isophthalic-terephthalic-butanediol-sebacic-ethylene-glycol-polymer.md",
    "1,3-苯二甲酸与1,4-苯二甲酸、1,4-丁二醇、癸二酸和乙二醇的聚合物",
    "Polymer of isophthalic acid, terephthalic acid, 1,4-butanediol, sebacic acid and ethylene glycol",
    N2020_6, D2020_6, NN2020_6,
    "食品接触材料及制品用涂料树脂（新品种）",
    "食品接触用涂料及涂层",
    "\n## 国际参考\n- 美国食品药品管理局（FDA）：允许用于食品接触用涂料\n- 欧盟委员会（EU）：允许用于食品接触用涂料\n"
)

# ============================================================
# 2020年第8号 (both already exist: polyethylene-pom and acrylic-acid-butadiene-styrene-copolymer)
# SKIPPED
# ============================================================

# ============================================================
# 2020年第9号 (7 items)
# ============================================================
N2020_9 = "2020年第9号"
D2020_9 = "2021-01-08"
NN2020_9 = "关于蝉花子实体（人工培植）等15种\"三新食品\"的公告"

write_page(
    "trimethylpropanamide-benzene-pp.md",
    "1,3,5-三(2,2-二甲基丙酰胺)苯",
    "1,3,5-Tris(2,2-dimethylpropanamide)benzene",
    N2020_9, D2020_9, NN2020_9,
    "食品接触材料及制品用添加剂（新品种，成核剂/澄清剂）",
    "聚丙烯（PP）塑料",
    "\n## 最大使用量\n按需使用\n"
)

write_page(
    "ci-pigment-red-101-pct.md",
    "C.I.颜料红101（氧化铁棕）",
    "C.I. Pigment Red 101 (Iron oxide brown)",
    N2020_9, D2020_9, NN2020_9,
    "食品接触材料及制品用着色剂（扩大使用范围）",
    "扩大至聚对苯二甲酸环己烷二甲醇酯（PCT）塑料",
    "\n## 最大使用量\n按需使用\n"
)

write_page(
    "magnesium-hydroxide-pom.md",
    "氢氧化镁",
    "Magnesium hydroxide",
    N2020_9, D2020_9, NN2020_9,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至聚甲醛（POM）塑料",
    "\n## 最大使用量\n按需使用\n"
)

write_page(
    "magnesium-carbonate-hydroxide-hydrate-pom.md",
    "水合铝酸碳酸镁",
    "Magnesium carbonate hydroxide hydrate with aluminum",
    N2020_9, D2020_9, NN2020_9,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至聚甲醛（POM）塑料",
    "\n## 最大使用量\n按需使用\n"
)

write_page(
    "polycyclooctene-evoh.md",
    "聚环辛烯",
    "Polycyclooctene",
    N2020_9, D2020_9, NN2020_9,
    "食品接触材料及制品用添加剂（扩大使用条件）",
    "乙烯-乙烯醇共聚物（EVOH）塑料（使用温度扩大至121℃）"
)

write_page(
    "isophthalic-dimethyl-terephthalate-neopentyl-glycol-ethylene-glycol-polymer.md",
    "1,3-苯二甲酸与1,4-苯二甲酸二甲酯、2,2-二甲基-1,3-丙二醇和1,2-乙二醇的聚合物",
    "Polymer of isophthalic acid, dimethyl terephthalate, neopentyl glycol and ethylene glycol",
    N2020_9, D2020_9, NN2020_9,
    "食品接触材料及制品用树脂（新品种，成膜物质）",
    "涂料及涂层"
)

write_page(
    "dimethyl-terephthalate-sebacic-acid-neopentyl-glycol-ethylene-glycol-polymer.md",
    "1,4-苯二甲酸二甲酯与癸二酸、2,2-二甲基-1,3-丙二醇和1,2-乙二醇的聚合物",
    "Polymer of dimethyl terephthalate, sebacic acid, neopentyl glycol and ethylene glycol",
    N2020_9, D2020_9, NN2020_9,
    "食品接触材料及制品用树脂（新品种，成膜物质）",
    "涂料及涂层"
)

# ============================================================
# 2021年第2号 (6 items)
# ============================================================
N2021_2 = "2021年第2号"
D2021_2 = "2021-02-20"
NN2021_2 = "关于α-淀粉酶等16种\"三新食品\"的公告"

write_page(
    "trimethylpropanamide-benzene-pp-2021.md",
    "1,3,5-三(2,2-二甲基丙酰胺)苯",
    "1,3,5-Tris(2,2-dimethylpropanamide)benzene",
    N2021_2, D2021_2, NN2021_2,
    "食品接触材料及制品用添加剂（新品种，成核剂）",
    "聚丙烯（PP）塑料"
)

write_page(
    "c11-15-isoalkanes-ink.md",
    "C11-15异烷烃",
    "C11-15 isoalkanes",
    N2021_2, D2021_2, NN2021_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至油墨（间接接触食品）"
)

write_page(
    "ci-pigment-blue-15-pct.md",
    "C.I.颜料蓝15",
    "C.I. Pigment Blue 15",
    N2021_2, D2021_2, NN2021_2,
    "食品接触材料及制品用着色剂（扩大使用范围）",
    "扩大至聚对苯二甲酸环己烷二甲醇酯（PCT）塑料"
)

write_page(
    "glass-fiber-ptfe-2021.md",
    "玻璃纤维",
    "Glass fiber",
    N2021_2, D2021_2, NN2021_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至聚四氟乙烯（PTFE）塑料（取消使用条件限制）"
)

write_page(
    "talc-adhesive-2021.md",
    "滑石粉",
    "Talc",
    N2021_2, D2021_2, NN2021_2,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至粘合剂"
)

write_page(
    "methacrylic-acid-butoxymethyl-acrylamide-styrene-ethyl-acrylate-polymer.md",
    "2-甲基-2-丙烯酸与N-(丁氧甲基)-2-丙烯酰胺、苯乙烯和2-丙烯酸乙酯的聚合物",
    "Polymer of methacrylic acid, N-(butoxymethyl)-2-acrylamide, styrene and ethyl acrylate",
    N2021_2, D2021_2, NN2021_2,
    "食品接触材料及制品用基础树脂（新品种）",
    "涂料及涂层"
)

# ============================================================
# 2021年第9号 (5 items)
# ============================================================
N2021_9 = "2021年第9号"
D2021_9 = "2021-10-22"
NN2021_9 = "关于食叶草等15种\"三新食品\"的公告"

write_page(
    "dimethyl-diallyl-ammonium-chloride-acrylamide-copolymer-paper.md",
    "N,N-二甲基-N-2-丙烯基-2-丙烯-1-氯化胺(1:1)与2-丙烯酰胺脱羧基盐酸盐的共聚物",
    "Copolymer of N,N-dimethyl-N-2-propenyl-2-propen-1-aminium chloride and 2-acrylamide decarboxylate hydrochloride",
    N2021_9, D2021_9, NN2021_9,
    "食品接触材料及制品用添加剂（新品种）",
    "纸和纸板"
)

write_page(
    "trimethyl-dihydroquinoline-polymer-rubber.md",
    "2,2,4-三甲基-1,2-二氢化喹啉聚合物",
    "2,2,4-Trimethyl-1,2-dihydroquinoline polymer",
    N2021_9, D2021_9, NN2021_9,
    "食品接触材料及制品用添加剂（扩大使用范围）",
    "扩大至橡胶材料及制品"
)

write_page(
    "isophthalic-terephthalic-tmcb-chdm-methylpropanediol-polymer.md",
    "1,4-苯二甲酸与1,3-苯二甲酸、2,2,4,4-四甲基-1,3-环丁二醇、1,4-环己烷二甲醇和2-甲基-1,3-丙二醇的聚合物",
    "Polymer of terephthalic acid, isophthalic acid, 2,2,4,4-tetramethyl-1,3-cyclobutanediol, 1,4-cyclohexanedimethanol and 2-methyl-1,3-propanediol",
    N2021_9, D2021_9, NN2021_9,
    "食品接触材料及制品用树脂（新品种，成膜物质）",
    "涂料及涂层"
)

write_page(
    "methacrylic-acid-methyl-methacrylate-acrylic-acid-polymer-coating.md",
    "2-甲基-2-丙烯酸与2-甲基-2-丙烯酸甲酯和2-丙烯酸的聚合物",
    "Polymer of methacrylic acid, methyl methacrylate and acrylic acid",
    N2021_9, D2021_9, NN2021_9,
    "食品接触材料及制品用树脂（新品种，成膜物质）",
    "涂料及涂层"
)

write_page(
    "isophthalic-terephthalic-tmcb-chdm-polymer.md",
    "1,4-苯二甲酸与1,3-苯二甲酸、2,2,4,4-四甲基-1,3-环丁二醇和1,4-环己烷二甲醇的聚合物",
    "Polymer of terephthalic acid, isophthalic acid, 2,2,4,4-tetramethyl-1,3-cyclobutanediol and 1,4-cyclohexanedimethanol",
    N2021_9, D2021_9, NN2021_9,
    "食品接触材料及制品用树脂（新品种）",
    "涂料及涂层"
)

print("\n=== DONE: All 2019-2021 entity pages created! ===")
