# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C6aRnU_FmKwtn98IVKeBoFJx_g3pmKIQ
"""

from math import *
import numpy as np
def f1(x):
    return x**4 -3*x**3 +x**2 + x + 1

#Metodo de Muller 

tol=0.000000001
nmax=20
h=100
error=100
#Determinan valores iniciales
p0=0.5
p1=-0.5
p2=0
h1=p1-p0
h2=p2-p1
g1=( f1(p1)- f1(p0) )/h1
g2=( f1(p2)- f1(p1))/h2
d=(g2 - g1  )/(h2+h1)
i=3

print("# iter  \t\t P  \t\t\t error")

#Ciclo iterativo 
while i<= nmax and abs(h)>tol :
  b= g2 + h2*d
  D=(b**2 -4*f1(p2)*d)**(1/2)

  if abs(b-D)<abs(b+D):
    E= b+D
  else:
    E=b-D
 
  h=-2*f1(p2)/E
  p=p2+h
  error= abs(p- p2)
  #Se determinan nuevos valores

  p0=p1
  p1=p2
  p2=p
  h1=p1-p0
  h2=p2-p1
  g1=( f1(p1)- f1(p0) )/h1
  g2=( f1(p2)- f1(p1))/h2
  d=(g2 - g1  )/(h2+h1)

  print("{0} \t\t {1:6.6f} \t {2:6.6f}".format(i, p,error ))

  i+=1