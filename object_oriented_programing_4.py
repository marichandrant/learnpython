#oops (advanced) - we will learn sometime later-> inheritance, polymorphism, abstraction, encapsulation, overloading, overriding (not much important for a Data Engineer)
#oops (core) - we will learn right now -> Hierarchy of programming -> package, subpackage, module, class, members, objects/constructor, variable, function/methods (important for everyone including Data Engineers)
#How to develop a typical python application?
#How to develop a typical spark application, by transforming from python to spark (pyspark)?

print("#oops (core) - we will learn right now -> Hierarchy of programming -> package, subpackage, module, class, members, objects/constructor, variable, function/methods (important for everyone including Data Engineers)")
print("1. Hierarchy of programming - If I wanted to create a python application, we need to go in a way of defining hierarchical programs")
#project -> package -> sub pkg -> module (py file) -> variables/methods/functions (We did this already, this is a regularly followed practice) -
# If Data engineer ask a Data engineer to develop a spark application to perform end to end etl (weblog example)
# If a Data engineer is going to develop some standalone/custom application (with some custom functionalities) and consume that application for his ETL pipeline ?
#project -> package -> sub pkg -> module (py file) -> classes -> variables/methods/functions -> objects + constructors (We are going to learn, this is a not a regularly followed practice)

print("a. Let's understand 'hierarchy of program' by creating project -> package -> sub pkg -> module (py file) -> classes -> methods")
#We went and creted learn->oops->common_module.py->emp_sal_management() & emp_leave_management() -> created few methods..
class emp_sal_management():#default constructor, parameterized /non-parameterized constructor
    def sal_bon(self,sal,bon):#members of the class (member function/member methods)
        return sal+bon
    def sal_bon_inc(self,sal,bon,inc):
        return sal+bon+inc

print("b. Let's know how to invoke/refer the classes & methods developed by us or somebody in 3 possible ways (finalize one way which ever is better)")
#1. one way of invoking the module/class
import learn.oops.common_module #create a link/reference to the module where the classes are there (not an advisable methodology)
invoke_class=learn.oops.common_module.emp_leave_management #we must use the full name to reference the class.

#2. another way of invoking the module/class
from learn.oops import common_module #Import the module where the classes are there (not an advisable methodology)
invoke_class=common_module.emp_leave_management #we must use the module name to reference the class.

#3. another way of invoking the module/class (IMPORTANT TO KNOW)
from learn.oops.common_module import * #Import all the classes inside the given module (advisable methodology)
from learn.oops.common_module import emp_sal_management_dc #Import all the classes inside the given module (advisable methodology)
from learn.oops.common_module import emp_leave_management #Import all the classes inside the given module (advisable methodology)
invoke_class1=emp_sal_management #directly reference the class.
invoke_class2=emp_leave_management#directly reference the class.

print("c. How do we make use of class by creating objects & constructors - Important")
print("What is classes and objects+constructor")
print("What is a class ? -> Class is a template/blueprint comprised of the programs in a form of functions and variables")
print("What is a object ? -> Object is an instance of a class or classes are instantiated/loaded in the memory in a variable called object")
print("What is a constructor ? -> We can instantiate the classess in objects by constructing the memory with different parameters/no parameters/default parameters")

#lets try to understand what is class, object, instance of the class in a simple way using xls sheet
#folders where xls stored is pkg.subpkg.module
#xls is the class
#tabs inside the xls is the members (methods/functions) of the class
#loading the xls in memory is the object (instance of the class)

#let's crate an object to refer the class members... (Minumum understanding of Classes and objects)
from learn.oops.common_module import emp_sal_management_dc#First we import the module and all/specific class
doubleclick_load_in_ram_object=emp_sal_management_dc()#Second - We create an object to load/instantiate class in memory by giving ()
print(doubleclick_load_in_ram_object.sal_bon(10000,1000))#Third - We can access the members of the class
print(doubleclick_load_in_ram_object.sal_bon_inc(10000,1000,500)) #Third - We can access the members of the class

from learn.oops.common_module import clsname#import the class
obj1=clsname("Irfan")#instantiate the class as object (construct the class in memory) #parameterized constructor
print(obj1.mem1())#refer/invoke the members of the class
print(obj1.mem2())

obj1=clsname("Prem")#instantiate the class as object (construct the class in memory)
print(obj1.mem1())#refer/invoke the members of the class
print(obj1.mem2())


#Let us instantiate/construct/initialize the class in a form of object using default/param/non-param constructors
print("Let us instantiate/construct/initialize the class in a form of object using default/param/non-param constructors")
print("Default Constructor")
from learn.oops.common_module import *
#Default constructor - construct the class with the default init function managed by python
obj1_def_cons=emp_sal_management_dc()
print(obj1_def_cons.sal_bon(10000,1500))
print(obj1_def_cons.sal_bon_inc(10000,1500,500))

print("Non-Parameterized constructor")
#Non-Parameterized constructor - construct the class with the init function defined with bonus (class variable) value hardcoded
obj2_def_cons=emp_sal_management_npc()
print(obj2_def_cons.sal_bon(10000))
print(obj2_def_cons.sal_bon_inc(10000,500))

print("Parameterized constructor")
#Parameterized constructor - construct the class with the init function defined with bonus (class variable) value passed as a parameter
IT_obj3_def_cons=emp_sal_management_pc(2000)
print(IT_obj3_def_cons.sal_bon(10000))
print(IT_obj3_def_cons.sal_bon_inc(10000,500))

MKT_obj3_def_cons=emp_sal_management_pc(3000)
print(MKT_obj3_def_cons.sal_bon(10000))
print(MKT_obj3_def_cons.sal_bon_inc(10000,500))








