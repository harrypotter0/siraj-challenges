#for data preprocessing
import pandas as pd
#read our dataset
df = pd.read_csv("bimodal_example.csv")
#show first 5 examples (in BTC)
df.head(n=5)
data = df.x
#plot histogram
sns.distplot(data, bins=20, kde=False)
#try to fit a normal distribution to this data
sns.distplot(data, fit=stats.norm, bins=20, kde=False,)
