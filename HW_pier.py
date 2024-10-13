#Say "Hello, World!" With Python
if __name__ == '__main__':
    stringa = "Hello, World!"
    print(stringa)


#Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2 == 1): 
        print("Weird")
    else: 
        if (2<=n and n<=5): 
            print("Not Weird")
        elif (6<=n and n<=20): 
            print("Weird")
        else:
            print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#################

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

#Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year %400 == 0 ) or (year%4 == 0 and year%100 !=0) :
        leap = True
        
    
    return leap
#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1,end='')

#Mutations
def mutate_string(string, position, character):
    appoggio = string[:position] + character + string[position+1:]
    return appoggio

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse = True)
    for i in arr:
        if i < arr[0] :
            print(i)
            break
########

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup = tuple(integer_list)
    print(hash(tup))
#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lista = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n ]
    print(lista)
#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lista = student_marks[query_name]
    media = 0
    for i in lista:
        media += i
    media /= 3
    print("%.2f" % media)

#Nested Lists
if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
    lista = sorted(lista, key = lambda x : x[1], reverse = False)
    poco , molto = zip(*lista)
    molto = list(molto)
    max_score = float(lista[0][1])
    for j in range(len(lista)):
        if max_score == molto[j]:
            lista.pop(0)
    second_score = float(lista[0][1])
    lista = sorted(lista, key = lambda x : x[0], reverse = False)
    poco , molto = zip(*lista)
    molto , poco = list(molto), list(poco)
    appoggio = []
    for k in range(len(lista)):
        if second_score == molto[k]:
            appoggio.append(poco[k])
for asd in appoggio :
    print(asd)

#sWAP cASEùdef swap_case(s):
    lista = list(s)
    for i in range(len(lista)): 
        if lista[i] == lista[i].upper():
            lista[i] = lista[i].lower()
        else:
            lista[i] = lista[i].upper()
    d = ''
    for j in lista:
        d += j
    return d
#String Split and Join

def split_and_join(line):
    # write your code here
    lista = line.split()
    s= ''
    d = '-'
    for i in range(len(lista)):
        s += lista[i]
        if i != (len(lista)-1):
            s += d
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?

def print_full_name(first, last):
    last += '!'
    print('Hello', first , last,'You just delved into python.')
#Find a string
def count_substring(string, sub_string):
    lista = [i for i in string]
    lista_1 = lista
    altro = [ ]
    for j in range((len(lista_1))-len(sub_string)+1): 
        word = ''
        for k in range(len(sub_string)):
            word += lista[k]
        lista.pop(0)
        altro.append(word)
    counter = 0
    for h in altro :
        if sub_string == h:
            counter += 1
    return counter
#String Validators
if __name__ == '__main__':
    s = input()
    lista = [i for i in s]
    #alfanumeri
    counter = 0
    for j in lista:
        if j.isalnum() == False:
            counter += 1
    if counter == len(lista) : 
        print("False")
    else: 
        print("True")
    #lettere
    counter = 0
    for j_1 in lista:
        if j_1.isalpha() == False:
            counter += 1
    if counter == len(lista) : 
        print("False")
    else: 
        print("True")
    #numeri
    counter = 0
    for j_2 in lista:
        if j_2.isdigit() == False:
            counter += 1
    if counter == len(lista) : 
        print("False")
    else: 
        print("True")
    #lettere minuscole
    counter = 0
    for j_3 in lista:
        if j_3.islower() == False:
            counter += 1
    if counter == len(lista) :
        print("False")
    else: 
        print("True")
        #lettere maiuscole
    counter = 0
    for j_4 in lista:
        if j_4.isupper() == False:
            counter += 1
    if counter == len(lista) : 
        print("False")
    else: 
        print("True")
########
#Text Alignment
 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
def wrap(string, max_width):
    lista = [i for i in string]
    stop = len(lista)
    poi = []
    for j in range(0,stop,max_width):
        unione = ''
        unione = "".join(lista[j:(j+max_width)])
        poi.append(unione)
    string = "\n".join(poi)
    return string
