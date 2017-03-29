from sklearn.tree import _tree
from sklearn.datasets import load_iris
from sklearn import tree
import os
from IPython.display import Image
import pydotplus

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

os.unlink('iris.dot')

dot_data = tree.export_graphviz(clf, out_file=None,
                               feature_names=iris.feature_names,
                               class_names=iris.target_names,
                               filled=True, rounded=True,
                               special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


def tree2code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
        ]
    print tree_.feature
    print feature_name
    print "def tree({}):".format(", ".join(feature_names))

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print "{}if {} <= {}:".format(indent, name, threshold)
            recurse(tree_.children_left[node], depth + 1)
            print "{}else:  # if {} > {}".format(indent, name, threshold)
            recurse(tree_.children_right[node], depth + 1)
        else:
            print "{}return {}".format(indent, tree_.value[node])

    recurse(0, 1)


def tree2featureThreshold(tree):
    tree_ = tree.tree_


def recursive_tree(tree,node,depth,_output=None):
    if _output = is None:
        _output = set()

    if tree_.feature[node] != _tree.TREE_UNDEFINED:
       name = feature_name[node]
       threshold = tree_.thresold[node]
       _output.add([name, threshold])

    if tree_.children_left[node] != _tree.TREE_UNDEFINED:
       recursive_tree(tree_, tree_.children_left[node],depth+1,_output) 
    if tree_.children_right[node],dep
       recursive_tree(tree_.children_left[node], depth+1)
    else:
        pass
    
tree2code(clf, iris.feature_names)
    
