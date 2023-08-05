# coding:utf8
import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pandas as pd
import pytz
import xlsxwriter


# Função para selecionar os dados para a coluna 'Análise'
def analisar_diferenca(diferenca):
    if diferenca > 0:
        return "Vagas Disponíveis"
    elif diferenca == 0:
        return "Não há vagas"
    elif diferenca < 0:
        return "Vagas excedidas"
    else:
        return ""


def escola(row):
    nome_escola = row.split(' ')[-1].capitalize() if 'MARINGA' not in row else 'Maringá'
    return nome_escola


def cr_curso(df):
    dict_cr = {}
    ndf = df.drop_duplicates().reset_index(drop=True)
    for index, row in ndf.iterrows():
        if row['Validador'] not in dict_cr and ~pd.isna(row['CR Curso']):
            dict_cr[row['Validador']] = int(row['CR Curso'])
    return dict_cr


def trata_turma(row):
    ano_sem = datetime.datetime.now()
    ano = str(ano_sem.year)
    sem = '1' if 1 <= ano_sem.month <= 6 else '2'
    ano_sem = f'{ano}/{sem}'
    turma = row.replace(f'{ano_sem}', '').replace(' -', '').strip()
    turma = turma.split()
    turma = f'{turma[0]} {turma[-1]}'
    return turma


