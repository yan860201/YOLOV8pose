import pandas as pd
import numpy as np

df = pd.read_csv("VID20230422213134.csv")
df_numpy = df.to_numpy()


def fillin(df, i, j):
    for tofill in range(j):
        if df[i + tofill, position] + df[i + tofill, position + 1] == 0:
            df[i + tofill, position] = (
                df[i - 1, position] - df[i - 1, position + 2]
            ) + df[i + tofill, position + 2]
            df[i + tofill, position + 1] = (
                df[i - 1, position + 1] - df[i - 1, position + 3]
            ) + df[i + tofill, position + 3]
        else:
            df[i + tofill, position + 2] = (
                -(df[i - 1, position] - df[i - 1, position + 2])
                + df[i + tofill, position]
            )
            df[i + tofill, position + 3] = (
                -(df[i - 1, position + 1] - df[i - 1, position + 3])
                + df[i + tofill, position + 1]
            )


for i in range(len(df)):
    for position in [6, 40]:
        if df_numpy[i, position] + df_numpy[i, position + 1] == 0:
            # j 表示連續為0的raw數
            j = 0
            while df_numpy[i + j, position] + df_numpy[i + j, position + 1] == 0:
                j += 1
            else:
                fillin(df_numpy, i, j)
        elif df_numpy[i, position + 2] + df_numpy[i, position + 3] == 0:
            j = 0
            while df_numpy[i + j, position + 2] + df_numpy[i + j, position + 3] == 0:
                j += 1
            else:
                fillin(df_numpy, i, j)

        else:
            continue

dance1_df = pd.DataFrame(df_numpy)
dance1_df.to_csv("VID20230422213134_補值.csv", index=None)
