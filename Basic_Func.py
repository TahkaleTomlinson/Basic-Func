User = input("Who is the current user:")

def greet():
     print("Hello "+ User)
greet()

day = input("How has your day been:")
if day == "good":
    function= input("Wonderful, What is the Function that you want to use")
if day == "bad":
    function=input("Sorry to hear that, but maybe a Function would make your day better. What is the Function that you want to use:")

def calc():
    n1= float(input("What is your first desired number:"))
    n2= float(input("What is your second desired number:"))
    operator= input("What is the operator that you want to use:")
    if operator == "+":
       answer = n1 + n2
       print(n1, "+", n2, "=", answer)
    elif operator == "-":
       answer = n1 - n2
       print(n1, "-", n2, "=", answer)
    elif operator == "/":
       answer = n1 / n2
       print(n1, "/", n2, "=", answer)
    elif operator == "*":
       answer = n1 * n2
       print(n1, "*", n2, "=", answer)

if function == "Calc":
    calc()
