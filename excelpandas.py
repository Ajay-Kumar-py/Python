import pandas as pd

def peoples_cell(cell):
    if cell =="n.a":
        return "ajay"
    else:
        return cell
def eps_cell(cell):
    if cell ==-1 or cell =="not available":
        return None
    else:
        return cell
df= pd.read_excel("stock_data.xlsx",sheet_name="Sheet1",converters={'people':peoples_cell,
                                                                    "eps":eps_cell

})

df.to_excel("stock.xlsx",sheet_name ='stocks',index=False,startrow=3,startcol=4 )

df1 =pd.DataFrame({"name":["ajay","abhi","nisha"],
                  "age":["29","28","26"],
                  "ID":["12","15","24"]})
print(df1)

with pd.ExcelWriter("add_sheets.xlsx") as writer:
    df.to_excel(writer,sheet_name="stock",index=False)
    df1.to_excel(writer,sheet_name="details",index=False)