#Lists
if __name__ == '__main__':
    N = int(input())
    lista = [ ]
    for i in range(N):
        comando = input().split()
        if comando[0] == 'insert':
            lista.insert( int(comando[1]), int(comando[2]))
        if comando[0] == 'print':
            print(lista)
        if comando[0] == 'remove': 
            lista.remove(int(comando[1]))
        if comando[0] == 'append':
            lista.append(int(comando[1]))
        if comando[0] == 'sort':
            lista.sort()
        if comando[0] == 'pop':
            lista.pop()
        if comando[0] == 'reverse' :
            lista.reverse()

#Capitalize!

# Complete the solve function below.
def solve(s):
    lista = [i for i in s]
    lista[0] = lista[0].upper()
    stringa = ""
    for i in range(len(lista)):
        stringa += lista[i]
        if lista[i] == " ":
            lista[i+1] = lista[i+1].upper()
    return stringa

#String Formatting
def print_formatted(number):
    # your code goes here
    lunghezza = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(lunghezza," "),str(oct(i)[2:]).rjust(lunghezza," "), str(hex(i)[2:].upper()).rjust(lunghezza," "),str(bin(i)[2:]).rjust(lunghezza," "))
    return
#########
#Introduction to Sets
def average(array):
    # your code goes here
    media = sum(set(array)) / len(set(array))
    return round(media, 3)
#Symmetric Difference

m = int(input())

a = set(map(int, input().split()[:m]))

n = int(input())

b = set(map(int, input().split()[:n]))
lista = list(a.difference(b))
lista_1 = (b.difference(a))
for i1 in lista_1:
    lista.append(i1)
lista.sort()
for i in lista:
    print(i)

