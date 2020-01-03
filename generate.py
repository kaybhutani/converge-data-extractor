import pandas as pd

def generate(data):
  for i in data:
    dataFrame = pd.DataFrame(data[i])
    dataFrame.to_excel("./static/temp/"+i+".xlsx")