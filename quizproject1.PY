import Mysql.connector



def CBASICQUIZ():
    ans=0
    print("Q1.Who is the father of C language?")
    print('''              1) Steve Jobs
              2) James Gosling
              3) Dennis Ritchie
              4) Rasmus Lerdorf''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q2.Which of the following is not a valid C variable name?")
    print('''               1) int number;
                2) float rate;
                3) int variable_count;
                4) int $main; ''')
    k=int(input())
    if(k==4):
        ans +=1
    print(ans)

    print("Q3.All keywords in C are in ____________")
    print('''              1) LowerCase letters
              2) UpperCase letters
              3) CamelCase letters
              4) None of the mentioned''')
    k=int(input())
    if(k==4):
        ans +=1
    print(ans)

    print("Q4.Which of the following is true for variable names in C?")
    print('''              1) They can contain alphanumeric characters as well as special characters
              2) It is not an error to declare a variable to be one of the keywords(like goto, static)
              3) Variable names cannot start with a digit
              4) Variable can be of any length''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q5.Which is valid C expression?")
    print('''              1) int my_num = 100,000;
              2) int my_num = 100000;
              3) int my num = 1000;
              4) int $my_num = 10000;''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print("Q6.Which of the following cannot be a variable name in C?")
    print('''              1) volatile
              2) true
              3) friend
              4) export''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)


    print("Q7.What is short int in C programming?")
    print('''              1) The basic data type of C
              2) Qualifier
              3) Short is the qualifier and int is the basic data type
              4) All of the mentioned''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q8.Which of the following declaration is not supported by C language?")
    print('''              1) String str;
              2) char *str;
              3) float str = 3e2;
              4) Both String str; & float str = 3e2;''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print("Q9.Which keyword is used to prevent any changes in the variable within a C program?")
    print('''              1) immutable
              2) mutable
              3) const
              4) volatile''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q10.What is the result of logical or relational expression in C?")
    print('''              1) True or False
              2) 0 or 1
              3) 0 if an expression is false and any positive number if an expression is true
              4) None of the mentioned''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)
    print(" ")
    print("YOUR FINAL RESULT IS:--->",ans)

def CADVQUIZ():
    ans=0
    print('''Q1.How many times LNCTU is printed?

            int main()
            {
                while(1)
                {
                  printf("LNCTU.com");
                }

            return 0;
            }''')
    print('''              1) One time
              2) Compilation Error
              3) Infinite times
              4) Runtime Error''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)


    print('''Q2.What is output of below program?)

    int main()
    {
    int i,j,count;
    count=0;
    for(i=0; i<5; i++);
    { 
	for(j=0;j<5;j++);
	{
	    count++;
	}
    }
    printf("%d",count);
    return 0;
    }''')

    print('''              1) 55
              2) 54
              3) 1
              4) 0''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print('''Q3.What is output of below program?

                int main()
                {
                  int i;
                  for(i=0; i<5; i++);
                    {
                      printf("cppbuzz");
                    }

                return 0;
                }''')

    print('''              1) cppbuzz is printed 5 times
              2) Compilation Error
              3) cppbuzz is printed 1 times
              4) Nothing is printed''')

    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print('''Q4.What is output of below program?

                int main()
                {
                 int i,j,k,count;
                 count=0;
                 for(i=0;i<5;i++)
                    {
                       for(j=0;j<5;j++)
                           {
                              count++;
                           }
                    }
                printf("%d",count);
                return 0;
                }''')
    print('''              1) 5
              2) 10
              3) 25
              4) 50''')

    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print('''Q5.What is output of below program?
    int main()
    {
     int i,j;
     for(i = 0,j=0;i<5;i++)
     {
       printf("%d%d--",i,j);
     }
     return 0;
    }''')
    print('''              1) 0--01--12--23--34--
              2) 00--10--20--30--40--
              3) Compilation Error
              4) 00--01--02--03--04-- ''')

    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print('''Q6.What is output of below program?

    int main()
    {
     int i;
     for(i=0; i<5; ++i++)
     {
       printf("Hello");
     }
     return 0;
    }''')
    print('''              1) Hello is printed 5 times
              2) Compilation Error
              3) Hello is printed 2 times
              4) Hello is printed 3 times ''')

    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print('''Q7.What is the output of below program?
    int main()
    {
     int i;

     for(i = 0,i<5,i++)
     {
       printf("Hello");
     }

     return 0;
    }''')


    print('''              1) Hello is printed 5 times
              2) Compilation Error
              3) Runtime Error
              4) Hello is printed 4 times''')

    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print('''Q8.What is output of below program?

    int main()
    {
     for(; ;);
     for(; ;);
        printf("Hello");
    return 0;
    }''')


    print('''              1) Compilation Error
              2) Runtime Error
              3) Nothing is printed
              4) Hello is printed infinite times ''')

    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print('''Q9.What is the output of below program?

    int main()
    {
    for(; ;)
    for(; ;)
        printf("Hello..");

    return 0;
    }''')
    print('''              1) Compilation Error
              2) Runtime Error
              3) Hello is printed one time
              4) Hello is printed infinite times ''')

    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q10.What is the meaning of below lines?
    void sum (int, int);''')
    print('''              1) sum is function which takes int arguments
              2) sum is a function which takes two int arguments and returns void
              3) it will produce compilation error
              4) Can't comment''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)
    print(" ")
    print("YOUR FINAL RESULT IN C ADVANCE:---> ",ans)

