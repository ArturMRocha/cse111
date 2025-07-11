import os

# Definição das constantes de lista de caracteres
LOWER=list("abcdefghijklmnopqrstuvwxyz")
UPPER=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS=list("0123456789")
SPECIAL=list("!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~")

# --- Construção de Caminho Robusta ---
# Descobre o diretório onde o script está sendo executado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Junta o caminho do diretório com os nomes dos arquivos
# Isso garante que os arquivos sejam encontrados, não importa como o script seja executado
DICTIONARY_FILE = os.path.join(script_dir, "wordlist.txt")
COMMON_PASSWORDS_FILE = os.path.join(script_dir, "toppasswords.txt")


def word_in_file(word, filename, case_sensitive=False):
    """
    Verifica se uma palavra existe em um arquivo de texto.

    Args:
        word (str): A palavra a ser procurada.
        filename (str): O caminho para o arquivo.
        case_sensitive (bool): Se a correspondência deve diferenciar maiúsculas de minúsculas.

    Returns:
        bool: True se a palavra for encontrada, False caso contrário.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line_word = line.strip()
                if case_sensitive:
                    if word == line_word:
                        return True
                else:
                    if word.lower() == line_word.lower():
                        return True
    except FileNotFoundError:
        print(f"Aviso: Arquivo de recurso não encontrado: {filename}")
    return False

def word_has_character(word, character_list):
    """
    Verifica se uma palavra contém algum caractere de uma lista fornecida.

    Args:
        word (str): A palavra a ser verificada.
        character_list (list): A lista de caracteres a procurar.

    Returns:
        bool: True se um caractere for encontrado, False caso contrário.
    """
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """
    Calcula a complexidade de uma palavra com base nos tipos de caracteres que ela contém.

    Args:
        word (str): A palavra a ser analisada.

    Returns:
        int: Uma pontuação de complexidade de 0 a 4.
    """
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# --- Início do Componente Criativo ---
def has_sequence_or_repetition(password):
    """
    Verifica se a senha contém sequências óbvias (ex: 'abc', '123') ou
    caracteres repetidos (ex: 'aaa', '777').

    Args:
        password (str): A senha a ser verificada.

    Returns:
        bool: True se um padrão for encontrado, False caso contrário.
    """
    # Verifica por repetições de 3 caracteres (ex: 'aaa')
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    
    # Verifica por sequências de 3 caracteres (ex: 'abc' ou '321')
    for i in range(len(password) - 2):
        try:
            # Verifica sequência numérica ou alfabética crescente (ex: '123', 'abc')
            if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
                return True
            # Verifica sequência numérica ou alfabética decrescente (ex: '321', 'cba')
            if ord(password[i]) - 1 == ord(password[i+1]) and ord(password[i+1]) - 1 == ord(password[i+2]):
                return True
        except TypeError:
            # Ignora erros se os caracteres não forem ordenáveis (improvável, mas seguro)
            continue
            
    return False
# --- Fim do Componente Criativo ---

def password_strength(password, min_length=10, strong_length=16):
    """
    Calcula a força de uma senha com base em vários critérios e imprime o feedback.

    Args:
        password (str): A senha a ser avaliada.
        min_length (int): O comprimento mínimo aceitável da senha.
        strong_length (int): O comprimento no qual a senha é considerada forte.

    Returns:
        int: Uma pontuação de força de 0 a 5.
    """
    if word_in_file(password, DICTIONARY_FILE, case_sensitive=False):
        print("A senha é uma palavra do dicionário e não é segura.")
        return 0

    if word_in_file(password, COMMON_PASSWORDS_FILE, case_sensitive=True):
        print("A senha é uma senha comumente usada e não é segura.")
        return 0

    if len(password) < min_length:
        print("A senha é muito curta e não é segura.")
        return 1
        
    if len(password) >= strong_length:
        print("A senha é longa, o comprimento supera a complexidade. Esta é uma boa senha.")
        return 5

    complexity = word_complexity(password)
    strength = 1 + complexity
    
    # --- Aplicação da Penalidade do Componente Criativo ---
    # Se uma sequência ou repetição for encontrada, uma penalidade é aplicada à pontuação.
    if has_sequence_or_repetition(password):
        print("Aviso: A senha contém caracteres sequenciais ou repetidos, o que a enfraquece.")
        strength = max(1, strength - 1) # Reduz a força em 1, mas não abaixo de 1
    
    print(f"A senha tem uma pontuação de complexidade de {complexity} e uma força de {strength}.")
    return strength

def main():
    """
    Executa o loop principal, solicitando ao usuário uma senha e relatando sua força.
    """
    print("--- Verificador de Força de Senha ---")
    print("Digite 'q' ou 'Q' para sair.")
    
    while True:
        password = input("\nDigite uma senha para testar: ")
        if password.lower() == 'q':
            print("Obrigado por usar o verificador de senhas. Adeus!")
            break
        
        strength = password_strength(password)
        print(f"-> Força da senha calculada: {strength}/5")

if __name__ == "__main__":
    main()