#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
dimensioni = list(map(int,input().split()))
vettore = list(map(int ,input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
counter = 0
for i in vettore:
    if i in a:
        counter += 1
    elif i in b:
            counter -= 1
print(counter)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
insieme = set()
for i in range(n):
    name = str(input().split())
    insieme.add(name)
print(len(insieme))
#############
#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N): 
    comando = input().split()
    if comando[0] == 'pop':
        s.pop()
    if comando[0] == 'remove':
        s.remove(int(comando[1]))
    if comando[0] == 'discard':
        s.discard(int(comando[1]))
print(sum(s))
#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
english = int(input())
lista_eng = set(map(int, input().split()))
french = int(input())
lista_fre = set(map(int, input().split()))
unione = set()
lista_eng = lista_eng.union(lista_fre)
print(len(lista_eng))
#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
english = int(input())
set_eng = set(map(int,input().split()))
french = int(input())
set_fre = set(map(int,input().split()))
print(len((set_eng.intersection(set_fre))))
#Set .difference() Operation
eng = int(input())
set_eng = set(map(int,input().split()))
fre = int(input())
set_fre = set(map(int,input().split()))
print(len(set_eng.difference(set_fre)))

#Set .symmetric_difference() Operation
eng = int(input())
s_eng = set(map(int,input().split()))
fre = int(input())
s_fre = set(map(int,input().split()))
print(len(s_eng.symmetric_difference(s_fre)))

#Set Mutations
num_ele = int(input())
a = set(map(int,input().split()))
num_set = int(input())
for i in range(num_set):
    command , num = input().split()
    other = set(map(int, input().split()))
    if command == "intersection_update":
        a &= other
    if command == "update": 
        a |= other
    if command == "symmetric_difference_update":
        a ^= other
    if command == "difference_update":
        a -= other
print(sum(a))

#The Captain's Room
k = int(input())
insieme = list(map(int,input().split()))
dizionario = {}
for i in insieme:
    if dizionario.get(i) == None:
        dizionario[i] = 1
    else:
        dizionario[i] += 1
risposta = min(dizionario, key = dizionario.get)
print(risposta)
#####################
#Check Subset
test = int(input())
for i in range(test):
    ele_a = int(input())
    a = set(map(int, input().split()))
    ele_b = int(input())
    b = set(map(int, input().split()))
    if a.intersection(b) == a:
        print(True)
    else: 
        print(False)

#Check Strict Superset
a = set(map(int,input().split()))
num = int(input())
counter = 0
for i in range(num):
    appoggio = set(map(int,input().split()))
    if (appoggio == appoggio.intersection(a)) and (appoggio != a):
        counter += 1 
if counter == num:
    print(True)
else : 
    print(False)

#Designer Door Mat
n ,m = map(int,input().split())
for i in range(1,(n+1)//2+1):
    if i < ((n+1)//2):
        print((".|."* ((i*2)-1)).center( m ,"-") )
    if i == ((n+1)//2):
        print("WELCOME".center( m ,"-") )
for k in range((n+1)//2 - 1,0,-1):
        print((".|."* ((k*2)-1)).center( m ,"-") )

#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    num_sott = len(string) // k
    for i in range(num_sott):
        parola = string[i*k:(i*k)+k]
        sotto = ""
        for j in range(len(parola)):
            if not(parola[j] in sotto):
                sotto += parola[j]
        print(sotto)
#collections.Counter()
from collections import Counter

num_shoe = int(input())
size_shoe = list(map(int, input().split()))
num_customers = int(input())
size_shoe = Counter(size_shoe)

saldo = 0 

for i in range(num_customers):
    b , c  = map(int, input().split())
    if size_shoe[b] > 0:
        saldo += c
        size_shoe[b] -= 1
print(saldo)

##################
#Calendar Module
import calendar

def stampa_giorno(giorno):
    if giorno == 0:
        print("MONDAY")
    if giorno == 1:
        print("TUESDAY")
    if giorno == 2:
        print("WEDNESDAY")
    if giorno == 3:
        print("THURSDAY")
    if giorno == 4:
        print("FRIDAY")
    if giorno == 5:
        print("SATURDAY")
    if giorno == 6:
        print("SUNDAY")

#stringa = mese giorno anno
stringa = input().split()
anno = int(stringa[2])
mese = int(stringa[0])
giorno = int(stringa[1])
calendario = calendar.TextCalendar(firstweekday = 6 )
week = list(calendario.itermonthdays2(anno,mese))
for i,j in week :
    if i == giorno :
        stampa_giorno(j)

##########
#Exceptions
t = int(input())
for i in range(t):
    a ,b =  input().split()
    if b == '0':
        try:
            print(int(a)/int(b))
        except ZeroDivisionError as e:
            print( "Error Code: integer division or modulo by zero")
    else:
        try:
            print(int(int(a)/int(b)))
        except ValueError as e:
            print( "Error Code:", e)
    

#Zipped!

n , x = map(int,input().split())
voti = []
lista =[]
matrice = []
for i in range(x):
    voti.append(list(map(float,input().split())))
    #lista.append(voti)
for j in range(len(voti[0])):
    app = []
    for h in range(len(voti)):
        app.append(voti[h][j])
    matrice.append(app)
for t in matrice:
    print(sum(t)/x)

#Python Evaluation
var = input()
eval(var)


#Re.split()
regex_pattern = r"[.|,]" 	# Do not delete 'r'.
########
#Map and Lambda Function
cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    a , b = 0, 1
    for i in range(n):
        fib.append(a)
        a , b = b , a+b
    return fib
    

#Any or All
n , lista = int(input()), list(map(int,input().split()))
print((all(a>0 for a in lista )) and (any(b == n for b in lista)))

################
#Detect Floating Point Number
import re

n = int(input())
for i in range(n):
    app = input()
    if re.match(r'^[+-?](\d+(\.\d*)?|\.\d+)$', app):
        print("True")
    else:
        print("False")
   
            
    
                     
                

#Arrays
def arrays(arr):
    # complete this function
    # use numpy.array
    vett = numpy.array( [float(i) for i in arr] )
    return vett[::-1]
#Shape and Reshape
import numpy as np
numeri = list(map(int, input().split()))
vett = np.array(numeri)
print(np.reshape(vett,(3,3)))

#Transpose and Flatten
import numpy as np
n , m = map(int , input().split())
lista = []
for i in range(n):
    lista.append(list(map(int , input().split())))
matrice = np.array(lista)
print(np.transpose(matrice))
print(matrice.flatten())

################
#Concatenate
import numpy as np
n, m, p = map(int, input().split())
lista = []
for i in range(n):
    lista.append( list(map(int, input().split())) )
matrice_n = np.array(lista)
lista = []
for i1 in range(m):
    lista.append( list(map(int, input().split())) )
matrice_m = np.array(lista)
print(np.concatenate((matrice_n,matrice_m)))
#Zeros and Ones
import numpy as np
lista = list(map(int,input().split()))
zeri = np.zeros((lista),dtype = int)
uno = np.ones((lista), dtype = int)
print(zeri)
print(uno)

#Eye and Identity
import numpy as np
np.set_printoptions(legacy=1.13)

n, m= map(int, input().split())
print(np.eye(n,m,k=0))
#Array Mathematics
import numpy as np

n , m = map(int,input().split())
lista = []
for i in range(n):
    app = list(map(int,input().split()))
    lista.append(app)
matrice_a = np.array(lista)

lista = []
for i in range(n):
    app = list(map(int,input().split()))
    lista.append(app)
matrice_b = np.array(lista)

print(np.add(matrice_a , matrice_b))
print(np.subtract(matrice_a , matrice_b))
print(np.multiply(matrice_a , matrice_b))
print(matrice_a // matrice_b)
print(np.mod(matrice_a , matrice_b))
print(np.power(matrice_a , matrice_b))

# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(legacy = '1.13')

vett = np.array(list(map(float,input().split())))
print(np.floor(vett))
print( np.ceil(vett))
print(np.rint(vett))
# #######
#Sum and Prod
import numpy as np

n , m = map(int, input().split())
lista = []
for i in range(n):
    lista.append(list(map(int,input().split())))
matrice = np.array(lista)
print(np.prod( np.sum(matrice, axis = 0)))

#Min and Max# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n, m = map(int,input().split())
lista = []
for i in range(n):
    lista.append(list(map(int,input().split())))
matrice = np.array(lista)
print(np.max(np.min(matrice, axis = 1)))
# Mean, Var, and Std
import numpy as np

n,m = map(int, input().split())
lista = []
for i in range(n):
    lista.append(list(map(int,input().split())))
matrice = np.array(lista)
print(np.mean(matrice, axis = 1))
print(np.var(matrice, axis = 0))
print(round(np.std(matrice), 11))

#Dot and Cross
import numpy as np 

n = int(input())
lista = []
for i in range(n):
    lista.append(list(map(int,input().split())))
matriceA = np.array(lista)
lista = []
for i1 in range(n):
    lista.append(list(map(int,input().split())))
matriceB = np.array(lista)
print(np.dot(matriceA, matriceB))

#Inner and Outer
import numpy as np

lista = list(map(int,input().split()))
A = np.array(lista)
lista = list(map(int,input().split()))
B = np.array(lista)
print(np.inner(A,B))
print(np.outer(A,B))

#Polynomials
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

lista = list(map(float,input().split()))
coefficenti = np.array(lista)
x_value = float(input())

print(np.polyval(coefficenti,x_value))

#Linear Algebra
import numpy as np 

n = int(input())
lista = []
for i in range(n):
    lista.append(list(map(float,input().split())))
vett = np.array(lista)
print(round( np.linalg.det(vett) , 2))    
#Birthday Cake Candles

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

######
#Number Line Jumps

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    for j in range(max(v1*v1 , v2*v2, x1*x1,x2*x2)):
        if (x1 + j*v1)==(x2+ j*v2):
            return 'YES'
    return 'NO'
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#The Minion Game
import collections as Counter
import itertools

def minion_game(string):
    # your code goes here
 
    stuart , kevin  = 0, 0
    vocali = ['A','E','I','O','U']
    for indice,i in enumerate(string): 
        if i not in vocali: 
            stuart += len(string)-indice
        else:
            kevin += len(string)-indice
    
    if stuart < kevin :
        return print("Kevin",kevin)
    elif stuart > kevin :
        return print("Stuart",stuart)
    else:
        return print("Draw")
    
                


#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        stringa = []
        for i in l :
            app = i[-10:]
            dopo = str(app[5:10])
            prima = str(app[0:5])
            stringa.append('+91 '+ prima+' '+dopo)
        f(stringa)
    return fun
#Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        # complete the function
        people = sorted(people, key= lambda x: int(x[2]), reverse=False)
        return [f(x) for x in people]
    return inner

#####@@#@@@@@@@@
#Collections.namedtuple()
from collections import defaultdict

n = int(input())
nomi = defaultdict(list)
lista1 = list(map(str, input().split()))
for ind, j in enumerate(lista1):
    if j == 'MARKS':
        nomi[j]
        mark_ind = ind
    elif j == 'NAME':
        nomi[j]
        nomi_ind = ind
for i in range(n):
    lista = list(map(str, input().split()))
    nomi['NAME'].append(lista[nomi_ind])
    nomi['MARKS'].append(int(lista[mark_ind]))
somma = sum(nomi['MARKS'])
persone = len(nomi['NAME'])
print(round(somma/persone, 2))

#Collections.OrderedDict()
from collections import OrderedDict
from collections import Counter

n = int(input())
dizio = {}
lista = []
for i in range(n):
    oggetto = input().rpartition(' ')
    tipo = oggetto[0]
    lista.append(tipo)
    money = int(oggetto[2])
    dizio[tipo] = money 
lista = Counter(lista)
costo = list(dizio.values())
nomi = list(dizio.keys())
for j in range(len(nomi)):
    print(nomi[j],costo[j]*lista[nomi[j]])

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

pollo = deque()
n = int(input())
for i in range(n):
    word = input().split()
    comando = word[0]
    if len(word)>1:
        numero = word[1]
    if comando == 'append':
        pollo.append(numero)
    if comando == 'pop':
        pollo.pop()
    if comando == 'popleft':
        pollo.popleft()
    if comando == 'appendleft':
        pollo.appendleft(numero)
for j in (list(pollo)):
    print(j, end=" ")

#Company Logo
import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = sorted(input())
    lista = (Counter(list(s)))
    ciao = (lista.most_common(3))
    for i ,j in ciao:
        print(i,j)

###########
#Group(), Groups() & Groupdict()
import re

stringa = input()
count = 0
for i in stringa:
    if i.isalnum():
        lettera = i
    else:
        count += 1
        if count == len(stringa): 
            print("-1")
        continue
    app = stringa[(count):]
    m = re.search(rf"({lettera})\1+", app)
    if m != None:
        print(m.group()[0])
        break
    count += 1
    if count == len(stringa): 
        print("-1")
    
    
###############
#Re.findall() & Re.finditer()
import re

stringa = input()
empty = []
vocali = ['a','e','i','o','u','A','E','I','O','U']
lista = re.findall(r"(?<=[q,w,r,t,y,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m])[a,e,i,o,u]{2,}(?=[q,w,r,t,y,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m])", stringa, flags=re.IGNORECASE)
if lista == empty:
    print('-1')
else:
    for i in lista:
        print(i)

#Recursive Digit Sum
import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    numero = str(n)
    lista = list(numero)
    lista1 = [ int(i) for i in lista ]
    conto = sum(lista1)*k
    while True:
        if conto > 10:
            numero = str(conto)
        else: 
            return conto
        lista = list(numero)
        lista1 = [ int(i) for i in lista ]
        conto = sum(lista1)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#############
#Time Delta

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    #t1[4] = tempo(t1[4], t1[5])
    #t2[4] = tempo(t1[4], t1[5])
    formato = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(" ".join(t1), formato)
    dt2 = datetime.strptime(" ".join(t2), formato)
    delta = int(abs((dt1 - dt2).total_seconds()))
    #delta += scalo_sec(t1[5],t2[5]) 
    return str(delta)

def scalo_sec(scalo1, scalo2): 
    segno1 = scalo1[0]
    segno2 = scalo2[0]
    ore1 = int(scalo1[1:3])
    ore2 = int(scalo2[1:3])
    min1 = int(scalo1[3:])
    min2 = int(scalo2[3:])
    scalo1_sec = (ore1 * 3600 + min1 * 60) * (1 if segno1 == '+' else -1)
    scalo2_sec = (ore2 * 3600 + min2 * 60) * (1 if segno2 == '+' else -1)
    return -(scalo1_sec-scalo2_sec)
    
def tempo(ris , fuso):
    ore_ris = int(ris[:2])
    ore_fuso= int(fuso[1:3])
    min_ris = int(ris[3:5])
    min_fuso = int(fuso[3:])
    if fuso == "-":
        fine = str(ore_ris - ore_fuso)
        fine1 = str(min_ris-min_fuso)
    else:
        fine = str(ore_ris + ore_fuso)
        fine1 = str(min_ris +min_fuso)
    a = fine+":"+fine1+":"+ris[6:]
    return a
    
def scalo_greve(scalo): 
    segno = scalo[0]
    ore = int(scalo[1:3])
    min = int(scalo[3:])
    scalo_sec = (ore * 3600 + min * 60) * (-1 if segno == '+' else 1)
    return scalo_sec


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = list(map(str,input().split()))

        t2 = list(map(str,input().split()))

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Validating Roman Numerals
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
#############
#Validating phone numbers
import re

n = int(input())
lista = []
for i in range(n):
    a = input()
    a = str(a)
    b = str(a[:3])
    if bool(re.match( r"^((7|8|9){1,2})",b)):
        if not(bool(re.findall(r"[a-zA-Z]", a))):
            if len(a) == 10:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
#∞##############
#Validating UID
import re

t = int(input())
for _ in range(t):
    id_emp = input()
    if len(id_emp) == 10 :
        if bool(re.match( r'.*[A-Z].*[A-Z].*',id_emp)):
            if bool(re.match( r'.*\d.*\d.*\d.*',id_emp)):
                if bool(re.match(r'^(?!.*(.).*\1)[a-zA-Z0-9]*$',id_emp)):
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    
    else:
        print("Invalid")
    
#############
#Validating and Parsing Email Addresses
import re

n =int(input())
for i in range(n):
    nome, email  = input().split()
    app = email.split('<')[1].strip('>')
    #vede se: prima parola @ parola . parola
    if bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,3}$',app)):
        #vede se la prima lettera e' un . o - o _
        if not bool(re.match(r'^[._-]',app)):
            #vede se dopo la @ ci sono sono lettere e un punto
            if bool(re.match(r'^[^@]+@([a-zA-Z]+)(\.[a-zA-Z]+)?$',app)):
                print(nome, email)
                

#############
#XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    somma = len(node.attrib)
    for child in node:
#la rendo ricorsiva perche anche i child hanno child quindi devo controllarli tutti 
        somma += get_attr_number(child)
    return somma



#DefaultDict Tutorial
from collections import defaultdict

n , m = map(int,input().split())
gr_a = []
gr_b = []
for _ in range(n):
    gr_a.append(input())
for _1 in range(m):
    gr_b.append(input())
    
dizio = defaultdict(list)
for ind, v in enumerate(gr_a):
    dizio[v].append(ind + 1)

for i in gr_b:
    if i in dizio:
        for j in dizio[i]:
            print(j, end=' ')
    else:
        print(-1, end=' ')
    print()


#Piling Up!
import sys

t = int(input())
lista =[]
for _ in range(t):
    n = int(input()) # n = len(cubi)
    cubi = list(map(int,input().split()))
    sin = 0
    des = n-1
    massimo = sys.float_info.max
    lista =[]
    while sin <= des:
        if cubi[sin] >= cubi[des]:
            app = cubi[sin] 
            sin += 1
        else:
            app = cubi[des]
            des -= 1
        if app > massimo:
            print("No")
            break
        else:
            lista.append(app)
        massimo = app
    if len(lista) == n:
        print("Yes")
#####################
#Re.start() & Re.end()
import re

stringa = input() 
k = input() 
#re.escape(k) fa in modo che k siano solo alphanum, toglie special caratteri
pattern = re.escape(k)
lista = []
inizio = 0
#visto che se faccio solo re.search(k,stringa)
#potrei perdere qualche occorrenza la controllo pezzo a pezzo
while inizio < len(stringa):
    match = re.search(pattern, stringa[inizio:])
    #se non trovo niente passo al prossimo pezzo
    if not match:
        break
    #conserviamo l'occorrenza
    lista.append(match.group(0))
    #incremento
    #l incremento va fatto cosi senno non tornano gli indici giusti in a
    a = (inizio+ match.start(), inizio-1+match.end() )
    inizio += match.start()+ 1
    print(a)
# se non ci sono occorrenze stampa (-1,-1)
if lista == []:
    print((-1 , -1))

#HTML Parser - Part 1
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag.ljust(10)}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
    def handle_endtag(self, tag):
        print(f"End   : {tag.ljust(10)}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag.ljust(10)}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

n = int(input())
parola = ""
for _ in range(n):
    a = input()
    parola += a
parser = MyHTMLParser()
parser.feed(parola)

#Regex Substitution
import re

def cambio_e(match):
    return "and"
def cambio_o(match):
    return "or"

n = int(input())
for _ in range(n):
    stringa = input()
    stringa = re.sub(r"(?<=\s)&&(?=\s)", cambio_e, stringa)
    print(re.sub(r"(?<=\s)\|\|(?=\s)",cambio_o,stringa))
    

#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
        
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data.ljust(0))
    
    
n = int(input())
parola = ""
for _ in range(n):
    app = input()
    parola += '\n' + app
parser = MyHTMLParser()
parser.feed(parola)
##################
#Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for key, value in attrs:
            print(f"-> {key} > {value if value is not None else 'None'}")
    def handle_startendtag(self, tag,attrs):
        print(tag.ljust(10))
        for key, value in attrs:
            print(f"-> {key} > {value if value is not None else 'None'}")
        
n = int(input())
parola = ""
for _ in range(n):
    app = input()
    parola += '\n' + app
parser = MyHTMLParser()
parser.feed(parola)

#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for _ in range(n):
    parola = input()
    #se contiene spazi o trattini bassi
    if (' ' or '_') in parola: 
        print("Invalid")
        continue
    #se ci sono 4 numeri e poi un -
    if not (bool(re.search(r'^(?:\d{4}-)*\d{4}$',parola)) or (len(parola) == 16 and all(i.isdigit() for i in parola))) :
        print("Invalid")
        continue
    #tolgo i trattini
    parola = "".join(parola.split("-"))

    #lunghezza
    if not len(parola) == 16 :
        print("Invalid")
        continue
    #primo num 4 o 5 o 6
    if not bool(re.search(r"^[456]" ,parola)):
        print("Invalid")
        continue
    # solo num
    if not all(i.isdigit() for i in parola):
        print("Invalid")
        continue
    #no ripetizioni di 4 num
    if bool(re.search(r"(\d)\1{3}",parola)):
        print("Invalid")
        continue
    print("Valid")

#Word Order
from collections import defaultdict
import re

n = int(input())
lista = []
for _ in range(n):
    a = input()
    lista.append(a)
nuovo = defaultdict(list)
for ind,ele in enumerate(lista):
    nuovo[ele].append(ind)
print(len(nuovo.keys()))
for ci , pato  in nuovo.items():
        print(len(pato), end=' ')
        
#####################
#Insertion Sort - Part 1


import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    a = arr[len(arr)-1]

    for i in range(len(arr)-2,-1,-1):
        if arr[i] > a:
            arr[i+1] = arr[i]
            print(" ".join(map(str, arr)))
        else:
            arr[i+1] = a
            print(" ".join(map(str, arr)))
            return
    print(" ".join(map(str, [1,2,3,4,5,6,7,8,9,10])))
   
  
         
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2


import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for ele in range(1,n):
        b = arr[ele]
        indice = ele
        for j in range(ele,0,-1):
            if b < arr[j-1]:
                arr[j] = arr[j-1]
                indice -= 1
            else: 
                break
        arr[indice] = b
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#Viral Advertising

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    people = 5
    like = 0 
    share = 0
    contenitore = 0 
    for day in range(0,n):
        like = math.floor(people / 2)
        contenitore += like
        share = math.floor(people/2) * 3
        people = share
    return contenitore

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    #attribute crea un dizionario contenente tutti gli 
    #attributi del nodo
    livello = len(node.attrib)
    #presa la lunghezza degli attributi dela radice
    #rifallo sui rami
    for child in node:
        livello += get_attr_number(child)
    return livello
###############
#XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    maxdepth = max(maxdepth, level+1)
    for child in elem: 
        ricorsivo = depth(child, level+1)
    return maxdepth
##############
#Validating Postal Codes
regex_integer_in_range = r"[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d).\1)"	# Do not delete 'r'.
#Hex Color Code

import re

n = int(input())
lista = []
for _ in range(n):
    stringa = input() 
    #se metti prima il {6} del {3} visto l ordine vede prima se 
    #ha 6 componenti con gli altri controlli, se fallisce 
    #allore passa a 3 componenti
    m = re.findall(r"[:\s][\s]?#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})",stringa)
    for i in m:
        print("#"+str(i))

###########
#Matrix Script

import math
import os
import random
import re
import sys
import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
nuovo = []
for colonna in range(m):
    lista = ""
    for riga in range(n):
        lista += matrix[riga][colonna]
    nuovo.append(lista)

lett = ""
for i in nuovo:
    lett += str(i)
lett = re.sub(r"(?<=\w)[^a-zA-Z0-9]+(?=\w)", " " , lett )
print(lett)

#
#
#