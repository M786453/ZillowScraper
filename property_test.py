import requests

PROPERTY_DETAILS_URL = "https://www.zillow.com/graphql/?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2263761f105f213460f11317ce8363575827a54a0ef622269b405e3e8fd479d1d4%22%7D%7D&variables=%7B%22zpid%22%3A50679473%2C%22platform%22%3A%22DESKTOP_WEB%22%2C%22formType%22%3A%22OPAQUE%22%2C%22contactFormRenderParameter%22%3A%7B%22zpid%22%3A50679473%2C%22platform%22%3A%22desktop%22%2C%22isDoubleScroll%22%3Atrue%7D%2C%22skipCFRD%22%3Afalse%7D"

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36",
            "Accept": "*/*"
            }

response = requests.get(PROPERTY_DETAILS_URL, headers=headers)

with open("property.json", "w") as p:

    p.write(response.text)
