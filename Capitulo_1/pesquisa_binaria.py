class pesquisa_binaria():

  def pesquisa_iterativa(self, lista, item):
    # baixo e alto rastreiam em qual parte da lista você pesquisará.
    baixo = 0
    alto = len(lista) - 1

    # Embora você não tenha reduzido a um elemento ...
    while baixo <= alto:
      # ... verifique o elemento do meio
      meio = (baixo + alto) // 2
      chute = lista[meio]
      # Encontrei o item.
      if chute == item:
        return meio
      # O chute era muito alto.
      if chute > item:
        alto = meio - 1
      # O chute foi muito baixo.
      else:
        baixo = meio + 1

    # Item não existe
    return None

  def pesquisa_recursiva(auto, lista, baixo, alto, item):
    # Verifique o caso base 
    if alto >= baixo: 

        meio = (alto + baixo) // 2
        chute = lista[meio]

        # Se o elemento estiver presente no próprio meio 
        if chute == item:
            return meio 

        # Se o elemento for menor que meio, então ele só pode
        # estar presente no subarray esquerdo 
        elif chute > item: 
            return auto.pesquisa_recursiva(lista, baixo, meio - 1, item) 

        # Caso contrário, o elemento só pode estar presente no subarray direito 
        else: 
            return auto.pesquisa_recursiva(lista, meio + 1, alto, item) 

    else: 
        # Elemento não está presente na matriz 
        return None

if __name__ == "__main__":
  # Devemos inicializar a classe para usar os métodos desta classe
  bs = pesquisa_binaria()
  minha_lista = [1, 3, 5, 7, 9]

  print(bs.pesquisa_iterativa(minha_lista, 3)) # => 1

  # 'Nenhum' significa nulo em Python. Usamos para indicar que o item não foi encontrado.
  print(bs.pesquisa_iterativa(minha_lista, -1)) # => None