import sys

print ("Bem vindo ao gerenciador de tarefa\n")
print ("1 = Adicionar\n2 = Remover\n3 = listar as tarefas\n4 = Consultar\n5 = sair\n")

lista_tarefa = []

while (1):
	process = int(input("Digete o numero que corresponde ao processo: "))
	if process == 1:
		tarefa = str(input("Digite a nova tarefa: "))
		lista_tarefa.append(tarefa)
	if process == 2:
		tarefa = int(input("Digite o nome da tarefa a remover: "))
		lista_tarefa.remove(tarefa)
	if process == 3:
		for i, tarefa in enumerate(lista_tarefa):
			print(f"{i + 1}-", tarefa)
	if process == 4:
		tarefa = str(input("Digite o nome da tarefa: "))
		if tarefa in lista_tarefa:
			print (f"1- ", lista_tarefa[lista_tarefa.index(tarefa)])
		else:
			print (f"A tarefa '{str(tarefa)}' não consta na lista de tarefa: ")
	if process == 5:
		print("Good bay your manager homework!")
		sys.exit(0)
	
