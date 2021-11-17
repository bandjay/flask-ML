from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd


def train_classifier(train_df,class_var):
    cols=train_df.columns
    X=train_df[cols[:-1]]
    y=train_df[class_var]
    clf = SVC(gamma='auto')
    clf.fit(X, y)
    y_pred=clf.predict(X)
    accuracy_score(y, y_pred)
    filename = 'ml_model.sav'
    pickle.dump(clf, open(filename, 'wb'))
    return f'Train accuracy : {100*accuracy_score(y, y_pred):.2f} %'
    
def make_predictions(test_df,class_var): 
    model = pickle.load(open('ml_model.sav', 'rb'))
    cols=test_df.columns
    X_test=test_df[cols[:-1]]
    y_test=test_df[class_var]
    y_pred=model.predict(X_test)
    return f'Test accuracy : {100*accuracy_score(y_test, y_pred):.2f} %'

def get_df(byte_str):
    #byte_str=b'sepal_length,sepal_width,petal_length,petal_width,species\n5.6,2.5,3.9,1.1,versicolor\n6.9,3.1,4.9,1.5,versicolor\n6.7,3.1,4.7,1.5,versicolor\n'
    lines=str(byte_str).split("\n")
    records=[]
    cols=lines[0].split(",")
    for i,rec in enumerate(lines[1:]):
        #rec=lines[1]
        temp_rec=rec.split(",")
        if len(temp_rec)==len(cols):
            records.append(list(map(float,temp_rec[:-1]))+[temp_rec[-1]])
        else:
            pass
    df=pd.DataFrame.from_records(records)
    df.columns=cols
    return df
