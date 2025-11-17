import pandas as pd
import os
from datetime import datetime

class ControleDespesas:
    def __init__(self, arquivo_excel):
        """Inicializa o controle lendo o arquivo de despesas."""
        self.arquivo_excel = arquivo_excel
        self.df = self._carregar_dados()

    def _carregar_dados(self):
        """Tenta carregar o arquivo Excel. Se não existir, cria um DataFrame vazio."""
        if os.path.exists(self.arquivo_excel):
            print(f"Lendo dados do arquivo: {self.arquivo_excel}")
            df = pd.read_excel(self.arquivo_excel)
        else:
            print(f"Arquivo '{self.arquivo_excel}' não encontrado. Criando um novo DataFrame.")
            df = pd.DataFrame(columns=['Data', 'Categoria', 'Descricao', 'Valor'])
       
        
        df['Data'] = pd.to_datetime(df['Data'])
        return df

    def _salvar_dados(self):
        """Salva o DataFrame atualizado no arquivo Excel."""
        self.df.to_excel(self.arquivo_excel, index=False)
        print(f"\nDados salvos em {self.arquivo_excel}")

    def somar_gastos_por_categoria(self):
        """Soma e exibe os gastos agrupados por categoria."""
        print("\n--- 📊 Gastos Totais por Categoria ---")
        if self.df.empty:
            print("Nenhuma despesa registrada para análise.")
            return None
           
        gastos_categoria = self.df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
       
        for categoria, total in gastos_categoria.items():
            print(f"{categoria:<15}: R$ {total:,.2f}")
           
        return gastos_categoria

    def exibir_total_mensal(self):
        """Calcula e exibe o total de despesas por mês."""
        if self.df.empty:
            return
           
        
        self.df['Mes_Ano'] = self.df['Data'].dt.to_period('M')
       
        total_mensal = self.df.groupby('Mes_Ano')['Valor'].sum()
       
        print("\n--- 📅 Total de Despesas por Mês ---")
        for mes, total in total_mensal.items():
            print(f"{mes}: R$ {total:,.2f}")

    def inserir_nova_despesa(self):
        """Permite que o usuário insira uma nova despesa via console."""
        print("\n--- ➕ Inserir Nova Despesa ---")
        try:
            # 1. Data (opcional, usa a data atual se vazia)
            data_input = input("Data (DD/MM/AAAA - Deixe em branco para usar hoje): ")
            if data_input:
                data = datetime.strptime(data_input, '%d/%m/%Y')
            else:
                data = datetime.now()
               
            # 2. Outros campos
            categoria = input("Categoria (Ex: Alimentação, Moradia, Transporte): ").strip().capitalize()
            descricao = input("Descrição: ").strip()
            valor = float(input("Valor (Ex: 50.50): "))

            nova_despesa = pd.DataFrame([{
                'Data': data,
                'Categoria': categoria,
                'Descricao': descricao,
                'Valor': valor
            }])
           
            # Adiciona a nova despesa ao DataFrame existente
            self.df = pd.concat([self.df, nova_despesa], ignore_index=True)
            self._salvar_dados()
            print("✅ Despesa inserida com sucesso!")

        except ValueError as e:
            print(f"❌ Erro na entrada de dados (Valor ou Data): {e}")
        except Exception as e:
            print(f"❌ Ocorreu um erro: {e}")

    def exportar_resumo_por_categoria(self, nome_arquivo="Resumo_Gastos_Categoria.xlsx"):
        """Exporta um novo arquivo Excel com o resumo de gastos por categoria."""
        gastos_categoria = self.somar_gastos_por_categoria()
       
        if gastos_categoria is not None:
            resumo_df = gastos_categoria.reset_index()
            resumo_df.columns = ['Categoria', 'Total Gasto (R$)']
           
            resumo_df.to_excel(nome_arquivo, index=False)
            print(f"\n--- 📤 Resumo exportado com sucesso para: {nome_arquivo} ---")
           
    def executar(self):
        """Menu de execução principal."""
        while True:
            print("\n==================================")
            print("  💻 Controle de Despesas Pessoais")
            print("==================================")
            print("1. Inserir Nova Despesa")
            print("2. Analisar Gastos por Categoria")
            print("3. Analisar Total Mensal")
            print("4. Exportar Resumo por Categoria")
            print("5. Sair")
           
            escolha = input("Selecione uma opção (1-5): ")
           
            if escolha == '1':
                self.inserir_nova_despesa()
            elif escolha == '2':
                self.somar_gastos_por_categoria()
            elif escolha == '3':
                self.exibir_total_mensal()
            elif escolha == '4':
                self.exportar_resumo_por_categoria()
            elif escolha == '5':
                print("Saindo do programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    
    NOME_ARQUIVO = "lancamentos_despesas.xlsx"
   
    
    controle = ControleDespesas(NOME_ARQUIVO)
    controle.executar()