import pandas as pd

from app.pipeline.transform import transform_concat_dataframes

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [4, 5]})
df_2 = pd.DataFrame({'col1': [7, 8], 'col2': [10, 11]})


def testar_concatenacao_lista_dataframe():
    """
    use o arrange, act e assert para testar o codigo.
    teste da função concat_dataframe dentro do arquivo transform.py
    """
    # arrange
    arrange = pd.concat([df_1, df_2], ignore_index=True)
    # act
    act = transform_concat_dataframes([df_1, df_2])
    # assert
    # usar pandas testing para comparar os dataframes
    pd.testing.assert_frame_equal(arrange, act)
