import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# 读取 Excel 文件
file_path = "缺值文件/暉洛3.csv"
df = pd.read_csv(file_path)

# 将缺失值替换为 NaN
df.replace(0, np.nan, inplace=True)

# 获取所有关节的代碼
# joint_codes = ["x1鼻", "y1鼻", "x2左眼", "y2左眼", "x3右眼", "y3右眼", "x4左耳", "y4左耳", "x5右耳", "y5右耳",
#                "x6左肩", "y6左肩", "x7右肩", "y7右肩", "x8左肘", "y8左肘", "x9右肘", "y9右肘", "x10左腕", "y10左腕",
#                "x11右腕", "y11右腕", "x12左髖", "y12左髖", "x13右髖", "y13右髖", "x14左膝", "y14左膝", "x15右膝", "y15右膝",
#                "x16左踝", "y16左踝", "x17右踝", "y17右踝","x1鼻.1", "y1鼻.1", "x2左眼.1", "y2左眼.1", "x3右眼.1", "y3右眼.1", "x4左耳.1", "y4左耳.1", "x5右耳.1", "y5右耳.1",
#                "x6左肩.1", "y6左肩.1", "x7右肩.1", "y7右肩.1", "x8左肘.1", "y8左肘.1", "x9右肘.1", "y9右肘.1", "x10左腕.1", "y10左腕.1",
#                "x11右腕.1", "y11右腕.1", "x12左髖.1", "y12左髖.1", "x13右髖.1", "y13右髖.1", "x14左膝.1", "y14左膝.1", "x15右膝.1", "y15右膝.1",
#                "x16左踝.1", "y16左踝.1", "x17右踝.1", "y17右踝.1"]
joint_codes = np.arange(68)

# 对每个关节进行插值修复
for code in joint_codes:
    non_nan_indices = df.index[~df[f"{code}"].isnull()]
    non_nan_values = df[f"{code}"][~df[f"{code}"].isnull()]
    
    # 创建插值函数
    interp_func = interp1d(non_nan_indices, non_nan_values, kind='cubic', fill_value='extrapolate')
    
    # 在整个范围内生成插值结果
    interpolated_values = interp_func(df.index)
    
    # 将插值结果填充回原始 DataFrame
    df[f"{code}"] = np.where(df[f"{code}"].isnull(), interpolated_values, df[f"{code}"])

    x = np.linspace(0, 1500, 3000)
    y = interp_func(x)
    plt.plot(non_nan_indices, non_nan_values, "o")
    plt.plot(x, y)
    plt.show()
    break

# 将修复后的数据保存到新的 Excel 文件
# df.to_excel("修复后的数据_中文.xlsx", index=False)
