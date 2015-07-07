import pandas as pd
#import arff

def readARFF():
  '''
  reads the arff file and converts to df
   
  '''
  arff_file = open("C:\Users\NANSH\Dropbox\SF State\Semester II\CSC 869 Data Mining\Mini Project 3\Part II Clustering information using Iris Dataset\customDB.arff", 'r')
  count = 0
  myList = []
  for line in arff_file:
    if not any( [line.startswith("@"), line.startswith("%"), line.strip()==""]):
      count+=1
      line=line.strip("\n")
      line=line.split(',')
      myList.append(line)
   
  # add list to pandas dataframe:
  headers = ['Instance_number', 'sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class', 'cluster']
  myList0 = []
  myList1 = []
  #myList2 = []
  for i in range(0,150): 
    if 'cluster0' in myList[i][6]:
      myList0.append(myList[i])
    elif 'cluster1' in myList[i][6]:
      myList1.append(myList[i])
    #elif 'cluster2' in myList[i][6]:
      #myList2.append(myList[i])
      #df.drop('Instance_number', axis=1, inplace=True)
  #print len(myList1)

  df0 = pd.DataFrame(myList0, columns = headers)
  df0.drop('Instance_number', axis=1, inplace=True)

  df1 = pd.DataFrame(myList1, columns = headers)
  df1.drop('Instance_number', axis=1, inplace=True)
  '''
  df2 = pd.DataFrame(myList2, columns = headers)
  df2.drop('Instance_number', axis=1, inplace=True)
  '''
  arff_file.close()
  #print df
  #print myList[6]
  return df0, df1

