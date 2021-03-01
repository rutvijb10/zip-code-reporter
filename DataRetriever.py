import pandas as pd

# Class To Retrieve Data
class DataRetriever(object) :

    # Method To Retrieve Data from HTTP URL (public source)
    def getDataFromURL(self, path) :
        return pd.read_csv(path)
