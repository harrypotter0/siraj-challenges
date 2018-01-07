
import tensorflow as tf
import tensorflow.contrib.learn as skflow
from sklearn import datasets
from tensorflow.contrib.learn.python import SKCompat


iris = datasets.load_iris()
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]

classifier = skflow.DNNClassifier(feature_columns=feature_columns, hidden_units=[10, 20, 10], n_classes=3)

classifier.fit(iris.data, iris.target, steps=50)

score = classifier.evaluate(iris.data, iris.target, steps=1)["accuracy"]
print("Accuracy: {}".format(score))
