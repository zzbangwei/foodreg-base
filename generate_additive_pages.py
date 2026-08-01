#!/usr/bin/env python3
"""Generate entity pages for food additives batch 1."""

import os

OUTDIR = os.path.expanduser("~/wiki-foodreg/entities/additives")

# ============================================================
# Small molecule additives data (from sanxin-catalog-2023-4.md)
# ============================================================
# Format: (filename, chinese_name, english_name, function, gb_standard, announcement, year, extra)
SMALL_MOLECULES = [
    # 2009年第11号
    ("cassia-gum", "决明胶", "Cassia Gum", "增稠剂",
     "GB 31619", "2009年第11号", "2009",
     "GB 31619《食品安全国家标准 食品添加剂 决明胶》"),
    ("massoia-bark-oil", "香厚壳桂皮油", "Massoia Bark Oil", "食品用香料",
     "GB 29938", "2009年第11号", "2009",
     "GB 29938《食品安全国家标准 食品用香料通则》"),
    ("sodium-homoeriodictyol", "(-)-高圣草酚钠盐", "(-)-Homoeriodictyol Sodium Salt", "食品用香料",
     "GB 29938", "2009年第11号", "2009",
     "GB 29938《食品安全国家标准 食品用香料通则》"),
    ("enzymatically-treated-isoquercitrin", "酶处理异槲皮苷", "Enzymatically Treated Isoquercitrin", "抗氧化剂",
     "2009年第11号公告", "2009年第11号", "2009",
     "按照2009年第11号公告规定的质量规格执行"),
    ("grape-seed-extract", "葡萄籽提取物", "Grape Seed Extract", "抗氧化剂",
     "2009年第11号公告", "2009年第11号", "2009",
     "按照2009年第11号公告规定的质量规格执行"),
    # 2010年第4号
    ("sodium-fumarate", "富马酸一钠", "Monosodium Fumarate", "酸度调节剂",
     "GB 1886.88", "2010年第4号", "2010",
     "GB 1886.88《食品安全国家标准 食品添加剂 富马酸一钠》"),
    ("spearmint-extract", "留兰香提取物", "Spearmint Extract", "食品用香料",
     "GB 29938", "2010年第4号", "2010",
     "GB 29938《食品安全国家标准 食品用香料通则》"),
    # 2010年第23号
    ("lysozyme", "溶菌酶", "Lysozyme", "防腐剂",
     "GB 1886.257", "2010年第23号", "2010",
     "GB 1886.257《食品安全国家标准 食品添加剂 溶菌酶》"),
    ("sodium-dl-malate", "DL-苹果酸钠", "Sodium DL-Malate", "酸度调节剂",
     "GB 30608", "2010年第23号", "2010",
     "GB 30608《食品安全国家标准 食品添加剂 DL-苹果酸钠》"),
    ("aspartame-acesulfame", "天门冬酰苯丙氨酸甲酯乙酰磺胺酸", "Aspartame-Acesulfame Salt", "甜味剂",
     "GB 1886.69", "2010年第23号", "2010",
     "GB 1886.69《食品安全国家标准 食品添加剂 天门冬酰苯丙氨酸甲酯乙酰磺胺酸》"),
    ("caramel-color-caustic-sulfite", "焦糖色（苛性硫酸盐法）", "Caramel Colour (Caustic Sulfite Process)", "着色剂",
     "GB 1886.64", "2010年第23号", "2010",
     "GB 1886.64《食品安全国家标准 食品添加剂 焦糖色》"),
    ("carbonyl-iron-powder", "羰基铁粉", "Carbonyl Iron Powder", "营养强化剂",
     "GB 29212", "2010年第23号", "2010",
     "GB 29212《食品安全国家标准 食品添加剂 羰基铁粉》"),
    ("l-tyrosine", "L-酪氨酸", "L-Tyrosine", "食品用香料",
     "2010年第23号公告", "2010年第23号", "2010",
     "按照2010年第23号公告规定的质量规格执行"),
    ("l-tryptophan", "L-色氨酸", "L-Tryptophan", "食品用香料",
     "2010年第23号公告", "2010年第23号", "2010",
     "按照2010年第23号公告规定的质量规格执行"),
    # 2012年第1号
    ("perlite", "珍珠岩", "Perlite", "助滤剂（加工助剂）",
     "GB 31634", "2012年第1号", "2012",
     "GB 31634《食品安全国家标准 食品添加剂 珍珠岩》"),
    # 2012年第6号
    ("purple-sweet-potato-color", "紫甘薯色素", "Purple Sweet Potato Colour", "着色剂",
     "GB 1886.244", "2012年第6号", "2012",
     "GB 1886.244《食品安全国家标准 食品添加剂 紫甘薯色素》"),
    ("monascus-yellow-pigment", "红曲黄色素", "Monascus Yellow Pigment", "着色剂",
     "GB 1886.66", "2012年第6号", "2012",
     "GB 1886.66《食品安全国家标准 食品添加剂 红曲黄色素》"),
    ("beta-apo-8-carotenal", "β-阿朴-8'-胡萝卜素醛", "β-Apo-8'-Carotenal", "着色剂",
     "GB 31620", "2012年第6号", "2012",
     "GB 31620《食品安全国家标准 食品添加剂 β-阿朴-8'-胡萝卜素醛》"),
    ("thaumatin", "索马甜", "Thaumatin", "甜味剂",
     "GB 1886.321", "2012年第6号", "2012",
     "GB 1886.321《食品安全国家标准 食品添加剂 索马甜》"),
    ("sodium-gluconate", "葡萄糖酸钠", "Sodium Gluconate", "酸度调节剂",
     "GB 1886.320", "2012年第6号", "2012",
     "GB 1886.320《食品安全国家标准 食品添加剂 葡萄糖酸钠》"),
    ("alpha-cyclodextrin", "α-环状糊精", "α-Cyclodextrin", "稳定剂、增稠剂",
     "GB 1886.351", "2012年第6号", "2012",
     "GB 1886.351《食品安全国家标准 食品添加剂 α-环状糊精》"),
    ("gamma-cyclodextrin", "γ-环状糊精", "γ-Cyclodextrin", "稳定剂、增稠剂",
     "GB 1886.353", "2012年第6号", "2012",
     "GB 1886.353《食品安全国家标准 食品添加剂 γ-环状糊精》"),
    ("beta-carotene-dunaliella-salina", "β-胡萝卜素（盐藻来源）", "β-Carotene (from Dunaliella salina)", "着色剂",
     "GB 1886.317", "2012年第6号", "2012",
     "GB 1886.317《食品安全国家标准 食品添加剂 β-胡萝卜素（盐藻来源）》"),
    ("lycopene-blakeslea-trispora", "番茄红素（三孢布拉霉来源）", "Lycopene (from Blakeslea trispora)", "着色剂",
     "2012年第6号公告", "2012年第6号", "2012",
     "按照2012年第6号公告规定的质量规格执行"),
    ("glutaraldehyde", "五碳双缩醛（戊二醛）", "Glutaraldehyde", "防腐剂",
     "GB 1886.349", "2012年第6号", "2012",
     "GB 1886.349《食品安全国家标准 食品添加剂 五碳双缩醛（戊二醛）》"),
    # 2012年第15号
    ("trisodium-diphosphate", "焦磷酸一氢三钠", "Trisodium Diphosphate", "水分保持剂、膨松剂、酸度调节剂",
     "GB 1886.348", "2012年第15号", "2012",
     "GB 1886.348《食品安全国家标准 食品添加剂 焦磷酸一氢三钠》"),
    ("nitrous-oxide", "氧化亚氮", "Nitrous Oxide", "推进剂",
     "GB 1886.350", "2012年第15号", "2012",
     "GB 1886.350《食品安全国家标准 食品添加剂 氧化亚氮》"),
    ("glucono-delta-lactone", "葡萄糖酸δ-内酯", "Glucono δ-Lactone", "稳定剂和凝固剂",
     "GB 7657", "2012年第15号", "2012",
     "GB 7657《食品安全国家标准 食品添加剂 葡萄糖酸δ-内酯》"),
    ("calcium-citrate-trihydrate", "柠檬酸钙（三水）", "Calcium Citrate Trihydrate", "营养强化剂",
     "2012年第15号公告", "2012年第15号", "2012",
     "按照2012年第15号公告规定的质量规格执行"),
    # 2013年第2号
    ("copper-chlorophyll", "叶绿素铜", "Copper Chlorophyll", "着色剂",
     "GB 1886.361", "2013年第2号", "2013",
     "GB 1886.361《食品安全国家标准 食品添加剂 叶绿素铜》"),
    # 2013年第5号
    ("calcium-acid-pyrophosphate", "酸式焦磷酸钙", "Calcium Acid Pyrophosphate", "膨松剂",
     "GB 1886.326", "2013年第5号", "2013",
     "GB 1886.326《食品安全国家标准 食品添加剂 酸式焦磷酸钙》"),
    # 2013年第8号
    ("potassium-polymetaphosphate", "聚偏磷酸钾", "Potassium Polymetaphosphate", "水分保持剂、乳化剂",
     "GB 1886.325", "2013年第8号", "2013",
     "GB 1886.325《食品安全国家标准 食品添加剂 聚偏磷酸钾》"),
    # 2014年第5号
    ("epsilon-polylysine", "ε-聚赖氨酸", "ε-Polylysine", "防腐剂",
     "GB 1886.362", "2014年第5号", "2014",
     "GB 1886.362《食品安全国家标准 食品添加剂 ε-聚赖氨酸》"),
    ("epsilon-polylysine-hydrochloride", "ε-聚赖氨酸盐酸盐", "ε-Polylysine Hydrochloride", "防腐剂",
     "2014年第5号公告", "2014年第5号", "2014",
     "按照2014年第5号公告规定的质量规格执行"),
    ("plant-activated-carbon-rice-husk", "植物活性炭（稻壳活性炭）", "Plant Activated Carbon (Rice Husk Carbon)", "着色剂",
     "GB 1886.363", "2014年第5号", "2014",
     "GB 1886.363《食品安全国家标准 食品添加剂 植物活性炭（稻壳活性炭）》"),
    # 2014年第11号
    ("tea-polyphenol-palmitate", "茶多酚棕榈酸酯", "Tea Polyphenol Palmitate", "抗氧化剂",
     "GB 1886.360", "2014年第11号", "2014",
     "GB 1886.360《食品安全国家标准 食品添加剂 茶多酚棕榈酸酯》"),
    # 2014年第17号
    ("tetrapotassium-diphosphate", "焦磷酸四钾", "Tetrapotassium Diphosphate", "水分保持剂、膨松剂、酸度调节剂",
     "GB 1886.340", "2014年第17号", "2014",
     "GB 1886.340《食品安全国家标准 食品添加剂 焦磷酸四钾》"),
    ("rosemary-extract-supercritical-co2", "迷迭香提取物（超临界CO₂）", "Rosemary Extract (Supercritical CO₂)", "抗氧化剂",
     "GB 1886.172", "2014年第17号", "2014",
     "GB 1886.172《食品安全国家标准 食品添加剂 迷迭香提取物》"),
    # 2016年第8号
    ("calcium-alginate", "海藻酸钙", "Calcium Alginate", "增稠剂、稳定剂",
     "GB 1886.308", "2016年第8号", "2016",
     "GB 1886.308《食品安全国家标准 食品添加剂 海藻酸钙》"),
    ("phosphoric-acid-wet-process", "磷酸（湿法）", "Phosphoric Acid (Wet Process)", "酸度调节剂",
     "GB 1886.304", "2016年第8号", "2016",
     "GB 1886.304《食品安全国家标准 食品添加剂 磷酸（湿法）》"),
    ("ferric-tartrate", "酒石酸铁", "Ferric Tartrate", "营养强化剂",
     "2016年第8号公告", "2016年第8号", "2016",
     "按照2016年第8号公告规定的质量规格执行"),
    ("magnesium-l-threonate", "L-苏糖酸镁", "Magnesium L-Threonate", "营养强化剂",
     "2016年第8号公告", "2016年第8号", "2016",
     "按照2016年第8号公告规定的质量规格执行"),
    ("galacto-oligosaccharides", "低聚半乳糖", "Galacto-Oligosaccharides (GOS)", "营养强化剂",
     "GB 1903.27", "2016年第8号", "2016",
     "GB 1903.27《食品安全国家标准 食品营养强化剂 低聚半乳糖》"),
    ("vitamin-k2-fermentation", "维生素K₂（发酵法）", "Vitamin K₂ (Fermentation)", "营养强化剂",
     "2016年第8号公告", "2016年第8号", "2016",
     "按照2016年第8号公告规定的质量规格执行"),
    # 2016年第9号
    ("ascorbyl-palmitate-enzymatic", "抗坏血酸棕榈酸酯（酶法）", "Ascorbyl Palmitate (Enzymatic)", "抗氧化剂",
     "2016年第9号公告", "2016年第9号", "2016",
     "按照2016年第9号公告规定的质量规格执行"),
    # 2017年第1号
    ("ammonium-carbonate", "碳酸铵", "Ammonium Carbonate", "膨松剂",
     "2017年第1号公告", "2017年第1号", "2017",
     "按照2017年第1号公告规定的质量规格执行"),
    # 2017年第8号
    ("advantame", "爱德万甜", "Advantame", "甜味剂",
     "2017年第8号公告", "2017年第8号", "2017",
     "按照2017年第8号公告规定的质量规格执行"),
    # 2017年第13号
    ("6s-5-methyltetrahydrofolate-calcium", "6S-5-甲基四氢叶酸钙", "6S-5-Methyltetrahydrofolate Calcium Salt", "营养强化剂",
     "2017年第13号公告", "2017年第13号", "2017",
     "按照2017年第13号公告规定的质量规格执行"),
]

