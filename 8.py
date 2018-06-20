import csv
import codecs
with codecs.open("RTC_2016.csv", "r",encoding='utf-8', errors='ignore') as fdata:
    rows = csv.reader(fdata)
    res = list(zip(*rows))
a1 = 3
a2 = 8
a3 = 10
a4 = 13
a5 = 1
a6 = 12
train = res[a1][a5:] + res[a2][a5:] + res[a3][a5:] + res[a4][a5:]
target = list(res[a6][a5:])
a = []
a.append(list(res[a1][a5:]))
a.append(list(res[a2][a5:]))
a.append(list(res[a3][a5:]))
a.append(list(res[a4][a5:]))
train = a

train1 = train
from sklearn import preprocessing

le_1 = preprocessing.LabelEncoder()
le_1.fit(train1[1])
train1[1] = list(le_1.transform(train1[1]))

le_2 = preprocessing.LabelEncoder()
le_2.fit(train1[2])
train1[2] = list(le_2.transform(train1[2]))

le_3 = preprocessing.LabelEncoder()
le_3.fit(train1[3])
train1[3] = list(le_3.transform(train1[3]))

target1 = target
le_t = preprocessing.LabelEncoder()
le_t.fit(target1)
target1 = list(le_t.transform(target1))

target1 = target
from sklearn import tree

clf = tree.DecisionTreeClassifier()

import numpy as np

x = np.array(train1)
x = x.transpose()
train1 = list(x)
clf = clf.fit(train1, target1)

import collections
import pydotplus
with open("fruit_classifier.txt", "w") as dot_data:
    dot_data = tree.export_graphviz(clf,
                                feature_names=train1[0],
                                out_file="f",
                                filled=True,
                                rounded=True)
# graph = pydotplus.graph_from_dot_data(dot_data)

# import graphviz
#
# dot_data = tree.export_graphviz(clf, out_file=None)
# dot_data.close()
# graph = graphviz.Source(dot_data)
# graph
print("sadda")
