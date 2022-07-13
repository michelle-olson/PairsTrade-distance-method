#import needed libraries
import pandas as pd

#this loads in the two csv files into two seperate dataframes to do a join
#replace with the correct file path if running on your own computer
stocksdf=pd.read_csv('/Users/computer-name/Desktop/python/stocks.csv')
cryptodf=pd.read_csv('/Users/computer-name/Desktop/python/BTC-monero.csv')


#this gets rid of stock closing time but keeps the date in the date column
for index in range(stocksdf.shape[0]):
	string = stocksdf.iloc[index,0]
	string = string.split()[0]
	stocksdf.iloc[index,0] = string
	index += 1


#this creates a new dataframe from merging the previous
#two dataframes by the Dates column
merged_df = pd.merge(stocksdf, cryptodf, how='inner', on= 'Dates')

#this converts the new dataframe into a csv file
merged_df.to_csv('/Users/computer-name/Desktop/python/securities.csv')
