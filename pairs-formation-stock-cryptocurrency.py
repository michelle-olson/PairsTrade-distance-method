# import pandas library
import pandas as pd
sec_df=pd.read_csv('/Users/computer-name/Desktop/python/finalsecurities.csv')

col_num = sec_df.shape[1]
outercol = 1
col_sum_list=[]

#this generates a list of the sum of the distance squared between two pairs
#it covers all possible combinations of pairs 
#between the two is measured
while outercol < col_num:
	innercol = outercol + 1
	while innercol < col_num:
		sum_list = []
		out_col_name = sec_df.columns[outercol]
		in_col_name = sec_df.columns[innercol]
		info_str = "Securities: " + out_col_name + ", " + in_col_name
		sum_list.append(info_str)
		sum = 0
		for row in range(sec_df.shape[0]):
			outer_sec = sec_df.iloc[row, outercol]
			inner_sec = sec_df.iloc[row, innercol]
			dist_sq = (outer_sec - inner_sec)*(outer_sec - inner_sec)
			sum += dist_sq

		sum_list.append(sum)
		col_sum_list.append(sum_list)
		innercol += 1

	outercol += 1

total_pairs = len(col_sum_list)
i = 0
print(sec_df)

while i < total_pairs:
	check = col_sum_list[i][1]
	if check < 14:
		print(col_sum_list[i][0] + ': ', check)
		print('The list index is: ', i)
	i += 1

#Palo Alto (2), Zscaler (3) = 3.9133 list index: 7
#Cloudflare (4), Ethereum (8)= 9.4871 list index: 21
#Zscaler (3), Cloudflare (4) = 9.7037 list index: 13
#Bitcoin (7), Ethereum (8) = 12.8683 list index: 27
