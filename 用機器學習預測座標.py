import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df_name = "暉洛1.csv"

df = pd.read_csv(f"缺值文件/{df_name}")

X = (
    df["幀"]
    .to_numpy()
    .reshape(
        -1,
    )
)
y = (
    df["14"]
    .to_numpy()
    .reshape(
        -1,
    )
)

Xmodel = np.poly1d(np.polyfit(X, y, 25))

myline = np.linspace(0, len(X) - 1, 1500)

plt.scatter(X, y)
plt.plot(myline, Xmodel(myline))
plt.show()
# y = df[["14", "15"]]

# regr = linear_model.LinearRegression()
# regr.fit(X, y)

# predictedXY = regr.predict([[10,]])

# print(predictedXY)
