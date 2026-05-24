"""Módulo responsável pelo carregamento dos dados."""

import os

import pandas as pd


def load_dataframe_to_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> None:
    """Receber Dataframe e Salvar como Excel.

    args:
    data_frame: data frame a ser salvo como excel.
    output_path: caminho para salvar o arquivo excel.
    file_name: nome do arquivo e extensao a ser salvo.

    returns:
    "Arquivo Salvo com Sucesso."
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    data_frame.to_excel(output_path + "/" + file_name, index=False)
    return "Arquivo Salvo com Sucesso"


if __name__ == "__main__":
    df_test = pd.DataFrame({"col1": [1, 2], "col2": [4, 5]})
    print(load_dataframe_to_excel(df_test, "data/output", "output.xlsx"))
