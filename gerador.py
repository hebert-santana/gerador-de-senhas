import random

print('=================================\n||      Gerador de Senhas      ||\n=================================')

num_senhas = int(input("Número de senhas: ") or 1)
tamanho_senha = 0

# tamanho mínimo da senha deve ser 8 dígitos
while tamanho_senha < 8:
    tamanho_senha = int(input("Total de dígitos na senha: ") or "8")
    if tamanho_senha < 8:
        print('A senha deve conter pelo menos 8 dígitos.')
        
print('=================================\n')

# possíveis caracteres
especiais = [ '.', '+', '-', '@', '#', '*', '!', '?', '~']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# função para gerar senhas
def geraSenha(n_senha, t_senha):
    senhas = []
    i = 1
    
    while i <= n_senha:
        senha = []
        
        while len(senha) < t_senha:
            senha.append(random.choice(especiais))
            if len(senha) == t_senha:
                break
            senha.append(random.choice(numeros))
            if len(senha) == t_senha:
                break
            senha.append(random.choice(letras_min))
            if len(senha) == t_senha:
                break
            senha.append(random.choice(letras_mai))
            
        senhas.append(senha)            
        i = i + 1
        
    return senhas

    
senhas_geradas = geraSenha(num_senhas, tamanho_senha)

# imprimindo as senhas
j = 1
for senha in senhas_geradas:
    password = ''.join(senha)
    print(f'Senha {j}: {password} \n')
    j = j + 1
    
print('=================================\n')
    
    
   
    