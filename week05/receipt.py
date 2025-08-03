import csv
from datetime import datetime

# As constantes de índice permanecem as mesmas.
PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
REQUEST_ID_INDEX = 0
REQUEST_QUANTITY_INDEX = 1

def main():
    try:
        # Lê o catálogo de produtos para um dicionário.
        products_dict = read_dictionary("products.csv", PRODUCT_ID_INDEX)

        # ALTERAÇÃO: Nome da loja conforme o requisito.
        print("Inkom Emporium")
        print()

        # Abre o arquivo de pedido do cliente para leitura.
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            # Pula a primeira linha (cabeçalho)
            next(reader)

            print("Itens Encomendados:")
            
            # Inicializa variáveis para os cálculos
            subtotal = 0
            total_items = 0

            # ALTERAÇÃO: Loop corrigido para iterar sobre o 'reader' do CSV.
            for row in reader:
                # O reader já divide a linha em uma lista.
                product_id = row[REQUEST_ID_INDEX]
                quantity = int(row[REQUEST_QUANTITY_INDEX])

                # Busca o produto no dicionário (pode gerar KeyError).
                product_data = products_dict[product_id]

                # Extrai os dados do produto.
                product_name = product_data[PRODUCT_NAME_INDEX]
                product_price = float(product_data[PRODUCT_PRICE_INDEX])

                # Exibe os detalhes do item no recibo.
                print(f"{product_name}: {quantity} @ ${product_price:.2f}")

                # Acumula os totais.
                total_items += quantity
                subtotal += product_price * quantity
        
        # Calcula imposto e total final.
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total_due = subtotal + sales_tax
        
        # Exibe o resumo do pedido.
        print()
        print(f"Número de Itens: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Imposto sobre Vendas (6%): ${sales_tax:.2f}")
        print(f"Total: ${total_due:.2f}")
        print()

        # ALTERAÇÃO: Mensagem final conforme o requisito.
        print("Thank you for shopping at the Inkom Emporium.")

        # Obtém a data e hora atuais.
        current_date_time = datetime.now()
        # ALTERAÇÃO: Formato de data e hora conforme o requisito.
        print(f"{current_date_time:%a %b %d %H:%M:%S %Y}")

    except FileNotFoundError as e:
        # ALTERAÇÃO: Mensagem de erro para FileNotFoundError conforme o requisito.
        print("Error: missing file")
        print(e)
    except PermissionError:
        print("Erro: sem permissão para ler um dos arquivos.")
    except KeyError as key_err:
        # ALTERAÇÃO: Mensagem de erro para KeyError conforme o requisito.
        print("Error: unknown product ID in the request.csv file")
        print(key_err)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def read_dictionary(filename, key_column_index):
    """Lê o conteúdo de um arquivo CSV em um dicionário composto.
    Parâmetros:
        filename: o caminho do arquivo CSV a ser lido.
        key_column_index: o índice da coluna a ser usada como chave no dicionário.
    Retorna: um dicionário que contém os dados do arquivo CSV.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Pula a linha do cabeçalho
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary


# Protege a chamada da função main.
if __name__ == "__main__":
    main()