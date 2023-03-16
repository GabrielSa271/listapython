# etapa 1
banda = []
print("Etapa 1:", banda)
# etapa 2
banda.append("John Lenon")
banda.append("Paul MaCartney")
banda.append("George Harrison")
print("Etapa 2:", banda)
# etapa 3
for menbros in range(2):
    banda.append(input("Novo menbro: "))
print("eatapa 3:", banda)
# etapa 4
del banda[-1]
del banda[-1]
print("etapa 4:", banda)
# etapa 5
banda.insert(0, "RingoStarr")
print("etapa 5:", banda)
print("The Fab:",len(banda))