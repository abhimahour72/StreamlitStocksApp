from operator import index
import streamlit as st
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import yfinance as yf

initialData = pd.read_csv("dd.csv")
st.title("Agastya Data assignment's solution")
st.subheader("Initial Data")
st.text("The data in the table below is what I first acquired from Yahoo Finance using the Yfinance \n"
        + "package. The date for which the stock's closing price is downloaded is shown in the \ncoloumn-header of "
        + "coloumns 2-5 in this instance. The profit margin and earning \n"
        + "increase are displayed in columns 6-7.")
initialData.set_index('label', inplace=True)
initialData.index.name = None
st.write(initialData)
initialData['oneMonth_Change'] = (
    initialData['oneSepTwentytwo'] - initialData['oneAugTwentytwo'])/initialData['oneAugTwentytwo']
initialData['fiftytwoWeekChange'] = (
    initialData['ThirthfirstDectwentyone'] - initialData['oneJanTwentyone'])/initialData['oneJanTwentyone']
initialData['earning_growth'] = initialData['earning_growth'].fillna(0)
initialData.drop(['oneAugTwentytwo', 'oneSepTwentytwo',
                 'oneJanTwentyone', 'ThirthfirstDectwentyone'], axis=1)
swap_list = ["oneMonth_Change", "fiftytwoWeekChange",
             "profit_Margin", "earning_growth"]

# Swapping the columns
initialData = initialData.reindex(columns=swap_list)
st.header(" ")

st.text("Here, column 2 shows the price change from 1/8/22 to 1/09/22 during a one-month period. \n"
        + "The 52-week change in price from 1/1/21 to 31/12/21 is shown in Column 3. whereas the \n"
        + "profit margin and profits growth are shown in Columns 4-5.")
st.write(initialData)

initialData['oneMonth_Change'] = initialData.oneMonth_Change.rank(pct=True)
initialData['fiftytwoWeekChange'] = initialData.fiftytwoWeekChange.rank(
    pct=True)
initialData['profit_Margin'] = initialData.profit_Margin.rank(pct=True)
initialData['earning_growth'] = initialData.earning_growth.rank(pct=True)


initialData['Total'] = initialData['oneMonth_Change'] + initialData['fiftytwoWeekChange']+initialData['profit_Margin'] \
    + initialData['earning_growth']

fff = initialData.sort_values(by='Total', ascending=False)

st.subheader(" ")
st.text("Here, I've calculated the percentile rank for each stock's data in the column, and I've added \nthe individual percentile rankings together in the total column.")

x = st.slider("To see the stock arranged in descending order, slide either way.",
              min_value=1, max_value=50, value=5)
st.write("By default, the top", x,
         "stocks are displayed. To modify the number of stocks displayed, slide left or right.")
st.write(fff.head(x))
