from tkinter import *
from tkinter import messagebox

def stressComp():
    EmpName=entry1.get()
    HFT=entry2.get()
    Age=entry3.get()
    jobSat=entry4.get()
    AvgWork=entry5.get()
    
    if(AvgWork==""):
        messagebox.showinfo("Analyzed Info","Blank Not Allowed")
    
    elif(HFT=="No" or HFT=="NO" or HFT=="no"):
        if(Age>="35" and jobSat == "Less" or jobSat == "less" or jobSat=="LESS"):
            messagebox.showinfo("Analyzed Info",EmpName + " is under complete stress, need care & attention")
        elif(Age<="35" and jobSat == "Less" or jobSat == "less" or jobSat=="LESS"):
            messagebox.showinfo("Analyzed Info",EmpName + " is very young but is a stress victim, need to be taken care")
        elif(jobSat == "More" or jobSat=="more" and jobSat=="MORE"):
            messagebox.showinfo("Analyzed Info", EmpName + " is very happy with his working at this organization")
        else:
            messagebox.showinfo("Analyzed Info",EmpName + " is prone to stress")
    
    elif(HFT=="Yes" or HFT=="YES" or HFT=="yes"):
        if(Age>="35" and jobSat == "Less"or jobSat == "less" or jobSat=="LESS" and AvgWork<="8"):
            messagebox.showinfo("Analyzed Info",EmpName + " is not comfortably synced with organizational environment ")
        elif(Age<="35" and jobSat == "Less" or jobSat == "less" or jobSat=="LESS" and AvgWork>="8"):
            messagebox.showinfo("Analyzed Info",EmpName + " needs to be given lower work hours to keep away from causing stress")
        elif(jobSat == "More" or jobSat=="more" and jobSat=="MORE"):
            messagebox.showinfo("Analyzed Info", EmpName + " is very happy with his working at this organization")
        else:
            messagebox.showinfo("Analyzed Info",EmpName + " is not under dissatifaction or stress")
            
    else:
        messagebox.showinfo("Analyzed Info",EmpName + " is stress free")

root=Tk()
root.title("Employee Stress Analysis")
root.geometry("1280x760")
root.configure(bg="#1888ff")

global entry1
global entry2
global entry3
global entry4
global entry5

Label(root,text="Employee Name",bg="#f5f5f5", font=("Times New Roman", 16)).place(x=20,y=20)
Label(root,text="Has Flexible Timings?",bg="#f5f5f5", font=("Times New Roman", 16)).place(x=20,y=70)
Label(root,text="Age",bg="#f5f5f5", font=("Times New Roman", 16)).place(x=20,y=120)
Label(root,text="Job Satisfaction", bg="#f5f5f5", font=("Times New Roman", 16)).place(x=20,y=170)
Label(root,text="Average Daily work hours", bg="#f5f5f5", font=("Times New Roman", 16)).place(x=20,y=220)

entry1=Entry(root,bd=10)
entry1.place(x=300,y=20)

entry2=Entry(root,bd=10)
entry2.place(x=300,y=70)

entry3=Entry(root,bd=10)
entry3.place(x=300,y=120)

entry4=Entry(root,bd=10)
entry4.place(x=300,y=170)

entry5=Entry(root,bd=10)
entry5.place(x=300,y=220)

Button(root, text="Analyze", command=stressComp, bg="#D3D3D3", height=2,width=15,bd=8).place(x=150,y=270)

root.mainloop()