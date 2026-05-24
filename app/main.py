"""Ponto de entrada da aplicação."""

from app.pipeline.extract import extract_from_excel
from app.pipeline.load import load_dataframe_to_excel
from app.pipeline.transform import transform_concat_dataframes

if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    data_frame = transform_concat_dataframes(data_frame_list)
    print(load_dataframe_to_excel(data_frame, "data/output", "output.xlsx"))
    print("Executado com sucesso!")
