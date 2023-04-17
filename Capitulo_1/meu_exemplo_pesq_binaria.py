def binary_search(array, target):
    """
    Implementação da pesquisa binária.
    Retorna o índice do elemento alvo no array, ou -1 se o alvo não for encontrado.
    """
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

#Explicação:
"""
Aqui está uma breve explicação do que está acontecendo no código:

• A função binary_search recebe dois parâmetros: um array e um valor alvo a ser procurado no array.
• As variáveis low e high são inicializadas como o índice mínimo e máximo do array, respectivamente.
• A pesquisa binária é implementada com um loop while. A cada iteração, o algoritmo calcula o índice médio do array, arredondando para baixo com a divisão inteira //.
• Se o valor do meio for igual ao alvo, a função retorna o índice do meio.
• Caso contrário, se o valor do meio for menor que o alvo, a busca continua na metade direita do array. Se for maior, a busca continua na metade esquerda.
• Se o alvo não for encontrado após percorrer todo o array, a função retorna -1.
"""