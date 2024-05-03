import sys
#Template for writing any python program
def main(arg):
 print(arg)
 print("Hello Weekday",arg[1])

#To trigger the 1000 lines of code, we need to creat a control (main())
if __name__=="__main__": #From here you start our python program
    if len(sys.argv)>=2:
        main(sys.argv)#the name of the module
    else:
        print("no enough argument passed to run our program")
        exit()
