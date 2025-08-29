import random
import csv

nomes = [
    "António", "Maria", "João", "Ana", "Paulo", "Carla", "Miguel", "Rita", "Pedro", "Sofia",
    "Luís", "Mariana", "José", "Beatriz", "André", "Cláudia", "Bruno", "Helena", "Tiago", "Marta",
    "Ricardo", "Patrícia", "Fábio", "Isabel", "Manuel", "Carolina", "Gonçalo", "Inês", "Alexandre", "Teresa",
    "Hugo", "Diana", "Daniel", "Raquel", "Vítor", "Laura", "César", "Joana", "Eduardo", "Filipa",
    "Rafael", "Camila", "Nuno", "Liliana", "Fernando", "Cátia", "Rui", "Vanessa", "Nelson", "Luciana"
]

cursos = ["Python", "JavaScript", "Data Science", "C", "Java", "C++", "Go", "Ruby", "PHP", "Rust"]

estudantes = []
for i, nome in enumerate(nomes[:50]):
    idade = random.randint(18, 35)
    curso = random.choice(cursos)
    email = f"{nome.lower()}@email.com"
    estudantes.append([nome, idade, curso, email])

with open("alunos.csv", mode='w', newline='', encoding='utf-8') as file:
	coluns = ['nome', 'idade', 'curso', 'email']
	writer = csv.DictWriter(file, fieldnames=coluns)
	writer.writeheader()
	for nome, idade, curso, email in estudantes:
		writer.writerow({
    	        "nome": nome,
        	    "idade": idade,
            	"curso": curso,
	            "email": email
    	    })
