# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:37:05 2022

@author: sun78
"""

pureDensityDict = {'H': ['0.0899', 'g/L', 'Hydrogen', 'H', '1', '氢', '气'], 'Li': ['0.534', 'g/cc', 'Lithium', 'Li', '3', '锂'], 'Be': ['1.848', 'g/cc', 'Beryllium', 'Be', '4', '铍'], 'B': ['2.34', 'g/cc', 'Boron', 'B', '5', '硼'], 'C': ['2.26', 'g/cc', 'Carbon', 'C', '6', '碳'], 'N': ['1.2506', 'g/L', 'Nitrogen', 'N', '7', '氮', '气'], 'O': ['1.429', 'g/L', 'Oxygen', 'O', '8', '氧', '气'], 'F': ['1.696', 'g/L', 'Fluorine', 'F', '9', '氟', '气'], 'Ne': ['0.9', 'g/L', 'Neon', 'Ne', '10', '氖', '气'], 'Na': ['0.971', 'g/cc', 'Sodium', 'Na', '11', '钠'], 'Mg': ['1.738', 'g/cc', 'Magnesium', 'Mg', '12', '镁'], 'Al': ['2.702', 'g/cc', 'Aluminum', 'Al', '13', '铝'], 'Si': ['2.33', 'g/cc', 'Silicon', 'Si', '14', '硅'], 'P': ['1.82', 'g/cc', 'Phosphorus', 'P', '15', '磷'], 'S': ['2.07', 'g/cc', 'Sulfur', 'S', '16', '硫'], 'Cl': ['3.214', 'g/L', 'Chlorine', 'Cl', '17', '氯', '气'], 'Ar': ['1.7824', 'g/L', 'Argon', 'Ar', '18', '氩', '气'], 'K': ['0.862', 'g/cc', 'Potassium', 'K', '19', '钾'], 'Ca': ['1.55', 'g/cc', 'Calcium', 'Ca', '20', '钙'], 'Sc': ['2.99', 'g/cc', 'Scandium', 'Sc', '21', '钪'], 'Ti': ['4.54', 'g/cc', 'Titanium', 'Ti', '22', '钛'], 'V': ['6.11', 'g/cc', 'Vanadium', 'V', '23', '钒'], 'Cr': ['7.19', 'g/cc', 'Chromium', 'Cr', '24', '铬'], 'Mn': ['7.43', 'g/cc', 'Manganese', 'Mn', '25', '锰'], 'Fe': ['7.874', 'g/cc', 'Iron', 'Fe', '26', '铁'], 'Co': ['8.9', 'g/cc', 'Cobalt', 'Co', '27', '钴'], 'Ni': ['8.9', 'g/cc', 'Nickel', 'Ni', '28', '镍'], 'Cu': ['8.96', 'g/cc', 'Copper', 'Cu', '29', '铜'], 'Zn': ['7.13', 'g/cc', 'Zinc', 'Zn', '30', '锌'], 'Ga': ['5.907', 'g/cc', 'Gallium', 'Ga', '31', '镓'], 'Ge': ['5.323', 'g/cc', 'Germanium', 'Ge', '32', '锗'], 'As': ['5.72', 'g/cc', 'Arsenic', 'As', '33', '砷'], 'Se': ['4.79', 'g/cc', 'Selenium', 'Se', '34', '硒'], 'Br': ['3.119', 'g/cc', 'Bromine', 'Br', '35', '溴'], 'Kr': ['3.75', 'g/L', 'Krypton', 'Kr', '36', '氪', '气'], 'Rb': ['1.63', 'g/cc', 'Rubidium', 'Rb', '37', '铷'], 'Sr': ['2.54', 'g/cc', 'Strontium', 'Sr', '38', '锶'], 'Y': ['4.47', 'g/cc', 'Yttrium', 'Y', '39', '钇'], 'Zr': ['6.51', 'g/cc', 'Zirconium', 'Zr', '40', '锆'], 'Nb': ['8.57', 'g/cc', 'Niobium', 'Nb', '41', '铌'], 'Mo': ['10.22', 'g/cc', 'Molybdenum', 'Mo', '42', '钼'], 'Tc': ['11.5', 'g/cc', 'Technetium', 'Tc', '43', '锝'], 'Ru': ['12.37', 'g/cc', 'Ruthenium', 'Ru', '44', '钌'], 'Rh': ['12.41', 'g/cc', 'Rhodium', 'Rh', '45', '铑'], 'Pd': ['12.02', 'g/cc', 'Palladium', 'Pd', '46', '钯'], 'Ag': ['10.5', 'g/cc', 'Silver', 'Ag', '47', '银'], 'Cd': ['8.65', 'g/cc', 'Cadmium', 'Cd', '48', '镉'], 'In': ['7.31', 'g/cc', 'Indium', 'In', '49', '铟'], 'Sn': ['7.31', 'g/cc', 'Tin', 'Sn', '50', '锡'], 'Sb': ['6.684', 'g/cc', 'Antimony', 'Sb', '51', '锑'], 'Te': ['6.24', 'g/cc', 'Tellurium', 'Te', '52', '碲'], 'I': ['4.93', 'g/cc', 'Iodine', 'I', '53', '碘'], 'Xe': ['5.9', 'g/L', 'Xenon', 'Xe', '54', '氙(xian)', '气'], 'Cs': ['1.873', 'g/cc', 'Cesium', 'Cs', '55', '铯'], 'Ba': ['3.59', 'g/cc', 'Barium', 'Ba', '56', '钡'], 'La': ['6.15', 'g/cc', 'Lanthanum', 'La', '57', '镧'], 'Ce': ['6.77', 'g/cc', 'Cerium', 'Ce', '58', '铈'], 'Pr': ['6.77', 'g/cc', 'Praseodymium', 'Pr', '59', '镨'], 'Nd': ['7.01', 'g/cc', 'Neodymium', 'Nd', '60', '钕'], 'Pm': ['7.3', 'g/cc', 'Promethium', 'Pm', '61', '钷'], 'Sm': ['7.52', 'g/cc', 'Samarium', 'Sm', '62', '钐'], 'Eu': ['5.24', 'g/cc', 'Europium', 'Eu', '63', '铕'], 'Gd': ['7.895', 'g/cc', 'Gadolinium', 'Gd', '64', '钆'], 'Tb': ['8.23', 'g/cc', 'Terbium', 'Tb', '65', '铽'], 'Dy': ['8.55', 'g/cc', 'Dysprosium', 'Dy', '66', '镝'], 'Ho': ['8.8', 'g/cc', 'Holmium', 'Ho', '67', '钬'], 'Er': ['9.07', 'g/cc', 'Erbium', 'Er', '68', '铒'], 'Tm': ['9.32', 'g/cc', 'Thulium', 'Tm', '69', '铥'], 'Yb': ['6.9', 'g/cc', 'Ytterbium', 'Yb', '70', '镱'], 'Lu': ['9.84', 'g/cc', 'Lutetium', 'Lu', '71', '镥'], 'Hf': ['13.31', 'g/cc', 'Hafnium', 'Hf', '72', '铪(ha)'], 'Ta': ['16.65', 'g/cc', 'Tantalum', 'Ta', '73', '钽'], 'W': ['19.35', 'g/cc', 'Tungsten', 'W', '74', '钨'], 'Re': ['21.04', 'g/cc', 'Rhenium', 'Re', '75', '铼'], 'Os': ['22.6', 'g/cc', 'Osmium', 'Os', '76', '锇(e)'], 'Ir': ['22.4', 'g/cc', 'Iridium', 'Ir', '77', '铱'], 'Pt': ['21.45', 'g/cc', 'Platinum', 'Pt', '78', '铂'], 'Au': ['19.32', 'g/cc', 'Gold', 'Au', '79', '金'], 'Hg': ['13.546', 'g/cc', 'Mercury', 'Hg', '80', '汞'], 'Tl': ['11.85', 'g/cc', 'Thallium', 'Tl', '81', '铊(ta)'], 'Pb': ['11.35', 'g/cc', 'Lead', 'Pb', '82', '铅'], 'Bi': ['9.75', 'g/cc', 'Bismuth', 'Bi', '83', '铋'], 'Po': ['9.3', 'g/cc', 'Polonium', 'Po', '84', '钋(po)'], 'Rn': ['9.73', 'g/L', 'Radon', 'Rn', '86', '氡(dong)', '气'], 'Ra': ['5.5', 'g/cc', 'Radium', 'Ra', '88', '镭'], 'Ac': ['10.07', 'g/cc', 'Actinium', 'Ac', '89', '锕'], 'Th': ['11.724', 'g/cc', 'Thorium', 'Th', '90', '钍(tu)'], 'Pa': ['15.4', 'g/cc', 'Protactinium', 'Pa', '91', '镤(pu)'], 'U': ['18.95', 'g/cc', 'Uranium', 'U', '92', '铀'], 'Np': ['20.2', 'g/cc', 'Neptunium', 'Np', '93', '镎(na)'], 'Pu': ['19.84', 'g/cc', 'Plutonium', 'Pu', '94', '钚(bu)'], 'Am': ['13.67', 'g/cc', 'Americium', 'Am', '95', '镅(mei)'], 'Cm': ['13.5', 'g/cc', 'Curium', 'Cm', '96', '锔(ju)'], 'Bk': ['14.78', 'g/cc', 'Berkelium', 'Bk', '97', '锫(pei)'], 'Cf': ['15.1', 'g/cc', 'Californium', 'Cf', '98', '锎(kai)']}
atomicMassDict = {'H': ['1', 'Hydrogen', 'H', '1.00794', '1', '1'], 'He': ['2', 'Helium', 'He', '4.002602', '18', '1'], 'Li': ['3', 'Lithium', 'Li', '6.941', '1', '2'], 'Be': ['4', 'Beryllium', 'Be', '9.012182', '2', '2'], 'B': ['5', 'Boron', 'B', '10.811', '13', '2'], 'C': ['6', 'Carbon', 'C', '12.0107', '14', '2'], 'N': ['7', 'Nitrogen', 'N', '14.0067', '15', '2'], 'O': ['8', 'Oxygen', 'O', '15.9994', '16', '2'], 'F': ['9', 'Fluorine', 'F', '18.9984032', '17', '2'], 'Ne': ['10', 'Neon', 'Ne', '20.1797', '18', '2'], 'Na': ['11', 'Sodium', 'Na', '22.98976928', '1', '3'], 'Mg': ['12', 'Magnesium', 'Mg', '24.3050', '2', '3'], 'Al': ['13', 'Aluminium', 'Al', '26.9815386', '13', '3'], 'Si': ['14', 'Silicon', 'Si', '28.0855', '14', '3'], 'P': ['15', 'Phosphorus', 'P', '30.973762', '15', '3'], 'S': ['16', 'Sulfur', 'S', '32.065', '16', '3'], 'Cl': ['17', 'Chlorine', 'Cl', '35.453', '17', '3'], 'Ar': ['18', 'Argon', 'Ar', '39.948', '18', '3'], 'K': ['19', 'Potassium', 'K', '39.0983', '1', '4'], 'Ca': ['20', 'Calcium', 'Ca', '40.078', '2', '4'], 'Sc': ['21', 'Scandium', 'Sc', '44.955912', '3', '4'], 'Ti': ['22', 'Titanium', 'Ti', '47.867', '4', '4'], 'V': ['23', 'Vanadium', 'V', '50.9415', '5', '4'], 'Cr': ['24', 'Chromium', 'Cr', '51.9961', '6', '4'], 'Mn': ['25', 'Manganese', 'Mn', '54.938045', '7', '4'], 'Fe': ['26', 'Iron', 'Fe', '55.845', '8', '4'], 'Co': ['27', 'Cobalt', 'Co', '58.933195', '9', '4'], 'Ni': ['28', 'Nickel', 'Ni', '58.6934', '10', '4'], 'Cu': ['29', 'Copper', 'Cu', '63.546', '11', '4'], 'Zn': ['30', 'Zinc', 'Zn', '65.409', '12', '4'], 'Ga': ['31', 'Gallium', 'Ga', '69.723', '13', '4'], 'Ge': ['32', 'Germanium', 'Ge', '72.64', '14', '4'], 'As': ['33', 'Arsenic', 'As', '74.92160', '15', '4'], 'Se': ['34', 'Selenium', 'Se', '78.96', '16', '4'], 'Br': ['35', 'Bromine', 'Br', '79.904', '17', '4'], 'Kr': ['36', 'Krypton', 'Kr', '83.798', '18', '4'], 'Rb': ['37', 'Rubidium', 'Rb', '85.4678', '1', '5'], 'Sr': ['38', 'Strontium', 'Sr', '87.62', '2', '5'], 'Y': ['39', 'Yttrium', 'Y', '88.90585', '3', '5'], 'Zr': ['40', 'Zirconium', 'Zr', '91.224', '4', '5'], 'Nb': ['41', 'Niobium', 'Nb', '92.90638', '5', '5'], 'Mo': ['42', 'Molybdenum', 'Mo', '95.94', '6', '5'], 'Tc': ['43', 'Technetium', 'Tc', '98', '7', '5'], 'Ru': ['44', 'Ruthenium', 'Ru', '101.07', '8', '5'], 'Rh': ['45', 'Rhodium', 'Rh', '102.905', '9', '5'], 'Pd': ['46', 'Palladium', 'Pd', '106.42', '10', '5'], 'Ag': ['47', 'Silver', 'Ag', '107.8682', '11', '5'], 'Cd': ['48', 'Cadmium', 'Cd', '112.411', '12', '5'], 'In': ['49', 'Indium', 'In', '114.818', '13', '5'], 'Sn': ['50', 'Tin', 'Sn', '118.710', '14', '5'], 'Sb': ['51', 'Antimony', 'Sb', '121.760', '15', '5'], 'Te': ['52', 'Tellurium', 'Te', '127.60', '16', '5'], 'I': ['53', 'Iodine', 'I', '126.904', '47', '17', '5'], 'Xe': ['54', 'Xenon', 'Xe', '131.293', '18', '5'], 'Cs': ['55', 'Caesium', 'Cs', '132.9054519', '1', '6'], 'Ba': ['56', 'Barium', 'Ba', '137.327', '2', '6'], 'La': ['57', 'Lanthanum', 'La', '138.90547', 'n/a', '6'], 'Ce': ['58', 'Cerium', 'Ce', '140.116', 'n/a', '6'], 'Pr': ['59', 'Praseodymium', 'Pr', '140.90765', 'n/a', '6'], 'Nd': ['60', 'Neodymium', 'Nd', '144.242', 'n/a', '6'], 'Pm': ['61', 'Promethium', 'Pm', '145', 'n/a', '6'], 'Sm': ['62', 'Samarium', 'Sm', '150.36', 'n/a', '6'], 'Eu': ['63', 'Europium', 'Eu', '151.964', 'n/a', '6'], 'Gd': ['64', 'Gadolinium', 'Gd', '157.25', 'n/a', '6'], 'Tb': ['65', 'Terbium', 'Tb', '158.92535', 'n/a', '6'], 'Dy': ['66', 'Dysprosium', 'Dy', '162.500', 'n/a', '6'], 'Ho': ['67', 'Holmium', 'Ho', '164.930', '32', 'n/a', '6'], 'Er': ['68', 'Erbium', 'Er', '167.259', 'n/a', '6'], 'Tm': ['69', 'Thulium', 'Tm', '168.93421', 'n/a', '6'], 'Yb': ['70', 'Ytterbium', 'Yb', '173.04', 'n/a', '6'], 'Lu': ['71', 'Lutetium', 'Lu', '174.967', '3', '6'], 'Hf': ['72', 'Hafnium', 'Hf', '178.49', '4', '6'], 'Ta': ['73', 'Tantalum', 'Ta', '180.94788', '5', '6'], 'W': ['74', 'Tungsten', 'W', '183.84', '6', '6'], 'Re': ['75', 'Rhenium', 'Re', '186.207', '7', '6'], 'Os': ['76', 'Osmium', 'Os', '190.23', '8', '6'], 'Ir': ['77', 'Iridium', 'Ir', '192.217', '9', '6'], 'Pt': ['78', 'Platinum', 'Pt', '195.084', '10', '6'], 'Au': ['79', 'Gold', 'Au', '196.966569', '11', '6'], 'Hg': ['80', 'Mercury', 'Hg', '200.59', '12', '6'], 'Tl': ['81', 'Thallium', 'Tl', '204.3833', '13', '6'], 'Pb': ['82', 'Lead', 'Pb', '207.2', '14', '6'], 'Bi': ['83', 'Bismuth', 'Bi', '208.98040', '15', '6'], 'Po': ['84', 'Polonium', 'Po', '210', '16', '6'], 'At': ['85', 'Astatine', 'At', '210', '17', '6'], 'Rn': ['86', 'Radon', 'Rn', '220', '18', '6'], 'Fr': ['87', 'Francium', 'Fr', '223', '1', '7'], 'Ra': ['88', 'Radium', 'Ra', '226', '2', '7'], 'Ac': ['89', 'Actinium', 'Ac', '227', 'n/a', '7'], 'Th': ['90', 'Thorium', 'Th', '232.03806', 'n/a', '7'], 'Pa': ['91', 'Protactinium', 'Pa', '231.03588', 'n/a', '7'], 'U': ['92', 'Uranium', 'U', '238.02891', 'n/a', '7'], 'Np': ['93', 'Neptunium', 'Np', '237', 'n/a', '7'], 'Pu': ['94', 'Plutonium', 'Pu', '244', 'n/a', '7'], 'Am': ['95', 'Americium', 'Am', '243', 'n/a', '7'], 'Cm': ['96', 'Curium', 'Cm', '247', 'n/a', '7'], 'Bk': ['97', 'Berkelium', 'Bk', '247', 'n/a', '7'], 'Cf': ['98', 'Californium', 'Cf', '251', 'n/a', '7'], 'Es': ['99', 'Einsteinium', 'Es', '252', 'n/a', '7'], 'Fm': ['100', 'Fermium', 'Fm', '257', 'n/a', '7'], 'Md': ['101', 'Mendelevium', 'Md', '258', 'n/a', '7'], 'No': ['102', 'Nobelium', 'No', '259', 'n/a', '7'], 'Lr': ['103', 'Lawrencium', 'Lr', '262', '3', '7'], 'Rf': ['104', 'Rutherfordium', 'Rf', '261', '4', '7'], 'Db': ['105', 'Dubnium', 'Db', '262', '5', '7'], 'Sg': ['106', 'Seaborgium', 'Sg', '266', '6', '7'], 'Bh': ['107', 'Bohrium', 'Bh', '264', '7', '7'], 'Hs': ['108', 'Hassium', 'Hs', '277', '8', '7'], 'Mt': ['109', 'Meitnerium', 'Mt', '268', '9', '7'], 'Ds': ['110', 'Darmstadtium', 'Ds', '271', '10', '7'], 'Rg': ['111', 'Roentgenium', 'Rg', '272', '11', '7'], 'Uub': ['112', 'Ununbium', 'Uub', '285', '12', '7'], 'Uut': ['113', 'Ununtrium', 'Uut', '284', '13', '7'], 'Uuq': ['114', 'Ununquadium', 'Uuq', '289', '14', '7'], 'Uup': ['115', 'Ununpentium', 'Uup', '288', '15', '7'], 'Uuh': ['116', 'Ununhexium', 'Uuh', '292', '16', '7'], 'Uuo': ['118', 'Ununoctium', 'Uuo', '294', '18', '7']}
"""
To convert atomic number to atomic symbol. 
numberToSymbolDict is greatly not recommended to be modified.
"""
numberToSymbolDict = {'1': 'H', '2': 'He', '3': 'Li', '4': 'Be', '5': 'B', '6': 'C', '7': 'N', '8': 'O', '9': 'F', '10': 'Ne', '11': 'Na', '12': 'Mg', '13': 'Al', '14': 'Si', '15': 'P', '16': 'S', '17': 'Cl', '18': 'Ar', '19': 'K', '20': 'Ca', '21': 'Sc', '22': 'Ti', '23': 'V', '24': 'Cr', '25': 'Mn', '26': 'Fe', '27': 'Co', '28': 'Ni', '29': 'Cu', '30': 'Zn', '31': 'Ga', '32': 'Ge', '33': 'As', '34': 'Se', '35': 'Br', '36': 'Kr', '37': 'Rb', '38': 'Sr', '39': 'Y', '40': 'Zr', '41': 'Nb', '42': 'Mo', '43': 'Tc', '44': 'Ru', '45': 'Rh', '46': 'Pd', '47': 'Ag', '48': 'Cd', '49': 'In', '50': 'Sn', '51': 'Sb', '52': 'Te', '53': 'I', '54': 'Xe', '55': 'Cs', '56': 'Ba', '57': 'La', '58': 'Ce', '59': 'Pr', '60': 'Nd', '61': 'Pm', '62': 'Sm', '63': 'Eu', '64': 'Gd', '65': 'Tb', '66': 'Dy', '67': 'Ho', '68': 'Er', '69': 'Tm', '70': 'Yb', '71': 'Lu', '72': 'Hf', '73': 'Ta', '74': 'W', '75': 'Re', '76': 'Os', '77': 'Ir', '78': 'Pt', '79': 'Au', '80': 'Hg', '81': 'Tl', '82': 'Pb', '83': 'Bi', '84': 'Po', '86': 'Rn', '88': 'Ra', '89': 'Ac', '90': 'Th', '91': 'Pa', '92': 'U', '93': 'Np', '94': 'Pu', '95': 'Am', '96': 'Cm', '97': 'Bk', '98': 'Cf'}
print("请注意H,N,O,F,Ne,Cl,Ar,Kr,Xe,Rn为气态密度")
print("请输出你想要查询的单质元素的化学符号或者原子序数，如：H或1，注意目前仅支持前98号元素")     # 提示命令行输入
symbolOrNumber = input()              # 注意字符串输入变量的数据类型转换
if symbolOrNumber.isdigit():
    print('您输入的是原子序数:',symbolOrNumber)
    elementName = numberToSymbolDict[symbolOrNumber]
elif symbolOrNumber.isalpha():
    print('您输入的是元素符号:',symbolOrNumber)
    elementName = symbolOrNumber
else:
    print('您输入的是其他字符，请重新输入')
print("\n","单质密度信息: Density | Unit| Name | Symbol | AtomicNumber | ChineseName | State\n",pureDensityDict[elementName],"\n","原子质量信息: AtomicNumber | Name | Symbol | RelativeAtomicMass | Group | Period\n",atomicMassDict[elementName])
print("原子序数：",atomicMassDict[elementName][0]," 元素符号：",atomicMassDict[elementName][2]," 密度：",pureDensityDict[elementName][0]," 相对原子质量：",atomicMassDict[elementName][3])

