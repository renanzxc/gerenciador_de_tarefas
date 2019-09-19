import psutil as ps
import os

def clearT():
  os.system('cls' if os.name == 'nt' else 'clear')

clearT()

opcao = 1
while(opcao != 0):
  print("######Gerenciador de Tarefas#########")
  print()
  print("1 - Listar processos")
  print("2 - Listar processos de um usuário")
  #print("3 - Alterar estado")
  print("4 - Trocar prioridade de execução")
  print("0 - Sair")

  print()
  opcao = int(input("Informe a opção desejada: "))
  if(opcao == 1):
    clearT()
    for proc in ps.process_iter():
      info = proc.as_dict(attrs=['pid', 'name', 'username', 'nice', 'cpu_times', 'status'])
      print('Processo: {} | PID: {} | Nice: {} | User: {} | TempoExec: {} | Status: {} |'.format(info['name'], info['pid'], info['nice'], info['username'], info['cpu_times'][0], info['status']))
    input()

  elif(opcao == 2):
    clearT()
    #print(ps.users()) #Era pra trazer os usuários
    user = input("De qual usuário devo listar os processos? ")
    print()
    print('Lista de processos em execução do usuário: '+user+'\n')
    for proc in ps.process_iter():
      info = proc.as_dict(attrs=['pid', 'name', 'username', 'nice', 'cpu_times', 'status'])
      if(info['username'] == user):
        print('Processo: {} | PID: {} | Nice: {} | User: {} | TempoExec: {} | Status: {} |'.format(info['name'], info['pid'], info['nice'], info['username'], info['cpu_times'][0], info['status']))
    input()
  
  elif(opcao == 4):
    pass
    #os.nice(1)

  clearT()

