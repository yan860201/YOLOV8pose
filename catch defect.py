import pandas as pd
import numpy as np

df = pd.read_csv("8x_p6_conf_077.csv")
df_numpy = df.to_numpy()


mark = []
for i in range(len(df)):
    counter = 0
    for k in range(18):
        if ((df_numpy[i, k]) + df_numpy[i, k + 1] == 0) ^ (
            df_numpy[i, k + 34] + df_numpy[i, k + 1 + 34] == 0
        ):
            counter += 1
        else:
            pass

    if counter > 0:
        mark.append(1)
    else:
        mark.append(0)

output = pd.DataFrame(mark)
output.to_csv("mark.csv", index=None)
