import pandas as pd
from faker import Faker
import random

# Inicializar faker
fake = Faker('pt_BR')

# Parâmetros
num_registros = 100000

# Exemplos de produtos
produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Smartphone']

# Gerar dados
dados = []
for _ in range(num_registros):
    qtde = random.randint(1, 10)
    vunit = round(random.uniform(100.0, 3000.0), 2)
    total = round(qtde * vunit,2)
    registro = {
        'Data_Venda': fake.date_between(start_date='-4y', end_date='today'),
        'Nome_Cliente': fake.name(),
        'Cidade': fake.city(),
        'Produto': random.choice(produtos),
        'Quantidade': qtde,
        'Valor_Unitario': vunit,
        'Valor_Total': total
    }
    dados.append(registro)

# Criar DataFrame e exportar para CSV
df = pd.DataFrame(dados)
df.to_csv('dados_vendas.csv', index=False, sep=';')

print("Arquivo 'dados_vendas.csv' gerado com sucesso!")