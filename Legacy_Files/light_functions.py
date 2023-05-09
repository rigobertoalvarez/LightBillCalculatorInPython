import tkinter as tk
import light_functions as light


def getbill(e,k,tc,bc,tb):
    return((e*k)+(tc*k)+bc+tb)


def getTbill(b,l1,c1,l2,c2,c3,k,te,tb):

    sum = float(0)

    if k > l2:
        sum += c1*l1
        sum += c2*(l2-l1+1)
        sum += c3*(k-l2)
    elif l2 >= k > l1:
        sum += c1*l1
        sum += c2*(k-l1)
    else:
        sum += c1*k

    return sum+(te*k)+b+tb




