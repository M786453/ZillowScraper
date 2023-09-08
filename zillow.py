import requests
import json
import pandas as pd

class zillow:

    def __init__(self):
        
        self.headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36",
                    "Accept": "*/*"
                    }
        
        self.properties_data = {"Property Address": [], "Owner Phone": []}

    def getListingDetails(self):

        LISTING_URL = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A36.81261568046124%2C%22east%22%3A-91.44158859375%2C%22south%22%3A25.48670686898427%2C%22west%22%3A-108.71209640625%7D%2C%22usersSearchTerm%22%3A%22TX%22%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22category%22%3A%22cat2%22%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22isCondo%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isApartment%22%3A%7B%22value%22%3Afalse%7D%2C%22isMultiFamily%22%3A%7B%22value%22%3Afalse%7D%2C%22monthlyPayment%22%3A%7B%22min%22%3A1078%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22sortSelection%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isLotLand%22%3A%7B%22value%22%3Afalse%7D%2C%22isTownhouse%22%3A%7B%22value%22%3Afalse%7D%2C%22isManufactured%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isApartmentOrCondo%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat2%22:[%22mapResults%22]}&requestId=2"

        listing_response = requests.get(LISTING_URL, headers=self.headers)

        listing_data = json.loads(listing_response.text)["cat2"]["searchResults"]["mapResults"]
        
        return listing_data

    
    def getPropertyOwnerPhone(self, zpid):

        PROPERTY_DETAILS_URL = "https://www.zillow.com/graphql/?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2263761f105f213460f11317ce8363575827a54a0ef622269b405e3e8fd479d1d4%22%7D%7D&variables=%7B%22zpid%22%3A"+ zpid + "%2C%22platform%22%3A%22DESKTOP_WEB%22%2C%22formType%22%3A%22OPAQUE%22%2C%22contactFormRenderParameter%22%3A%7B%22zpid%22%3A" + zpid + "%2C%22platform%22%3A%22desktop%22%2C%22isDoubleScroll%22%3Atrue%7D%2C%22skipCFRD%22%3Afalse%7D"

        property_details_response = requests.get(PROPERTY_DETAILS_URL, headers=self.headers)

        property_details = json.loads(property_details_response.text)["data"]["property"]

        phone = property_details["listedBy"][0]["elements"][1]["text"]

        return phone

    def store(self):
        
        df = pd.DataFrame(self.properties_data)

        writer = pd.ExcelWriter("zillow.xlsx",engine='xlsxwriter')

        df.to_excel(writer,sheet_name="sheet1",index=False)

        writer._save()        
    
    def scrape(self):

        listing_data = self.getListingDetails()

        counter = 1

        for property in listing_data:

            try:
                zpid = str(property["zpid"])
                property_address = property["address"]
                property_owner_phone = self.getPropertyOwnerPhone(zpid)

                # update properties data
                self.properties_data["Property Address"].append(property_address)
                self.properties_data["Owner Phone"].append(property_owner_phone)
                
                # store locally
                self.store()

                #Log
                print("Property#"+ str(counter) + ":", str({"Address": property_address, "Phone": property_owner_phone}))

                counter +=1 
            except Exception as e:
                print(str(e))




zillow().scrape()