# ============================================================
# Enzyme preparations data
# ============================================================
# Format: (filename, enzyme_name, english_name, source_strain, donor, announcement, year, usage)
ENZYMES = [
    # 2009年第11号
    ("phospholipase-c-p-pastoris", "磷脂酶C", "Phospholipase C",
     "巴斯德毕赤酵母 (*Pichia pastoris*)",
     "某一土壤样品中所衍生的磷脂酶C基因",
     "2009年第11号", "2009",
     "催化磷脂水解"),
    ("glutaminase-b-amyloliquefaciens", "谷氨酰胺酶", "Glutaminase",
     "解淀粉芽孢杆菌 (*Bacillus amyloliquefaciens*)",
     "—",
     "2009年第11号", "2009",
     "催化L-谷氨酰胺水解"),
    ("asparaginase-a-niger", "天门冬酰胺酶", "Asparaginase",
     "黑曲霉 (*Aspergillus niger*)",
     "黑曲霉 (*Aspergillus niger*)",
     "2009年第11号", "2009",
     "催化L-天冬酰胺水解"),
    ("asparaginase-a-oryzae", "天门冬酰胺酶", "Asparaginase",
     "米曲霉 (*Aspergillus oryzae*)",
     "米曲霉 (*Aspergillus oryzae*)",
     "2009年第11号", "2009",
     "催化L-天冬酰胺水解"),
    ("pectin-lyase-a-niger", "果胶裂解酶", "Pectin Lyase",
     "黑曲霉 (*Aspergillus niger*)",
     "黑曲霉 (*Aspergillus niger*)",
     "2009年第11号", "2009",
     "果蔬汁饮料、果酒、果泥、葡萄酒等，分解果胶"),
    ("pectin-esterase-a-oryzae", "果胶酯酶", "Pectin Esterase",
     "米曲霉 (*Aspergillus oryzae*)",
     "针尾曲霉 (*Aspergillus aculeatus*)",
     "2009年第11号", "2009",
     "催化果胶酯水解"),
    ("pullulanase-b-subtilis", "普鲁兰酶", "Pullulanase",
     "枯草芽孢杆菌 (*Bacillus subtilis*)",
     "嗜酸普鲁兰芽胞杆菌 (*Bacillus acidopullulyticus*)",
     "2009年第11号", "2009",
     "催化普鲁兰多糖水解"),
    # 2010年第4号
    ("nuclease-p-citrinum", "核酸酶", "Nuclease",
     "橘青霉 (*Penicillium citrinum*)",
     "—",
     "2010年第4号", "2010",
     "催化核酸水解"),
    ("deaminase-a-melleus", "脱氨酶", "Deaminase",
     "蜂蜜曲霉 (*Aspergillus melleus*)",
     "—",
     "2010年第4号", "2010",
     "催化脱氨反应"),
    ("protease-a-melleus", "蛋白酶", "Protease",
     "蜂蜜曲霉 (*Aspergillus melleus*)",
     "—",
     "2010年第4号", "2010",
     "催化蛋白水解"),
    # 2010年第23号
    ("glycerophospholipid-cholesterol-acyltransferase-b-licheniformis", "甘油磷脂胆固醇酰基转移酶", "Glycerophospholipid Cholesterol Acyltransferase",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "杀鲑气单胞菌杀鲑亚种 (*Aeromonas salmonicida* subsp. *salmonicida*)",
     "2010年第23号", "2010",
     "催化甘油磷脂与胆固醇酰基转移"),
    # 2012年第6号
    ("lipase-c-cylindracea", "脂肪酶", "Lipase",
     "柱晶假丝酵母 (*Candida cylindracea*)",
     "—",
     "2012年第6号", "2012",
     "催化脂类物质水解"),
    ("pullulanase-p-naganoensis", "普鲁兰酶", "Pullulanase",
     "长野解普鲁兰杆菌 (*Pullulanibacillus naganoensis*)",
     "—",
     "2012年第6号", "2012",
     "催化普鲁兰多糖水解"),
    # 2012年第15号
    ("lactase-k-lactis", "乳糖酶（β-半乳糖苷酶）", "Lactase (β-Galactosidase)",
     "乳克鲁维酵母 (*Kluyveromyces lactis*)",
     "—",
     "2012年第15号", "2012",
     "水解乳及乳制品中的乳糖"),
    ("dextranase-c-erraticum", "右旋糖酐酶", "Dextranase",
     "无定毛壳菌 (*Chaetomium erraticum*，又名细丽毛壳 *Chaetomium gracile*)",
     "—",
     "2012年第15号", "2012",
     "催化右旋糖酐水解"),
    ("protease-b-stearothermophilus", "蛋白酶", "Protease",
     "嗜热脂解芽孢杆菌 (*Bacillus stearothermophilus*)",
     "—",
     "2012年第15号", "2012",
     "催化蛋白水解"),
    # 2013年第2号
    ("lactase-p-pastoris", "乳糖酶（β-半乳糖苷酶）", "Lactase (β-Galactosidase)",
     "巴斯德毕赤酵母 (*Pichia pastoris*)",
     "米曲霉 (*Aspergillus oryzae*)",
     "2013年第2号", "2013",
     "水解乳及乳制品中的乳糖"),
    # 2015年第1号
    ("lactase-b-bifidum", "乳糖酶（β-半乳糖苷酶）", "Lactase (β-Galactosidase)",
     "两歧双歧杆菌 (*Bifidobacterium bifidum*)",
     "—",
     "2015年第1号", "2015",
     "水解乳及乳制品中的乳糖"),
    # 2017年第10号
    ("beta-glucanase-p-funiculosum", "β-葡聚糖酶", "β-Glucanase",
     "绳状青霉 (*Penicillium funiculosum*)",
     "—",
     "2017年第10号", "2017",
     "催化β-葡聚糖的水解"),
    # 2018年第2号
    ("fructosyltransferase-a-oryzae", "果糖基转移酶", "Fructosyltransferase",
     "米曲霉 (*Aspergillus oryzae*)",
     "—",
     "2018年第2号", "2018",
     "将蔗糖转化为低聚果糖"),
    # 2018年第8号
    ("chitosanase-b-subtilis", "壳聚糖酶", "Chitosanase",
     "枯草芽孢杆菌 (*Bacillus subtilis*)",
     "—",
     "2018年第8号", "2018",
     "催化壳聚糖水解"),
    ("lipase-m-circinelloides", "脂肪酶", "Lipase",
     "卷枝毛霉 (*Mucor circinelloides*，又名爪哇毛霉 *Mucor javanicus*)",
     "—",
     "2018年第8号", "2018",
     "催化脂类物质水解"),
    # 2019年第4号
    ("glucose-oxidase-p-chrysogenum", "葡糖氧化酶", "Glucose Oxidase",
     "产黄青霉 (*Penicillium chrysogenum*)",
     "—",
     "2019年第4号", "2019",
     "催化葡萄糖的氧化"),
    # 2019年第6号
    ("glucoamylase-t-reesei", "葡糖淀粉酶", "Glucoamylase",
     "李氏木霉 (*Trichoderma reesei*)",
     "李氏木霉 (*Trichoderma reesei*)",
     "2019年第6号", "2019",
     "催化淀粉水解"),
    # 2020年第4号 (new enzyme preparations - some already have pages)
    ("maltotetraohydrolase-b-licheniformis", "麦芽四糖水解酶", "Maltotetraohydrolase",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "施氏假单胞菌 (*Pseudomonas stutzeri*)",
     "2020年第4号", "2020",
     "烘焙食品等，延缓焙烤制品老化"),
    ("xylanase-t-reesei", "木聚糖酶", "Xylanase",
     "李氏木霉 (*Trichoderma reesei*)",
     "Talaromyces leycettanus",
     "2020年第4号", "2020",
     "谷物加工，分离谷物淀粉、谷物蛋白和谷物纤维"),
    ("alpha-glucosidase-t-reesei", "α-葡萄糖苷酶", "α-Glucosidase",
     "李氏木霉 (*Trichoderma reesei*)",
     "黑曲霉 (*Aspergillus niger*)",
     "2020年第4号", "2020",
     "谷物加工，将低聚麦芽糖转化为低聚异麦芽糖"),
    ("lactase-b-licheniformis", "乳糖酶（β-半乳糖苷酶）", "Lactase (β-Galactosidase)",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "两歧双歧杆菌 (*Bifidobacterium bifidum*)",
     "2020年第4号", "2020",
     "乳及乳制品加工，水解乳糖"),
    ("carboxypeptidase-a-niger", "羧肽酶", "Carboxypeptidase",
     "黑曲霉 (*Aspergillus niger*)",
     "黑曲霉 (*Aspergillus niger*)",
     "2020年第4号", "2020",
     "干酪和发酵肉制品加工，去除苦味和加速成熟"),
    ("lipase-a-niger", "脂肪酶", "Lipase",
     "黑曲霉 (*Aspergillus niger*)",
     "黄色镰刀菌 (*Fusarium culmorum*)",
     "2020年第4号", "2020",
     "烘焙食品等，增加生面团发酵稳定性"),
    ("alpha-amylase-t-reesei", "α-淀粉酶", "α-Amylase",
     "李氏木霉 (*Trichoderma reesei*)",
     "白曲霉 (*Aspergillus kawachii*)",
     "2020年第4号", "2020",
     "酒精发酵和谷物加工，提高酒精得率和淀粉液化速率"),
    ("protease-t-reesei", "蛋白酶", "Protease",
     "李氏木霉 (*Trichoderma reesei*)",
     "李氏木霉 (*Trichoderma reesei*)",
     "2020年第4号", "2020",
     "酒精发酵和谷物加工，提高果汁和淀粉得率"),
    ("glucose-isomerase-s-rubiginosus", "葡糖异构酶", "Glucose Isomerase",
     "锈棕色链霉菌 (*Streptomyces rubiginosus*)",
     "锈棕色链霉菌 (*Streptomyces rubiginosus*)",
     "2020年第4号", "2020",
     "生产高果糖玉米糖浆，提高果糖分子甜度"),
    ("lipase-h-polymorpha", "脂肪酶", "Lipase",
     "多形汉逊酵母 (*Hansenula polymorpha*)",
     "异孢镰刀菌 (*Fusarium heterosporum*)",
     "2020年第4号", "2020",
     "油脂加工"),
    # 2020年第9号
    ("beta-amylase-b-licheniformis", "β-淀粉酶", "β-Amylase",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "弯曲芽孢杆菌 (*Bacillus flexus*)",
     "2020年第9号", "2020",
     "催化淀粉水解"),
    # 2021年第2号
    ("alpha-amylase-b-licheniformis", "α-淀粉酶", "α-Amylase",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "嗜纤维菌 (*Cytophaga* sp.)",
     "2021年第2号", "2021",
     "催化淀粉水解"),
    ("protease-b-subtilis-aquaticus", "蛋白酶", "Protease",
     "枯草芽孢杆菌 (*Bacillus subtilis*)",
     "水生栖热菌 (*Thermus aquaticus*)",
     "2021年第2号", "2021",
     "催化蛋白水解"),
    ("lactase-b-subtilis", "乳糖酶（β-半乳糖苷酶）", "Lactase (β-Galactosidase)",
     "枯草芽孢杆菌 (*Bacillus subtilis*)",
     "两歧双歧杆菌 (*Bifidobacterium bifidum*)",
     "2021年第2号", "2021",
     "水解乳及乳制品中的乳糖"),
    # 2021年第5号
    ("protease-b-subtilis-amyloliquefaciens", "蛋白酶", "Protease",
     "枯草芽孢杆菌 (*Bacillus subtilis*)",
     "解淀粉芽孢杆菌 (*Bacillus amyloliquefaciens*)",
     "2021年第5号", "2021",
     "催化蛋白水解"),
    ("phosphoinositide-phospholipase-c-p-fluorescens", "磷酸肌醇磷脂酶C", "Phosphoinositide Phospholipase C",
     "荧光假单胞菌 (*Pseudomonas fluorescens*)",
     "从土壤中分离的编码磷酸肌醇磷脂酶C基因的微生物",
     "2021年第5号", "2021",
     "催化磷酸肌醇水解"),
    # 2021年第6号
    ("4-alpha-glycosyltransferase-a-pallidus", "4-α-糖基转移酶", "4-α-Glycosyltransferase",
     "苍白空气芽孢杆菌 (*Aeribacillus pallidus*)",
     "—",
     "2021年第6号", "2021",
     "催化α-1,4-糖苷键的转移"),
    ("alpha-amylase-a-niger", "α-淀粉酶", "α-Amylase",
     "黑曲霉 (*Aspergillus niger*)",
     "微小根毛霉 (*Rhizomucor pusillus*)",
     "2021年第6号", "2021",
     "催化淀粉水解"),
    ("polygalacturonase-t-reesei", "多聚半乳糖醛酸酶", "Polygalacturonase",
     "李氏木霉 (*Trichoderma reesei*)",
     "塔宾曲霉 (*Aspergillus tubingensis*)",
     "2021年第6号", "2021",
     "果汁加工，提高果汁得率和澄清果汁"),
    ("pectin-esterase-t-reesei", "果胶酯酶", "Pectin Esterase",
     "李氏木霉 (*Trichoderma reesei*)",
     "塔宾曲霉 (*Aspergillus tubingensis*)",
     "2021年第6号", "2021",
     "催化果胶酯水解"),
    ("phosphoinositide-phospholipase-c-b-licheniformis", "磷酸肌醇磷脂酶C", "Phosphoinositide Phospholipase C",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "假单胞菌 (*Pseudomonas* sp.)",
     "2021年第6号", "2021",
     "催化磷酸肌醇水解"),
    ("phospholipase-c-b-licheniformis", "磷脂酶C", "Phospholipase C",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "苏云金芽孢杆菌 (*Bacillus thuringiensis*)",
     "2021年第6号", "2021",
     "催化磷脂水解"),
    ("xylanase-t-reesei-thermopolyspora", "木聚糖酶", "Xylanase",
     "李氏木霉 (*Trichoderma reesei*)",
     "柔曲高温多孢菌 (*Thermopolyspora flexuosa*)",
     "2021年第6号", "2021",
     "催化木聚糖水解"),
    ("glucoamylase-a-niger", "葡糖淀粉酶", "Glucoamylase",
     "黑曲霉 (*Aspergillus niger*)",
     "密粘褶菌 (*Gloeophyllum trabeum*)",
     "2021年第6号", "2021",
     "催化淀粉水解"),
    ("lipase-t-reesei", "脂肪酶", "Lipase",
     "李氏木霉 (*Trichoderma reesei*)",
     "尖孢镰刀菌 (*Fusarium oxysporum*)",
     "2021年第6号", "2021",
     "催化脂类物质水解"),
    # 2021年第9号
    ("protease-a-caldiproteolyticus", "蛋白酶", "Protease",
     "热解蛋白无氧芽孢杆菌 (*Anoxybacillus caldiproteolyticus*)",
     "—",
     "2021年第9号", "2021",
     "水解蛋白"),
    ("glutaminase-b-licheniformis", "谷氨酰胺酶", "Glutaminase",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "地衣芽孢杆菌 (*Bacillus licheniformis*)",
     "2021年第9号", "2021",
     "催化L-谷氨酰胺水解"),
    ("xylanase-t-reesei-niger-tubingensis", "木聚糖酶", "Xylanase",
     "李氏木霉 (*Trichoderma reesei*)",
     "黑曲霉塔宾变种 (*Aspergillus niger* var. *tubingensis*)",
     "2021年第9号", "2021",
     "催化木聚糖水解"),
]


