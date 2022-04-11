import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import seaborn as sb
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score

from sklearn.model_selection import train_test_split

train_data = pd.read_csv('Train.csv', delimiter = ';')
dframe = train_data.dropna()
        
def Data_Processor(t_frame):
    
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    t = pd.DataFrame()
    t_frame['HasFlexibleTimings']= label_encoder.fit_transform(t_frame['HasFlexibleTimings']) 
    t_frame['IsIndividualContributor']= label_encoder.fit_transform(t_frame['IsIndividualContributor']) 
    t_frame['RemoteWorkSatistfaction']= label_encoder.fit_transform(t_frame['RemoteWorkSatistfaction']) 
    t_frame['WorkLoadLevel']= label_encoder.fit_transform(t_frame['WorkLoadLevel']) 
    t = pd.concat([pd.get_dummies(t_frame[col]) for col in ['Department','EducationField', 'Gender', 'JobRole', 'MaritalStatus']], axis=1)
    t.groupby(level=0, axis=1).sum()
    t_frame = pd.concat([t_frame, t], axis=1)
    t_frame.drop(['Department','EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'EmployeeID'], axis=1, inplace=True)

    return t_frame;
    
def Normalize(dframe):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    frm = pd.DataFrame();
    frm = dframe
    frm.loc[:, ['Age', 'AvgDailyHours','LeavesTaken', 'MonthlyIncome', 
           'PercentSalaryHike', 'TotalWorkingYears', 'YearsAtCompany', 'YearsWithCurrManager']] = scaler.fit_transform(frm.loc[:, ['Age', 'AvgDailyHours','LeavesTaken', 'MonthlyIncome', 
           'PercentSalaryHike', 'TotalWorkingYears', 'YearsAtCompany', 'YearsWithCurrManager']]);
    return frm;
    
dframe = Data_Processor(dframe)
ndf = Normalize(dframe)

X = ndf[['Age', 'AvgDailyHours', 'Education', 'HasFlexibleTimings',
       'IsIndividualContributor', 'JobInvolvement', 'JobSatisfaction',
       'LeavesTaken', 'MicromanagedAtWork', 'MonthlyIncome',
       'NumCompaniesWorked', 'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'RemoteWorkSatistfaction',
       'SelfMotivationLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'WorkLifeBalance', 'WorkLoadLevel', 'YearsAtCompany',
       'YearsSinceLastPromotion', 'YearsWithCurrManager', 'Human Resources',
       'Research & Development', 'Sales', 'Human Resources', 'Life Sciences',
       'Marketing', 'Medical', 'Other', 'Technical Degree', 'Female', 'Male',
       'Healthcare Representative', 'Human Resources', 'Laboratory Technician',
       'Manager', 'Manufacturing Director', 'Research Director',
       'Research Scientist', 'Sales Executive', 'Sales Representative',
       'Divorced', 'Married', 'Single']]

y = ndf['Target']
    
Xtrain, Xtest, ytrain, ytest = train_test_split( X, y, test_size = 0.2, random_state = 40)


