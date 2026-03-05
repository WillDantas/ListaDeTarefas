import json
from datetime import datetime

ARQUIVO = "tarefas.json"




def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)


def adicionar_tarefa(tarefas):
    titulo = input("Digite o nome da tarefa: ")
    
    tarefa = {
        "titulo": titulo,
        "concluida": False,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!\n")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i + 1}. {tarefa['titulo']} [{status}] - Criada em: {tarefa['data_criacao']}")
    print()


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa para concluir: ")) - 1
        
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("🎉 Tarefa concluída!\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Digite um número válido.\n")



def main():
    tarefas = carregar_tarefas()

    while True:
        print("==== MENU ====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    main()