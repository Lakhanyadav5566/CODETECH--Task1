# Creating a simple Calculator using python
# first we taking input from user

a =float(input("enter your first number: "))
operator=input("enter operator(+,-,*,/): ")
b =float(input("enter your second number: "))

def calc(a,b,operator):

    if operator == "+":        
        return  a+b
        
    elif operator == "-":
        return a-b
        
    elif operator == "*":
         return a*b
        
    elif operator == "/":

        if (b != 0):      # using nesting condition 
            return a/b
            
        else:
            print("Error! zero division error")
    elif operator == "%":   
        return a%b
    else: 
        print("invalid")

# performing the calculation and display the result
calculator = calc(a,b,operator)
print(f"The result is: {calculator}")
