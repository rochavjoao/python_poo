from lutadores import *

popo = Boxeador('Popó')
bambam = Boxeador('Bambam')

print(popo)
print(bambam)

popo.cruzado(bambam)
print(bambam)
popo.gancho(bambam)
print(bambam)
bambam.soco(popo)
print(popo)