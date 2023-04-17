<h1> Introdução a Algoritmos</h1> 

<h2>📄 Neste capítulo </h2>
<h4>• Você vai ver os fundamentos para compreender todo o livro <br>• Vai conseguir escrever o seu primeiro algoritmo de busca (Pesquisa Binária) <br>• Aprenderá sobre o tempo de execução de um algoritmo (na notação Big O) </h4>

<h2>🧠 Conceitos interessantes: </h2>
<h3> O que é um Algoritmo? </h3>
<h4> Um algoritmo é um conjunto de instruções que realiza uma tarefa. Exemplo:</h4>
<img align="center" height="350" width="350"src= "https://user-images.githubusercontent.com/43351342/232489831-26c132e2-8338-4242-90a9-be0956c48ebc.png">

<h2>🔍 Pesquisa Binária</h2>
<h4>A pesquisa binária é um algoritmo utilizado para encontrar um determinado item em uma lista ordenada. Esse algoritmo é muito eficiente e rápido, principalmente quando se trabalha com listas grandes.</h4>
<h3>O algoritmo funciona da seguinte forma:</h3>
</h4> Primeiro, ele verifica o item que está no meio da lista. Se o item que estamos procurando for menor do que o item no meio da lista, então sabemos que ele só pode estar na metade inferior da lista. Caso contrário, sabemos que ele só pode estar na metade superior da lista. Em seguida, o algoritmo repete esse processo na metade selecionada da lista, e assim por diante, até que o item desejado seja encontrado.</h4>
<h4> Em resumo, a pesquisa binária é um algoritmo que usa divisões sucessivas para encontrar um item em uma lista ordenada. Ele é muito rápido e eficiente, e pode ser usado em muitas aplicações diferentes, como em bancos de dados, sistemas de busca na internet e muito mais. </h4>
<img align="center" height="350" width="350" src = "https://user-images.githubusercontent.com/43351342/232503297-3d777cc4-14ff-4e11-a580-f30cb60ee54a.png">

<h2>⏳ Notação Big O </h2>
<h4>Notação Big O é uma maneira de medir a eficiência de um algoritmo. Ela nos ajuda a entender o tempo de execução de um algoritmo, ou seja, quanto tempo ele leva para executar uma determinada tarefa.</h4>
<h4>A notação Big O é escrita como "O(n)", em que "n" é o tamanho da entrada para o algoritmo. Ela indica quantas operações o algoritmo precisa executar para concluir a tarefa, em relação ao tamanho da entrada. Por exemplo, um algoritmo que precisa executar 5 operações para uma entrada de tamanho 10 pode ser descrito como "O(10)".</h4>
<h4>A notação Big O é importante porque nos permite comparar a eficiência de diferentes algoritmos. Algoritmos com uma notação Big O menor são mais eficientes e rápidos do que aqueles com uma notação Big O maior. Por exemplo, um algoritmo com uma notação Big O de "O(n)" é mais eficiente do que um algoritmo com uma notação Big O de "O(n²)". É escrita da seguinte forma: </h4>
   <img align="center" height="350" width="350" src = "https://user-images.githubusercontent.com/43351342/232507850-d271d8dd-15e4-4ffe-846c-73c36cb60c22.png">

<h3> Vendo diferentes tempos de execução Big O </h3>
<h4>A notação Big O é usada para medir a eficiência de um algoritmo em relação ao tamanho da entrada. Aqui segue um exemplo prático que pode ser executado em casa com um pedaço de papel: Suponha que vocÊ tenha que desenhar uma grade com 16 divisões</h4>
 <img align="center" height="350" width="350" src = "https://user-images.githubusercontent.com/43351342/232574783-bb186bc5-2e38-48db-ac3a-bdfa9378c2aa.png">

<h3>Algoritmo 1</h3>
<h4>Uma forma de solucionar o problema seria desenhando no papel uma divisão de casa vez. A notação Big O conta o número de operações. Nesse exemplo seriam 16 divisões. </h4>
<h3>Algoritmo 2</h3>
<h4> A segunda forma seria dobrando o papel. Ao fazer isso você execulta duas diisões em uma única dobra(operação). Seria necessário apenas 4 dobras para você fazer as 16 operações.</h4>



