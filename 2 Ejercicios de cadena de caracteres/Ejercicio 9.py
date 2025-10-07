'''Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.'''

fecha_cumple = input("Escribe la fecha de tu cumpleaños en formato dd/mm/aaaa: ")
dia = fecha_cumple.split("/")[0]
mes = fecha_cumple.split("/")[1]
anio = fecha_cumple.split("/")[2]
print("Dia: ", dia)
print("Mes: ", mes)
print("Año: ", anio)
