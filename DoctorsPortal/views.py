from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from pprint import pprint
from django.shortcuts import redirect
from .models import TblUser,TblPatientDetails
from django.db.models import Q

import json
def home(request):
    return render(request,'DoctorsPortal/signin.html')

def patientRegistration(request):
    if not request.session['intLoginUserId']:
        return render(request,'DoctorsPortal/signin.html')
    else:
        return render(request,'DoctorsPortal/patientRegistration.html')
def signin(request):
    return render(request,'DoctorsPortal/signin.html')

def signUp(request):
    return render(request,'DoctorsPortal/signup.html')

def checkSignin(request):
    """
    func to check uname and password are valid
    """
    if request.method == 'POST':
        dctResponse = {}
        dctResponse = {'strStatus':'SUCCESS'}
        jsnLoginCredentials = request.POST['jsnLoginCredentials']
        dctLoginCredentials = json.loads(jsnLoginCredentials)
        strUname = ''
        intLoginUserId = ''
        strLoginEmail = dctLoginCredentials['strEmail']
        strLoginPassword = dctLoginCredentials['strPassword']

        boolUserExist = TblUser.objects.filter(Q(email__iexact=strLoginEmail)).exists()
        try:
            if boolUserExist == True:
                #checking Password
                tbmUserData = TblUser.objects.filter(Q(email=strLoginEmail),Q(password = strLoginPassword))
                try:
                    if tbmUserData[0]:
                        strUname = tbmUserData[0].name
                        intLoginUserId = tbmUserData[0].userId
                        pass
                except Exception as err:
                    print(err)
                    dctResponse['strStatus'] = 'ERROR'
                    dctResponse['strMessage'] = 'Password Doesnot match'
                    return JsonResponse(dctResponse)
                pass
            else:
                dctResponse['strStatus'] = 'ERROR'
                dctResponse['strMessage'] = 'User Doesnot Exist.Please Sign Up.'
                return JsonResponse(dctResponse)
        except:
            dctResponse['strStatus'] = 'ERROR'
            dctResponse['strMessage'] = 'User Doesnot Exist.Please Sign Up.'
            return JsonResponse(dctResponse)
        
        request.session["strLoginUsername"] = strUname
        request.session["intLoginUserId"] = intLoginUserId
        return JsonResponse(dctResponse)
#addNewUserRegistration

def addNewUserRegistration(request):
    """
    func to add new User
    """
    if request.method == 'POST':
        dctResponse = {}
        dctResponse = {'strStatus':'SUCCESS'}
        jsnNewRegistrationData = request.POST['jsnNewRegistrationData']
        dctNewRegistrationData = json.loads(jsnNewRegistrationData)
        
        #Add new Data
        try:
            tbmNewUserData = TblUser()
            tbmNewUserData.name = dctNewRegistrationData['strUsername']
            tbmNewUserData.age = int(dctNewRegistrationData['intAge'])
            tbmNewUserData.email = dctNewRegistrationData['strEmail']
            tbmNewUserData.mobile = dctNewRegistrationData['strMobile']
            tbmNewUserData.password = dctNewRegistrationData['strPassword']
            tbmNewUserData.dattimeCreated = datetime.now()
            tbmNewUserData.intLastAction = int(1)
            tbmNewUserData.save()

            request.session['strLoginUsername'] = dctNewRegistrationData['strUsername']
            request.session['intLoginUserId'] = tbmNewUserData.userId
        except Exception as err:
            dctResponse['strStatus'] = 'ERROR'
            dctResponse['strMessage'] = 'Issue While Saving data'
        return JsonResponse(dctResponse)

def addNewPatientRegistration(request):
    """
    func to add new Patient
    """
    if request.method == 'POST':
        dctResponse = {}
        dctResponse = {'strStatus':'SUCCESS'}
        jsnNewPatientRegistrationData = request.POST['jsnNewPatientRegistrationData']
        dctNewRegistrationData = json.loads(jsnNewPatientRegistrationData)
              

        #Add new Data
        try:
            tbmNewUserData = TblPatientDetails()
            tbmNewUserData.name = dctNewRegistrationData['strPatientname']
            tbmNewUserData.age = int(dctNewRegistrationData['intPatientAge'])
            tbmNewUserData.mobile = dctNewRegistrationData['strPatientMobile']
            tbmNewUserData.place = dctNewRegistrationData['strPlace']
            tbmNewUserData.intCreatedUserId = request.session['intLoginUserId']
            tbmNewUserData.dattimeCreated = datetime.now()
            tbmNewUserData.intLastAction = int(1)
            tbmNewUserData.save()

            #Get Saved Data
            tbmAllPatientsData = TblPatientDetails.objects.filter(~Q(intLastAction = 0))
            dctResponse = getPatientDetailsData(tbmAllPatientsData)
        except Exception as err:
            print(err)
            dctResponse['strStatus'] = 'ERROR'
            dctResponse['strMessage'] = 'Issue While Saving data'
            
        return JsonResponse(dctResponse)

def getAllPatientDetailsData(request):
    """
    Function To get Patient Details Data
    """
    if request.method == 'POST':
        dctResponse = {}
        lstDetailsData = []
        dctDetailsData = {}
        dctResponse = {'strStatus':''}
        tbmAllPatientsData = TblPatientDetails.objects.filter(~Q(intLastAction = 0))
        try:
            if tbmAllPatientsData[0]:
                dctGetResponse = getPatientDetailsData(tbmAllPatientsData)
                dctResponse['strStatus'] = dctGetResponse['strStatus']
                lstDetailsData = dctGetResponse['lstDetailsData']

        except:
            dctResponse['strStatus'] = 'ERROR'
            dctResponse['strMessage'] = 'Issue While getting data'
            return JsonResponse(dctResponse)

        dctResponse = {'strStatus' : 'SUCCESS','lstDetailsData':lstDetailsData}
        return JsonResponse(dctResponse)

def getPatientDetailsData(tbmAllPatientsData):
    lstDetailsData = []
    dctDetailsData = {}
    dctResponse = {'strStatus' : ''}
    try:
        for eachTbm in tbmAllPatientsData:
                    dctDetailsData = {}
                    dctDetailsData['strPatientName'] = eachTbm.name
                    dctDetailsData['intPatientAge'] = eachTbm.age
                    dctDetailsData['intPatientMobile'] = eachTbm.mobile
                    dctDetailsData['intPatientPlace'] = eachTbm.place
                    lstDetailsData.append(dctDetailsData)
        pass
    except:
        dctResponse['strStatus'] = 'ERROR'
        dctResponse['strMessage'] = 'Issue While getting data'
        pass
    dctResponse['strStatus'] = 'SUCCESS'
    dctResponse['lstDetailsData'] = lstDetailsData

    return dctResponse

def logout(request):
    """
    function to logout
    """
    if request.method == 'POST':
        dctResponse = {}
        dctResponse = {'strStatus':'SUCCESS'}
        request.session['strLoginUsername'] = ''
        request.session['intLoginUserId'] = ''
        return JsonResponse(dctResponse)
    








