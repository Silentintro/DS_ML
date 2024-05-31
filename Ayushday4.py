## while loop

# i=1
# while i<6:
#     print(i)
#     i+=1
# i=1
# while i<6:
#     print(i)
    # if i==3:
    #     break
    # i+=1

    # i=0
    # while i<6:
    #     i+=1
    # if i==3:
    #  continue
    # print(i)

    # i=1
    # while i<6:
        
    #     i+=1
            
    #     print("i is no longer 6")

## function

# def my_function():
#       print("hello from a function")
# my_function()
        

# def my_function1(fname):
#     print(fname + "singh")

# my_function1("Ayush")
# my_function1("vijay")

# def add(num1,num2):
#  result= (num1 + num2)
#  return result
# num1=200 
# num2=399
# output = add (num1,num2)
# print(output)


# def my_function2(*kids):
#     print(" the youngest child is " + kids[2])
# my_function2("rohan","vijay","Ayush")

# def my_country(country ="india"):
#     print("i am from " + country)
# my_country("new york")  
# my_country()
# my_country("russia")   
    
# def square_element(input_list):
#     temp=[]
#     for x in input_list:
#         temp.append(x**2)
#     return temp
# output= square_element([2,4,7,8,5])
# print(output)

# def average(input_list):
#     n=sum(input_list)
#     h=len(input_list)
   
#     return  n/h
# print(average([2,5,2]))

# def apna_min(lst):
#     minimum =x[0]
#     for i in lst:
#         if minimum>i:
#            minimum = i
#     return minimum
# x=[78,46,98,5,8,7,]
# print(apna_min(x))



## lambda function

def my_function(n):
    return lambda a:a*n

triple = my_function(3)
print(triple(22)) 