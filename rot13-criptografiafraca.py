# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:24:40 2020

@author: umabatatahacker
"""

#ROT13 = basicamente, eu criei uma cifra de acordo com o que se conhece sobre o metodo de substituição do ROT13
#se voce tiver uma palavra já em ROT13 é só testar, e se quiser passar para ROT13 = beleza. O procedimento funciona de ambas as formas já que consiste em mera substituição
# temos o alfabeto divido em 2, cada parte com 13 letras, transformei estas partes em vetores



alfabeto_parte_um = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
alfabeto_parte_dois = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]

x = input('digite e veja a mágica acontecer') 
# x é a variavel que recebera a palavra que o usuário deseja descriptografar ou criptografar 

#agora é preciso ver quais caracteres pertencem a quais vetores para assim substitui-los
#achei mais organizado salvar a substituição em um vetor

x_convertido= []
for i in list(x):
    if(i in alfabeto_parte_um):
        x_convertido.append(alfabeto_parte_dois[alfabeto_parte_um.index(i)])
    else:      
        x_convertido.append(alfabeto_parte_um[alfabeto_parte_dois.index(i)])     

resultado_final = ''.join(x_convertido)
print(x + ' ' +'significa:' + ' ' + resultado_final)

