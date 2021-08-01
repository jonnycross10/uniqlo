import requests
import json

cookies = {
    'GlobalE_Data': '^%^7B^%^22countryISO^%^22^%^3A^%^22US^%^22^%^2C^%^22cultureCode^%^22^%^3A^%^22en-US^%^22^%^2C^%^22currencyCode^%^22^%^3A^%^22USD^%^22^%^2C^%^22apiVersion^%^22^%^3A^%^222.1.4^%^22^%^7D',
    'dwanonymous_5a9e935560dfa5e7eb98c0dfd3d7d419': 'acaqnGKkkyVQ6a4uhRhVxzUrLz',
    'GlobalE_CT_Data': '^%^7B^%^22CUID^%^22^%^3A^%^22815295212.795768414.761^%^22^%^2C^%^22CHKCUID^%^22^%^3Anull^%^7D',
    '_gcl_au': '1.1.1994313186.1627272391',
    'RES_TRACKINGID': '330067172568522',
    'ResonanceSegment': '1',
    '_bamls_usid': 'b7e1eab2-0ac4-4a36-8a01-54089f7b5293',
    'BVBRANDID': '42c0b339-38e1-44f4-969e-45f64aa25866',
    '_scid': '6a9bc8fe-d8a6-4c13-8f14-b158ad21c3af',
    '_lc2_fpi': '21122434c741--01fbgfwcys1tvgav42cyxb1j7r',
    '_mibhv': 'anon-1627272393720-7501539108_6598',
    '__cq_uuid': '5c9141e0-7548-11ea-9c3f-c597e50f71a3',
    '_sctr': '1^|1627196400000',
    '_pin_unauth': 'dWlkPU5qaG1NalJtWkdVdFl6RTVNUzAwWkRFekxXRmpPREV0TkRBMll6SmlPRFF4TnpZMg',
    '_fbp': 'fb.1.1627272395949.173359817',
    '__attentive_cco': '1627272396102',
    '__attentive_id': '3c048d38fd4f4b33b0e687dea41c8353',
    'extole_access_token': 'HICVDD9TOHC4SMCU8EAU94PSVG',
    '_loop_ga': 'GA1.2.999120280.1627272393',
    '_rdt_uuid': '1627272396577.23a3d549-c571-476f-b26a-7f42220d5bc3',
    '_gaexp': 'GAX1.2.uSLXaap8RTa1v5Rl8kgs2w.18881.1',
    '_aeaid': '77d87b13-7413-4c0b-8552-8163a05bbda6',
    'sn3t4d1n': 'A0Ue_uB6AQAAPpbdMACDJMFeT7VEv2Cr7wX8qWkUNWZy0aR9U0MIgqKoLbYtAWjcEsuucsP1wH8AAEB3AAAAAA^|1^|1^|6bd9e44328f5824dcdbea20b657040fdb5e78b7e',
    'fita.sid.uniqlo_us': 'LF-Ma3Q_rEqoWrLnM__xYSLCToI7Kde2',
    'RoktRecogniser': '6018aada-edf2-406d-a4ba-536a9a26de25',
    'cqcid': 'acaqnGKkkyVQ6a4uhRhVxzUrLz',
    '__cq_dnt': '0',
    'dw_dnt': '0',
    'dw': '1',
    'dw_cookies_accepted': '1',
    '_gid': 'GA1.2.1042636973.1627758402',
    '_li_dcdm_c': '.uniqlo.com',
    '__attentive_ss_referrer': '^\\^https://www.google.com/^\\^',
    '__attentive_dv': '1',
    '_loop_ga_gid': 'GA1.2.1158275453.1627758403',
    'GlobalE_Full_Redirect': 'false',
    '_gcl_aw': 'GCL.1627758511.Cj0KCQjw6ZOIBhDdARIsAMf8YyE4-MuQf5Z5RtCje4gNH-80ZiKMSK9CxqwDsidz2KZe_NQOyOWHimMaAqorEALw_wcB',
    '_gcl_dc': 'GCL.1627758511.Cj0KCQjw6ZOIBhDdARIsAMf8YyE4-MuQf5Z5RtCje4gNH-80ZiKMSK9CxqwDsidz2KZe_NQOyOWHimMaAqorEALw_wcB',
    '_gac_UA-494938-36': '1.1627758513.Cj0KCQjw6ZOIBhDdARIsAMf8YyE4-MuQf5Z5RtCje4gNH-80ZiKMSK9CxqwDsidz2KZe_NQOyOWHimMaAqorEALw_wcB',
    '_gac_UA-35976953-6': '1.1627758513.Cj0KCQjw6ZOIBhDdARIsAMf8YyE4-MuQf5Z5RtCje4gNH-80ZiKMSK9CxqwDsidz2KZe_NQOyOWHimMaAqorEALw_wcB',
    'testVersion': 'versionA',
    'applyCouponToggle': 'true',
    'storeZipCode': '95765',
    'emailCookie': 'crossjonny5^@gmail.com',
    'dwac_98863d425aea329e9145100996': 'R1ZaEuepbIC9BKwr1csIrWFuy6ky61pk2vE^%^3D^|dw-only^|^|^|USD^|false^|US^%^2FEastern^|true',
    'cquid': '^|^|',
    'sid': 'R1ZaEuepbIC9BKwr1csIrWFuy6ky61pk2vE',
    'dwsid': '6Xuf3zqsygu88ipdmi2hss9DDmTv7vzv2wcNhjTdjf64h-YPXsqIK1TZquRglso3KG2M7u34h9sdEgLarkU3fQ==',
    '_abck': 'AD46A5DF55ACD7BB4D1AB04C32E89DD2~0~YAAQHgF8aP+uWP56AQAA6ApPAAYj0l64l0PQXisQKYIgaH8R1wFHvlDwf2H0C/XPNotaipl44gkOXrCyZ9xUP5xfSKlRLiKFALM1oVUj5qzQ41iWnPL5Fi1gNJIh0Yi6ABTlNjzrlUc+N1fvbv3C02L+UTc+Hui6ZlfT8O8bSjalhEMTCflNovV/pfyFlWVfjDe2iNpFFsd9MwDE8vccfVrD8fULPWxH4HgTYeiCqwahCXLehWxt9u349jBXfvf0Tvt41XKNjqMuLsEHX1WvjZdO2ShDBiv7LL1cUPcg9z1VzjBoCfIXlHIKqsmOe3B7SDM6hg6iFzrRyORrHk1pSxe1Hchmp3fNl90Gjtx+WqZBwyiNU8MdrocAnZUlXPj9XUdpXZ5bFyOuSvKYd38lk0iUfZ07vMnk~-1~-1~-1',
    'bm_sz': '7F8D5F59F8F67939AFC86C4E5B404785~YAAQHgF8aAGvWP56AQAA6ApPAAxil2qoBCHgaYTVZhqrpL17RcZ9a3GVJNLHjw6warEZ49UfLIeT9p8Id69agXjw+ZKkK2ahrqyh9RNk4IHz5Gd+kXTtVZ0UXSfdyzjIOXPKjh3R1pAr5epUx7QsMbPm2zx4XRvLfQ4f7y2kRxv/t3CjiCdj5ZM0ZsoNdHSzQgtQSIiqkkRXmi6gvEgWD6fO0TbZ4A/g9fUt1WNl79wSHNi8C+6JKXa3q7q2/Xrw8nPjlQM6SQsNB6B4EknAf0aKqXaDkOAhQ35HQZ8stl7rxsI=~4599857~3360052',
    'GlobalE_Ref': 'https^%^3A//www.google.com/',
    'RES_SESSIONID': '829084670274967',
    'ak_bmsc': 'F718A96BBAEFA36A1C8DA1905C3B4AF4~000000000000000000000000000000~YAAQHgF8aDqvWP56AQAA6hJPAAyUdqab3uuZG7+KsuINwd1hE0VgSIauhhskZQUZtJCE/UeTu3hd4BSJTAT3jC7EhEVAWkZCX0jtIeLsvIZBFPXEXGO6dfNJj0E9ToH2EUA4nVXYZzqp5+VQhON9BllB4G0ZMDiY6PivDfvKqHQJ0dmtvaTCWcI8WIQypN82teYCSO0EEfXNUBmf2CdPI3cm3S9mMZl0Hfzv3O8Z8Rn8rWPZQHM8FjMMcO2s34r2lD2eDEq4ISTXkwbyGw+xj1mip28m1LcE95nCPnDhT1hnQVB0UYHkBY2PjRkY32WzVpEXCiXtn/y41INXThFz1HsQkc6ItW9ve2dtBpoHXLl2qoHoT/jLg9Eq4AlgjDc/57H/bmuxLFp3XXx5OZt4I2S1/D9elXmXe2Dsu/GEhVuBW1QOOSG5pfD4j6hVSvmgYBjocioit3vgvLxhj7ffchcqY7YhYiHoVqFLZ46llMppYf/HzLyGhlVl1OY=',
    'userId': 'acaqnGKkkyVQ6a4uhRhVxzUrLz',
    '_bamls_seid': '9aba0279-a7dd-47ca-bc96-3ae4bc195f4f',
    '__idcontext': 'eyJjb29raWVJRCI6IkxZWU1GRUVRWlBDSkxJTlpNM0ZBQUc0R0hVMjdUREZMUEo3NktVNk5aREJBPT09PSIsImRldmljZUlEIjoiTFlZTUZFRVFaRFhNTFBWSEdIVVg0V1BJS01SN1ZQVjVIRVE0WVNXTTM3RFE9PT09IiwiaXYiOiJTSk1FUlpSTDNZSUxXQ1dUVElCSFBWRjZVST09PT09PSIsInYiOjF9',
    'bounceClientVisit1828v': 'N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0ArgHYCWAjmAPZkDGjAtkRegQKZVE4HXkRAAaEACcYIUsTIBzRowVherDuJApeCmAG0AugF8gA',
    'BVBRANDSID': '7822ccd8-7b71-496e-8a3d-2eb7ab5a4d92',
    '__cq_bc': '^%^7B^%^22bbbx-UniqloUS^%^22^%^3A^%^5B^%^7B^%^22id^%^22^%^3A^%^22423560^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22433109^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22442963^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22441013^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22434976^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22427916^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22436881^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22432164^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22427211^%^22^%^7D^%^2C^%^7B^%^22id^%^22^%^3A^%^22439659^%^22^%^7D^%^5D^%^7D',
    '_ga_T7HS3TVJBM': 'GS1.1.1627797787.4.1.1627799326.0',
    '_ga': 'GA1.2.999120280.1627272393',
    'stc111579': 'env:1627797788^%^7C20210901060308^%^7C20210801065848^%^7C8^%^7C1013844:20220801062848^|uid:1627272395707.100854231.37676048.111579.569139022.:20220801062848^|srchist:1013844^%^3A1627797788^%^3A20210901060308:20220801062848^|nsc:2:20220731195112^|tsa:0:20210801065848',
    'cto_bundle': 'x_kDMV9abHBZUnJYYUdmNE1oMzBsczNZenVjSDdYSVhDT3pBd1I0QlBGOWl2MWJQODk2V1pmdXZXTE9KWXBzJTJCdW14MTlSR1Z6SFYzSzYzT1B2S0pzWUlpNEVOZHM2VGF2eFBnalNnZEVyeUFtTjA2JTJCRXNKOTVBQTYxZElkajBFOGVFT1pTOTRNJTJCY2llaVA5NnNVU3M4c21QM2clM0QlM0Q',
    '__cq_seg': '0~-0.47^!1~-0.06^!2~-0.08^!3~0.27^!4~0.38^!5~-0.06^!6~-0.43^!7~0.03^!8~-0.29^!9~-0.53^!f0~15~9',
    '_uetsid': '709ea5c0f23211ebad94817212da16a4',
    '_uetvid': 'dd3f3ea0edc611ebac0cb1b23862ff17',
    '__attentive_pv': '63',
    '_derived_epik': 'dj0yJnU9ZzJpX0xFRnZxcWpnTl9LN2RlaFRjUjd6TDFpYTh4RlUmbj02ZEZleWF3aVRmaDFOZGhadzZtX2l3Jm09MSZ0PUFBQUFBR0VHUHlJJnJtPTEmcnQ9QUFBQUFHRUdQeUk',
}

headers = {
    'authority': 'www.uniqlo.com',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.uniqlo.com/us/en/men-dry-stretch-easy-shorts-423560.html?dwvar_423560_color=COL17&cgid=men-shorts',
    'accept-language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,zu;q=0.6',
}

params = (
    ('remoteIncludeUrl', 'Product-GetAvailability'),
    ('pid', '423560COL68SMA005000'),
    ('Quantity', '1'),
    ('ajax', 'true'),
)

response = requests.get('https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Globale-Cache', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Globale-Cache?remoteIncludeUrl=Product-GetAvailability&pid=423560COL68SMA005000&Quantity=1&ajax=true', headers=headers, cookies=cookies)


dct = json.loads(response.text)

print(dct['status'])
