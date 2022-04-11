import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import seaborn as sb
import trail as t
from sklearn import svm
%matplotlib inline

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

from tkinter import *
from tkinter import messagebox

def TD():
    sb.set_style("darkgrid")
    mpl.rcParams['font.size'] = 14
    mpl.rcParams['figure.figsize'] = (9, 5)
    mpl.rcParams['figure.facecolor'] = '#00000000'
    train_data = pd.read_csv('Train.csv', delimiter = ';')
    print(train_data)
    messagebox.showinfo("Analyzed Info","This is the required data")

def Graph():
    train_data = pd.read_csv('Train.csv', delimiter = ';')
    dframe = train_data.dropna()
    mpl.figure(figsize=(8,5))
    mpl.title('Count of Employees experiencing Stress')
    sb.countplot(x = dframe.Target)
    messagebox.showinfo("Analyzed Info","Here is the graph displaying the count of employees experiencing stress")
    
def BoxPlot():
    train_data = pd.read_csv('Train.csv', delimiter = ';')
    mpl.figure(figsize=(10,8))
    mpl.title('Job Involvement vs IsIndividualContributor')
    sb.boxplot(train_data.IsIndividualContributor, train_data.JobInvolvement, hue=train_data.Target)
    messagebox.showinfo("Analyzed Info","Here's the box plot displaying Job Involvement versus IsIndividualContributor")

def HeatWave():
    train_data = pd.read_csv('Train.csv', delimiter = ';')
    dframe = train_data.dropna()
    scaler = StandardScaler()
    frm = pd.DataFrame();
    frm = dframe
    frm.loc[:, ['Age', 'AvgDailyHours','LeavesTaken', 'MonthlyIncome', 
           'PercentSalaryHike', 'TotalWorkingYears', 'YearsAtCompany', 'YearsWithCurrManager']] = scaler.fit_transform(frm.loc[:, ['Age', 'AvgDailyHours','LeavesTaken', 'MonthlyIncome', 
           'PercentSalaryHike', 'TotalWorkingYears', 'YearsAtCompany', 'YearsWithCurrManager']]);
    mpl.figure(figsize=(30,20))
    sb.heatmap(frm.corr(),annot=True, annot_kws={"fontsize":10})
    messagebox.showinfo("Analyzed Info","The display of heat wave for entire dataset")

def SVM():
    svm_c = svm.SVC(C= 0.5, kernel='rbf')
    svm_c.fit(t.Xtrain, t.ytrain)
    yhskl = svm_c.predict(t.Xtest)
    print("Accuracy of SVM: ",accuracy_score(t.ytest, yhskl))
    messagebox.showinfo("Analyzed Info","Support Vector Machine accuracy analysis")
    
def RF():
    rf = RandomForestClassifier(n_estimators=300, random_state=10)
    rf.fit(t.Xtrain,t.ytrain)
    yh = rf.predict(t.Xtest)
    print("Accuracy of Random Forest: ", accuracy_score(t.ytest, yh))
    rf_gp = {'n_estimators': [900, 925, 950, 975, 1000],'criterion': ['gini', 'entropy']}
    rf_gs = GridSearchCV(estimator=rf,param_grid=rf_gp,scoring='accuracy', n_jobs=-1)
    rf_gs.fit(t.Xtrain, t.ytrain)
    rf_gp = rf_gs.best_params_
    rf_br = rf_gs.best_score_
    print(rf_gs)
    messagebox.showinfo("Analyzed Info","Random Forest Accuracy Analysis")

root=Tk()
root.title("Stress Analysis for Management's Verification")
root.geometry("1280x760")
root.configure(bg="#1888ff")

Label(root,text="Click to display the details of traning data", bg="#f5f5f5", font=("Times New Roman", 20)).place(x=20,y=30)
Button(root, text="Train details", command=TD, bg="#D3D3D3", font=("Times New Roman", 10), height=2,width=20,bd=8).place(x=505,y=20)

Label(root,text="Click to check stress graph of employees count vs target", bg="#f5f5f5", font=("Times New Roman", 20)).place(x=20,y=100)
Button(root, text="Generate Graph", command=Graph, bg="#D3D3D3", font=("Times New Roman", 10), height=2,width=20,bd=8).place(x=660,y=90)

Label(root,text="Click to check box plot", bg="#f5f5f5", font=("Times New Roman", 20)).place(x=20,y=170)
Button(root, text="Box Plot", command=BoxPlot, bg="#D3D3D3", font=("Times New Roman", 10), height=2,width=20,bd=8).place(x=300,y=160)

Label(root,text="Click to check Heat Wave", bg="#f5f5f5", font=("Times New Roman", 20)).place(x=20,y=240)
Button(root, text="Heat Wave", command=HeatWave, bg="#D3D3D3", font=("Times New Roman", 10), height=2,width=20,bd=8).place(x=340,y=230)

Label(root,text="Click to view SVM Accuracy", bg="#f5f5f5", font=("Times New Roman", 20)).place(x=20,y=310)
Button(root, text="SVM Analysis", command=SVM, bg="#D3D3D3", font=("Times New Roman", 10), height=2,width=20,bd=8).place(x=370,y=300)

Label(root,text="Click to view RF Accuracy", bg="#f5f5f5", font=("Times New Roman", 20)).place(x=20,y=380)
Button(root, text="RF Analysis", command=RF, bg="#D3D3D3", font=("Times New Roman", 10), height=2,width=20,bd=8).place(x=365,y=370)

root.mainloop()