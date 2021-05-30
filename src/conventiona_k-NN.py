import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

window.title("Conventional KNN")

lbl = tk.Label(window, text="CONVENTIONAL KNN", font=("Arial", 10))

lbl.grid(column=0, row=0)

txt = tk.Entry(window, font=("Times new roman", 8), width=50)

txt.grid(column=1, row=2)

def Uploading(event = None):
    filename = filedialog.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),("All","*.*")))
    txt.insert(0, filename)

b1 = tk.Button(window, text="Upload", command=Uploading)

b1.grid(column=0, row=2, padx=2)

lb5 = tk.Label(window, text="Enter the k value:", font=("Arial", 10))

lb5.grid(column=0, row=3)

txt1 = tk.Entry(window, font=("Times new roman", 8), width=50)

txt1.grid(column=1, row=3)


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

    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    k=int(txt1.get())
    neigh = KNeighborsClassifier(n_neighbors=k)
    neigh.fit(x_train, y_train)
    y_pred=neigh.predict(x_test)
    pres_acc=metrics.accuracy_score(y_test, y_pred)
    c=confusion_matrix(y_test, y_pred)
    print("For k value as {}".format(k),"we got the highest accuracy percentage : {}%".format(pres_acc*100))
    print(c)
    precision = c[0][0]/(c[0][0]+c[0][1])
    recall = c[0][0]/(c[0][0]+c[1][0])
    print("The precision obtained:",precision)
    print("The Recall obtained:",recall)
def cancel_clicked():
    txt.delete(0, 'end')

b2 = tk.Button(window, text="Ok", command=ok_clicked)

b2.grid(column=1, row=4)

b3 = tk.Button(window, text="Cancel", command=cancel_clicked)

b3.grid(column=2, row=4)

window.geometry('750x400')

window.mainloop()
