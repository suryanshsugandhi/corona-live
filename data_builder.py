import pandas as pd
from datetime import datetime

# Data sorting and clustering
class DataBuilder():
    __now = datetime.now()
    __today = __now.strftime("%m-%d-%Y")

    def __init__(self):
        filename = self.__today + '.csv'
        self.data = pd.read_csv('./data/' + filename)
        self.__countries = self.data['Country/Region'].unique().tolist()

    def tracker_data(self):
        """
            Return full data for map view
            Args = None
        """
        self.data.sort_values(by=['Country/Region'], inplace=True)
        return self.data.to_json(orient='index')

    def region_data(self, region="Mainland China"):
        """
            Verify region and return stats
            Args = Region name as str
        """
        df2 = self.data.groupby('Country/Region')
        val = df2.sum()
        region = region.title()
        if(region in self.__countries):
            return val.loc[region].to_json(orient='index')
        else:
            # RAISE REGION NOT FOUND ERROR HERE !!!
            return "No data"

    def total_data(self):
        """
            Return total number of confirmed, dead and recovered victims
            Args = None
        """
        df2 = self.data.sum(axis = 0, skipna = True)
        val = {
            "Confirmed" : int(df2['Confirmed']),
            "Deaths" : int(df2['Deaths']),
            "Recovered" : int(df2['Recovered']),
        }
        return val