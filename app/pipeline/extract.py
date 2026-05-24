import glob  # biblioteca para buscar arquivos e pastas (listar arquivos)
import os  # biblioteca para manipular arquivos e pastas
from pathlib import Path
from typing import (
    List,
)  # biblioteca para tipagem (retornar lista de DataFrames)

import pandas as pd

local = Path(__file__).parents[0].resolve()
path = local / 'data' / 'input'


def extract_from_excel(input_folder: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de uma pasta e retornar um DataFrame

    Args:
        input_folder (str): Caminho da pasta onde estão os arquivos

    Returns:
        List[pd.DataFrame]: Lista de DataFrames com a lista de DataFrames.
    """

    all_files = glob.glob(os.path.join(input_folder, '*.xlsx'))
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    return data_frame_list


if __name__ == '__main__':

    dataframes = extract_from_excel(path)
    print(dataframes)
