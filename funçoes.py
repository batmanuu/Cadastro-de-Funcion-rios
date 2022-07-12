
def lin(txt):
    print("-" * 30)
    print(txt)
    
    
def lin2(txt):
    print("=" * 40)
    print(txt)
    print("=" * 40)

def menu():
    lin("[1] CADASTRAR FUNCIONÁRIO")
    lin("[2] LOCALIZAR FUNCIONÁRIO")
    lin("[3] LISTA DE FUNCIONÁRIOS")
    lin("[4] ALTERAR INFORMAÇÕES")
    lin("[5] EXCLUIR FUNCIONÁRIO")
    lin("[0] SAIR")
    print("-" * 30)

def cadastro(funcionarios, codigo, nome, profissao, salario):
    lin2("        CADASTRAR FUNCIONÁRIO")
    codigo= int(input("INSIRA CÓDIGO: "))
    nome= input("INSIRA NOME: ")
    profissao= input("INSIRA PROFISSÃO: ")
    salario=float(input("INSIRA SALÁRIO: "))
    lin2("FUNCIONÁRIO CADASTRADO COM SUCESSO!") 
    
    funcionarios[codigo]= {
        "codigo": codigo, 
        "nome": nome, 
        "profissao": profissao,
        "salario": salario}

def localizar(funcionarios):
    lin2("       LOCALIZAR FUNCIONÁRIO")
    codigo= int(input("INSIRA CÓDIGO:"))

    if codigo in funcionarios:
        print("=" * 90)
        print("Codigo:{}".format(funcionarios[codigo]["codigo"]), "|Nome:{}".format(funcionarios[codigo]["nome"]), "|Profissão:{}".format(funcionarios[codigo]["profissao"]), "|Salario:{}".format(funcionarios[codigo]["salario"]))
        print("=" * 90)
    else:
        lin2("FUNCIONÁRIO NÃO ENCONTRADO")

def alterar(funcionarios):
    lin2("   ALTERAR INFORMAÇÕES DO FUNCIONÁRIO")
    codigo= int(input("Insira código do funcionário que deseja alterar:"))
    
    if codigo in funcionarios:
        print("=" * 90)
        print("Codigo:{}".format(funcionarios[codigo]["codigo"]), "|Nome:{}".format(funcionarios[codigo]["nome"]), "|Profissão:{}".format(funcionarios[codigo]["profissao"]), "|Salario:{}".format(funcionarios[codigo]["salario"]))
        print("=" * 90)
        funcionarios[codigo]["nome"]= input("Insira nome:")
        funcionarios[codigo]["profissao"]= input("Insira profissão:")
        funcionarios[codigo]["salario"]= float(input("Insira salário:"))
        lin2("   DADOS DO FUNCIONÁRIO ATUALIZADOS")
    else:
        lin2("FUNCIONÁRIO NÃO ENCONTRADO")

def deletar(funcionarios):
    lin2("       EXCLUIR FUNCIONÁRIO")
    codigo= int(input("INSIRA CÓDIGO: "))
    del funcionarios[codigo]

    lin2("  FUNCIONÁRIO REMOVIDO COM SUCESSO")

def media_salario(funcionarios):
  soma = 0
  media = 0
  for f in funcionarios:
    temp = funcionarios[f]
    soma += float(temp["salario"])
  media = float(soma / len(funcionarios))
  print("SOMA DOS SALÁRIOS CADASTRADOS:", soma)
  print("MÉDIA DOS SALÁRIOS CADASTRADOS:",media)

def listar(funcionarios):
    lin2("         LISTA DE FUNCIONÁRIOS")
    if len(funcionarios) > 0:
        print("-" * 90)
        for f in funcionarios:
            temp = funcionarios[f]
            print("Codigo:{}".format(temp["codigo"]), "|Nome:{}".format(temp["nome"]), "|Profissão:{}".format(temp["profissao"]), "|Salario:{}".format(temp["salario"]))
            print("-" * 90)
        print("TOTAL DE FUNCIONÁRIOS:{}\n".format(len(funcionarios)))
        media_salario(funcionarios)
        print("-" * 90)