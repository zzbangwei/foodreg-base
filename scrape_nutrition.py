#!/usr/bin/env python3
"""Process GB 14880 nutrition fortifier data and generate entity pages."""

import json
import os
import re
from collections import defaultdict

# Raw data extracted from browser console (115 entries including 1 header row)
raw_data = [
    {"name": "营养强化剂", "source": "化合物来源", "scope": "应用范围", "remark": "备注"},  # header
    {"name": "酵母β-葡聚糖", "source": "酵母β-葡聚糖", "scope": "允许用于普通食品", "remark": "该营养强化剂由《关于批准紫甘薯色素等9种食品添加剂的公告》增补。"},
    {"name": "3'-唾液酸乳糖钠盐", "source": "3'-唾液酸乳糖钠盐", "scope": "允许用于特殊膳食用食品", "remark": "由栀子油等22种"三新食品"的公告（2026年 第1号）增补"},
    {"name": "3'-唾液酸乳糖钠盐", "source": "3'-唾液酸乳糖钠盐", "scope": "允许用于普通食品", "remark": "由栀子油等22种"三新食品"的公告（2026年 第1号）增补"},
    {"name": "铬", "source": "硫酸铬、氯化铬", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "碘", "source": "碘酸钾、碘化钾、碘化钠", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "酪蛋白磷酸肽", "source": "酪蛋白磷酸肽", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "钠", "source": "碳酸氢钠、磷酸二氢钠、柠檬酸钠、氯化钠、磷酸氢二钠", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "酪蛋白钙肽", "source": "酪蛋白钙肽", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "酪蛋白磷酸肽", "source": "酪蛋白磷酸肽", "scope": "允许用于普通食品", "remark": ""},
    {"name": "乳铁蛋白", "source": "乳铁蛋白", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "乳铁蛋白", "source": "乳铁蛋白", "scope": "允许用于普通食品", "remark": ""},
    {"name": "二十二碳六烯酸（DHA）", "source": "二十二碳六烯酸油脂，来源：裂壶藻（Schizochytrium sp）、吾肯氏壶藻（Ulkenia amoeboida）、寇氏隐甲藻（Crypthecodinium cohnii）；金枪鱼油（Tuna oil）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "二十二碳六烯酸（DHA）", "source": "二十二碳六烯酸油脂，来源：裂壶藻（Schizochytrium sp）、吾肯氏壶藻（Ulkenia amoeboida）、寇氏隐甲藻（Crypthecodinium cohnii）；金枪鱼油（Tuna oil）", "scope": "允许用于普通食品", "remark": ""},
    {"name": "花生四烯酸（AA 或 ARA）", "source": "花生四烯酸油脂，来源：高山被孢霉（Mortierella alpina）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "1,3-二油酸 2-棕榈酸甘油三酯", "source": "1,3-二油酸 2-棕榈酸甘油三酯", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "花生四烯酸（AA 或 ARA）", "source": "花生四烯酸油脂，来源：高山被孢霉（Mortierella alpina）", "scope": "允许用于普通食品", "remark": ""},
    {"name": "1,3-二油酸 2-棕榈酸甘油三酯", "source": "1,3-二油酸 2-棕榈酸甘油三酯", "scope": "允许用于普通食品", "remark": ""},
    {"name": "低聚果糖", "source": "低聚果糖（菊苣来源）、低聚果糖（蔗糖来源，经来源于米曲霉的β-果糖基转移酶作用制得）、低聚果糖（白砂糖来源）、低聚果糖（蔗糖来源，经来源于日本曲霉的β-果糖基转移酶作用制得）", "scope": "允许用于普通食品", "remark": "化合物来源低聚果糖（蔗糖来源，经来源于米曲霉的β-果糖基转移酶作用制得），由关于批准紫甘薯色素等9种食品添加剂的公告（2012年 第6号）增补；\n化合物来源低聚果糖（白砂糖来源），由关于批准聚偏磷酸钾作为食品添加剂新品种等的公告（2013年 第8号）增补；\n化合物来源低聚果糖（蔗糖来源，经来源于日本曲霉的β-果糖基转移酶作用制得），由关于甜叶菊多酚等20种"三新食品"的公告（2025年第1号）增补"},
    {"name": "叶黄素", "source": "叶黄素（万寿菊来源）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "γ-亚麻酸", "source": "γ-亚麻酸", "scope": "允许用于普通食品", "remark": ""},
    {"name": "叶黄素", "source": "叶黄素（万寿菊来源）", "scope": "允许用于普通食品", "remark": ""},
    {"name": "左旋肉碱（L-肉碱）", "source": "左旋肉碱（L-肉碱）、左旋肉碱酒石酸盐（L-肉碱酒石酸盐）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "磷", "source": "磷酸三钙（磷酸钙）、磷酸氢钙", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "鸟氨酸", "source": "L-盐酸鸟氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "铜", "source": "硫酸铜、葡萄糖酸铜、柠檬酸铜、碳酸铜", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "瓜氨酸", "source": "L-瓜氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "锰", "source": "硫酸锰、氯化锰、碳酸锰、柠檬酸锰、葡萄糖酸锰", "scope": "允许用于普通食品", "remark": ""},
    {"name": "色氨酸", "source": "L-色氨酸（非动物源性）", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "锰", "source": "硫酸锰、氯化锰、碳酸锰、柠檬酸锰、葡萄糖酸锰", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "组氨酸", "source": "L-组氨酸、L-盐酸组氨酸一水物", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "钾", "source": "葡萄糖酸钾、柠檬酸钾、磷酸二氢钾、磷酸氢二钾、氯化钾", "scope": "允许用于普通食品", "remark": ""},
    {"name": "钾", "source": "葡萄糖酸钾、柠檬酸钾、磷酸二氢钾、磷酸氢二钾、氯化钾", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "精氨酸", "source": "L-精氨酸、L-盐酸精氨酸、L-精氨酸-天冬氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "镁", "source": "硫酸镁、氯化镁、氧化镁、碳酸镁、磷酸氢镁、葡萄糖酸镁、乳酸镁", "scope": "允许用于特殊膳食用食品", "remark": "化合物来源乳酸镁，由关于桃胶等15种"三新食品"的公告（2023年第8号）增补"},
    {"name": "铜", "source": "硫酸铜、葡萄糖酸铜、柠檬酸铜、碳酸铜", "scope": "允许用于普通食品", "remark": ""},
    {"name": "镁", "source": "硫酸镁、氯化镁、氧化镁、碳酸镁、磷酸氢镁、葡萄糖酸镁、乳酸镁、L-苏糖酸镁", "scope": "允许用于普通食品", "remark": "化合物来源L-苏糖酸镁【仅限01.03.02调制乳粉（儿童用乳粉和孕产妇用乳粉除外）和14.0饮料类（14.01及14.06涉及品种除外）】，由关于海藻酸钙等食品添加剂新品种的公告（2016年第8号）增补；\n化合物来源乳酸镁，由关于桃胶等15种"三新食品"的公告（2023年第8号）增补。"},
    {"name": "硒", "source": "硒酸钠、亚硒酸钠、富硒酵母（仅限用于特殊医学用途配方食品（13.01中涉及品种除外））", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "硒", "source": "亚硒酸钠、硒酸钠、硒蛋白、富硒食用菌粉、L-硒-甲基硒代半胱氨酸（包括以N-乙酰基-3-氯-L-丝氨酸甲酯和甲硒醇钠为原料制得的食品营养强化剂L-硒-甲基硒代半胱氨酸）、硒化卡拉胶、富硒酵母", "scope": "允许用于普通食品", "remark": "化合物来源L-硒-甲基硒代半胱氨酸（以N-乙酰基-3-氯-L-丝氨酸甲酯和甲硒醇钠为原料)，由关于蓝莓花色苷等14种"三新食品"的公告(2023年第3号)增补"},
    {"name": "锌", "source": "硫酸锌、葡萄糖酸锌、甘氨酸锌、氧化锌、乳酸锌、柠檬酸锌、氯化锌、乙酸锌、碳酸锌、柠檬酸锌（三水）", "scope": "允许用于普通食品", "remark": "化合物来源柠檬酸锌(三水)，由关于批准酸式焦磷酸钙等3种食品添加剂新品种等的公告（2013年 第5号）增补"},
    {"name": "锌", "source": "硫酸锌、葡萄糖酸锌、氧化锌、乳酸锌、柠檬酸锌、氯化锌、乙酸锌", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "赖氨酸", "source": "L-盐酸赖氨酸、L-赖氨酸醋酸盐、L-赖氨酸、L-赖氨酸-L-谷氨酸二水物、L-赖氨酸-天冬氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "钙", "source": "碳酸钙、葡萄糖酸钙、柠檬酸钙、L-乳酸钙、磷酸氢钙、氯化钙、磷酸三钙（磷酸钙）、甘油磷酸钙、氧化钙、硫酸钙", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "苯丙氨酸", "source": "L-苯丙氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "钙", "source": "碳酸钙（包括海藻来源）、葡萄糖酸钙、柠檬酸钙、乳酸钙、L-乳酸钙、磷酸氢钙、L-苏糖酸钙、甘氨酸钙、天门冬氨酸钙、柠檬酸苹果酸钙、醋酸钙（乙酸钙）、氯化钙、磷酸三钙（磷酸钙）、维生素E琥珀酸钙、甘油磷酸钙、氧化钙、硫酸钙、骨粉（超细鲜骨粉）、柠檬酸钙(三水)", "scope": "允许用于普通食品", "remark": "化合物来源柠檬酸钙(三水)，由关于批准焦磷酸一氢三钠等5种食品添加剂新品种的公告（2012年 第15号）增补\n碳酸钙（海藻来源）作为钙的化合物来源由关于威尼斯镰刀菌蛋白等14种"三新食品"的公告（2025年第7号）增补（2025年11月27日）"},
    {"name": "铁", "source": "硫酸亚铁、葡萄糖酸亚铁、柠檬酸铁铵、富马酸亚铁（延胡索酸亚铁）、柠檬酸铁、焦磷酸铁、乙二胺四乙酸铁钠（仅限用于辅食营养补充品）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "β-丙氨酸", "source": "β-丙氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由关于威尼斯镰刀菌蛋白等14种"三新食品"的公告（2025年 第7号）增补"},
    {"name": "酪氨酸", "source": "L-酪氨酸（非动物源性）", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "铁", "source": "硫酸亚铁、葡萄糖酸亚铁、柠檬酸铁铵、富马酸亚铁（延胡索酸亚铁）、柠檬酸铁、乳酸亚铁、氯化高铁血红素、焦磷酸铁、铁卟啉、甘氨酸亚铁、还原铁、乙二胺四乙酸铁钠、羰基铁粉、碳酸亚铁、柠檬酸亚铁、琥珀酸亚铁、血红素铁、电解铁、柠檬酸亚铁钠", "scope": "允许用于普通食品", "remark": "化合物来源柠檬酸亚铁钠，由关于(±)-1-环己基乙醇等食品添加剂新品种的公告（2018年 第8号）增补"},
    {"name": "肌醇", "source": "肌醇（环己六醇）。原料：植酸钙镁、植酸钾", "scope": "允许用于普通食品", "remark": "肌醇（环己六醇）（原料为植酸钾），由关于莱茵衣藻等36种"三新食品"的公告（2022年第2号）增补"},
    {"name": "生物素", "source": "D-生物素", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "异亮氨酸", "source": "L-异亮氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "泛酸", "source": "D-泛酸钙、D-泛酸钠", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "生物素", "source": "D-生物素", "scope": "允许用于普通食品", "remark": ""},
    {"name": "泛酸", "source": "D-泛酸钙、D-泛酸钠", "scope": "允许用于普通食品", "remark": ""},
    {"name": "叶酸", "source": "叶酸（蝶酰谷氨酸）、6S-5-甲基四氢叶酸钙（仅限特殊医学用途配方食品(13.01中涉及品种除外)，除13.01~13.04外的其他特殊膳食用食品）、（6S）-5-甲基四氢叶酸，氨基葡萄糖盐（仅限除13.01~13.04外的其他特殊膳食用食品（仅限孕妇及乳母营养补充食品、运动营养食品））", "scope": "允许用于特殊膳食用食品", "remark": "化合物来源6S-5-甲基四氢叶酸钙，由关于蛋白质谷氨酰胺酶等21种"三新食品"的公告（2020年第6号）和关于α-淀粉酶等16种"三新食品"的公告（2021年第2号）增补\n化合物来源（6S）-5-甲基四氢叶酸，氨基葡萄糖盐，由关于金花茶培养物等11种"三新食品"的公告（2024年第6号）和关于威尼斯镰刀菌蛋白等14种"三新食品"的公告（2025年第7号）增补\n化合物来源6S-5-甲基四氢叶酸钙【仅限除13.01~13.04外的其他特殊膳食用食品（仅限辅食营养补充品）】由关于牡丹籽油等16种"三新食品"的公告（2026年第5号）增补"},
    {"name": "叶酸", "source": "叶酸（蝶酰谷氨酸）、（6S）-5-甲基四氢叶酸，氨基葡萄糖盐、6S-5-甲基四氢叶酸钙", "scope": "允许用于普通食品", "remark": "化合物来源（6S）-5-甲基四氢叶酸，氨基葡萄糖盐，由关于爱德万甜等6种食品添加剂新品种、食品添加剂环己基氨基磺酸钠 （又名甜蜜素）等6种食品添加剂扩大用量和使用范围的公告（2017年第8号）增补；\n化合物来源6S-5-甲基四氢叶酸钙，由关于食品营养强化剂新品种6S-5-甲基四氢叶酸钙以及氮气等8种扩大使用范围的食品添加剂的公告（2017年第13号）增补。"},
    {"name": "烟酸（尼克酸）", "source": "烟酸、烟酰胺", "scope": "允许用于普通食品", "remark": ""},
    {"name": "亮氨酸", "source": "L-亮氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "维生素 C", "source": "L-抗坏血酸、L-抗坏血酸钠、L-抗坏血酸钙、L-抗坏血酸钾、抗坏血酸-6-棕榈酸盐（抗坏血酸棕榈酸酯）、抗坏血酸棕榈酸酯（酶法）", "scope": "允许用于特殊膳食用食品", "remark": "化合物来源抗坏血酸棕榈酸酯（酶法），由关于蓝莓花色苷等14种"三新食品"的公告(2023年第3号)增补。"},
    {"name": "维生素 C", "source": "L-抗坏血酸、L-抗坏血酸钙、维生素C磷酸酯镁、L-抗坏血酸钠、L-抗坏血酸钾、L-抗坏血酸-6-棕榈酸盐（抗坏血酸棕榈酸酯）、抗坏血酸棕榈酸酯（酶法）", "scope": "允许用于普通食品", "remark": "化合物来源抗坏血酸棕榈酸酯（酶法），由关于蓝莓花色苷等14种"三新食品"的公告(2023年第3号)增补。"},
    {"name": "维生素 B12", "source": "氰钴胺、盐酸氰钴胺、羟钴胺", "scope": "允许用于普通食品", "remark": ""},
    {"name": "蛋氨酸", "source": "L-蛋氨酸（非动物源性）、N-乙酰基-L-甲硫氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "维生素 B6", "source": "盐酸吡哆醇、5'-磷酸吡哆醛", "scope": "允许用于普通食品", "remark": ""},
    {"name": "维生素 B2", "source": "核黄素、核黄素-5'-磷酸钠", "scope": "允许用于普通食品", "remark": ""},
    {"name": "缬氨酸", "source": "L-缬氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "维生素 B2", "source": "核黄素、核黄素-5'-磷酸钠", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "维生素 B1", "source": "盐酸硫胺素、硝酸硫胺素", "scope": "允许用于普通食品", "remark": ""},
    {"name": "维生素 K", "source": "植物甲萘醌", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "维生素 K", "source": "植物甲萘醌、维生素K2（发酵法）、维生素K2（合成法，以维生素K3、法尼醇和香叶醇为原料）、维生素K2（合成法，以七烯萜醇、维生素 K3 为主要原料）", "scope": "允许用于普通食品", "remark": "化合物来源维生素K2（发酵法），由关于海藻酸钙等食品添加剂新品种的公告（2016年第8号）增补；\n化合物来源维生素K2（合成法，以维生素K3、法尼醇和香叶醇为原料），由关于葡糖淀粉酶等28种"三新食品"的公告（2019年第6号）增补。\n化合物来源维生素K2（合成法，以七烯萜醇、维生素 K3 为主要原料），由关于蝉花子实体（人工培植）等15种"三新食品"的公告（2020年第9号）增补。"},
    {"name": "维生素 E", "source": "d-α-生育酚、dl-α-生育酚、d-α-醋酸生育酚、dl-α-醋酸生育酚、混合生育酚浓缩物、d-α-琥珀酸生育酚、dl-α-琥珀酸生育酚", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "半胱氨酸", "source": "L-胱氨酸、L-半胱氨酸、L-半胱氨酸盐酸盐一水物、L-半胱氨酸盐酸盐", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "维生素 D", "source": "麦角钙化醇（维生素 D2）、胆钙化醇（维生素 D3）", "scope": "允许用于普通食品", "remark": ""},
    {"name": "胱氨酸", "source": "L-胱氨酸、L-半胱氨酸、L-半胱氨酸盐酸盐一水物、N-乙酰基-L-半胱氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "β-胡萝卜素", "source": "β-胡萝卜素", "scope": "允许用于普通食品", "remark": ""},
    {"name": "维生素 A", "source": "醋酸视黄酯（醋酸维生素 A）、棕榈酸视黄酯（棕榈酸维生素 A）、β-胡萝卜素 、全反式视黄醇", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "丙氨酸", "source": "L-丙氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "钼", "source": "钼酸钠、钼酸铵", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "脯氨酸", "source": "L-脯氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "甘氨酸", "source": "甘氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "酪蛋白钙肽", "source": "酪蛋白钙肽", "scope": "允许用于普通食品", "remark": ""},
    {"name": "左旋肉碱（L-肉碱）", "source": "左旋肉碱（L-肉碱）、左旋肉碱酒石酸盐（L-肉碱酒石酸盐）", "scope": "允许用于普通食品", "remark": ""},
    {"name": "牛磺酸", "source": "牛磺酸（氨基乙基磺酸）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "谷氨酰胺", "source": "L-谷氨酰胺", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "牛磺酸", "source": "牛磺酸（氨基乙基磺酸）", "scope": "允许用于普通食品", "remark": ""},
    {"name": "谷氨酸", "source": "L-谷氨酸、L-谷氨酸钾一水物、L-谷氨酸钙四水物", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "L-赖氨酸", "source": "L-盐酸赖氨酸、L-赖氨酸天门冬氨酸盐", "scope": "允许用于普通食品", "remark": ""},
    {"name": "磷", "source": "磷酸三钙（磷酸钙）、磷酸氢钙", "scope": "允许用于普通食品", "remark": ""},
    {"name": "丝氨酸", "source": "L-丝氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "肌醇", "source": "肌醇（环己六醇）。原料：植酸钙镁、植酸钾", "scope": "允许用于特殊膳食用食品", "remark": "肌醇（环己六醇）（原料为植酸钾），由关于莱茵衣藻等36种"三新食品"的公告（2022年第2号）增补"},
    {"name": "胆碱", "source": "氯化胆碱、酒石酸氢胆碱", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "苏氨酸", "source": "L-苏氨酸", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
    {"name": "胆碱", "source": "氯化胆碱、酒石酸氢胆碱", "scope": "允许用于普通食品", "remark": ""},
    {"name": "烟酸（尼克酸）", "source": "烟酸、烟酰胺", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "维生素 B12", "source": "氰钴胺、盐酸氰钴胺、羟钴胺", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "维生素 B6", "source": "盐酸吡哆醇、5'-磷酸吡哆醛", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "维生素 B1", "source": "盐酸硫胺素、硝酸硫胺素", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "维生素 E", "source": "d-α-生育酚、dl-α-生育酚、d-α-醋酸生育酚、dl-α-醋酸生育酚、混合生育酚浓缩物、维生素E琥珀酸钙、d-α-琥珀酸生育酚、dl-α-琥珀酸生育酚", "scope": "允许用于普通食品", "remark": ""},
    {"name": "维生素 A", "source": "醋酸视黄酯（醋酸维生素 A）、棕榈酸视黄酯（棕榈酸维生素 A）、全反式视黄醇、β-胡萝卜素", "scope": "允许用于普通食品", "remark": ""},
    {"name": "维生素 D", "source": "麦角钙化醇（维生素 D2）、胆钙化醇（维生素 D3）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "酵母β-葡聚糖", "source": "", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "低聚半乳糖", "source": "低聚半乳糖（乳糖来源）、低聚半乳糖（乳清滤出液来源）", "scope": "允许用于特殊膳食用食品", "remark": "化合物来源低聚半乳糖（乳糖来源）【经米曲霉(Aspergillus oryzae)生产的β-半乳糖苷酶制得】，由关于海藻酸钙等食品添加剂新品种的公告（2016年第8号）增补"},
    {"name": "低聚半乳糖", "source": "低聚半乳糖（乳清滤出液来源)", "scope": "允许用于普通食品", "remark": "化合物来源低聚半乳糖（乳清滤出液来源)，由关于爱德万甜等6种食品添加剂新品种、食品添加剂环己基氨基磺酸钠 （又名甜蜜素）等6种食品添加剂扩大用量和使用范围的公告（2017年第8号）增补"},
    {"name": "低聚果糖", "source": "低聚果糖（菊苣来源）、低聚果糖（蔗糖来源，经来源于米曲霉的β-果糖基转移酶作用制得）、低聚果糖（白砂糖来源）、低聚果糖（蔗糖来源，经来源于日本曲霉的β-果糖基转移酶作用制得）", "scope": "允许用于特殊膳食用食品", "remark": "化合物来源低聚果糖（蔗糖来源，经来源于米曲霉的β-果糖基转移酶作用制得），由关于批准紫甘薯色素等9种食品添加剂的公告（2012年 第6号）增补；\n化合物来源低聚果糖（白砂糖来源），由关于批准聚偏磷酸钾作为食品添加剂新品种等的公告（2013年 第8号）增补；\n化合物来源低聚果糖（蔗糖来源，经来源于日本曲霉的β-果糖基转移酶作用制得），由关于甜叶菊多酚等20种"三新食品"的公告（2025年第1号）增补"},
    {"name": "多聚果糖", "source": "多聚果糖（菊苣来源）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "棉子糖", "source": "棉子糖（甜菜来源）", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "聚葡萄糖", "source": "", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "核苷酸", "source": "5'单磷酸胞苷（5'-CMP）、5'单磷酸尿苷（5'-UMP）、5'单磷酸腺苷（5'-AMP）、5'-肌苷酸二钠、5'-鸟苷酸二钠、5'-尿苷酸二钠、5'-胞苷酸二钠", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "半乳甘露聚糖", "source": "", "scope": "允许用于特殊膳食用食品", "remark": ""},
    {"name": "2'-岩藻糖基乳糖", "source": "2'-岩藻糖基乳糖", "scope": "允许用于特殊膳食用食品", "remark": "2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 K-12 DH1 MDO，供体：螺杆菌；生产菌来源：大肠杆菌K-12 MG1655，供体：螺杆菌；生产菌来源：大肠杆菌BL21(DE3)，供体：奈瑟菌），由关于桃胶等15种"三新食品"的公告（2023年第8号）增补；\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 BL21(DE3)；供体：幽门螺杆菌），由关于石斛原球茎等23种"三新食品"的公告（2024年第2号）增补；\n2'-岩藻糖基乳糖（生产菌来源：生产菌来源：大肠杆菌 BL21 star（DE3），供体：大肠杆菌O126；生产菌来源：谷氨酸棒状杆菌 ATCC 13032，供体：滑动假土地杆菌），由关于阿拉伯木聚糖等8种"三新食品"的公告（2024年第3号）增补；\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 K-12 GI724；供体：普通拟杆菌），由关于拟微球藻油等12种"三新食品"的公告（2024年第5号）增补；\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 BL21(DE3)，供体：脆弱拟杆菌；生产菌来源：大肠杆菌 BL21(DE3)，供体：埃希氏菌），由关于金花茶培养物等11种"三新食品"的公告（2024年第6号）增补。\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 BL21(DE3)，供体：螺杆菌；生产菌来源：大肠杆菌 W，供体：螺杆菌，由关于甜叶菊多酚等20种"三新食品"的公告（2025年第1号）增补。"},
    {"name": "2'-岩藻糖基乳糖", "source": "2'-岩藻糖基乳糖", "scope": "允许用于普通食品", "remark": "2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 K-12 DH1 MDO，供体：螺杆菌；生产菌来源：大肠杆菌K-12 MG1655，供体：螺杆菌；生产菌来源：大肠杆菌BL21(DE3)，供体：奈瑟菌），由关于桃胶等15种"三新食品"的公告（2023年第8号）增补；\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 BL21(DE3)；供体：幽门螺杆菌），由关于石斛原球茎等23种"三新食品"的公告（2024年第2号）增补；\n2'-岩藻糖基乳糖（生产菌来源：生产菌来源：大肠杆菌 BL21 star（DE3），供体：大肠杆菌O126；生产菌来源：谷氨酸棒状杆菌 ATCC 13032，供体：滑动假土地杆菌），由关于阿拉伯木聚糖等8种"三新食品"的公告（2024年第3号）增补；\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 K-12 GI724；供体：普通拟杆菌），由关于拟微球藻油等12种"三新食品"的公告（2024年第5号）增补；\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 BL21(DE3)，供体：脆弱拟杆菌；生产菌来源：大肠杆菌 BL21(DE3)，供体：埃希氏菌），由关于金花茶培养物等11种"三新食品"的公告（2024年第6号）增补。\n2'-岩藻糖基乳糖（生产菌来源：大肠杆菌 BL21(DE3)，供体：螺杆菌；生产菌来源：大肠杆菌 W，供体：螺杆菌，由关于甜叶菊多酚等20种"三新食品"的公告（2025年第1号）增补。"},
    {"name": "乳糖-N-新四糖", "source": "乳糖-N-新四糖", "scope": "允许用于特殊膳食用食品", "remark": "乳糖-N-新四糖（生产菌来源：大肠杆菌K-12 DH1 MDO；供体：奈瑟菌和螺杆菌），由关于桃胶等15种"三新食品"的公告（2023年第8号）增补；\n乳糖-N-新四糖（生产菌来源：大肠杆菌 BL21 star（DE3）；供体：奈瑟菌和螺杆菌），由关于拟微球藻油等12种"三新食品"的公告（2024年第5号）增补。"},
    {"name": "乳糖-N-新四糖", "source": "乳糖-N-新四糖", "scope": "允许用于普通食品", "remark": "乳糖-N-新四糖（生产菌来源：大肠杆菌K-12 DH1 MDO；供体：奈瑟菌和螺杆菌），由关于桃胶等15种"三新食品"的公告（2023年第8号）增补；\n乳糖-N-新四糖（生产菌来源：大肠杆菌 BL21 star（DE3）；供体：奈瑟菌和螺杆菌），由关于拟微球藻油等12种"三新食品"的公告（2024年第5号）增补。"},
    {"name": "d-核糖", "source": "", "scope": "允许用于特殊膳食用食品", "remark": "由关于石斛原球茎等23种"三新食品"的公告（2024年第2号）增补"},
    {"name": "天冬氨酸", "source": "L-天冬氨酸、L-天冬氨酸镁", "scope": "允许用于特殊膳食用食品", "remark": "由国家卫生健康委员会 国家市场监督管理总局关于特殊膳食用食品中氨基酸管理的公告（2023年 第11号）增补"},
]

# Remove header
data = [d for d in raw_data if d['name'] != '营养强化剂']

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
    # Add source (only if not empty)
    if d['source'].strip():
        merged[name]['sources'].add(d['source'])
    # Add scope
    merged[name]['scopes'].add(d['scope'])
    # Add remark (only if not empty)
    if d['remark'].strip():
        merged[name]['remarks'].add(d['remark'])

# Classification
vitamins = ['维生素 A', '维生素 B1', '维生素 B2', '维生素 B6', '维生素 B12', '维生素 C',
            '维生素 D', '维生素 E', '维生素 K', '烟酸（尼克酸）', '泛酸', '叶酸',
            '生物素', '肌醇', '胆碱', 'β-胡萝卜素', '叶黄素', '左旋肉碱（L-肉碱）',
            'L-赖氨酸']

mineral_names = ['钙', '铁', '锌', '硒', '碘', '铜', '锰', '镁', '钾', '磷', '钠',
                 '铬', '钼']

amino_acid_names = ['赖氨酸', '蛋氨酸', '色氨酸', '苯丙氨酸', '缬氨酸', '亮氨酸',
                    '异亮氨酸', '苏氨酸', '组氨酸', '精氨酸', '谷氨酸', '谷氨酰胺',
                    '天冬氨酸', '甘氨酸', '丙氨酸', '脯氨酸', '丝氨酸', '半胱氨酸',
                    '胱氨酸', '酪氨酸', '牛磺酸', '鸟氨酸', '瓜氨酸', 'β-丙氨酸']

fatty_acid_names = ['二十二碳六烯酸（DHA）', '花生四烯酸（AA 或 ARA）', 'γ-亚麻酸',
                    '1,3-二油酸 2-棕榈酸甘油三酯']

nucleotide_names = ['核苷酸']

prebiotic_names = ['低聚果糖', '低聚半乳糖', '多聚果糖', '棉子糖', '聚葡萄糖',
                   '半乳甘露聚糖', '酵母β-葡聚糖', '2\'-岩藻糖基乳糖', '乳糖-N-新四糖']

other_names = ['酪蛋白磷酸肽', '酪蛋白钙肽', '乳铁蛋白', '3\'-唾液酸乳糖钠盐', 'd-核糖']

# Build categories
categories = {
    '维生素类': [],
    '矿物质类': [],
    '氨基酸类': [],
    '脂肪酸类': [],
    '核苷酸类': [],
    '益生元类': [],
    '其他类': [],
}

name_to_category = {}
for n in vitamins:
    name_to_category[n] = '维生素类'
for n in mineral_names:
    name_to_category[n] = '矿物质类'
for n in amino_acid_names:
    name_to_category[n] = '氨基酸类'
for n in fatty_acid_names:
    name_to_category[n] = '脂肪酸类'
for n in nucleotide_names:
    name_to_category[n] = '核苷酸类'
for n in prebiotic_names:
    name_to_category[n] = '益生元类'
for n in other_names:
    name_to_category[n] = '其他类'

def get_category(name):
    if name in name_to_category:
        return name_to_category[name]
    # Check prefix
    for cat_name in ['维生素', 'L-']:
        if name.startswith(cat_name):
            if cat_name == '维生素':
                return '维生素类'
    # Check if it's a mineral
    if len(name) <= 2:
        print(f"  WARNING: unknown short name: {name}")
    return '未分类'

# Assign categories
uncertain = []
for name, info in merged.items():
    cat = get_category(name)
    if cat == '未分类':
        uncertain.append(name)
        print(f"  UNCLASSIFIED: {name}")
    else:
        categories[cat].append(name)

# Also check special case: L-赖氨酸 vs 赖氨酸
# L-赖氨酸 is in vitamins, 赖氨酸 (special food only) is in amino acids

# Handle L-赖氨酸 specially - it's classified as vitamin for "普通食品" scope
# but '赖氨酸' (without L-) used in special foods is amino acid
# In the merged data, they should be separate entries since name is different

# Print summary
print(f"\nTotal unique nutrition fortifiers: {len(merged)}")
for cat, names in categories.items():
    print(f"  {cat}: {len(names)}")

print(f"\n  Uncertain: {len(uncertain)}")
for u in uncertain:
    print(f"    - {u}")

# Generate master list
BASE_DIR = '/home/ubuntu/wiki-foodreg/entities/nutrition-fortifiers'
os.makedirs(BASE_DIR, exist_ok=True)

# Master list content
lines = []
lines.append("# GB 14880-2012 食品营养强化剂使用标准 — 营养强化剂总清单")
lines.append("")
lines.append("## 数据来源")
lines.append("- **标准**: GB 14880-2012 食品安全国家标准 食品营养强化剂使用标准")
lines.append("- **网站**: https://14880.foodvip.net/index/supple/index")
lines.append("- **数据提取日期**: 2026-06-22")
lines.append("- **记录总数**: 114条原始记录，去重后{}种营养强化剂".format(len(merged)))
lines.append("")
lines.append("---")
lines.append("")

# Table of contents
lines.append("## 目录")
lines.append("")
for cat, names in categories.items():
    if names:
        lines.append(f"- [{cat}](#{cat.lower()})（{len(names)}种）")
lines.append("")

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
            # Truncate very long remarks
            if len(r) > 100:
                r_short = r[:100] + "..."
            else:
                r_short = r
            remark_strs.append(r_short.replace('\n', '；'))
        remark_str = "；".join(remark_strs) if remark_strs else "—"

        # Truncate source for table
        if len(sources_str) > 120:
            sources_str = sources_str[:120] + "..."

        lines.append(f"| {i} | {name} | {sources_str} | {scope_str} | {remark_str} |")
    lines.append("")

# Write master list
master_path = os.path.join(BASE_DIR, 'master-list.md')
with open(master_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f"\nWrote master list: {master_path}")

# Generate individual entity pages
entity_count = 0
for name, info in merged.items():
    # Clean filename
    safe_name = name.replace('/', '-').replace('\\', '-')
    entity_path = os.path.join(BASE_DIR, f'{safe_name}.md')

    # Build scopes
    scopes = []
    if '允许用于普通食品' in info['scopes']:
        scopes.append('允许用于普通食品')
    if '允许用于特殊膳食用食品' in info['scopes']:
        scopes.append('允许用于特殊膳食用食品')

    # Build sources
    sources = sorted(info['sources']) if info['sources'] else ["[待确认]"]

    # Build remarks
    remarks = sorted(info['remarks']) if info['remarks'] else ["—"]

    content = []
    content.append(f"# {name}")
    content.append("")
    content.append("## 基本信息")
    content.append("")
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

    with open(entity_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    entity_count += 1

print(f"Wrote {entity_count} entity pages to {BASE_DIR}/")

# Print uncertain items
if uncertain:
    print("\n=== ITEMS NEEDING CONFIRMATION ===")
    for u in uncertain:
        print(f"  - {u}")
