# ch4_data_wrangling.py
import pandas as pd

df = pd.DataFrame({
    "id": [1,2,3,4],
    "group": ["A","B","A","B"],
    "score": [88, 92, 75, 85]
})

df_a = df[df["group"] == "A"]
# mutate
df["score_norm"] = (df["score"] - df["score"].mean()) / df["score"].std()
# group summarize

summary = df.groupby("group")["score"].agg(["mean","count"])
print("Filtered (group A):\n", df_a)
print("\nNormalized:\n", df)
print("\nGroup summary:\n", summary)
