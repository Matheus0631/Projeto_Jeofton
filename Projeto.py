def inserir_notas():
    num_notas = int(input("Digite a quantidade de notas que vc deseja inserir:"))
    notas = [] #Vai receber as notas.

    for i in range(num_notas):                  #vai fazer um loop de acordo com a quantidade de notas desejadas pelo usuário.
        nota = float(input(f"digite a {i + 1}ª nota:"))
        notas.append(nota)      #Vai adicionar o valor da variável nota na lista.
    return notas                #Vai retornar as notas.

#Essa função vai calcular a média de acordo com a quantidade de notas na lista.

def calcular_medias(notas):     
    if not notas:           #Vai verificar se a lista está vazia e retornar o erro.
        return "ERRO:A lista está vazia, é necessário que você adicione alguma nota para poder calcular a média. "
    
    for nota in notas:      #Vai varificar na lista se tem alguma nota irregular e retornar o erro.
        if nota <0 or nota > 10:
            return "Erro:As notas devem estar entre 0 e 10."
    

    return sum(notas)/len(notas)            #vai somar as notas dentro da lista e dividir pela quantidade de notas dentro dela.


        #Vai mostrar os resultados.
def resultados(notas, media):
    print("\n Notas inseridas:", notas)
    if isinstance(media, str):
        print(media)

    else:
        print(f"Média das notas {media:.2f}")


def main():

    print("Bem-Vindo ao calculador de médias!\n")

    notas_alunos = inserir_notas()

    media_notas = calcular_medias(notas_alunos)

    resultados(notas_alunos,media_notas)


if __name__ == "__main__":
    main()  

