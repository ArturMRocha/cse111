# Este arquivo contém a função parse_formula, que converte uma
# string de fórmula química em uma lista que o nosso programa pode usar.

from re import findall

def parse_formula(formula: str) -> list:
    """
    Converte uma fórmula química em uma lista de tuplas.
    Exemplo: "H2O" se torna [("H", 2), ("O", 1)]
    """
    # Expressão regular para encontrar pares de (Elemento)(Quantidade)
    pattern = r"([A-Z][a-z]?)(\d*)"
    matches = findall(pattern, formula)

    # Processa os resultados para adicionar quantidade 1 onde não for especificado
    parsed_list = []
    for symbol, quantity_str in matches:
        quantity = int(quantity_str) if quantity_str else 1
        parsed_list.append((symbol, quantity))

    return parsed_list