def acompanhamento_cfs(arq_ch, name):
    # Leitura do arquivo
    df_vagas = pd.read_excel(arq_ch)

    # Dicionários para seleção de tipo de turma e escola
    dicionario_tipos = {
        "U1": "Eletiva",
        "U2": "Eletiva",
        "U3": "Eletiva",
        "E": "Especial",
        "E1": "Especial",
        "E2": "Especial",
        "GCL": "Global Class",
        "GCL1": "Global Class",
        "GCL2": "Global Class",
        "GCL3": "Global Class",
        "GCL3 1": "Global Class",
        "GCL3 2": "Global Class",
        "LEAEADBA": "LEA",
        "LEAEADCV": "LEA",
        "LEAEADDI": "LEA",
        "LEAEADEH": "LEA",
        "LEAEADME": "LEA",
        "LEAEADNE": "LEA",
        "LEAEADPO": "LEA",
        "LETTCEAD": "LETTC",
        "LETTCU1": "LETTC",
        "LETTCU2": "LETTC",
        "A": "Regular",
        "B": "Regular",
        "C": "Regular",
        "D": "Regular",
        "U": "Regular",
    }

    # Ordenação das colunas
    df_vagas = df_vagas[
        ["Estabelecimento", "CR Curso", "Curso", "Período", "Agrupamento", "Turma", "Disciplina", "Divisão",
         "Qtde de Alunos Matriculados", "Nr Vagas Cadastradas", "Professor", "Data da Semana", "Tem Corte"]]

    df_vagas = df_vagas.loc[df_vagas['Estabelecimento'] != 'PUCPR - CURITIBA'].reset_index(drop=True)
    df_vagas = df_vagas.loc[df_vagas['Data da Semana'] != " "]
    df_vagas = df_vagas.loc[df_vagas['Tem Corte'] == "Sim"]

    df_vagas.insert(0, 'Validador', '', True)
    df_vagas['Validador'] = df_vagas.apply(
        lambda row: f"{str(row['Estabelecimento']).strip()} "
                    f"{str(row['Curso']).strip()} "
                    f"{trata_turma(row['Turma'])}",
        axis=1)
    dict_cr = {}
    dict_cr = cr_curso(df_vagas.loc[:, ('CR Curso', 'Validador')])

    # Conversão de colunas para inteiro
    df_vagas["Período"] = df_vagas["Período"].fillna(0.0).astype(int)
    df_vagas["Qtde de Alunos Matriculados"] = df_vagas["Qtde de Alunos Matriculados"].replace(' ', 0.0).fillna(0.0) \
        .astype(int)
    df_vagas["Nr Vagas Cadastradas"] = df_vagas["Nr Vagas Cadastradas"].replace(' ', 0.0).fillna(0.0).astype(int)
    df_vagas["CR Curso"] = df_vagas.apply(lambda row_vagas: dict_cr.get(row_vagas['Validador']), axis=1)

    del df_vagas['Validador']

    # Criação da coluna 'Escola', com os valores do dicionário conforme o código do curso
    df_vagas.insert(1, 'Escola', '', True)
    df_vagas['Escola'] = df_vagas.apply(lambda row_vagas: escola(row_vagas['Estabelecimento']), axis=1)

    # Criação das colunas de Análise (se existem vagas) e diferença (vagas totais - alunos cadastrados)
    df_vagas.insert(11, 'Análise', "")
    df_vagas.insert(12, 'Diferença', "")

    df_vagas['Diferença'] = df_vagas.apply(
        lambda row_vagas: row_vagas["Nr Vagas Cadastradas"] - row_vagas["Qtde de Alunos Matriculados"], axis=1)
    df_vagas['Análise'] = df_vagas.apply(lambda row_vagas: analisar_diferenca(row_vagas["Diferença"]), axis=1)

    # Criação da coluna 'Tipo' (de turma)
    df_vagas.insert(6, 'Tipo', "", True)
    df_vagas['Tipo'] = df_vagas.apply(
        lambda row_vagas: dicionario_tipos.get(row_vagas["Agrupamento"], row_vagas["Agrupamento"]), axis=1)

    # Remoção de linhas duplicadas (não essencial para este contexto)
    df_vagas = df_vagas.drop_duplicates()

    # Criação do arquivo de saída
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()

    # Criação de estilos de células
    formato_verde = workbook.add_format({'font_color': '#006100'})
    formato_verde.set_bg_color('#C6EFCE')
    formato_amarelo = workbook.add_format({'font_color': '#9C5700'})
    formato_amarelo.set_bg_color('#FFEB9C')
    formato_vermelho = workbook.add_format({'font_color': '#9C0031'})
    formato_vermelho.set_bg_color('#FFC7CE')

    # Looping para impressão dos resultados
    row = 1
    for index, linha in df_vagas.iterrows():
        disciplina = linha[8]
        if "Eu, Não Robô" in disciplina or "Eu, não Robô" in disciplina:
            linha[6] = "Slash"  # Tipo de turma

        # Para cada coluna, exceto 'Data da Semana'
        for x in range(0, 15):
            item = str(linha[x])
            if item == "nan":
                item = ''
            if x == 12:  # Coluna de análise
                if item == "Vagas Disponíveis":
                    worksheet.write(row, x, item, formato_verde)
                elif item == "Não há vagas":
                    worksheet.write(row, x, item, formato_amarelo)
                elif item == "Vagas excedidas":
                    worksheet.write(row, x, item, formato_vermelho)
                else:
                    worksheet.write(row, x, item)
            elif x == 13:  # Coluna de diferença
                if str(linha[x - 1]) == "Vagas Disponíveis":
                    worksheet.write(row, x, item.split('.')[0], formato_verde)
                elif str(linha[x - 1]) == "Não há vagas":
                    worksheet.write(row, x, item.split('.')[0], formato_amarelo)
                elif str(linha[x - 1]) == "Vagas excedidas":
                    worksheet.write(row, x, item.split('.')[0], formato_vermelho)
                else:
                    worksheet.write(row, x, item.split('.')[0])
            else:
                worksheet.write(row, x, item)

        row += 1

    # Formatação da tabela (cabeçalho)
    worksheet.add_table(0, 0, row - 1, 14, {'style': 'Table Style Light 1', 'columns': [
        {'header': 'Estabelecimento'},
        {'header': 'Escola'},
        {'header': 'CR Curso'},
        {'header': 'Curso'},
        {'header': 'Período'},
        {'header': 'Sigla'},
        {'header': 'Tipo'},
        {'header': 'Turma'},
        {'header': 'Disciplina'},
        {'header': 'Divisão'},
        {'header': 'Matriculados'},
        {'header': 'Vagas Cadastradas'},
        {'header': 'Análise'},
        {'header': 'Diferença'},
        {'header': 'Professor'}
    ]})

    # Formatação da tabela (largura das colunas)
    worksheet.set_column('A:A', 18)
    worksheet.set_column('B:B', 23)
    worksheet.set_column('C:C', 10.5)
    worksheet.set_column('D:D', 50)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 15)
    worksheet.set_column('G:G', 11)
    worksheet.set_column('H:H', 43)
    worksheet.set_column('I:I', 65)
    worksheet.set_column('J:J', 9)
    worksheet.set_column('K:K', 28)
    worksheet.set_column('L:L', 22)
    worksheet.set_column('M:M', 17)
    worksheet.set_column('N:N', 12)
    worksheet.set_column('O:O', 51)

    workbook.close()


if __name__ == '__main__':
    # Janela para usuário selecionar arquivo
    Tk().withdraw()
    arq_ch = askopenfilename(
        filetypes=[('Arquivo excel', '.xlsx')],
        title='Selecione o relatório de carga horária por turma / disciplina')

    # Seleção da data atual
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    dt_now = utc_now.astimezone(pytz.timezone("America/Sao_Paulo"))

    file_name = f'CFS_arquivo_vagas {str(dt_now.strftime("%Y-%m-%d %H-%M"))}.xlsx'

    acompanhamento_cfs(arq_ch, file_name)
