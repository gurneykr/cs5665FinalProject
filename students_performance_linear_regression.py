# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:45:22 2019

@author: Krista Gurney
"""


import pandas
import numpy
import matplotlib.pyplot
import sklearn.linear_model

df = pandas.read_csv("StudentsPerformanceLinearRegression.csv")
#df = pandas.read_csv("StudentsPerformance.csv")

X = df[['test_preparation_course','math_score', 'reading_score']].values.reshape(-1,3)
y = df['average_score'].values

model = sklearn.linear_model.LinearRegression(fit_intercept=True)
model.fit(X,y)

'''
# Extract the coeffecients. 
print("omega0 (intercept) =",model.intercept_)
print("omega1 =", model.coef_[0])
print("omega2 =", model.coef_[1])
print("omega3 =", model.coef_[2])
'''

# Compute SSE and R-squared. 
predicted = model.predict(X)
SSE = ((predicted - y)**2).sum()
print("SSE = ", SSE)
R_sq = model.score(X,y)
print("R-squared = ", R_sq)

'''
xfit = numpy.linspace(0,300,600).reshape(-1,1)
yfit = model.predict(xfit)

# Plot the data
matplotlib.pyplot.scatter(X,y)
matplotlib.pyplot.title('Students Performance in Exams')
matplotlib.pyplot.xlabel('gender, race, parental education')
matplotlib.pyplot.ylabel('Average Score')
matplotlib.pyplot.plot(xfit,yfit)
'''