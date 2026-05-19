# Limpeza de Dados CSV

## Descrição

Projeto Python para limpeza de dados de vendas em CSV. O script `limpeza.py` lê o arquivo `vendas.csv`, remove duplicatas, trata valores vazios e exporta `vendas_limpo.csv`.

## Tecnologias usadas

- Python 3
- pandas

## Como rodar

1. Instale dependências:

```powershell
python -m pip install -r requirements.txt
```

2. Execute o script:

```powershell
python limpeza.py
```

3. O arquivo limpo será gerado como:

- `vendas_limpo.csv`

## Arquivos do projeto

- `limpeza.py` - Script de limpeza de dados
- `vendas.csv` - Arquivo de exemplo com dados fictícios
- `requirements.txt` - Dependências do projeto
- `README.md` - Documentação do projeto
- `.gitignore` - Arquivos ignorados pelo Git

## Comportamento

- Remove linhas duplicadas
- Remove linhas completamente vazias
- Preenche valores vazios em colunas de texto com `N/A`
- Preenche valores vazios em colunas numéricas com `0`
- Exporta `vendas_limpo.csv`
