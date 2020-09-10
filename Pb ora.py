# suma elem. de pe pozitii pare minut suma elementelor de pe poz impare

from timeit import default_timer as timer
import  timeit
def fct_1(lista):
    sum_even = 0
    sum_odd = 0
    for i in range(len(lista)): #len(n) merge in toti pasii de la 0 la n-1
        if i % 2 == 0:
            sum_even += lista[i]
        else:
            sum_odd += lista[i]
    return sum_even - sum_odd

def fct_2(lista,i):
    if i % 2 == 0 and i < len(lista):
         return lista[i] + fct_2(lista, i + 1)
    elif i % 2 and i<len(lista):
            return  -lista[i] + fct_2(lista, i + 1)
    return 0

def fct_3(lista,flag):
    if len(lista)==0:
        return 0
    if flag:
         return lista[0] + fct_3(lista[1:],not flag)
    return  -lista[0] + fct_3(lista[1:], not flag)

def fct_3_cool(lista,flag):
	if len(lista) == 0:
		return 0
	return flag * lista[0] + fct_3_cool(lista[1:],flag*(-1))

def fct_4 (lista):
    if len(lista) == 0:
        return 0
    return lista[0]-fct_4(lista[1:])


def main():
    lista = []
    n = input("Please enter the number of elements: ")
    for i in range(int(n)):
        print("Element "+ str(i+1) + ": ")
        data = int(input())
        lista.append(data)

   # lista = [1, 2, 3, 4, 59, 12, 989, 19, -15]
    min = 10000
    before = timer()
    result = fct_1(lista)
    after = timer()
    print("fct_1: " + str(result) + " execution time: " + str(after - before))
    speed = after - before
    if speed < min:
        min = speed
        fastest_function = "fct_1"

    before = timer()
    result = fct_2(lista,0)
    after = timer()
    print("fct_2: " + str(result) + " execution time: " + str(after - before))
    speed = after - before
    if speed < min:
        min = speed
        fastest_function = "fct_2"

    before = timer()
    result = fct_3(lista,True)
    after = timer()
    print("fct_3: " + str(result) + " execution time: " + str(after - before))
    speed = after - before
    if speed < min:
        min = speed
        fastest_function = "fct_3"

    before = timer()
    result = fct_3_cool(lista,True)
    after = timer()
    print("fct_3_cool: " + str(result) + " execution time: " + str(after - before))
    speed = after - before
    if speed < min:
        min = speed
        fastest_function = "fct_3_cool"

    before = timer()
    result = fct_4(lista)
    after = timer()
    print("fct_4: " + str(result) + " execution time: " + str(after - before))
    speed = after - before
    if speed < min:
        min = speed
        fastest_function = "fct_4"
    print("The fastest alghortihm is "+ str(fastest_function) + " which has an execution speed of " + str(min))

main()