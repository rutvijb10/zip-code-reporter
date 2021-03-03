# Class To Filter Address Data by removing invalid records
# The Data passed to the methods should be Pandas DataFrame
class AddressFilter :

    # Method to get indices of non null addresses
    def validAddressCondition(self, data) :
        return data['Address01'].notnull()

    # Method to get indices of US Zip Codes
    def validUSZipCodeCondition(self, data) :
        return data['ZipCode'].str.len() == 5
    
    # Method to get indices of Canada Zip Codes
    def validCanadaZipCodeCondition(self, data) :
        return data['ZipCode'].str.len() == 7

    # Method to get indices of Canada and US Zip Codes
    def validZipCodeCondition(self, data) :
        return self.validUSZipCodeCondition(data) | self.validCanadaZipCodeCondition(data)

    # Method to filter data based on Valid Addresses and Valid Zip Codes
    def filterInvalidData(self, data) :
        validData = data[
            self.validAddressCondition(data) 
            & self.validZipCodeCondition(data)
        ]
        return validData
