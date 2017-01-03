# import pandas as pd
#
# # Create a Pandas dataframe from the data.
# df = pd.DataFrame({'Data': [10, 220, 30, 20, 15, 30, 45]})
#
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('pandas_simple.xlsx', engine='openpyxl')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet2')
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
from openpyxl import Workbook

class WritterXL(object):

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.mapper = {'A1' : 'Company Name',
                       'B1' : 'Position'

        }
        for x in self.mapper.keys():
            self.ws[x] = self.mapper[x]


    def write_to_file(self, data):
        print(data)
        self.ws.append(data)
        self.wb.save("../sample.xlsx")


if __name__ == "__main__":
    xl = WritterXL()
    xl.write_to_file(['jA', 'B'])
