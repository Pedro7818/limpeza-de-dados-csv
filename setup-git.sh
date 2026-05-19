#!/bin/bash
# Script para inicializar repositórios Git e fazer commit inicial
# Execute este script em cada diretório do projeto

# Configurar Git (execute uma única vez)
git config --global user.name "Pedro"
git config --global user.email "seu-email@exemplo.com"

# Inicializar repositório
git init

# Adicionar arquivos
git add .

# Fazer commit inicial
git commit -m "Projeto: Limpeza de dados CSV para portfólio de estágio"

echo "✅ Repositório inicializado com sucesso!"
echo "Próximo passo: Criar repositório no GitHub e fazer push"
