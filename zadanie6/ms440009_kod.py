import pandas as pd 
from lightgbm import LGBMRegressor

X_train = pd.read_csv("~/SAD/data/X_train.csv")
Y_train = pd.read_csv("~/SAD/data/Y_train.csv").squeeze()
X_test = pd.read_csv("~/SAD/data/X_test.csv")

model = LGBMRegressor(
    n_estimators=2000,
    learning_rate = 0.05,
    max_depth=15,
    num_leaves=35,
    subsample=0.8
)

model.fit(X_train, Y_train)

pred = model.predict(X_test)

df = pd.DataFrame({
    "Id" : X_test.index,
    "Expected":pred
})

df.to_csv("ms440009.csv", index=False)