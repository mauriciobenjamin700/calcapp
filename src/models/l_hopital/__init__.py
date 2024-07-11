"""
Conceito:
    O teorema de L'Hopital afirma que o limite de uma função feita apartir de uma fração equivale ao limite das derivadas dessa função
    
    ex: 
        lim x -> a, f(x)/g(x)

Condição de Uso:
    Ao separar os termos e calcularmos, obtemos zero
    
    ex:
        lim x -> a, f(x)/g(x)
            - f(a) == 0
            - g(a) == 0
            
        Logo: 0/0
        
Exemplo de uso:

lim x -> 2, ((x^2 - 4) / (x -2))

Passso 1:

Verificar se conseguimos obter zero nos dois termos:
    se 2^2 -4 == 0 e 2 -2 == 0
        Podemos Usar o Teorema
        
Para este caso, sim obtemos zero tanto em cima quanto em baixo

Passo 2:

Calculamos a derivada de ambos os termos

Termo1 == x^2 -4
    

Termo2 == x-2 

"""