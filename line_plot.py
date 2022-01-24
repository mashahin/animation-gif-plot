# import libraries
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt
import gif

# set plot style and resolution
plt.style.use("seaborn")
gif.options.matplotlib["dpi"] = 100

# load stock data
df = yf.download("TSLA", start="2019-01-01", end="2021-12-31")
tsla_df = df[["Adj Close"]].resample("M").last()

# define plot helper function


@gif.frame
def plot_1(df, i):
    df = df.copy()
    df.iloc[i:] = np.nan
    ax = df.plot(title="Tesla stock price", legend=False, style="o--")
    ax.set_xlabel("Month of year")
    ax.set_ylabel("Price in US$")


frames = []
for i in range(1, len(tsla_df)):
    frames.append(plot_1(tsla_df, i))

gif.save(frames, "tesla_stock_price.gif",
         duration=15, unit="s",
         between="startend")
