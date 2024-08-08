import requests


# Configurar la sesión de requests para utilizar el proxy de Tor
session = requests.session()
session.proxies = {
    "http": "socks5h://localhost:9050",
    "https": "socks5h://localhost:9050",
}

# Ajustes iniciales
DATA_URL = "https://www.tripadvisor.es/data/graphql/ids"
offset = 0

PAYLOAD = [
    {
        "variables": {
            "locationId": 190146,
            "albumId": -160,
            "subAlbumId": -160,
            "client": "ar",
            "dataStrategy": "ar",
            "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
            "offset": 40,
            "limit": 20,
        },
        "extensions": {"preRegisteredQueryId": "2d46abde60a014b0"},
    }
]
# # Ejemplo de User-Agent de Safari (opcional)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
# }

response = session.post(DATA_URL, json=PAYLOAD).json()

print(response)


"""
Summary
URL: https://www.tripadvisor.es/data/graphql/ids
Status: 200
Source: Network
Address: 2.21.181.142:443 (Proxy)
Initiator: 
sra6t7e8e23z-c.es-ES.js:583:22485

Request
:method: POST
:scheme: https
:authority: www.tripadvisor.es
:path: /data/graphql/ids
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9
Connection: keep-alive
Content-Length: 235
Content-Type: application/json
Cookie: _lr_env_src_ats=false; _lr_retry_request=true; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%2221598546-f196-f8d7-4ba6-fd08e61ba282%22%2C%22e%22%3A1710722267420%2C%22c%22%3A1710722248722%2C%22l%22%3A1710722252420%7D; __eoi=ID=fb74afb42d724efb:T=1710709318:RT=1710722250:S=AA-AfjbhhonhJyw3wJnEaeAl3kuo; __gads=ID=14d5568f8d1414e7:T=1710709318:RT=1710722250:S=ALNI_Mb7oiUtEQImm9v2WZvP32hWEX5wlw; __gpi=UID=00000d48b1997a7a:T=1710709318:RT=1710722250:S=ALNI_MZ_RdzvZjObU1M_pDUJp-iU-4roZQ; TASession=V2ID.04737163528A770724F838E456B2E241*SQ.10*LS.Attraction_Review*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*EAU._; _ga=GA1.1.440145626.1710709315; _ga_QX0Q50ZC9P=GS1.1.1710722248.3.0.1710722248.60.0.0; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%224ab03e5b-2552-04c9-a224-73037a54f15d%22%2C%22c%22%3A1710709314688%2C%22l%22%3A1710722248723%7D; TASID=04737163528A770724F838E456B2E241; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+18+2024+01%3A37%3A27+GMT%2B0100+(Central+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=68615be7-8cfb-4f66-820d-0a900e512d4d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1%2CV2STACK42%3A1&geolocation=ES%3BMD&AwaitingReconsent=false; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; __vt=lGHSG8EXLKhpI2_zABQCwRB1grfcRZKTnW7buAoPsSwmksfHZS0sgqmM48dDk-K6LcUUHFBuxuU3YBeHuS1U8KoDu1vYk02ucdQAx8CrJIqBii5hF_HTdw4-hcGcCVIdiqn9sFFYWhc6Y9fYFUw-MhJYgr8; TAUD=LA-1710709320006-1*HDD-1-2024_03_31.2024_04_01*RDD-2-2024_03_17*LD-8267130-2024.3.31.2024.4.1*LG-8267132-2.1.F.; PAC=AGif5Km_D57T-6PypxF7vm2uu7SZwExC9OGeVf7uiRjp2-uKWC-lP4ANmSoQQRraDgR5otIm7KI7r1qLZAUlgBSBVkUODIWLxuFKze2FswkFzxzHYaqed9A_AXngwaB_mQ%3D%3D; pbjs_unifiedID=%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-03-17T21%3A02%3A08%22%7D; pbjs_unifiedID_cst=uCy6LMAsIA%3D%3D; _lr_sampling_rate=100; WLRedir=requested; ServerPool=A; TATravelInfo=V2*AY.2024*AM.3*AD.31*DY.2024*DM.4*DD.1*A.2*MG.-1*HP.2*FL.3*DSM.1710709320220*RS.1; PMC=V2*MS.79*MD.20240202*LD.20240317; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.320.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.486.491.494.495.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1423.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1659.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.1985.1987.2003.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2213.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3100.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3296.3299.3300.3306.3307.3309.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5231.6931.7031.7235.7831.7931.8931.9731.10231.10631.10831.11031.11531.12831.13632.13731.14237.15731.16831.21233.23031.24431; OptanonAlertBoxClosed=2024-03-17T21:01:54.267Z; eupubconsent-v2=CP7nWxgP7nWxgAcABBENAsEsAP_gAEPgACiQg1QrYAAgAEAAQAA0ACAAQgAqADIAHIAPABDACQAJYATgBQACqAFgAWgAvgBiAGUANAA1ABzADsAPgAhQBEAEYAJIATAAnABQACrAFoAW4AugC_AGEAYoAyADKAGiANgA2gBvgDkAOcAdwB4gD-AQsAiACLgEcAR4Ak4BKgEtAJkAmwBOgChAFIAKgAVoAsoBcAFyAL6AYABggDDAGOAM6AaQBqwDXANgAcEA4gDkgHiAecA-AD5gH2AfsA_wEAgIMAg4BEYCMAI1ARwBHQCRQElASaAloCXAEwAJwATqAngCfgFFgKQApIBTQCswFeAV8AswBcAC5gF2ALyAX0AwMBgwGEAMUAZIAzUBnAGdANAAaKA0wDUAG0ANsAbgA34BwgDtgHfAPNAeoB6wD3gHyAPqAfuA_4EAQIEAgUBBICDAEIQISAhOBC4EMAIbARFAiUCJoEUgRUAiwBF4CMQEagI4AR2Aj0BIgCSwEngJUAStAlkCWgEvAJigTKBM0CaQJqATZAnECcgE6QJ2AncBP8ChgKIgUYBRsCkAKRAUnApYClwFRAKkgVSBVQCrIFXAVeArIBXcCvgK_gWGBYsCyALJAWYAs8BaIC1YFrgWxAt0C3oFwgXFAuUC5oF0AXVAuwC7oF5AXnAvYC94F-gX9AwADAwGMgRXgmyCb0E4ATignMCdUE7ATxAnmBPYINQg1QYwAEQAKAAuABwAHgAVAAuABwADwAIAASAAvgBiAGUANAA1AB4AD8AIgATAAoABTACrAFwAXQAxABoADeAH4AQkAiACJAEcAJYATQAwABhgDLAGaANkAcgA-IB9gH7AP8BAACDgERgIsAjABGoCOAI6ASIAkoBPwCoAFzALyAX0AxQBnwDRAGvANoAbgA6QB2wD7AH_AQgAiYBF4CPQEiAJWATFAmQCZQEzgJ2AUPApACkQFJgKkAVYArIBXcCxALFAWjAtgC2QFugLkAXQAu0Bd8C8gLzAX0AwQBtkE2wTcgm8Cb4E4YJygnMBOkCdcE7QTuAngBPMINQBQIASADoALgA2QCIAGEAToAuQBtgEDggAYAHQArgCIAGEAToBA4MAHAB0AFwAbIBEADCALkAgcIADgA6AGyARAAwgCdAFyAQOFAAwAuAGEAgcMABAGEAgcOADAA6AIgAYQBOgEDgIrkAAQBhAIHEgAYBEADCAQOKABQAdAEQAMIAnQCBw.f_wACHwAAAAA; pbjs_sharedId=e16d809d-05ba-4733-8ff7-7116bd5f6b89; pbjs_sharedId_cst=uCy6LMAsIA%3D%3D; TART=%1%enc%3A4KXXqwiZkNYCUpQpax6HBufdy1l8wYU%2FIPF6LA9jgVXZo1ZUgaqwbE3sCBI2bKgICeyaC1LeImE%3D; TADCID=VIhvBLiAf-nnu3YPABQCmq6heh9ZSU2yA8SXn9Wv5HxIGmDJo0S77TPuIcbI0e5dYDg0M2Hbcf1idy08P23xaXbA-Z48H5KKhDE; TASameSite=1; VRMCID=%1%V1*id.10568*llp.%2FRestaurants-g187514-zfn13207892-Madrid%5C.html*e.1707535101766; datadome=T_TRpQhd4jIGZDioWvuIxo3hM4kkudwg7buxx1IJ_gKpxxdTArS2OcAuG964Ff5EXqBoXPL_mgM5LX8Z353iKJlgFaYVZzBTtdH0c75v_1E59NJCkIGqga8LywJDXUHn; TASSK=enc%3AAFiD%2FP3VUOGdHc%2Fbhd%2FUtLuJCLieca9FpsKF%2FoGtTHABzn0cCSx7ei4uvjAVJHYVyioF%2Bah3orw6oKuDfXd4cfFciIsozdwlCAqMRtS8GlUe10xj5YOtXdz389IvHBKj9w%3D%3D; TAUnique=%1%enc%3Al0KAiBSqMDTgpderCJmQ1gKugNLWYn50iXIbCFaDYkg2jHwltRJPGQ%3D%3D
Host: www.tripadvisor.es
Origin: https://www.tripadvisor.es
Referer: https://www.tripadvisor.es/Attraction_Review-g187514-d190146-Reviews-Royal_Palace_of_Madrid-Madrid.html
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15

Response
:status: 200
Cache-Control: no-store,must-revalidate
Content-Encoding: br
Content-Length: 4481
Content-Type: application/json;charset=utf-8
Date: Mon, 18 Mar 2024 00:38:09 GMT
Server: envoy
Vary: Accept-Encoding
x-request-id: 705469d0-586b-4a56-affb-18ec5aa303bd


"""