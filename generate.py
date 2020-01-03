import pandas as pd

def generate(data):
  for i in data:
    try:
      dataFrame = pd.DataFrame(data[i])
      dataFrame.to_excel("./static/temp/"+i+".xlsx")
    except:
      print("excel not generated for" + i)