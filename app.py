# Antes de rodar esse script lembre-se de garantir a instalação dos módulos necessários:
# python -m pip install --no-cache -r ./requirements.txt

# Imports de bibliotecas

import pandas as pd
import sqlite3

def create_data():
    """Função serve apenas para criar dados na tabela para ter o que retornar na query"""
    data = {
        "first_name":["João", "Maria", "José"],
        "last_name":["Silva", "Santos", "Souza"]
    }

    pd.DataFrame(data).to_sql(con=engine, name="Usuarios", if_exists="append", index=False)

# Se estiver no windows vc precisa 'escapar' a contra barra 
# pra funcionar corretamente ex: 'C:\\banco.db'
CAMINHO = "Coloca aqui o caminho do arquivo '.db'"

engine = sqlite3.connect(CAMINHO)

# Isso aqui só serve pra criar alguma coisa na tabela pra poder ter dados lá, se a sua base ja tiver coisas lá pode deixar comentado
# create_data()

return_value = engine.execute("select * from Usuarios").fetchall()

print(return_value)


