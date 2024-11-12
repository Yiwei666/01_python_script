import math

# 定义所有原子的电负性值，使用字典表示，未提供电负性数据的元素值设为None
electronegativity_values = {
    "H": 2.20, "He": None, "Li": 0.98, "Be": 1.57, "B": 2.04, "C": 2.55,
    "N": 3.04, "O": 3.44, "F": 3.98, "Ne": None, "Na": 0.93, "Mg": 1.31,
    "Al": 1.61, "Si": 1.90, "P": 2.19, "S": 2.58, "Cl": 3.16, "Ar": None,
    "K": 0.82, "Ca": 1.00, "Sc": 1.36, "Ti": 1.54, "V": 1.63, "Cr": 1.66,
    "Mn": 1.55, "Fe": 1.83, "Co": 1.88, "Ni": 1.91, "Cu": 1.90, "Zn": 1.65,
    "Ga": 1.81, "Ge": 2.01, "As": 2.01, "Se": 2.55, "Br": 2.96, "Kr": None,
    "Rb": 0.82, "Sr": 0.95, "Y": 1.22, "Zr": 1.33, "Nb": 1.60, "Mo": 2.16,
    "Tc": 2.10, "Ru": 2.20, "Rh": 2.28, "Pd": 2.20, "Ag": 1.93, "Cd": 1.69,
    "In": 1.78, "Sn": 1.96, "Sb": 2.05, "Te": 2.10, "I": 2.66, "Xe": 2.60,
    "Cs": 0.79, "Ba": 0.89, "La": 1.10, "Ce": 1.12, "Pr": 1.13, "Nd": 1.14,
    "Pm": None, "Sm": 1.17, "Eu": None, "Gd": 1.20, "Tb": None, "Dy": 1.22,
    "Ho": 1.23, "Er": 1.24, "Tm": 1.25, "Yb": None, "Lu": 1.0, "Hf": 1.3,
    "Ta": 1.5, "W": 1.7, "Re": 1.9, "Os": 2.2, "Ir": 2.2, "Pt": 2.2,
    "Au": 2.4, "Hg": 1.9, "Tl": 1.8, "Pb": 1.8, "Bi": 1.9, "Po": 2.0,
    "At": 2.2, "Rn": None, "Fr": 0.7, "Ra": 0.9, "Ac": 1.1, "Th": 1.3,
    "Pa": 1.5, "U": 1.7, "Np": 1.3, "Pu": 1.3
}

def calculate_bond_properties():
    # 提示用户输入原子对
    pair_input = input("请输入两个原子符号，用英文逗号分隔（例如：H,O）：").strip()
    atom1, atom2 = pair_input.split(",")

    # 获取原子的电负性
    en1 = electronegativity_values.get(atom1)
    en2 = electronegativity_values.get(atom2)

    # 检查电负性值是否有效
    if en1 is None or en2 is None:
        print("输入的原子符号无效或缺少电负性数据，请重新输入。")
        return

    # 计算电负性差值，并保留小数点后2位
    en_difference = abs(en1 - en2)
    en_difference = round(en_difference, 2)

    # 打印原子符号和电负性
    print(f"{atom1} 的电负性: {en1}")
    print(f"{atom2} 的电负性: {en2}")
    print(f"电负性差值的绝对值: {en_difference}")

    # 根据经验公式计算离子性和共价性比例
    ionic_character_percentage = (1 - math.exp(-0.25 * (en_difference ** 2))) * 100
    covalent_character_percentage = 100 - ionic_character_percentage

    # 打印成键过程中的离子性和共价性比例
    print(f"离子性比例: {ionic_character_percentage:.2f}%")
    print(f"共价性比例: {covalent_character_percentage:.2f}%")

    # 根据离子性和共价性比例判断成键类型
    if ionic_character_percentage > 50:
        bond_type = "离子键"
    else:
        bond_type = "共价键"
    
    print(f"该原子对的成键类型: {bond_type}")

# 运行计算函数
calculate_bond_properties()
