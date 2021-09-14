from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):
    
    counter=0
    url = "https://bitspanindia.com/getcretid.php"
    response = requests.request("GET", url)
    res=json.loads(response.text)
    # print(res)
      #{"rid":"SK121757","noc":"3","is_e_cup":"0","slno":"708482",'ses': '8A95BD484094C57E9B1DA16EEF1A279B'}
    url = "https://www.psaonline.utiitsl.com/psaonline/ScaCoupdisToMultipleBranch"
    if res["rid"] !="NOTH":
        payload={
        'vleName': 'MD RAA',
        'entityID': 'AOI',
        'coupCount': '100000'}
        payload["vleId"]=res["rid"]
        if res["is_e_cup"]=="0":
            payload["noOfCoupons"]=res["noc"]
            payload["noOfeCoupons"]=0
        else:
            payload["noOfCoupons"]=0
            payload["noOfeCoupons"]=res["noc"]  
        headers = {
          'cookie': 'JSESSIONID='+res["ses"]
        }   
        response = requests.request("POST", url, headers=headers, data=payload,verify=False)    
        if (response.text.find('Session Invalid') != -1):
            print ("=============>Session Exparied ",res["rid"],res["slno"])
            counter=-1
        else:
            print ("==================>Sent",res["rid"],res["slno"])
            url5 = "https://bitspanindia.com/submitapproval.php"
            payload5={'acs': 'JBJHDY8958asd'}
            payload5["slno"]=res["slno"]
            response = requests.request("POST", url5, data=payload5)
            if(response.text=="1"):
                # print("Updated")
                counter=10
            else:
                counter=11
    else:
         counter=3
    if counter==10:
        return HttpResponse(
            '''
            Coupon send to '''+res["rid"]+''' ========> '''+res["noc"]+'''.
            window.setTimeout(function () {
                location.reload();
            }, 2000);
            
            '''
        )
    if counter==-1:
        return HttpResponse("Session Exparied.")