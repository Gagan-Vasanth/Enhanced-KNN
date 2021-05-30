import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

window.title("Enhanced KNN")

lbl = tk.Label(window, text="ENHANCED KNN", font=("Arial", 10))

lbl.grid(column=0, row=0)

txt = tk.Entry(window, font=("Times new roman", 8), width=50)

txt.grid(column=1, row=2)

def Uploading(event = None):
    filename = filedialog.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),("All","*.*")))
    txt.insert(0, filename)

b1 = tk.Button(window, text="Upload", command=Uploading)

b1.grid(column=0, row=2, padx=2)

def ok_clicked():
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import datasets
    from sklearn import metrics
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import average_precision_score
    import pandas as pd
    data = pd.read_csv(txt.get())
    data["class"] = [1 if i == "p" else 0 for i in data["class"]]
    data.drop("veil-type",axis=1,inplace=True)
    for column in data.drop(["class"], axis=1).columns:
        value = 0
        step = 1/(len(data[column].unique())-1)
        for i in data[column].unique():
            data[column] = [value if letter == i else letter for letter in data[column]]
            value += step
    
    y = data['class'].values
    X = data.drop(["class"], axis=1).values
    if( len(X)>1000):
        n=len(X)//100
    else:
        n=len(X)//10
    prev_acc=0;k=0
    while(n>0):
        x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
        neigh = KNeighborsClassifier(n_neighbors=n)
        neigh.fit(x_train, y_train)
        y_pred=neigh.predict(x_test)
        pres_acc=metrics.accuracy_score(y_test, y_pred)
        c=confusion_matrix(y_test, y_pred)
        if(prev_acc<pres_acc and pres_acc!=1.0):
            prev_acc=pres_acc
            k=n
        n-=1
    lb3 = tk.Label(window, text=k)
    lb3.grid(column=1, row=4)
    lb5 = tk.Label(window, text=format(pres_acc*100)+"%")
    lb5.grid(column=1, row=5)
    print("For k value as {}".format(k if k!=0 else 1),"we got the highest accuracy percentage : {}%".format(pres_acc*100))
    print(c)
    precision = c[0][0]/(c[0][0]+c[0][1])
    recall = c[0][0]/(c[0][0]+c[1][0])
    print("The precision obtained:",precision)
    print("The Recall obtained:",recall)
            

def cancel_clicked():
    txt.delete(0, 'end')

b2 = tk.Button(window, text="Ok", command=ok_clicked)

b2.grid(column=1, row=3)

b3 = tk.Button(window, text="Cancel", command=cancel_clicked)

b3.grid(column=2, row=3)

lb2 = tk.Label(window, text=" The Best 'K' value for the above data set is =", font=("Times new roman", 8))

lb2.grid(column=0, row=4)

lb4 = tk.Label(window, text=" The Highest accuracy obtained by using the above 'K' value for the data set is =", font=("Times new roman", 8))

lb4.grid(column=0, row=5)

window.geometry('750x400')

window.mainloop()
