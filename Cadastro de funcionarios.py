import funçoes 

funçoes.menu()
n = int(input("Insira o número da opção desejada:"))   

codigo = 0
nome= 0
profissao= 0
salario = 0

funcionarios= {
    1212: {
        "codigo": "1212",
        "nome" : "Thiago Neves Rodrigues", 
        "profissao": "Marceneiro",
        "salario" : "1200.00"
    },
    3214: {
        "codigo": "3214",
        "nome":"Ana Vitória Rodrigues Farias",
        "profissao": "Fisioterapeuta",
        "salario" : "3500.00"
    }
}



while n != 0:
    
    
     
    if n == 1:
      funçoes.cadastro(funcionarios, codigo, nome, profissao, salario)  
      
      funçoes.menu()
      n = int(input("Insira o número da opção desejada:")) 
      

    if (n==2):
      funçoes.localizar(funcionarios)

      funçoes.menu()
      n = int(input("Insira o número da opção desejada:"))  
    
    if (n==3):
      funçoes.listar(funcionarios)
      
      
      funçoes.menu()
      n = int(input("Insira o número da opção desejada:"))  
    
    if (n==4):
      funçoes.alterar(funcionarios)

      funçoes.menu()
      n = int(input("Insira o número da opção desejada:"))

    if (n==5):
      funçoes.deletar(funcionarios)
      
      funçoes.menu()
      n = int(input("Insira o número da opção desejada:"))
     
        