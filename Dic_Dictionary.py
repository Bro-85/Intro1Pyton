#declaram si initializare un map
note_elevi = {'Gigel': 10, 'Costel': 8, 'Ana': 9}
#adugam elemente
note_elevi['Sebi'] = 7
#printam dictul
print(note_elevi)
#aflam elemente din dictionar 'dic'
print(note_elevi['Gigel'])
#sau
print(note_elevi.get('Gigel'))

#actualizam valori
note_elevi['Sebi'] = 9
print(note_elevi)
#aflam dimensiunea
print(len(note_elevi))
#stergem valori
note_elevi.pop('Ana')
print(note_elevi)
#dupa stergerea valori nu mai poate fi adaugat
print(note_elevi.get('Ana', 'nu mai exista acest element'))
print(note_elevi)
#trebuie adaugat din nou acel elemet in lista ca si mai sus
note_elevi['Ana'] = 9
print(note_elevi)
#pentru a vedea chieile(numele care corespunde notelor)
print(note_elevi.keys())