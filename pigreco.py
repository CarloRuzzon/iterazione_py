pigreco = 4.
divisione = 3.
segno = -1
b = input ("Inserisci un numero:")
pigreco -= 4. / divisione
for i in range(2, b):
    divisione += 2.
    pigreco -= (4. / divisione * segno)
    segno = -segno
print pigreco
