import pandas as pd

# Class to extract ZIP Code Data With Unique Address Count
class ZIPCodeExtractor :

    def __init__(self, dataRetriever, addressFilter):
        self.dataRetriever = dataRetriever
        self.addressFilter = addressFilter

    # Method to get Unique Addresses for Zip Code
    # Takes an array of URL paths as parameter and returns the aggregated, combined / merged data frame
    def getUniqueAddressesForZipCodes(self, paths) :
        aggregateData = pd.DataFrame(columns=['ZipCode', 'Count'])
        for path in paths :
            addresses = self.dataRetriever.getDataFromURL(path)
            groupedZipCodes = self.getAggregatedDataForAddresses(addresses)
            aggregateData = pd.merge(aggregateData, groupedZipCodes, on=['ZipCode'], how='outer')\
                .set_index('ZipCode').sum(axis=1)\
                .to_frame(name='Count').astype(int).reset_index()
        return aggregateData
    
    # Method to compute aggregate data for a set of addresses (dataframe)
    def getAggregatedDataForAddresses(self, addresses) :
        validData = self.addressFilter.filterInvalidData(addresses)
        groupedZipCodes = validData.groupby('ZipCode').Address01.nunique()\
            .to_frame(name='Count').reset_index()
        return groupedZipCodes
