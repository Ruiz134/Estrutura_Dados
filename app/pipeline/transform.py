import pandas as pd
from typing import List



def transform_concat_dataframes(data: list[pd.DataFrame]) -> pd.DataFrame:

    """
        Função para transformar uma lista de DataFrames em um unico DataFrame
        concatenando todos os dataframes em um só e ordenando por id

    args:
        data (list[pd.DataFrame]): Lista de DataFrames
    
    returns:
        pd.DataFrame: DataFrame concatenado
    """

    df = pd.concat(data, ignore_index=True)
    # df = df.sort_values(by=['id'])
    # df = df.reset_index(drop=True)
    return df