from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import tree

def main():
   df, _ = readCSVFile("dataset-all-categorical.csv")
   newdf, classl = catToInt(df)
   model = tree.DecisionTreeClassifier()

   #tree.export_graphviz(model, out_file="tree.dot")
   result =  cross_val_score(model, newdf, classl, cv=10)
   mean_accuracy = np.mean(result)
   std_d = np.std(result)
   print result
   print "accuracy = {}\nStd Dev = {}".format(mean_accuracy, std_d)


def readCSVFile(filepath):
   df = pd.read_csv(filepath, index_col=0)
   (_, _, sufix) = filepath.rpartition('\\')
   (prefix, _, _) =sufix.rpartition('.')
   print "csv read and converted to dataframe !!"
   # df['class'] = df['class'].apply(replaceLabel)
   return df, prefix

def catToInt(df):
   # replace the Nan with "NA" which acts as a unique category
   df.fillna("NA", inplace=True)
   mapper={}
   
   # make list of all column headers 
   categorical_list = list(df.columns.values)
   #print categorical_list
   #exclude the class column
   categorical_list.remove('CLASS')
   newdf = pd.DataFrame(columns=categorical_list)
   
   #Converting Categorical Data to integer labels
   for x in categorical_list:
       mapper[x]=preprocessing.LabelEncoder()
   for x in categorical_list:
       newdf[x]= mapper[x].fit_transform(df.__getattr__(x))

   # make a class series encoded : 
   le = preprocessing.LabelEncoder()
   myclass = le.fit_transform(df.__getattr__('CLASS'))
   return newdf, myclass

main()