from faker import Faker
import pandas as pd
import random

fake = Faker("pt_BR")

categorias = [
    "Roupas",
    "Eletrônicos",
    "Beleza",
    "Casa",
    "Livros",
    "Esportes"
]

vendedores = [
    "Ana",
    "Carlos",
    "Maria",
    "João",
    "Pedro",
    "Julia"
]

status_list = [
    "Concluído",
    "Cancelado",
    "Em andamento"
]

dados = []

for pedido_id in range(1, 1001):

    dados.append({
        "pedido_id": pedido_id,
        "data": fake.date_between(
            start_date="-12M",
            end_date="today"
        ),
        "vendedor": random.choice(vendedores),
        "categoria": random.choice(categorias),
        "valor": round(random.uniform(20, 1500), 2),
        "status": random.choices(
            status_list,
            weights=[75, 15, 10]
        )[0]
    })

df = pd.DataFrame(dados)

df.to_csv(
    "data/marketplace.csv",
    index=False
)

print("Dataset criado com sucesso!")