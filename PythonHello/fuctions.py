def square(x):
    #square is defined and its goin to take one arguement x
    return x * x
    #if x is handed over, x squared will be returned
for i in range(10):
        #a loop for 0 to 9
    print("{} squared is {}".format(i,square(i)))
