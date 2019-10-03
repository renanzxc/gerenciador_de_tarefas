import psutil as ps
import os

def clearT():
  os.system('cls' if os.name == 'nt' else 'clear')

def listProcess():
  clearT()
  for proc in ps.process_iter():
    info = proc.as_dict(attrs=['pid', 'name', 'username', 'nice', 'cpu_times', 'status'])
    print('Processo: {} | PID: {} | Nice: {} | User: {} | TempoExec: {} | Status: {} |'.format(info['name'], info['pid'], info['nice'], info['username'], info['cpu_times'][0], info['status']))
  

def listProcessUser():
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

def changePriorityProcess():
  listProcess()
  p = ps.Process(int(input("Informe o PID do processo: ")))
  p.nice(int(input("Informe a nova prioridade -20 a 20: ")))
  input()

def changeStateProcess():
  listProcess()
  p = ps.Process(int(input("Informe o PID do processo: ")))
  print(""" 
1 - Bloquear;
2 - Continuar ;
3 - Executar;
4 - Reiniciar;
5 - Finalizar. """)
  opcao = int(input())
  if (opcao == 1):
    p.suspend()
  elif(opcao == 2):
    p.resume()
  elif(opcao == 3):
    pass
  elif(opcao == 4):
    pass
  elif(opcao == 5):
    p.kill()

  

clearT()

opcao = 1
while(opcao != 0):
  print("######Gerenciador de Tarefas#########")
  print()
  print("1 - Listar processos")
  print("2 - Listar processos de um usuário")
  print("3 - Alterar estado")
  print("4 - Trocar prioridade de execução")
  print("0 - Sair")

  print()
  opcao = int(input("Informe a opção desejada: "))
  if(opcao == 1):
    listProcess()
    input()
  elif(opcao == 2):
    listProcessUser()
  elif(opcao == 3):
    changeStateProcess()    
  elif(opcao == 4):
    changePriorityProcess()
    #os.nice(1)

  clearT()

