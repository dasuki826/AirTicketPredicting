# system library
import numpy as np

# user-library
from ClassificationUniformBlending import ClassificationUniformBlending


def mainDecisionTreeClf():
    isTrain = 1 # 1 for train, 0 for test
    isOutlierRemoval = 0 # 1 for outlier removal, 0 otherwise

    performance = 0
    normalizedPerformance = 0
    clf = ClassificationUniformBlending(isTrain, isOutlierRemoval)
    for i in range(8):
        print "Route: {}".format(i)
        [perfor, normaPefor] = clf.evaluateOneRouteForMultipleTimes(clf.routes[i])
        performance += perfor
        normalizedPerformance += normaPefor

    performance = round(performance/8, 2)
    normalizedPerformance = round(normalizedPerformance/8, 2)


    print "\nAverage Performance: {}%".format(performance)
    print "Average Normalized Performance: {}%".format(normalizedPerformance)

    #nn.visualizePrediction(nn.routes[0])



if __name__ == "__main__":
    mainDecisionTreeClf()