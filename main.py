# --- Partea de citire ---
K = int(input())  # Citim acoperirea si o convertim la int
N = int(input())  # Citim nodurile si le convertim la inte
M = int(input())  # Citim muchiile si le convertim la int

E = []  # Declaram lista de muchii

# Citim de atatea M ori linii in plus

for i in range(M):
    E.append(input().split())
var = ''

for x in E:
    var += str(int(2 * x[0]) - 1) + 'V' + str(int(2 * x[1]) - 1) + 'V' + str(2 * x[0]) + 'V' + str(2 * x[1]) + 'V'

print(K)
print(N)
print(M)
print(E)

clauza = []  # Declaram clauza
formula = []
s = ''
var_pare = []
var_impare = []

for i in range(N * K):  # Generam o lista de variabile impare
    if i % 2 == 1:
        var_impare.append(i)  # Adaugam variabila in lista respectiva

for i in range(1, N * K + 1):  # Generam o lista de variabile pare
    if i % 2 == 0:
        var_pare.append(i)  # Adaugam variabila in lista respectiva

print(var_impare)  # afisam variabilele impare

for i in range(len(var_impare) - 1):  # Adaugam '~' in literalii din clauzele
    # din lista de elemente impare
    for j in range(i + 1, len(var_impare)):
        formula.append(['~' + str(var_impare[i]), '~' + str(var_impare[j])])

        print(var_impare[i])
        print(var_impare[j])

print(var_pare)

for i in range(len(var_pare) - 1):
    for j in range(i + 1, len(var_pare)):
        formula.append(['~' + str(var_pare[i]), '~' + str(var_pare[j])])

        print(var_pare[i])
        print(var_pare[j])

for clauza in formula:
    s += '('
    for i in range(len(clauza)):
        s += str(clauza[i])
        s += 'V'
    s = s[:-1]  # Eliminam ultimul V din clauza de literali
    s += ')^'
    
s = s[:-1]  # Eliminam ultimul ^
s += var
print(s)