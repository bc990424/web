import requests
def result(date):
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    para = {
        "KEY": "05789270567a48d48024fc06439a91b1",
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": "J10",
        "SD_SCHUL_CODE": "7530137",
        "MLSV_YMD": date[:6]
    }
    res = requests.get(url, params=para)
    meal_data = res.json()
    meell = list(meal_data['mealServiceDietInfo'][1].values())[0]
    for i in meell:
        if i['MLSV_YMD'] == date:
            return i["DDISH_NM"].split("<br/>")