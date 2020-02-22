def Perceptron(TrainingSet, T):
    theta0,theta1 = 0,0
    returnList =[]
    for i in range(T):
        for j in range(len(TrainingSet)):
            if TrainingSet[j][1]*(theta0*TrainingSet[j][0][0] + theta1*TrainingSet[j][0][1]) <=0 :
                theta0, theta1 = theta0+TrainingSet[j][1]*TrainingSet[j][0][0] , theta1+TrainingSet[j][1]*TrainingSet[j][0][1]
                print(theta0,theta1)
                returnList.append([theta0,theta1])
    print(returnList)

if __name__ == "__main__":
    Perceptron([[[-1,1],1],
                [[1,-1],1],
                [[1,1],-1],
                [[2,2],-1]], 4)