import requests

PROPERTY_DETAILS_URL = "https://www.zillow.com/graphql/?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2263761f105f213460f11317ce8363575827a54a0ef622269b405e3e8fd479d1d4%22%7D%7D&variables=%7B%22zpid%22%3A50679473%2C%22platform%22%3A%22DESKTOP_WEB%22%2C%22formType%22%3A%22OPAQUE%22%2C%22contactFormRenderParameter%22%3A%7B%22zpid%22%3A50679473%2C%22platform%22%3A%22desktop%22%2C%22isDoubleScroll%22%3Atrue%7D%2C%22skipCFRD%22%3Afalse%7D"

headers = {
            "Cookie": 'x-amz-continuous-deployment-state=AYABeN1HVbT7J%2Fc0LVxS0uOvwFUAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADIzW1MqY6aaa0NJ+2QAwGpVwKstRimHsgo7p255gcJA5J0sSkV75ObYSZQU1jhdVDSbVQCYFUa4D9IWwR+TrAgAAAAAMAAQAAAAAAAAAAAAAAAAAAASJh0vSZEdNeGlUUleGT57%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxVo3LCvqy13UL0Z2YKLrBHbOr6mSsy+2MqYxt6; JSESSIONID=6C07615BE4C618539DA81B00A698E15A; zguid=24|%244cf08c0c-8a55-4308-9ac2-a57d58fde8ac; zgsession=1|2ead6964-7360-4195-9ab3-34701e94dd99; _ga=GA1.2.1628308424.1694148875; _gid=GA1.2.1506497957.1694148875; zjs_anonymous_id=%224cf08c0c-8a55-4308-9ac2-a57d58fde8ac%22; zjs_user_id=null; zg_anonymous_id=%2214db3169-c5e1-4203-97e5-f68eff9d6c8a%22; x-amz-continuous-deployment-state=AYABeJOdkVTfInkWf8xqhX%2Fm1eIAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADHvx4WCDQyYXA%2FuFJAAw+vsRLpEFWMdOCWBWq8kK%2FTCDCt0gFGvn9Cg6%2FKbWn+XSzUqLX4Zz0iuB8L3ScYO%2FAgAAAAAMAAQAAAAAAAAAAAAAAAAAAF7mKMSy%2F94sO%2FFLfzGVHSn%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAzz9kZWctWz%2F71SyRGT4sGWGzarasOwMDr7nLNq; _gcl_au=1.1.649793574.1694149149; DoubleClickSession=true; __pdst=6d088fc0ceeb4e59904dc1c951148a06; _fbp=fb.1.1694149153245.222697292; tfpsi=98b0a3ea-7663-49de-91de-8b8164f9369a; _pin_unauth=dWlkPU9ESTFaREE1TTJJdE1USm1aaTAwTURVMkxUZzVOV1V0TmpnMU5EQTJNV0UyWVdVMw; _clck=icghu2|2|feu|0|1346; pxcts=78670fe7-4e05-11ee-bf32-9cc3979fd939; _pxvid=7866fc5b-4e05-11ee-bf32-54c53dc0eae8; __gads=ID=7e997c1b120b140a:T=1694149128:RT=1694150971:S=ALNI_MaegjswS-k-9vySyoiNthOU5pUO6g; __gpi=UID=00000c9dd26b3fe2:T=1694149128:RT=1694150971:S=ALNI_MawcLhIWaYF5aoToTrRUTNZtMbXBw; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_cfp=1; _pxff_bsco=1; _gat=1; _px3=50b82e694f03a73c803a296c93ab3fbad1ae192e26efbbaec6c6228a434d228c:nTgM7Ar10l04Dx8BGdhkqHO1pNt256TJJX5M6oB8OCV8eZf/pHS5d+dDyHj2eB8wSIv2mSXC+q3HEtQoqQlUQA==:1000:EPjFN6ko9RoX7aTNNyGl3bGZqGpFPDTttsyoCoxV8Yw29Ou2SUqx0TZ4qyhpIwOGYO0+Hb8oImZH2J36esMlm+3KB1QqOHWEpWcFdjZp97VDjcIzLegfn/cgQJGLWFcaolLNe2pQdYSGaqcSdq1cIzg6Pyk0NRiWWf2OGbXlMPYUMfSWVHCnaQqQhaQuW+pHxNPM+O/Q5whrnZsLrJx25Q==; AWSALB=ct+QyBDt1jMYf/Tz0NVVL8Oa5KHyS5RhBMbqe56KbxeM1O8biFGfbt0rBZ4mKR25X18VDUoTOHwUDy+um8vQYSvoHxUvFtEwfsarVgfb0JM3RBAzH9beaTTyFKwh; AWSALBCORS=ct+QyBDt1jMYf/Tz0NVVL8Oa5KHyS5RhBMbqe56KbxeM1O8biFGfbt0rBZ4mKR25X18VDUoTOHwUDy+um8vQYSvoHxUvFtEwfsarVgfb0JM3RBAzH9beaTTyFKwh; search=6|1696743237556%7Crect%3D36.81261568046124%252C-91.44158859375%252C25.48670686898427%252C-108.71209640625%26rid%3D54%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Dpricea%26z%3D1%26listPriceActive%3D1%26type%3Dhouse%26lt%3Dfsbo%26price%3D200000-%26mp%3D1078-%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0954%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; _uetsid=72fe6a904e0411ee9d33b7e3d0ed2073; _uetvid=72ff9a204e0411eea067d3be926e6b3c; _clsk=1t2uy3d|1694151245653|10|0|x.clarity.ms/collect',
            "Sec-Ch-Ua": "",
            "Content-Type": "application/json",
            'Client-Id': "for-sale-sub-app-browser-client",
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36",
            "Sec-Ch-Ua-Platform": "",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.zillow.com/homedetails/158-Gilson-Rd-Brownsville-TX-78520/50679473_zpid/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "If-None-Match": 'W/"3109a-yKMauXY2HjSKYdbDnX9aMBf4SCw-gzip"'
            }

response = requests.get(PROPERTY_DETAILS_URL, headers=headers)

with open("property.json", "w") as p:

    p.write(response.text)
