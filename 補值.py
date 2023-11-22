import pandas as pd
import numpy as np

df_name = "暉洛1.csv"

df = pd.read_csv(f"缺值文件/{df_name}")
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


def fillin_upperlimb(df, i, j):
    for tofill in range(j - j // 2):
        df[i + tofill, position : position + 2] = df[i - 1, position : position + 2] + (
            (df[i - 1, position : position + 2] - df[i - 2, position : position + 2])
            * (tofill + 1)
        )
    for tofill in range(j // 2):
        df[i + j - 1 - tofill, position : position + 2] = df[
            i + j, position : position + 2
        ] + (
            (
                df[i + j, position : position + 2]
                - df[i + j + 1, position : position + 2]
            )
            * (tofill + 1)
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

    for position in [14, 16, 18, 20, 48, 50, 52, 54]:
        if df_numpy[i, position] + df_numpy[i, position + 1] == 0:
            j = 0
            while df_numpy[i + j, position] + df_numpy[i + j, position + 1] == 0:
                j += 1
            else:
                fillin_upperlimb(df_numpy, i, j)
        else:
            continue


dance1_df = pd.DataFrame(df_numpy)
dance1_df.to_csv(f"缺值文件/{df_name}_補值.csv", index=None)
