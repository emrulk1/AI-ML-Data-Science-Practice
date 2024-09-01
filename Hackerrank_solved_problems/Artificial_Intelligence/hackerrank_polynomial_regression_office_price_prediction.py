# Enter your code here. Read input from STDIN. Print output to STDOUT
# problem link: https://www.hackerrank.com/challenges/predicting-house-prices/problem
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

if __name__ == "__main__":
    n_features , n_samples  = map(int , input().split())
    # print(n_samples , n_features)
    
    mat = []
    
    for i in range(n_samples):
        row = list(map(float, input().split()))
        mat.append(row)
    
    mat = np.array(mat)
    # print(mat[:,-1])
    # print(mat[:, :-1])
    
    X_train = mat[:, :-1]
    y_train = mat[:,-1]
    
    # print("dimension of X_train :", X_train.shape)
    # print("dimension of y_train :", y_train.shape)
    # print(type(y_train))
    
    # Constructing the polynomials of our Independent features 
    # poly_reg = PolynomialFeatures(degree = 3)
    # X_p = poly_reg.fit_transform(X_train)
    # print("dimension of X_p : ", X_p.shape)
    
    degree = 3
    poly_reg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
    
    
    # Fitting Simple Linear Regression to the Training set
    # regressor = LinearRegression()
    # regressor.fit(X_p, y_train)
    
    poly_reg.fit(X_train, y_train)
    
    X_test = []
    test_samples = int(input().strip())
    for i in range(test_samples):
        row = list(map(float, input().split()))
        X_test.append(row)
    
    X_test = np.array(X_test)
    # print(X_test.shape)
    
    y_test = poly_reg.predict(X_test)
    # print("dimension of y_test : ", y_test.shape)
    
    # print(y_test)
    
    for value in y_test:
        print(round(value,2))
    
    # 1.0 2.0
    # 3.0 4.0
    # 5.0 6.0
