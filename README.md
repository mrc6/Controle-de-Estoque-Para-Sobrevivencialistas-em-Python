# Controle-de-Estoque-Para-Sobrevivencialistas-em-Python

Este programa é uma CLI no qual você poderá gerenciar o estoque de alimentos perecíveis de sua dispensa.
# Como baixar?
- No terminal digite o comando `git clone https://github.com/mrc6/Controle-de-Estoque-Para-Sobrevivencialistas-em-Python.git`

# Requisitos
- Python > 3.6
- MongoDB

# O que é possível fazer com este programa?
- Criar um produto em estoque com nome, quantidade e data de validade
- Excluir um produto
- Verificar quais produtos estão vencidos
- Listar todos os produtos

# Como usar
- Na pasta raiz do projeto, depois de subir o MongoDB, no shell (linux) digite o seguinte comando: `python3 -m venv .venv && source .venv/bin/activate`
- Instale as dependências digitando no terminal `pip3 install -r requirements.txt`
- Acesse o diretório do projeto digitando no terminal `cd ces`
- Agora digite o comando `python3 ces.py` para rodar o programa e siga as instruções da tela