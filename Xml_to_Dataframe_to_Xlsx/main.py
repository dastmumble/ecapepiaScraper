import os
import pandas as pd

Dataframe = pd.read_xml("./pigPriceDetail.xml")

#엑셀 선택하고 시트 선택하기
file_path = "./output.xlsx"
sheetName = "test"
#엑셀로 입력하기
if not os.path.isfile(file_path):
    Dataframe.to_excel(
        file_path,
        sheet_name=sheetName,
        index=False,
        )
else:
    with pd.ExcelWriter(
        file_path,
        mode = "a",
        engine="openpyxl",
        if_sheet_exists="overlay"
        ) as writer:
        startingRow = writer.sheets["test"].max_row
        Dataframe.to_excel(
            writer,
            sheet_name=sheetName,
            startrow=startingRow, 
            index =False,
            header=False, 
            )

