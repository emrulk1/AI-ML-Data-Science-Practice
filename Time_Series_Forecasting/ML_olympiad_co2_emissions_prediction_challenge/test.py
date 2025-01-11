# %% [code] {"execution":{"iopub.status.busy":"2024-03-11T15:26:48.831005Z","iopub.execute_input":"2024-03-11T15:26:48.831523Z","iopub.status.idle":"2024-03-11T15:26:48.889648Z","shell.execute_reply.started":"2024-03-11T15:26:48.831487Z","shell.execute_reply":"2024-03-11T15:26:48.888722Z"},"jupyter":{"outputs_hidden":false}}
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
# Train=pd.read_csv('/kaggle/input/ml-olympiad-co2-emissions-prediction-challenge/train.csv')
Train=pd.read_csv('ml-olympiad-co2-emissions-prediction-challenge/train.csv')
# Test= pd.read_csv('/kaggle/input/ml-olympiad-co2-emissions-prediction-challenge/test.csv')
Test= pd.read_csv('ml-olympiad-co2-emissions-prediction-challenge/test.csv')
# sample_submission= pd.read_csv('/kaggle/input/ml-olympiad-co2-emissions-prediction-challenge/sample_submission.csv')
sample_submission= pd.read_csv('ml-olympiad-co2-emissions-prediction-challenge/sample_submission.csv')
# %% [code] {"execution":{"iopub.status.busy":"2024-03-11T15:26:48.891712Z","iopub.execute_input":"2024-03-11T15:26:48.892389Z","iopub.status.idle":"2024-03-11T15:26:48.917882Z","shell.execute_reply.started":"2024-03-11T15:26:48.892357Z","shell.execute_reply":"2024-03-11T15:26:48.916618Z"},"jupyter":{"outputs_hidden":false}}
#replace ".."with .100
# Train=Train.replace('..', .100)
# Test=Test.replace('..', 0.100)
for column_name in Train.dorpna().columns:
    if Train[column_name].dtypes == 'float64' or Train[column_name].dtypes == 'int64':
        Train[column_name].fillna(Train[column_name].mean(), inplace=True)

for column_name in Test.dorpna().columns:
    if Test[column_name].dtypes == 'float64' or Test[column_name].dtypes == 'int64':
        Test[column_name].fillna(Test[column_name].mean(), inplace=True)

# %% [code] {"execution":{"iopub.status.busy":"2024-03-11T15:26:48.919205Z","iopub.execute_input":"2024-03-11T15:26:48.920037Z","iopub.status.idle":"2024-03-11T15:26:48.92641Z","shell.execute_reply.started":"2024-03-11T15:26:48.920002Z","shell.execute_reply":"2024-03-11T15:26:48.924899Z"},"jupyter":{"outputs_hidden":false}}
#Unique country for iteration
unique = Train['Country Name'].unique()

# %% [code] {"execution":{"iopub.status.busy":"2024-03-11T15:26:48.929443Z","iopub.execute_input":"2024-03-11T15:26:48.930452Z","iopub.status.idle":"2024-03-11T15:27:02.902191Z","shell.execute_reply.started":"2024-03-11T15:26:48.930404Z","shell.execute_reply":"2024-03-11T15:27:02.900943Z"},"jupyter":{"outputs_hidden":false}}
#trainig and inferencing with LogisticRegression and ARIMA
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
from sklearn.ensemble import VotingRegressor, RandomForestRegressor, ExtraTreesRegressor, HistGradientBoostingRegressor
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

lr = LinearRegression()
lgr = LogisticRegression()
dt = DecisionTreeRegressor(max_depth=4, random_state=42)
hb = HuberRegressor()
xgb = XGBRegressor()
rf =  RandomForestRegressor()
et = ExtraTreesRegressor()

j=0
for i in unique:
    transposed_df=0
    fg = Train[Train['Country Name'] == i].reset_index(drop=True)
    columns_to_drop = ['Country Code', 'Country Name','Indicator']
    fg = fg.drop(columns_to_drop, axis=1)
    transposed_df = fg.transpose()
    #print(fg)
    #print('done for now')
    Xtrain = transposed_df[[0,1, 2,3,4,5,6,7,8,9,10]]
    Xtrain
    Ytrain=transposed_df[11]
    Ytrain
    # logistic_regression = LogisticRegression()
    logistic_regression = LogisticRegression(penalty='l2', C=1.0, solver='liblinear')
    try:
        # Initialize the models
        # ridge_model = Ridge(alpha=1.0)
        # xgb_model = XGBRegressor(random_state=42)

        # Create the Voting Regressor ensemble
        # ensemble = VotingRegressor(estimators=[('ridge', ridge_model), ('xgb', xgb_model)])

        logistic_regression.fit(Xtrain,Ytrain)
        # ensemble.fit(Xtrain, Ytrain)
        fgt = Test[Test['Country Name'] == i].reset_index(drop=True)
        columns_to_drop = [ 'Country Name','Indicator']
        fgt = fgt.drop(columns_to_drop, axis=1)
        transposed_df = fgt.transpose()
        #print(transposed_df)

        Xtest = transposed_df[[0,1, 2,3,4,5,6,7,8,9,10]]
        forecast = logistic_regression.predict(Xtest.astype(float))
        # forecast = ensemble.predict(Xtest.astype(float))

        model = ARIMA(Ytrain.astype(float), order=(0,1,0))  # Adjust order as needed
        model_fit = model.fit()


        forecast2 = model_fit.forecast(steps=16)

        row_index = sample_submission[sample_submission.eq(i).any(axis=1)].index[0]


        new_values = [i, forecast[0], forecast[1],forecast[2], forecast[3], forecast[4],forecast2[31]]
        sample_submission.loc[row_index] = new_values
    except:
        j+=1

# %% [code] {"execution":{"iopub.status.busy":"2024-03-11T15:27:02.903585Z","iopub.execute_input":"2024-03-11T15:27:02.903944Z","iopub.status.idle":"2024-03-11T15:27:02.921941Z","shell.execute_reply.started":"2024-03-11T15:27:02.903915Z","shell.execute_reply":"2024-03-11T15:27:02.920545Z"},"jupyter":{"outputs_hidden":false}}
# sample_submission

# %% [code] {"execution":{"iopub.status.busy":"2024-03-11T15:27:02.92391Z","iopub.execute_input":"2024-03-11T15:27:02.92439Z","iopub.status.idle":"2024-03-11T15:27:02.947365Z","shell.execute_reply.started":"2024-03-11T15:27:02.924345Z","shell.execute_reply":"2024-03-11T15:27:02.946038Z"},"jupyter":{"outputs_hidden":false}}
sample_submission.to_csv('submission_18_03_2024.csv', index=False)