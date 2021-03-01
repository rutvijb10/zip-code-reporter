from DataRetriever import DataRetriever
from AddressFilter import AddressFilter
from ZIPCodeExtractor import ZIPCodeExtractor

BASE_PATH = 'https://journeyblobstorage.blob.core.windows.net'
SUB_DOMAIN = '/sabpublic/Group'

def getURLPaths() :
    fileNames = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    paths = [ BASE_PATH + SUB_DOMAIN + fileName +'.csv' for fileName in fileNames]
    return paths

if __name__ == "__main__":
    dataRetriever = DataRetriever()
    addressFilter = AddressFilter()
    zipCodeExtractor = ZIPCodeExtractor(dataRetriever, addressFilter)
    paths = getURLPaths()
    aggregateData = zipCodeExtractor.getUniqueAddressesForZipCodes(paths)
    aggregateData.to_csv('./output/UniqueAddresses.csv',index=False)