import numpy as np
import time


def optimalisationF(type, coeff, startValue, stopConditions, learnRate=0.01):
    steps = [startValue]
    x = startValue
    startTime = time.time()
    for _ in range(stopConditions.maxNumOfIterations):
       # print(x)
        if(type == "g"): #gradient descent
            diff = learnRate*(3*coeff.a*x**2 + 2*coeff.b*x + coeff.c)
        elif(type == "n"): #newton's formula
            diff = learnRate * (3*coeff.a*x**2+2*coeff.b*x+coeff.c)/(6*coeff.a*x+2*coeff.b)#learnRate*(a*x**3+b*x**2+c*x+d)/(3*a*x**2+2*b*x+c)
        if np.abs(diff) < stopConditions.tolerance:
            print("Terminated by Tolerance stop condition")
            break
        if time.time() - startTime >= stopConditions.timeout:
            print("Terminated by Timeout stop condition")
            break
        x = x - diff
        steps.append(x)
        if x <= stopConditions.desiredValue:
            print("Terminated by desired value stop condition")
            break
    print(x)
    return x#, steps


def optimalisationG (type, coeff, startValue, stopConditions, learnRate=0.01):
    print("optimisationG called")
    startTime = time.time()
    k = 0
    x = startValue
    for i in range(stopConditions.maxNumOfIterations):
        print(x)
        print(np.dot(np.transpose(x),np.dot(coeff.a,x)) + np.dot(np.transpose(coeff.b),x)+coeff.c)
        if(type == "g"): #gradient descent
            diff = learnRate * (np.dot(2,np.dot(coeff.a, x))+ coeff.b)
#           diff = learnRate * (np.transpose(b) + np.dot(a,np.transpose(x)) + np.dot(np.transpose(a), np.transpose(x))) #learnRate*(3*a*x**2 + 2*b*x + c)
        elif(type == "n"): #newton's formula

            diff =  learnRate * np.divide(np.dot(np.transpose(x),np.dot(coeff.a,x)) + np.dot(np.transpose(coeff.b),x)+coeff.c  ,np.dot(2,np.dot(coeff.a, x))+ coeff.b) 
#           diff =  learnRate * np.divide(np.dot(2,np.dot(a, x))+ b ,np.dot(2,a)) 
#           diff =  learnRate * np.divide((np.transpose(b) + np.dot(a,np.transpose(x)) + np.dot(np.transpose(a), np.transpose(x))),(a+np.transpose(a))) 
#           learnRate * (c+ np.dot(np.transpose(b), x) + np.dot(np.transpose(x), np.dot(a, x)))/(b + np.dot(a,x) + np.dot(np.transpose(a), x)) #learnRate * (a*x**3+b*x**2+c*x+d)/(3*a*x**2+2*b*x+c)
        else:
            raise "TypeError"
        if(np.all(np.abs(diff) <= stopConditions.tolerance)):
            print("Terminated by Tolerance stop condition")
            break
        if(time.time()- startTime >= stopConditions.timeout):
            print("Terminated by Timeout stop condition")
            break
        x = x - diff
        if(np.all(np.abs(x) <= stopConditions.desiredValue)):
            print("Terminated by desired value stop condition")
            break
        k = k+1
    print(x)
    print(k)
    return x


def optimalisationFRandom(type, uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
    print("\noptimalisationFRandom called")
    x = np.random.normal((uniformDistributionRange[1] + uniformDistributionRange[0]) / 2, (uniformDistributionRange[1] - uniformDistributionRange[0]) / 6)
    return optimalisationF(type, coeff, x, stopConditions, learnRate)


def optimalisationFRandomN(type, n, uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
    print("optimalisationFRandomN called")
    x_values = []
    for i in range(n):
        x_values.append(optimalisationFRandom(type, uniformDistributionRange, coeff, stopConditions, learnRate))
    print(x_values) 
    print("standard deviation: ",np.std(x_values))
    print("mean value: ", np.mean(x_values))
    




def optimalisationGRandom(type, uniformDistributionRange, coeff, stopConditions, learnRate = 0.2):
   # print("optimalisationGRandom to be implemented")
    print("\noptimalisationGRandom called")
    x = []
    for i in range(len(coeff.b)):
        x.append(np.random.normal((uniformDistributionRange[1] + uniformDistributionRange[0]) / 2, (uniformDistributionRange[1] - uniformDistributionRange[0]) / 6))
    
    return optimalisationG(type, coeff, x, stopConditions, learnRate)

def optimalisationGRandomN(type, n, uniformDistributionRange, coeff, stopConditions, learnRate = 0.2):
    #print("optimalisationGRandomN to be implemented")
    print("\noptimalisationGRandomN called")
    x_values = []
    for i in range(n):
        x_values.append(optimalisationGRandom(type, uniformDistributionRange, coeff, stopConditions, learnRate))
    standardDeriviations = []
    meanValues = []
    for i in range(n):
        standardDeriviations.append(np.std(x_values[i]))
        meanValues.append(np.mean(x_values[i]))
    print("standard deriviations: ", standardDeriviations)
    print("mean values: ", meanValues)
