from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

accuracy = []
i = 0

names = ["Decision Tree", "Linear SVM", "Neural Net", "Naive Bayes"]


classifiers = [
    DecisionTreeClassifier(),
    SVC(kernel="linear", C=0.025),
    MLPClassifier(alpha=1),
    GaussianNB()]

for clf in classifiers:
    clf.fit(X, Y)
    prediction = clf.predict(X)
    acc_score = accuracy_score(Y, prediction) * 100
    accuracy.append(acc_score)
    print('Accuracy for {} is :{}'.format(names[i], acc_score))
    i = i + 1
