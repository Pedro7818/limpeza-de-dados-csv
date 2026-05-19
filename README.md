# Limpeza de Dados CSV

## 📋 Descrição

Este projeto implementa um script Python que realiza a limpeza e tratamento de dados em arquivos CSV. O script lê um arquivo CSV contendo dados fictícios de vendas, remove linhas duplicadas, trata valores vazios e exporta um arquivo CSV limpo.

### Funcionalidades:
- ✅ Leitura de arquivo CSV
- ✅ Remoção de linhas duplicadas
- ✅ Tratamento de valores vazios (preenchimento inteligente)
- ✅ Remoção de linhas completamente vazias
- ✅ Exportação de arquivo limpo com timestamp
- ✅ Relatório detalhado do processo

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**
- **Pandas** - Manipulação e análise de dados
- **CSV** - Formato de arquivo

## 📦 Requisitos

```bash
pip install pandas
```

## 🚀 Como Executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o script
```bash
python main.py
```

### 3. Resultado
O script gerará um arquivo `vendas_limpas_YYYYMMDD_HHMMSS.csv` contendo os dados limpos.

## 📄 Estrutura dos Arquivos

- `main.py` - Script principal de limpeza de dados
- `vendas_exemplo.csv` - Arquivo CSV de exemplo com dados de vendas (contendo dados sujos para teste)
- `README.md` - Este arquivo
- `requirements.txt` - Dependências do projeto

## 📊 Exemplo de Saída

```
📖 Lendo arquivo: vendas_exemplo.csv
📊 Total de linhas originais: 13

🔍 Valores vazios por coluna (antes da limpeza):
id                0
data              0
produto           1
quantidade        2
preco_unitario    0
categoria         1
vendedor          2

✅ Linhas completamente vazias removidas
✅ Valores vazios tratados
✅ 1 linhas duplicadas removidas

📊 Total de linhas finais: 11
✨ Arquivo limpo salvo em: vendas_limpas_20240121_143025.csv
```

## 💡 Notas

- Valores vazios em colunas de texto são preenchidos com "N/A"
- Valores vazios em colunas numéricas são preenchidos com 0
- Linhas completamente vazias são removidas
- O arquivo de saída inclui um timestamp para evitar sobrescrita

## 📝 Licença

Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais.
