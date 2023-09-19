from typing import Type
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import requests
from datetime import datetime

def home(request):
    rover = "Perseverance"
    sol = "1"
    landdate = "2021-02-18"
    
    CurrentEarthDate = datetime.now()
    launchdate = "2020-07-30" 
    LandDate = datetime(int(landdate[:4]),int(landdate[5:7]), int(landdate[8:10]), 0, 0, 0, 0)
    CurrentSol = str((CurrentEarthDate-LandDate)*0.9732442967141608)[:str((CurrentEarthDate-LandDate)*0.9732442967141608).find(" days")] 
    camera = "Camera"
    earthdate = "2021-02-19"
    requestlink = "https://api.nasa.gov/mars-photos/api/v1/rovers/"+rover+"/photos?sol="+sol+"&api_key=p9gmwsLowAl5YIQmJO6q9Tx5mM8Z20awbJ6Bl6FW"
    RoverAPIRequest = requests.get(requestlink)
    RoverAPIData = RoverAPIRequest.json()
    ImageSourceLink1 = RoverAPIData["photos"][0]["img_src"] 
    ImageSourceLink2 = RoverAPIData["photos"][1]["img_src"] 
    ImageSourceLink3 = RoverAPIData["photos"][2]["img_src"] 
    ImageSourceLink4 = RoverAPIData["photos"][3]["img_src"] 
    ImageSourceLink5 = RoverAPIData["photos"][4]["img_src"] 
    ImageSourceLink6 = RoverAPIData["photos"][5]["img_src"]
    ImageSourceLink7 = RoverAPIData["photos"][6]["img_src"]
    ImageSourceLink8 = RoverAPIData["photos"][7]["img_src"]
    ImageSourceLink9 = RoverAPIData["photos"][8]["img_src"]
    ImageSourceLink10 = RoverAPIData["photos"][9]["img_src"]
    ImageSourceLink11 = RoverAPIData["photos"][10]["img_src"]
    ImageSourceLink12 = RoverAPIData["photos"][11]["img_src"]
    ImageSourceLink13 = RoverAPIData["photos"][12]["img_src"]
    ImageSourceLink14 = RoverAPIData["photos"][13]["img_src"]
    ImageSourceLink15 = RoverAPIData["photos"][14]["img_src"]
    ImageSourceLink16 = RoverAPIData["photos"][15]["img_src"]
    ImageSourceLink17 = RoverAPIData["photos"][16]["img_src"]
    ImageSourceLink18 = RoverAPIData["photos"][17]["img_src"]
    ImageSourceLink19 = RoverAPIData["photos"][18]["img_src"]
    ImageSourceLink20 = RoverAPIData["photos"][19]["img_src"]
    if "sol" in request.GET and "rover" in request.GET:
        sol = request.GET['sol']
        rover = request.GET['rover']
        if rover == "Perseverance":
            landdate = "2021-02-18" 
        elif rover == "Curiosity":
            landdate = "2011-11-26" 
    requestlink = "https://api.nasa.gov/mars-photos/api/v1/rovers/"+rover+"/photos?sol="+sol+"&api_key=p9gmwsLowAl5YIQmJO6q9Tx5mM8Z20awbJ6Bl6FW"
    RoverAPIRequest = requests.get(requestlink)
    RoverAPIData = RoverAPIRequest.json()
    try:
        sol = RoverAPIData["photos"][0]["sol"]
        try:
            ImageSourceLink1 = RoverAPIData["photos"][0]["img_src"] 
            ImageSourceLink2 = RoverAPIData["photos"][1]["img_src"] 
            ImageSourceLink3 = RoverAPIData["photos"][2]["img_src"] 
            ImageSourceLink4 = RoverAPIData["photos"][3]["img_src"] 
            ImageSourceLink5 = RoverAPIData["photos"][4]["img_src"]
            ImageSourceLink6 = RoverAPIData["photos"][5]["img_src"]
            ImageSourceLink7 = RoverAPIData["photos"][6]["img_src"]
            ImageSourceLink8 = RoverAPIData["photos"][7]["img_src"]
            ImageSourceLink9 = RoverAPIData["photos"][8]["img_src"]
            ImageSourceLink10 = RoverAPIData["photos"][9]["img_src"]
            ImageSourceLink11 = RoverAPIData["photos"][10]["img_src"]
            ImageSourceLink12 = RoverAPIData["photos"][11]["img_src"]
            ImageSourceLink13 = RoverAPIData["photos"][12]["img_src"]
            ImageSourceLink14 = RoverAPIData["photos"][13]["img_src"]
            ImageSourceLink15 = RoverAPIData["photos"][14]["img_src"]
            ImageSourceLink16 = RoverAPIData["photos"][15]["img_src"]
            ImageSourceLink17 = RoverAPIData["photos"][16]["img_src"]
            ImageSourceLink18 = RoverAPIData["photos"][17]["img_src"]
            ImageSourceLink19 = RoverAPIData["photos"][18]["img_src"]
            ImageSourceLink20 = RoverAPIData["photos"][19]["img_src"]
        except:
            ImageSourceLink1 = RoverAPIData["photos"][0]["img_src"] 
            ImageSourceLink2 = RoverAPIData["photos"][1]["img_src"] 
            ImageSourceLink3 = RoverAPIData["photos"][2]["img_src"] 
            ImageSourceLink4 = RoverAPIData["photos"][3]["img_src"] 
            ImageSourceLink5 = RoverAPIData["photos"][4]["img_src"] 
            ImageSourceLink6 = RoverAPIData["photos"][5]["img_src"]
            ImageSourceLink7 = RoverAPIData["photos"][6]["img_src"]
            ImageSourceLink8 = RoverAPIData["photos"][7]["img_src"]
            ImageSourceLink9 = RoverAPIData["photos"][8]["img_src"]
            ImageSourceLink10 = RoverAPIData["photos"][9]["img_src"]
            ImageSourceLink11 = RoverAPIData["photos"][0]["img_src"]
            ImageSourceLink12 = RoverAPIData["photos"][1]["img_src"]
            ImageSourceLink13 = RoverAPIData["photos"][2]["img_src"]
            ImageSourceLink14 = RoverAPIData["photos"][3]["img_src"]
            ImageSourceLink15 = RoverAPIData["photos"][4]["img_src"]
            ImageSourceLink16 = RoverAPIData["photos"][5]["img_src"]
            ImageSourceLink17 = RoverAPIData["photos"][6]["img_src"]
            ImageSourceLink18 = RoverAPIData["photos"][7]["img_src"]
            ImageSourceLink19 = RoverAPIData["photos"][8]["img_src"]
            ImageSourceLink20 = RoverAPIData["photos"][9]["img_src"]
        landdate = RoverAPIData["photos"][0]["rover"]["landing_date"]
        launchdate = RoverAPIData["photos"][0]["rover"]["launch_date"]
        camera = RoverAPIData["photos"][0]["camera"]["full_name"]
        earthdate = RoverAPIData["photos"][0]["earth_date"]
        LandDate = datetime(int(landdate[:4]),int(landdate[5:7]), int(landdate[8:10]), 0, 0, 0, 0)
        CurrentSol = str((CurrentEarthDate-LandDate)*0.9732442967141608)[:str((CurrentEarthDate-LandDate)*0.9732442967141608).find(" days")]
        return render(request,"home.html", {'imagesrc1':ImageSourceLink1, 'imagesrc2':ImageSourceLink2, 'imagesrc3':ImageSourceLink3, 'imagesrc4':ImageSourceLink4, 'imagesrc5':ImageSourceLink5, 'imagesrc6':ImageSourceLink6,'imagesrc7':ImageSourceLink7,'imagesrc8':ImageSourceLink8,'imagesrc9':ImageSourceLink9,'imagesrc10':ImageSourceLink10,'imagesrc11':ImageSourceLink11,'imagesrc12':ImageSourceLink12,'imagesrc13':ImageSourceLink13,'imagesrc14':ImageSourceLink14,'imagesrc15':ImageSourceLink15,'imagesrc16':ImageSourceLink16,'imagesrc17':ImageSourceLink17,'imagesrc18':ImageSourceLink18,'imagesrc19':ImageSourceLink19,'imagesrc20':ImageSourceLink20, 'sols':sol, 'rover': rover, 'landdate': landdate, 'launchdate': launchdate, 'camera': camera, 'earthdate':earthdate, 'currentsol':CurrentSol})
    except Exception:
        error = "Data for "+rover+" on Sol "+ sol+" not available. Please choose another Sol."
        return render(request,"home.html", {'imagesrc1':ImageSourceLink1, 'imagesrc2':ImageSourceLink2, 'imagesrc3':ImageSourceLink3, 'imagesrc4':ImageSourceLink4, 'imagesrc5':ImageSourceLink5,'imagesrc6':ImageSourceLink6,'imagesrc7':ImageSourceLink7,'imagesrc8':ImageSourceLink8,'imagesrc9':ImageSourceLink9,'imagesrc10':ImageSourceLink10,'imagesrc11':ImageSourceLink11,'imagesrc12':ImageSourceLink12,'imagesrc13':ImageSourceLink13,'imagesrc14':ImageSourceLink14,'imagesrc15':ImageSourceLink15,'imagesrc16':ImageSourceLink16,'imagesrc17':ImageSourceLink17,'imagesrc18':ImageSourceLink18,'imagesrc19':ImageSourceLink19,'imagesrc20':ImageSourceLink20, 'sols':"1", 'rover': "Perseverance", 'landdate': landdate, 'launchdate': launchdate, 'camera': camera, 'earthdate':earthdate, 'currentsol':CurrentSol, 'error':error})