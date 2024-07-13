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

def extract_terms(expression: str):
    """
    Extrai os termos de uma expressão matemática simples.

    Args:
        expression (str): A expressão matemática da qual extrair os termos.

    Returns:
        list: Uma lista contendo os termos da expressão.
    """
    # Remove espaços em branco desnecessários e divide a expressão com base nos sinais de + ou -
    terms = []
    term = ""
    for char in expression:
        if char in "+-":
            if term:
                terms.append(term.strip())
                term = ""
            term += char
        else:
            term += char
    if term:
        terms.append(term.strip())

    return terms


def derive_number(value: str = "x^2"):
    """
    Calculates the derivative of a given number.

    The derivative of a constant is always 0. This function takes a number as input,
    checks if it's a valid number, and returns the derivative of that number, which is 0.

    Parameters:
    - number (str): A string representation of a number.

    Returns:
    - str: The derivative of the input number, which is always '0'.

    """
    
    if len(value) == 0:
        raise ValueError("Números devem ter pelo menos 1 item!")
    
    result = ''
    
    if value.isnumeric(): # Case when the value is a number, it's a constant, so its derivative is zero
        print("\nIt's a constant, so its derivative is always ZERO!\n")
        result = '0'
    
    signal = ['+', '-'] 
    
    if len(value) > 1 and value[0] in signal:
        
        if str(value[1:]).isnumeric():
            result = '0'
    
    elif len(value) == 3: # Checking if it's a power, like x^2 for example
        if value[1] == '^': # Checking if the mathematical operation is a power, like x^2, if so, we'll treat it as a power to calculate
            base = value[0]
            exponent = int(value[2])
            if exponent == 2:
                result = f"{exponent}{base}"
            elif exponent == 1: # If it's a power of 1, the derivative is the base raised to the exponent minus 1
                result = base
            elif exponent == 0:
                result = '1'
            else: # If it's a power of a number different from 1, the derivative is the multiplication of the exponent by the base replacing 1 of the exponent at the end
                result = f"{exponent}{base}^{exponent-1}"
    
        elif value[1] in ['+', '-']:
            result = base  
            
    return result


def derivada(Mathematical_Expression: str = "x^2-4"):

    result = ''
    
    length = len(Mathematical_Expression)
    
    if length == 0:
        raise ValueError("Expreções matemáticas devem ter pelo menos 1 item!")
    
    elif length == 1:
        result = derive_number(Mathematical_Expression)

    elif length == 3:
        pass
    else:
        elements = extract_terms(Mathematical_Expression)
        
        for element in elements:
            data = derive_number(element)
            if data == '0':
                data = ''
            result += data
        #for idx in range(0, length ,1):
        #    if elements[idx]
        
    return result

print(derivada("x^2-4+3"))