from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # SOLICITANDO DADOS PARA O USUARIO.
    print("\nAdicionando usuários")
    nome = input("Digite o seu nome:")
    email = input("Digite o seu e-mail:")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\nListando usuários cadastrados")
    listar_usuarios = service.listar_todos_usuarios()
    for usuario in listar_usuarios:
        print(
            f"Nome: {usuario.nome} - Email: `{usuario.email} - semha: {usuario.senha}"
        )


if __name__ == "__main__":
    main()