def JAVABASICQUIZ():
    ans=0
    print("Q1.Who invented Java Programming?")
    print('''              1) Guido van Rossum
              b) James Gosling
              c) Dennis Ritchie
              d) Bjarne Stroustrup''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print("Q2.Which statement is true about Java?")
    print('''              1) Java is a sequence-dependent programming language
              2) Java is a code dependent programming language
              3) Java is a platform-dependent programming language
              4) Java is a platform-independent programming language''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print("Q3.Which component is used to compile, debug and execute the java programs?")
    print('''              1) JRE
              2) JIT
              3) JDK
              4) JVM''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q4.Which one of the following is not a Java feature?")
    print('''              1) Object-oriented
              2) Use of pointers
              3) Portable
              4) Dynamic and Extensible''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print("Q5.Which of these cannot be used for a variable name in Java?")
    print('''              1) identifier & keyword
              2) identifier
              3) keyword
              4) none of the mentioned''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q6.What is the extension of java code files?")
    print('''              1) .js
              2) .txt
              3) .class
              4) .java''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print("Q7. What is Truncation in Java?")
    print('''              1) Floating-point value assigned to a Floating type
              2) Floating-point value assigned to an integer type
              3) Integer value assigned to floating type
              4) Integer value assigned to floating type''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print("Q8. What is the extension of compiled java classes?")
    print('''              1) .txt
              2) .js
              3) .class
              4) .java''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q9. Which exception is thrown when java is out of memory?")
    print('''              1) MemoryError
                2) OutOfMemoryError
                3) MemoryOutOfBoundsException
                4) MemoryFullException''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print("Q10.Which of these are selection statements in Java?")
    print('''              1) break
              2) continue
              3) for()
              4) if()''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

