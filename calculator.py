#creating a calculator

x = input("do you want to start?(yes/no)")
x = x.lower()
y = "yes"
if x == "yes":
    print("+ : add , - : substract ,* : multiply , / :divide ,mod : modulus , ^ : power")
    while y == "yes":
        n1 = int(input("enter number :"))
        while x == "yes":
            print(n1)
            op = input("enter operator :")

            if op == "+":
                n2 = int(input("enter number :"))
                n1 = n1 + n2
            elif op == "-":
                n2 = int(input("enter number :"))
                n1 = n1 - n2
            elif op == "*":
                n2 = int(input("enter number :"))
                n1 = n1 * n2
            elif op == "/":
                n2 = int(input("enter number :"))
                if n2 == 0:
                    print("not defined")
                else:
                    n1 = n1 / n2

            elif op == "mod":
                if n1 >= 0:
                    n1 = n1
                else:
                    n1 = -n1
            elif op == "^":
                n2 = int(input("enter number :"))
                n1 = n1 ** n2
            else:
                print('enter correct operator')
            x = input("do you wish to continue ?(yes/no):")
            x = x.lower()

        y = input("do you want to clear all input and restart your calculations?(yes/no)").lower()
        if y == "yes":
            x = "yes"


        print("your final answer is:",n1)

else:
    print("grateful for your visit!")
    print("come again next time!")
    print("('u')")