# ============================================================
# Functions to generate markdown content
# ============================================================

def small_molecule_page(data):
    filename, cn_name, en_name, func, gb_std, announcement, year, gb_detail = data

    has_gb_number = gb_std.startswith("GB ")
    gb_text = gb_std if has_gb_number else announcement
    gb_name = gb_detail

    content = f"""# {cn_name} ({en_name})

## 基本信息

| 项目 | 内容 |
|------|------|
| **中文名称** | {cn_name} |
| **英文名称** | {en_name} |
| **功能类别** | {func} |
| **首次批准** | {year}年（{announcement}） |
| **批准类型** | 食品添加剂新品种 |

## 使用范围与最大使用量

该物质作为食品添加剂，使用范围和最大使用量按照{announcement}的规定执行。

## 工艺必要性

该物质作为食品添加剂新品种，{announcement}批准其用于食品工业，以发挥{func}功能。

## 质量规格标准

| 项目 | 内容 |
|------|------|
| **质量规格标准号** | {gb_text} |
| **标准名称** | {gb_name} |
| **适用标准（三新目录）** | {gb_text} |

## 相关公告

- {announcement}

---

*来源：国家卫健委三新食品公告*
"""
    return content


def enzyme_page(data):
    filename, cn_name, en_name, source, donor, announcement, year, usage = data

    # Determine file path for reference
    if cn_name.startswith("乳糖酶"):
        enzyme_type = "乳糖酶（β-半乳糖苷酶）"
    elif cn_name.startswith("蛋白酶"):
        enzyme_type = "蛋白酶"
    elif cn_name.startswith("脂肪酶"):
        enzyme_type = "脂肪酶"
    elif cn_name.startswith("α-淀粉酶"):
        enzyme_type = "α-淀粉酶"
    elif cn_name.startswith("木聚糖酶"):
        enzyme_type = "木聚糖酶"
    elif cn_name.startswith("葡糖淀粉酶"):
        enzyme_type = "葡糖淀粉酶"
    elif cn_name.startswith("普鲁兰酶"):
        enzyme_type = "普鲁兰酶"
    elif cn_name.startswith("果胶酯酶"):
        enzyme_type = "果胶酯酶"
    elif cn_name.startswith("果胶裂解酶"):
        enzyme_type = "果胶裂解酶"
    elif cn_name.startswith("磷脂酶C"):
        enzyme_type = "磷脂酶C"
    elif cn_name.startswith("磷酸肌醇磷脂酶C"):
        enzyme_type = "磷酸肌醇磷脂酶C"
    elif cn_name.startswith("谷氨酰胺酶"):
        enzyme_type = "谷氨酰胺酶"
    elif cn_name.startswith("多聚半乳糖醛酸酶"):
        enzyme_type = "多聚半乳糖醛酸酶"
    elif cn_name.startswith("乳糖酶"):
        enzyme_type = "乳糖酶（β-半乳糖苷酶）"
    else:
        enzyme_type = cn_name

    content = f"""# {cn_name} ({en_name})

## 基本信息

| 项目 | 内容 |
|------|------|
| **中文名称** | {cn_name} |
| **英文名称** | {en_name} |
| **功能类别** | 食品工业用酶制剂 |
| **来源菌种** | {source} |
| **供体** | {donor} |
| **首次批准** | {year}年（{announcement}） |
| **批准类型** | 食品工业用酶制剂新品种 |

## 用途

{usage}。

## 化学信息

| 项目 | 内容 |
|------|------|
| **酶学分类** | 食品工业用酶制剂 |
| **性质** | 符合GB 1886.174《食品安全国家标准 食品添加剂 食品工业用酶制剂》规定 |

## 质量规格标准

| 项目 | 内容 |
|------|------|
| **质量规格标准号** | GB 1886.174 |
| **标准名称** | 《食品安全国家标准 食品添加剂 食品工业用酶制剂》 |
| **适用标准（三新目录）** | GB 1886.174 |

> {en_type}为食品工业用酶制剂，其质量规格执行《食品安全国家标准 食品添加剂 食品工业用酶制剂》（GB 1886.174）。该标准适用于所有食品工业用酶制剂新品种。

## 国际批准情况

- **美国FDA**：允许作为食品工业用酶制剂使用

## 相关公告

- {announcement}

---

*来源：国家卫健委三新食品公告*
"""
    return content


# ============================================================
# Main script
# ============================================================

def main():
    created = 0
    skipped = 0

    # Generate small molecule pages
    for data in SMALL_MOLECULES:
        filename = data[0]
        path = os.path.join(OUTDIR, f"{filename}.md")

        if os.path.exists(path):
            print(f"SKIP (exists): {filename}.md")
            skipped += 1
            continue

        content = small_molecule_page(data)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CREATED: {filename}.md")
        created += 1

    # Generate enzyme pages
    for data in ENZYMES:
        filename = data[0]
        path = os.path.join(OUTDIR, f"{filename}.md")

        if os.path.exists(path):
            print(f"SKIP (exists): {filename}.md")
            skipped += 1
            continue

        content = enzyme_page(data)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CREATED: {filename}.md")
        created += 1

    print(f"\n=== Summary ===")
    print(f"Created: {created}")
    print(f"Skipped: {skipped}")
    print(f"Total: {created + skipped}")


if __name__ == "__main__":
    main()