def JAVADVANCE():
    ans=0

    print('''Q1.What will be the output of the following Java code?

    class increment {
        public static void main(String args[]) 
        {        
             int g = 3;
             System.out.print(++g * 8);
        } 
    }''')
    print('''              1) 32
              2) 33
              3) 24
              4) 25''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print('''Q2.What will be the output of the following Java program?

    class output {
        public static void main(String args[]) 
        {
            double a, b,c;
            a = 3.0/0;
            b = 0/4.0;
            c=0/0.0;
 
	    System.out.println(a);
            System.out.println(b);
            System.out.println(c);
        } 
    }''')
    print('''              1) NaN
              2) Infinity
              3) 0.0
              4) all of the mentioned''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q3.What will be the output of the following Java program?

    class variable_scope 
    {
        public static void main(String args[]) 
        {
            int x;
            x = 5;
            {
	        int y = 6;
	        System.out.print(x + " " + y);
            }
            System.out.println(x + " " + y);
        } 
    }''')
    print('''              1) Compilation error
              2) Runtime error
              3) 5 6 5 6
              4) 5 6 5''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print('''Q4.What will be the error in the following Java code?

    byte b = 50;
    b = b * 50;''')
    print('''              1) b cannot contain value 50
              2) b cannot contain value 100, limited by its range
              3) No error in this code
              4) * operator has converted b * 50 into int, which can not be converted to byte without casting''')

    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q5.What will be the output of the following Java program?

    class leftshift_operator 
    {
        public static void main(String args[]) 
        {        
             byte x = 64;
             int i;
             byte y; 
             i = x << 2;
             y = (byte) (x << 2)
             System.out.print(i + " " + y);
        } 
    }''')
    print('''              1) 0 256
              2) 0 64
              3) 256 0
              4) 64 0''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print('''Q6.What will be the output of the following Java program?

    class Output 
    {
        public static void main(String args[])
        {
            int arr[] = {1, 2, 3, 4, 5};
            for ( int i = 0; i < arr.length - 2; ++i)
                System.out.println(arr[i] + " ");
        } 
    }''')
    print('''              1) 1 2 3 4 5
              2) 1 2 3 4
              3) 1 2
              4) 1 2 3''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q7.What will be the output of the following Java code snippet?

    class abc
    {
        public static void main(String args[])
    {
        if(args.length>0)
        System.out.println(args.length);
    }
    }''')
    print('''              1) The snippet compiles and runs but does not print anything
              2) The snippet compiles, runs and prints
              3) The snippet compiles, runs and prints 1
              4) The snippet does not compile''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print('''Q8.What will be the output of the following Java code?

    class String_demo 
    {
        public static void main(String args[])
        {
            char chars[] = {'a', 'b', 'c'};
            String s = new String(chars);
            System.out.println(s);
        }
   }''')
    print('''              1) abc
              2) a
              3) b
              4) c''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans) 

    print('''Q9.What will be the output of the following Java code?

    class output 
    {
        public static void main(String args[])
        { 
           String c = "Hello i love java";
           boolean var;
           var = c.startsWith("hello");
           System.out.println(var);
        }
    }''')
    print('''              1) 0
              2) true
              3) 1
              4) false''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q10.What will be the output of the following Java code?

    class Output 
    {
        public static void main(String args[]) 
        {
            Integer i = new Integer(257);  
            byte x = i.byteValue();
            System.out.print(x);
        }
    }''')
    print('''              1) 257
              2) 256
              3) 1
              4) 0''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("  ")
    print("YOUR FINAL RESULYT IS:--->",ans)

def PYTHONBASIC():
    ans=0
    print(" ")
    print("Q1.Who developed Python Programming Language?")
    print('''              1) Wick van Rossum
              2) Rasmus Lerdorf
              3) Guido van Rossum
              4) Niene Stom''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q2.Which type of Programming does Python support?")
    print('''              1) object-oriented programming
              2) structured programming
              3) functional programming
              4) all of the mentioned''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print("Q3.Is Python case sensitive when dealing with identifiers?")
    print('''              1) no
              2) yes
              3) machine dependent
              4) none of the mentioned''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print("Q4.Which of the following is the correct extension of the Python file?")
    print('''              1) .python
              b) .pl
              c) .py
              d) .p''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q5.Is Python code compiled or interpreted?")
    print('''              1) Python code is both compiled and interpreted
              2) Python code is neither compiled nor interpreted
              3) Python code is only compiled
              4) Python code is only interpreted''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print("Q6.All keywords in Python are in _________")
    print('''              1) Capitalized
              2) lower case
              3) UPPER CASE
              4) None of the mentioned''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q7.prinWhat will be the value of the following Python expression?)

                             4 + 3 % 5''')
    print('''              1) 7
              2) 2
              3) 4
              4) 1''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)
    
    print("Q8.Which of the following is used to define a block of code in Python language?")
    print('''              1) Indentation
              2) Key
              3) Brackets
              4) All of the mentioned''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print("Q9.Which keyword is used for function in Python language?")
    print('''              1) Function
              2) Def
              3) Fun
              4) Define''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)
    
    print("Q10.Which of the following character is used to give single-line comments in Python?")
    print('''              1) //
              2) #
              3) !
              4) /*''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)
    print(" ")
    print("YOUR FINAL RESULT:--->",ans)



def PYTHONADVANCE():
    ans=0

    print('''Q1.The following python program can work with ____ parameters.

    def f(x):
    def f1(*args, **kwargs):
           print("Sanfoundry")
           return x(*args, **kwargs)
    return f1''')
    print('''              1) any number of
              2) 0
              3) 1
              4) 2''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)


    print('''Q2.What will be the output of the following Python code?

    x = 'abcd'
    for i in x:
    print(i.upper())''')
    print('''              1) a B C D
              2) a b c d
              3) error
              4) A B C D''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)


    print('''Q3.What will be the output of the following Python code snippet?

            for i in [1, 2, 3, 4][::-1]:
            print (i)''')
    print('''              1) 4 3 2 1
              2) error
              3) 1 2 3 4
              4) none of the mentioned''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)


    print("Q4.Which module in the python standard library parses options received from the command line?")
    print('''              1) getarg
              2) getopt
              3) main
              4) os''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)


    print('''Q5.What will be the output of the following Python program?

z=set('abc')
z.add('san')
z.update(set(['p', 'q']))
z''')
    print('''              1) {‘a’, ‘c’, ‘c’, ‘p’, ‘q’, ‘s’, ‘a’, ‘n’}
              2) {‘abc’, ‘p’, ‘q’, ‘san’}
              3) {‘a’, ‘b’, ‘c’, ‘p’, ‘q’, ‘san’}
              4) {‘a’, ‘b’, ‘c’, [‘p’, ‘q’], ‘san}''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)


    print('''Q6.What will be the output of the following Python code?

            print("abc. DEF".capitalize())''')
    print('''              1) Abc. def
              2) abc. def
              3) Abc. Def
              4) ABC. DEF''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print("Q7.Which of the following statements is used to create an empty set in Python?")
    print('''              1) ( )
              2) [ ]
              3) { }
              4) set()''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)


    print('''Q8.What will be the value of ‘result’ in following Python program?

    list1 = [1,2,3,4]
    list2 = [2,4,5,6]
    list3 = [2,6,7,8]
    result = list()
    result.extend(i for i in list1 if i not in (list2+list3) and i not in result)
    result.extend(i for i in list2 if i not in (list1+list3) and i not in result)
    result.extend(i for i in list3 if i not in (list1+list2) and i not in result)''')
    print('''              1) [1, 3, 5, 7, 8]
              2) [1, 7, 8]
              3) [1, 2, 4, 7, 8]
              4) error''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)


    print("Q9.To add a new element to a list we use which Python command?")
    print('''              1) list1.addEnd(5)
              2) list1.addLast(5)
              3) list1.append(5)
              4) list1.add(5)''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print('''Q10.What will be the output of the following Python code?

            print('*', "abcde".center(6), '*', sep='')''')
    print('''              1) * abcde *
              2) *abcde *
              3) * abcde*
              4) * abcde *  ''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)
    print(" ")
    print("YOUR FINAL RESULT:--->",ans)




def CPBASIC():
    ans=0

    print("Q1.Who invented C++?")
    print('''              a) Dennis Ritchie
              2) Ken Thompson
              3) Brian Kernighan
              4) Bjarne Stroustrup''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print("Q2.What is C++?")
    print('''1              1) C++ is an object oriented programming language
              2) C++ is a procedural programming language
              3) C++ supports both procedural and object oriented programming language
              4) C++ is a functional programming language''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q3.Which of the following is the correct syntax of including a user defined header files in C++?")
    print('''              1) #include [userdefined]
              2) #include “userdefined”
              3) #include <userdefined.h>
              4) #include <userdefined>''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print("Q4.Which of the following is used for comments in C++?")
    print('''              1) /* comment */
              2) // comment */
              3) // comment
              4) both // comment or /* comment */''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print("Q5.Which of the following user-defined header file extension used in c++?")
    print('''              1) hg
              2) cpp
              3) h
              4) hf''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("Q6.Which of the following is a correct identifier in C++?")
    print('''              1) VAR_1234
              2) $var_name
              3) 7VARNAME
              4) 7var_name''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print("Q7.Which of the following is not a type of Constructor in C++?")
    print('''              1) Default constructor
              2) Parameterized constructor
              3) Copy constructor
              4) Friend constructor''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)


    print("Q8.Which of the following approach is used by C++?")
    print('''              1) Left-right
              2) Right-left
              3) Bottom-up
              4) Top-down''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

    print("What is virtual inheritance in C++?")
    print('''              1) C++ technique to enhance multiple inheritance
              2) C++ technique to ensure that a private member of the base class can be accessed somehow
              3) C++ technique to avoid multiple inheritances of classes
              4) C++ technique to avoid multiple copies of the base class into children/derived class''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)
    

    print('''Q10.What will be the output of the following C++ code snippet?

    #include <stdio.h>
    #include<iostream>
    using namespace std;
    int main ()
    {
        int array[] = {0, 2, 4, 6, 7, 5, 3};
        int n, result = 0;
        for (n = 0; n < 8; n++) 
        {
            result += array[n];
        }
        cout << result;
        return 0;
    }''')
    print('''              a) 21
              b) 27
              c) 26
              d) 25''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print("Q10.By default, all the files in C++ are opened in _________ mode.")
    print('''              1) Binary
              2) VTC
              3) Text
              4) ISCII''')
    k=int(input())
    if(k==3):
        ans+=1
    print(ans)

