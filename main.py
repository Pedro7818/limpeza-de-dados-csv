import pandas as pd
import os
from datetime import datetime

def limpar_dados(arquivo_entrada, arquivo_saida):
    """
    Lê um arquivo CSV, remove duplicatas, trata valores vazios
    e exporta um CSV limpo.
    
    Args:
        arquivo_entrada (str): Caminho do arquivo CSV de entrada
        arquivo_saida (str): Caminho do arquivo CSV de saída
    """
    
    try:
        # Ler o arquivo CSV
        print(f"📖 Lendo arquivo: {arquivo_entrada}")
        df = pd.read_csv(arquivo_entrada)
        
        print(f"📊 Total de linhas originais: {len(df)}")
        
        # Exibir informações sobre valores vazios antes da limpeza
        print("\n🔍 Valores vazios por coluna (antes da limpeza):")
        print(df.isnull().sum())
        
        # Remover linhas completamente vazias
        df = df.dropna(how='all')
        print(f"\n✅ Linhas completamente vazias removidas")
        
        # Tratar valores vazios - preencher com valores padrão por tipo
        for coluna in df.columns:
            if df[coluna].dtype == 'object':
                # Para colunas de texto, preencher com "N/A"
                df[coluna].fillna("N/A", inplace=True)
            elif df[coluna].dtype in ['float64', 'int64']:
                # Para colunas numéricas, preencher com 0
                df[coluna].fillna(0, inplace=True)
        
        print(f"✅ Valores vazios tratados")
        
        # Remover linhas duplicadas
        duplicatas_antes = len(df)
        df = df.drop_duplicates()
        duplicatas_removidas = duplicatas_antes - len(df)
        
        if duplicatas_removidas > 0:
            print(f"✅ {duplicatas_removidas} linhas duplicadas removidas")
        else:
            print(f"✅ Nenhuma duplicata encontrada")
        
        # Exportar CSV limpo
        df.to_csv(arquivo_saida, index=False, encoding='utf-8')
        
        print(f"\n📊 Total de linhas finais: {len(df)}")
        print(f"✨ Arquivo limpo salvo em: {arquivo_saida}")
        print(f"\n📋 Primeiras linhas do arquivo limpo:")
        print(df.head())
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{arquivo_entrada}' não encontrado")
        return False
    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {str(e)}")
        return False

if __name__ == "__main__":
    # Definir caminhos
    arquivo_entrada = "vendas_exemplo.csv"
    arquivo_saida = f"vendas_limpas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    # Executar limpeza
    limpar_dados(arquivo_entrada, arquivo_saida)
