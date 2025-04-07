users = []

def transformar_nome(nome):
    return nome.strip().upper()

def validar_idade(idade):
    if idade < 18:
        raise ValueError("Usuário deve ter no mínimo 18 anos.")
    return idade

def verificar_email_unico(email):
    for user in users:
        if user["email"] == email:
            raise ValueError("Email já cadastrado.")
    return email.strip().lower()

def criar_usuario(nome, idade, email):
    import pdb; pdb.set_trace()  # Inicia o debugger aqui
    nome = transformar_nome(nome)
    idade = validar_idade(idade)
    email = verificar_email_unico(email)
    
    user = {"id": len(users) + 1, "nome": nome, "idade": idade, "email": email}
    users.append(user)
    return user

def listar_usuarios():
    return users

def atualizar_usuario(user_id, nome=None, idade=None, email=None):
    import pdb; pdb.set_trace()  # Inicia o debugger aqui
    for user in users:
        if user["id"] == user_id:
            if nome:
                user["nome"] = transformar_nome(nome)
            if idade is not None:
                user["idade"] = validar_idade(idade)
            if email:
                if email != user["email"]:
                    verificar_email_unico(email)
                user["email"] = email.strip().lower()
            return user
    raise ValueError("Usuário não encontrado.")

def deletar_usuario(user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            return users.pop(i)
    raise ValueError("Usuário não encontrado.")

# Exemplo para testar
if __name__ == "__main__":
    #### EXECUÇÂO DO CÓDIGO ####
    #### FLUXO MOCADO ####
    print("=== Criando usuários ===")
    try:
        criar_usuario("Ana", 20, "ana@email.com")
        criar_usuario("João", 25, "joao@email.com")
        criar_usuario("Bia", 17, "bia@email.com")  # Deve dar erro de idade
    except Exception as e:
        print("Erro:", e)

    print("\n=== Listando usuários ===")
    for u in listar_usuarios():
        print(u)

    print("\n=== Atualizando usuário ===")
    try:
        atualizar_usuario(1, idade=30, email="ana_novo@email.com")
    except Exception as e:
        print("Erro:", e)

    print("\n=== Usuários após atualização ===")
    for u in listar_usuarios():
        print(u)
    import pdb; pdb.set_trace()  # Inicia o debugger aqui - vamos entrar no metodo a partir desse ponto // comando s
    print("\n=== Deletando usuário ===")
    deletar_usuario(2)

    print("\n=== Usuários após exclusão ===")
    for u in listar_usuarios():
        print(u)
