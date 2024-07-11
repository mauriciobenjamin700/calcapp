"""
Conceito:
    
    
    ex: 
        x^2 - 4 == 2x

Condição de Uso:

        
Exemplo de uso:

x^2 - 4

Passso 1:

verificar se existem constantes (Uma constante é um número normal, imutavel):
    - No exemplo a cima, 4 é uma constante, pois é usada diretamente para realizar uma subtração
    - Logo descartarmos o 4

Passo 2:

Vereficiar se variaveis na expreção (Variaveis são entradas de dados customizadas pelo usuário, neste caso temos apenas 'x' como variavel)
    - X é uma variavel, então mapeamos ele e que o influencia, neste caso: (x^2)

Passo 3:
Realizar a modificação de potências para multiplicações:

    - iremos reduzir 1 digito do expoente para gerar uma multiplicação.
    - x^2 == 2x^1
    - logo, obtemos 2x como resultado
    
    - Caso tivessemos a seguinte expressão: x - 2 e quisessemos derivar:
    - x - 2 == 1
    - pois 2 é uma constante, então descartamos
    - Qualquer variavel sem um expoente, como apenas 'x' pode ser entendida matemáticamente como "x^1", o que o permite se tornar uma especie de "constante de sí mesmo"
    - logo, quando trabalhamos com uma varíavel "constante" (ela sempre vai ser ela mesma), definimos seu valor de derivação como a constante: '1'
    - Ao final temos '1' como resultado final
    

Termo1 == x^2 -4
    

Termo2 == x-2 

"""

def check_constants(Mathematical_Expression: str = "x^2-4"):
    """
    Recebe uma expreção matemática e checa se existem constantes dentro da expreção
    
    Uma constate é um número imutavel dentro da expreção ou um valor X ^ 1 que representa a constante '1'
    
    Args:
        - Mathematical_Expression:: str: Uma expreção matemática e checa se existem constantes dentro dela
        
    Return:
        bool: True if existem constantes dentro da expreção e false caso não existam constantes dentro da função
    """
    
    if len(Mathematical_Expression) == 0: # Validando caso usuário não passe nada
        raise ValueError("Expreções matemáticas devem ter pelomenos 1 item!")
    
    if len(Mathematical_Expression) == 1: # Caso ele passe apenas um valor, precisamos saber se esse valor é uma variavel ou um número
        if Mathematical_Expression.isnumeric(): # Caso seja número, é uma constante, logo retornamos True
            return True
    
    return False
        
    
    

def derivada(Mathematical_Expression: str = "x^2-4"):
    pass