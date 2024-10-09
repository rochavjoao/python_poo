from lutadores import *

popo = Boxeador('Popó')
bambam = Boxeador('Bambam')

charles = Muay_Thai('Charles do Bronx')
khabib = Muay_Thai('Khabib')

print(popo)
print(bambam)

popo.cruzado(bambam)
print(bambam)
popo.gancho(bambam)
print(bambam)
bambam.soco(popo)
print(popo)

print(charles)
print(khabib)

charles.chute_alto(khabib)
print(khabib)

jones = MMA('Jhon Jones')
anderson = MMA('Spider Silva')

anderson.cruzado(jones)
jones.chave_braco(bambam)
print(bambam)
print(jones)

anderson.superman_punch(jones)
print(jones)