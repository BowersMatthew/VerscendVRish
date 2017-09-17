import pandas as pd
from sodapy import Socrata
from Data import Data
class DataProcessing:
    # DataProcessing
    # File for holding the code to process the data
    def __init__(self, data):
        self.Data = data
        self.df = None


    def getData(self):

        # if state id keep state column
        client = Socrata("data.cms.gov", None)
        results = client.get("bedw-p97b", limit=200000)
        holder = pd.DataFrame.from_records(results)
        if self.Data.dateRange != '*':
            holder = holder[holder['reference_period'] == self.Data.dateRange]
        #print(holder.to_json())
        holder = holder[holder['type_of_service'] == self.Data.service]
       # print(holder.to_json())
        if self.Data.location == 'all':
            holder = holder[holder['aggregation_level'] == "STATE"]
          #  print(holder.to_json())
            holder = holder.filter(items=self.Data.data)
            self.df = holder
            return
        else:
            holder = holder[holder['aggregation_level'] == "COUNTY"]
            holder = holder[holder['state'] == self.Data.location]
            holder = holder.filter(items=self.Data.data)
            self.df = holder
            return

    def createJSON(self):
        return self.df.to_json(orient='records')
