import statistics
import pandas as pd 
import csv

df = pd.read_csv("StudentsPerformance.csv")

male_list = df["reading score"].tolist()
female_list = df["writing score"].tolist()

male_mean = statistics.mean(male_list)
female_mean = statistics.mean(female_list)

male_median = statistics.median(male_list)
female_median = statistics.median(female_list)


male_std = statistics.stdev(male_list)
female_std = statistics.stdev(female_list)

maleStdStart1,maleStdEnd1 = male_mean - male_std,male_mean + male_std

maleStdStart2,maleStdEnd2 = male_mean - (2*male_std),male_mean + (2*male_std)

maleStdStart3,maleStdEnd3 = male_mean - (3*male_std),male_mean + (3*male_std)


femaleStdStart1,femaleStdEnd1 = female_mean - female_std,female_mean + female_std

femaleStdStart2,femaleStdEnd2 = female_mean - (2*female_std),female_mean + (2*female_std)

femaleStdStart3,femaleStdEnd3 = female_mean - (3*female_std),female_mean + (3*female_std)

male_listWithin_1_st = [result for result in male_list if result > maleStdStart1 and result < maleStdEnd1]
male_listWithin_2_st = [result for result in male_list if result > maleStdStart2 and result < maleStdEnd2]
male_listWithin_3_st = [result for result in male_list if result > maleStdStart3 and result < maleStdEnd3]

female_listWithin_1_st = [result for result in female_list if result > femaleStdStart1 and result < femaleStdEnd1]
female_listWithin_2_st = [result for result in female_list if result > femaleStdStart2 and result < femaleStdEnd2]
female_listWithin_3_st = [result for result in female_list if result > femaleStdStart3 and result < femaleStdEnd3]

print("{}% is the data for male within 1 standard deviation  ".format(len(male_listWithin_1_st)*100.0/len(male_list)))
print("{}% is the data for male within 2 standard deviation  ".format(len(male_listWithin_2_st)*100.0/len(male_list)))
print("{}% is the data for male within 3 standard deviation  ".format(len(male_listWithin_3_st)*100.0/len(male_list)))

print("{}% is the data for female within 1 standard deviation  ".format(len(female_listWithin_1_st)*100.0/len(female_list)))
print("{}% is the data for female within 2 standard deviation  ".format(len(female_listWithin_2_st)*100.0/len(female_list)))
print("{}% is the data for female within 3 standard deviation  ".format(len(female_listWithin_3_st)*100.0/len(female_list)))

