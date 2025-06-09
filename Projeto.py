def inserir_nome():
    while True:    
        nome = input("Digite o nome do(a) aluno(a): ") .strip()
        if nome:
            return nome
        
        else:
            print("Erro:Este campo não pode ficar vazio. Tente novamente.")


def inserir_notas():  #Vai verificar a quantidade de notas que o usuário vai inserir para calcular a média
    while True:
        try:        #Vai verificar se a quantidade de notas é maior que 0. Caso não seja vai executar o ValueERROR e interomper a execução do código. 
            num_notas = int(input("Digite a quantidade de notas que você deseja inserir: "))
            if num_notas > 0:
                break
            print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    notas = []      #Lista de notas
    i = 0
    while i < num_notas:
        try:
            nota = float(input(f"Digite a {i + 1}ª nota: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                i += 1
            else:
                print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
    return notas
#Essa função vai calcular a média de acordo com a quantidade de notas na lista.

def calcular_medias(notas):     
    return sum(notas)/len(notas)            #vai somar as notas dentro da lista e dividir pela quantidade de notas dentro dela.


        #Vai mostrar os resultados.
def resultados(nome,notas,media):
    print(f"\n--- Os resultados do(a) aluno(a) {nome} ---")
    print("Notas inseridas:", notas)
    print(f"Média final: {media:.2f}")

   

def main():         #Essa função vai armazenar todas as outras, criando variáveis para armazenar as notas e média.
    try:
        nome_aluno = inserir_nome()
        notas_dos_alunos = inserir_notas()
        media_das_notas = calcular_medias(notas_dos_alunos)
        resultados(nome_aluno, notas_dos_alunos, media_das_notas)

    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":          #Vai iniciar o código e puxar a função main com os resultados.
    main()  