def CPADVANCE():
    ans=0
    print('''Q1.What will be the output of the following C++ function?

    int main()
    {
        register int i = 1;
        int *ptr = &i;
        cout << *ptr;
	return 0;
    }''')
    print('''              1) Runtime error may be possible
              2) Compiler error may be possible
              3) 1
              4) 0''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print('''Q2.What will be the output of the following C++ code?

    #include<iostream>
    using namespace std;
    int main ()
    {
   int cin;
   cin >> cin;
   cout << "cin: " << cin;
   return 0;
    }''')
    print('''              1) Segmentation fault
              2) Nothing is printed
              3) Error
              4) cin: garbage value''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q3.What will be the output of the following C++ program?

    #include <iostream> 
    #include <string>
    #include <cstring>
    using namespace std; 
    int main(int argc, char const *argv[])
    {
	const char *a = "Hello\0World";
	cout<<a;
	return 0;
    }''')
    print('''              1) Hello
              2) World
              3) Error
              4) Hello World''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print('''Q4.What will be the output of the following C++ code?

    #include <iostream>
    using namespace std;
    int main()
    {
        char c = 74;
        cout << c;
        return 0;
    }''')
    print('''              a) I
              2) J
              3) A
              4) N''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print('''Q5.What will be the output of the following C++ program?

    #include <iomanip>
    #include <iostream>
    using namespace std;
    int main()
    {
        cout << setprecision(17);
        double d = 0.1;
        cout << d << endl;
        return 0;
    }''')
    print('''              1) compile time error
              2) 0.100001
              3) 0.11
              4) 0.10000000000000001''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print('''Q6.What will be the output of the following C++ code?

    #include <iostream>
    using namespace std;
    int main()
    {
        int a = 5;
        float b;
        cout << sizeof(++a + b);
        cout << a;
        return 0;
    }''')
    print('''              1) 2 5
              2) 4 5
              3) 4 6
              4) 2 6''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)

    print('''Q7.What will be the output of the following C++ program?

    #include <iostream>
    #include <string>
    using namespace std;
    int main ()
    {
      std::string str ("Sanfoundry.");
      str.back() = '!';
      std::cout << str << endl;
      return 0;
    }''')
    print('''              1) Sanfoundry!
              2) Sanfoundry!.
              3) Sanfoundry.
              4) Sanfoundry.!''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print('''Q8.What will be the output of the following C++ program?

    #include <iostream>
    using namespace std;
    int main()
    {
        int n = 5;
        void *p = &n;
        int *pi = static_cast<int*>(p);
        cout << *pi << endl;
        return 0;
    }''')
    print('''              1) 5
              2) 6
              3) compile time error
              4) runtime error''')
    k=int(input())
    if(k==1):
        ans+=1
    print(ans)

    print('''Q9.What will be the output of the following C++ code?

    #include <iostream>
    using namespace std;
    int main ()
    {
        int a, b, c;
        a = 2;
        b = 7;
        c = (a > b) ? a : b;
        cout << c;
        return 0;
    }''')
    print('''              1) 12
              2) 14
              3) 6
              4) 7''')
    k=int(input())
    if(k==4):
        ans+=1
    print(ans)

    print(''''Q10.What will be the output of the following C++ code snippet?

    #include <stdio.h>
    #include<iostream>
    using namespace std;
    int main ()
    {
        int array[] = {0, 2, 4, 6, 7, 5, 3};
        int n, result = 0;
        for (n = 0; n < 8; n++) 
        {
            result += array[n];
        }
        cout << result;
        return 0;
    }''')
    print('''              1) 21
              2) 27
              3) 26
              4) 25''')
    k=int(input())
    if(k==2):
        ans+=1
    print(ans)
    print(" ")
    print("YOUR FINAL RESULT:--->",ans)

           
