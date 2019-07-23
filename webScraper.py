import pandas
import requests



# structure = {"Data1": [1,3,4,5,],
#              "Data2": [9,0,3,4],
#              "Data3": [88, 34,22,1]}
#
# print(pandas.DataFrame(structure))

indicators = {"Previous Close": [],
              "Open": [],
              "Bid": [],
              "Ask": [],
              "Day's Range": [],
              "52 Week Range": [],
              "Volume": [],
              "Avg. Volume": [],
              "Market Cap": [],
              "Beta": [],
              "PE Ratio (TIM)": [],
              "EPS (TTM)": [],
              "Earnings Date": [],
              "Dividend & Yield": [],
              "Ex-Dividend Date": [],
              "1y Target Est": []}

              

call = requests.get(url="https://finance.yahoo.com/quote/TRTC?p=TRTC&.tsrc=fin-srch")
# print(call.text)
htmlText = call.text

splitList = htmlText.split("Previous Close")

firstSplit = splitList[1].split("\">")[2]
secondSplit = firstSplit.split("</td>")
print(secondSplit[0].replace("</span>", ""))
