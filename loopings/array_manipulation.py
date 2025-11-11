array1 = [45, 0, 66, 0, 81, 57, 90]
array2 = [0, 2, 3, 4, 5, 0, 7]

resultado_condicional = [x for x in array1 if x > 3] + [y for y in array2 if y > 3]

print(resultado_condicional) 