def REGISTRATION():
    connection = mysql.connector.connect(user='root', password='system', host='localhost',database='quizdb')
    Cursor = connection.cursor(prepared=True)
    Cursor.execute("select count (*) from REGISTRATION")

    
    print("ENTER YOUR DETAIL'S")
    print(" ")
    NAME=input("Enter Your Name:----> ")
    print(" ")
    FATHER_NAME=input("ENTER YOUR FATHER'S NAME:---> ")
    print(" ")
    MOBILE_NO=input("ENTER YOUR MOBILE NUMBER:---> ")
    print(" ")
    EMAIL_ID=input("ENTER YOUR EMAIL ID:---> ")
    print(" ")
    ADDRESS=input("ENTER YOUR ADDRESS:---> ")
    print(" ")
    EDUCATION=input("ENTER YOUR QUALIFICATION:---> ")
    print(" ")
    print("             REGISTRATION SUCCESSFULLY")
    print("               THANK YOU")
    print("       YOUR DETAIL'S IS      ")
    print("")
    print("YOUR NAME IS",NAME)
    print("YOUR FATHER'S NAMNE IS ",FATHER_NAME)
    print("    CONTACT DETAIL'S    ")
    print(" ")
    print("YOUR MOBILE NUMBER IS",MOBILE_NO)
    print("YOUR EMAIL_ID ",EMAIL_ID)
    print("YOUR ADDRESS IS ",ADDRESS)
    print("YOUR QUALIFIACATION IS ",EDUCATION)

    
    K=(list(Cursor))
    for i in k:
        m=(i[0])
        if(m<=8):
            m=m+1
    
            ID='STUDQZ'+'0'+str(m)
        
        else:
            m=m+1
    
            ID='STUDQZ'+str(m)
            
    Qry = ("INSERT INTO REGISTRATION VALUES(%s, %s, %s, %s, %s, %s,%S)")
    val=(ID,NAME,FATHER_NAME,MOBILE_NO,EMAIL_ID,ADDRESS,EDUCATION)
    Cursor.execute(Qry,val)
    connection.commit()
    Cursor.close()

    
          

def LOGIN():
    USER=input("ENTER YOUR EMAIL ID:--->")
    print(" ")
    PASSWORD=input("ENTER YOUR PASSWORD:--->")
    print(" ")

def START():
    LOOP=0
    print("================================================================================")
    print("============================    QUIZZZ    ======================================")
    print("================================================================================")
    print("PRESS 1 FOR REGISTRATION")
    print(" ")
    print("PRESS 2 FOR LOGIN")
    print(" ")
    print("PRESS 3 FOR UPDATE RECORD")
    print(" ")
    INPUT=int(input())
    if(INPUT==1):
        REGISTRATION()
    elif(INPUT==2):
        LOGIN()
    elif(INPUT==3):
        UPDATE_RECORD()
    else:
        print("WRONG CHOICE")
    
START()
