import os

def process_data(input_file):
    data_dict = {}

    # 读取文件并处理数据
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()

            # 忽略空行和以#开头的行
            if not line or line.startswith('#'):
                continue

            # 拆分数据并提取第2列、倒数第2列和倒数第4列
            columns = line.split()
            col2, col_minus2, col_minus4 = map(float, (columns[1], columns[-2], columns[-4]))

            # 合并相同的第2列数据，并相应地累加倒数第2列和倒数第4列数据
            if col2 in data_dict:
                data_dict[col2][0] += col_minus2
                data_dict[col2][1] += col_minus4
            else:
                data_dict[col2] = [col_minus2, col_minus4]


    # 打印处理后的数据
    print("合并后的第2列，相应倒数第4列，第2列数据")

    average_CN = 0                                      # 累加计算平均氧配位数
    for key, values in data_dict.items():
        # print(f"Column 2: {key}, Sum of Col -2: {values[0]}, Sum of Col -4: {values[1]}")
        print(key, values[1], round(values[0],3), "%")    # 第二列，倒数第4列，倒数第2列
        average_CN = average_CN + key*values[0]*0.01
    print("两相平均配位数：", average_CN)


    # 提示用户输入浮点数x、y和z，用英文逗号分隔
    user_input = input("请输入浮点数：硅酸盐中X-O平均配位数y_CN_SilicateAve, 两相中总的杂质原子数z_total_Nx（用英文逗号分隔）: ")       # z_total_Nx杂质原子数, y_CN_SilicateAve是硅酸盐单相中X-O配位数

    # 将输入的字符串拆分成浮点数列表
    y, z = map(float, user_input.split(','))

    x = average_CN   # 两相平均X-O配位数
    
    # 计算w = x/y*z
    w = x / y * z    # 进入到silicate的X原子数
    
    k = x / y        # 两相配位数/硅酸盐均相配位数


    # 打印计算结果
    print("进入到silicate中的X原子数：", round(w,4))
    print("留在silicon中的X原子数：", round(z-w,4))
    print("X两相平均氧化程度，k值，即X-O两相配位数/硅酸盐X-O配位数:", round(k,4))



if __name__ == '__main__':

    # 获取当前文件夹下的所有文件名
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # 打印文件名（不包括子文件夹）
    for file in files:
        print(file)

    # 提示用户输入要处理的文件名
    filename = input("请输入要处理的文件名：")


    # 读取数据并打印
    with open(filename, 'r') as file:
        data = file.readlines()
        for line in data:
            print(line.strip())


    # 使用示例
    input_file = filename
    process_data(input_file)
