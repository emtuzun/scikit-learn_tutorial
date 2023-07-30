from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2], [3, 3]], [0, 2, 4, 5])
print(reg.coef_)
print(reg.intercept_)
my_prediction = reg.predict([[4,4]])
print(my_prediction)