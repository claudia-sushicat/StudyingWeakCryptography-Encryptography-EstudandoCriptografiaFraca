# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 01:00:56 2020

@author: umabatatahacker
"""

#a cifra de cesar se trata do mesmo metodo de substituição,  e aqui vamos  criptografar...


p_um = ['a','b','c','d','e','f','g','h','i','j','k','l','m',"n",'o','p','q','r','s','t','u','v','w','x','y','z']
p_dois = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a",'b',"c"]


x = input("Digite o que deseja converter:")

x_convertido= []
for i in list(x):
    if(i in p_um):
        x_convertido.append(p_dois[p_um.index(i)])
    else:      
        x_convertido.append(p_um[p_dois.index(i)])     

resultado_final = ''.join(x_convertido)
print(x + ' ' +'significa:' + ' ' + resultado_final)



#para descriptografar precisa fazer o caminho inverso, mas, no sentido de que a p_dois vira a p_um, mas isso é simples
#
#x_convertido= []
#for i in list(x):
#    if(i in p_dois):
#        x_convertido.append(p_um[p_dois.index(i)])
#    else:      
#        x_convertido.append(p_dois[p_um.index(i)])     


