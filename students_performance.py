# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:49:06 2019

@author: Krista Gurney
"""

import pandas as pd
import numpy
import matplotlib.pyplot
import sklearn.linear_model

df = pd.read_csv(r'C:\Users\Krista Gurney\Documents\cs5665\FinalProject\StudentsPerformance.csv')

mean_math = df['math_score'].mean()
min_math = df['math_score'].min()
max_math = df['math_score'].max()

mean_reading = df['reading_score'].mean()
min_reading = df['reading_score'].min()
max_reading = df['reading_score'].max()

mean_writing = df['writing_score'].mean()
min_writing = df['writing_score'].min()
max_writing = df['writing_score'].max()

mean = df['average_score'].mean()

'''
print('Mean of the average score: '+str(mean))
print('Mean math score: '+ str(mean_math))
print('Min math score: '+ str(min_math))
print('Max math score: ' + str(max_math))

print('Mean reading score: '+ str(mean_reading))
print('Min reading score: '+ str(min_reading))
print('Max reading score: ' + str(max_reading))

print('Mean writing score: '+ str(mean_writing))
print('Min writing score: '+ str(min_writing))
print('Max writing score: ' + str(max_writing))
'''

high_average = 0
low_average = 0
high_and_completed = 0

for score in df['average_score']:
    if score >= 80:
        high_average += 1
#        for testprep in df['test preparation course']:
 #           if testprep == 'completed':
  #              high_and_completed += 1
    else:
        low_average += 1
        
#p_high_and_completed = high_and_completed/ (high_average)
##########################     
high_math = 0
low_math = 0
for score in df['math_score']:
    if score >= 80:
        high_math += 1
    else:
        low_math += 1
 ########################       
high_reading = 0
low_reading = 0
for score in df['reading_score']:
    if score >= 80:
        high_reading += 1
    else:
        low_reading += 1        
########################       
high_writing = 0
low_writing = 0
for score in df['writing_score']:
    if score >= 80:
        high_writing += 1
    else:
        low_writing += 1  
        
##################

female_count = 0
for gender in df['gender']:
    if gender == 'female':
        female_count +=1

male_count = 1000 - female_count
print('females: ',female_count,' males: ', male_count)

##########################
completed = 0
for testprep in df['test_preparation_course']:
    if testprep == 'completed':
        completed += 1
        
not_completed = 1000 - completed

print('completed: ', completed, ' not completed: ', not_completed)
############################
high_school = 0
some_college = 0
bachelors_or_higher = 0

for education in df['parental_level_of_education']:
    if education == 'high school':
        high_school += 1
    elif education == 'some college':
        some_college += 1
    else:
        bachelors_or_higher += 1
        
print('high school: ', high_school)
print('some_college: ', some_college)
print('bachelors_or_higher: ', bachelors_or_higher)        
################################
p_female = female_count / 1000
p_male = male_count / 1000

p_completed_prep = completed /1000
p_not_completed_prep = not_completed / 1000

p_high_average = high_average / 1000
p_low_average = low_average / 1000

p_high_math = high_math / 1000
p_low_math = low_math / 1000

p_high_reading = high_reading / 1000
p_low_reading = low_reading / 1000

p_high_writing = high_writing / 1000
p_low_writing  = low_writing  / 1000

p_bacheolors_higher = bachelors_or_higher/ 1000
p_high_school = high_school /1000
p_some_college = some_college / 1000


print("p_female: ", p_female)
print("p_male: ", p_male)
print("-----------------")

print("p_completed_prep: ", p_completed_prep)
print("p_not_completed_prep: ", p_not_completed_prep)
print("-----------------")
print("p_high_average: ", p_high_average)
print("p_low_average: ", p_low_average)
print("-----------------")
print("p_high_math: ", p_high_math)
print("p_low_math: ", p_low_math)
print("-----------------")
print("p_high_reading: ", p_high_reading)
print("p_low_reading: ", p_low_reading)
print("-----------------")
print("p_high_writing: ", p_high_writing)
print("p_low_writing: ", p_low_writing)
print("-----------------")
print("p_bacheolors_higher: ", p_bacheolors_higher)
print("p_high_school: ", p_high_school)
print("p_some_college: ", p_some_college)
print("-----------------")



##############################################################
completed = df[df.test_preparation_course == "completed"]
#print(completed)
completed_and_high = completed[completed.average_score >=80]
#print(completed_and_high)
print(len(completed_and_high))

not_completed = df[df.test_preparation_course == "none"]
not_completed_and_high = not_completed[not_completed.average_score >= 80]
#print(not_completed_and_high)
#print(len(not_completed_and_high))
p_high_not_completed = (len(not_completed_and_high)/1000)/ p_not_completed_prep
print("p_high_not_completed: ", p_high_not_completed)

p_high_completed = (len(completed_and_high)/1000)/ p_completed_prep
print("p_high_completed: ", p_high_completed)


high = df[df.average_score >= 80]

bachelor_and_high = high[high.parental_level_of_education == "bachelor's degree"]
master_and_high = high[high.parental_level_of_education == "master's degree"]
p_bachelor_and_master_high = (len(bachelor_and_high) + len(master_and_high))/1000

p_high_bachelor_master = p_bachelor_and_master_high / p_bacheolors_higher
print("p_high_bachelor_master: ", p_high_bachelor_master)

high_school_and_high = high[high.parental_level_of_education == "high school"]
#print(high_school_and_high )
p_high_school_and_high = (len(high_school_and_high)/1000)/ p_high_school
print("p_high_school_and_high: ", p_high_school_and_high )









