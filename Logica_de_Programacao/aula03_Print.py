
"""
#\r\n = CRLF
O print imprime e já quebra a linha!
Dentor do print eu coloca os argumentos que são impressos
O Python é caseSentitive!

"""
print(12, 34, sep='-') # Assim eu utilizo outro separador
print(12, 34, sep='-', end='\r\n') # Esse é o padrão
print(12, 34, sep='-', end='#\n')