import pandas as pd

INPUT_CSV = "vendas.csv"
OUTPUT_CSV = "vendas_limpo.csv"


def limpar_vendas(arquivo_entrada: str, arquivo_saida: str) -> bool:
    """Lê um CSV de vendas, remove duplicatas, trata valores vazios e exporta um CSV limpo."""
    try:
        print(f"📥 Lendo arquivo: {arquivo_entrada}")
        df = pd.read_csv(arquivo_entrada)

        print(f"📊 Linhas originais: {len(df)}")
        print("\n🔎 Valores vazios por coluna antes da limpeza:")
        print(df.isnull().sum())

        df = df.dropna(how="all")
        print("\n✅ Linhas completamente vazias removidas")

        for coluna in df.columns:
            if df[coluna].dtype == "object":
                df[coluna] = df[coluna].fillna("N/A")
            else:
                df[coluna] = df[coluna].fillna(0)

        print("✅ Valores vazios tratados")

        duplicatas_antes = len(df)
        df = df.drop_duplicates()
        removidas = duplicatas_antes - len(df)
        print(f"✅ {removidas} linha(s) duplicada(s) removida(s)")

        df.to_csv(arquivo_saida, index=False, encoding="utf-8")
        print(f"\n✅ CSV limpo salvo em: {arquivo_saida}")
        print(f"📊 Linhas finais: {len(df)}")
        print("\n✨ Exemplo de dados limpos:")
        print(df.head(5).to_string(index=False))
        return True

    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_entrada}")
        return False
    except Exception as erro:
        print(f"❌ Erro ao processar o CSV: {erro}")
        return False


if __name__ == "__main__":
    limpar_vendas(INPUT_CSV, OUTPUT_CSV)
