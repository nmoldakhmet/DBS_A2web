from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from dbsweb.models import diseaseTypeModel
from dbsweb.models import countryModel
from dbsweb.models import diseaseModel
from dbsweb.models import discoverModel
from dbsweb.models import usersModel
from dbsweb.models import publicservantModel
from dbsweb.models import doctorModel
from dbsweb.models import specializeModel
from dbsweb.models import recordModel

from dbsweb.forms import diseaseTypeForms
from dbsweb.forms import countryForms
from dbsweb.forms import diseaseForms
from dbsweb.forms import discoverForms
from dbsweb.forms import usersForms
from dbsweb.forms import publicservantForms
from dbsweb.forms import doctorForms
from dbsweb.forms import specializeForms
from dbsweb.forms import recordForms



def showmain(request) :
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'index2.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def insertionTable1(request) :
    if request.method == "POST" :
        if request.POST.get('id') and request.POST.get('description') :
            saverecord = diseaseTypeModel()
            saverecord.id = request.POST.get('id') 
            saverecord.description = request.POST.get('description')
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable1.html')
    else :
            return render(request, 'insertTable1.html')

def insertionTable2(request) :
    if request.method == "POST" :
        if request.POST.get('cname') and request.POST.get('population') :
            saverecord = countryModel()
            saverecord.cname = request.POST.get('cname') 
            saverecord.population = request.POST.get('population')
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable2.html')
    else :
            return render(request, 'insertTable2.html')

def insertionTable3(request) :
    if request.method == "POST" :
        if request.POST.get('diseasecode') and request.POST.get('pathogen') and request.POST.get('description') and request.POST.get('id') :
            saverecord = diseaseModel()
            saverecord.diseasecode = request.POST.get('diseasecode') 
            saverecord.pathogen = request.POST.get('pathogen')
            saverecord.description  = request.POST.get('description') 
            var = diseaseTypeModel()
            var.id = request.POST.get('id')
            saverecord.id = var
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable3.html')
    else :
            return render(request, 'insertTable3.html')

def insertionTable4(request) :
    if request.method == "POST" :
        if request.POST.get('firstencdate') and request.POST.get('diseasecode') and request.POST.get('cname') and request.POST.get('id') :
            saverecord = discoverModel()
            saverecord.firstencdate = request.POST.get('firstencdate') 
            var = diseaseModel()
            var.diseasecode = request.POST.get('diseasecode')
            saverecord.diseasecode = var
            var2 = countryModel()
            var2.cname = request.POST.get('cname') 
            saverecord.cname = var2
            saverecord.id = request.POST.get('id') 
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable4.html')
    else :
            return render(request, 'insertTable4.html')

def insertionTable5(request) :
    if request.method == "POST" :
        if request.POST.get('email') and request.POST.get('name') and request.POST.get('surname') and request.POST.get('salary') and request.POST.get('phone') and request.POST.get('cname') :
            saverecord = usersModel()
            saverecord.email  = request.POST.get('email') 
            saverecord.name  = request.POST.get('name')
            saverecord.surname   = request.POST.get('surname') 
            saverecord.salary   = request.POST.get('salary') 
            saverecord.phone  = request.POST.get('phone')
            var2 = countryModel()
            var2.cname = request.POST.get('cname') 
            saverecord.cname = var2
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable5.html')
    else :
            return render(request, 'insertTable5.html')

def insertionTable6(request) :
    if request.method == "POST" :
        if request.POST.get('email') and request.POST.get('department') and request.POST.get('id') :
            saverecord = publicservantModel()
            var = usersModel()
            var.email = request.POST.get('email') 
            saverecord.email = var
            saverecord.department  = request.POST.get('department')
            saverecord.id  = request.POST.get('id')
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable6.html')
    else :
            return render(request, 'insertTable6.html')

def insertionTable7(request) :
    if request.method == "POST" :
        if request.POST.get('email') and request.POST.get('degree') :
            saverecord = doctorModel()
            var = usersModel()
            var.email = request.POST.get('email') 
            saverecord.email = var
            saverecord.degree  = request.POST.get('degree')
            saverecord.id  = request.POST.get('id')
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable7.html')
    else :
            return render(request, 'insertTable7.html')

def insertionTable8(request) :
    if request.method == "POST" :
        if request.POST.get('email') and request.POST.get('specid') and request.POST.get('id') :
            saverecord = specializeModel()
            var3 = usersModel()
            var3.email = request.POST.get('email')
            var2 = doctorModel()
            var2.email = var3 
            saverecord.email = var3
            var = diseaseTypeModel()
            var.id = request.POST.get('id')
            saverecord.specid = var
            saverecord.id = request.POST.get('id')
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable8.html')
    else :
            return render(request, 'insertTable8.html')

def insertionTable9(request) :
    if request.method == "POST" :
        if request.POST.get('email') and request.POST.get('cname') and request.POST.get('diseasecode') and request.POST.get('totaldeaths') and request.POST.get('totalpatients') :
            saverecord = recordModel()
            var = usersModel()
            var.email = request.POST.get('email') 
            saverecord.email = var
            var2 = countryModel()
            var2.cname = request.POST.get('cname') 
            saverecord.cname = var2
            var3 = diseaseModel()
            var3.diseasecode = request.POST.get('diseasecode') 
            saverecord.diseasecode  = var3
            saverecord.totaldeaths  = request.POST.get('totaldeaths')
            saverecord.totalpatients  = request.POST.get('totalpatients') 
            saverecord.id  = request.POST.get('id') 
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'insertTable9.html')
    else :
            return render(request, 'insertTable9.html')


def deleteRecordTable1(request, id) :
    deleterecord=diseaseTypeModel.objects.get(id = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable2(request, id) :
    deleterecord=countryModel.objects.get(cname = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable3(request, id) :
    deleterecord=diseaseModel.objects.get(diseasecode = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable4(request, id) :
    deleterecord=discoverModel.objects.get(id = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable5(request, id) :
    deleterecord=usersModel.objects.get(email = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable6(request, id) :
    deleterecord=publicservantModel.objects.get(id = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable7(request, id) :
    deleterecord= doctorModel.objects.get(id = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable8(request, id) :
    deleterecord= specializeModel.objects.get(id = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })

def deleteRecordTable9(request, id) :
    deleterecord= recordModel.objects.get(id = id)
    deleterecord.delete()
    showAllDiseaseType = diseaseTypeModel.objects.all()
    showAllCountry = countryModel.objects.all()
    showAllDisease = diseaseModel.objects.all()
    showAllDiscover = discoverModel.objects.all()
    showAllUsers = usersModel.objects.all()
    showAllPublicServant = publicservantModel.objects.all()
    showAllDoctor = doctorModel.objects.all()
    showAllSpecialize = specializeModel.objects.all()
    showAllRecord = recordModel.objects.all()
    return render(request, 'delete.html',{"dataDisType" : showAllDiseaseType, "datacount" : showAllCountry, "dataDis" : showAllDisease, "dataDiscover" : showAllDiscover, "dataUsers" : showAllUsers, "dataPubServ" : showAllPublicServant, "dataDoc" : showAllDoctor, "dataSpec" : showAllSpecialize, "dataRecord" : showAllRecord })



def editTable1(request, id) :
    editobject = diseaseTypeModel.objects.get(id = id)
    return render(request, 'editTable1.html', {"diseaseTypeModel":editobject})


def updateTable1(request, id) :
    UpdateTable=diseaseTypeModel.objects.get(id = id)
    form=diseaseTypeForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable1.html', {"diseaseTypeModel":UpdateTable})

def editTable2(request, id) :
    editobject = countryModel.objects.get(cname = id)
    return render(request, 'editTable2.html', {"countryModel":editobject})


def updateTable2(request, id) :
    UpdateTable=countryModel.objects.get(cname = id)
    form=countryForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable2.html', {"countryModel":UpdateTable})


def editTable3(request, id) :
    editobject = diseaseModel.objects.get(diseasecode = id)
    return render(request, 'editTable3.html', {"diseaseModel":editobject})


def updateTable3(request, id) :
    UpdateTable=diseaseModel.objects.get(diseasecode = id)
    form=diseaseForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable3.html', {"diseaseModel":UpdateTable})


def editTable4(request, id) :
    editobject = discoverModel.objects.get(id = id)
    return render(request, 'editTable4.html', {"discoverModel":editobject})


def updateTable4(request, id) :
    UpdateTable=discoverModel.objects.get(id = id)
    form=discoverForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable4.html', {"discoverModel":UpdateTable})

def editTable5(request, id) :
    editobject = usersModel.objects.get(email = id)
    return render(request, 'editTable5.html', {"usersModel":editobject})


def updateTable5(request, id) :
    UpdateTable=usersModel.objects.get(email = id)
    form=usersForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable5.html', {"usersModel":UpdateTable})

def editTable6(request, id) :
    editobject = publicservantModel.objects.get(id = id)
    return render(request, 'editTable6.html', {"publicservantModel":editobject})


def updateTable6(request, id) :
    UpdateTable=publicservantModel.objects.get(id = id)
    form=publicservantForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable6.html', {"publicservantModel":UpdateTable})

def editTable7(request, id) :
    editobject = doctorModel.objects.get(id = id)
    return render(request, 'editTable7.html', {"doctorModel":editobject})


def updateTable7(request, id) :
    UpdateTable=doctorModel.objects.get(id = id)
    form=doctorForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable7.html', {"doctorModel":UpdateTable})

def editTable8(request, id) :
    editobject = specializeModel.objects.get(id = id)
    return render(request, 'editTable8.html', {"specializeModel":editobject})


def updateTable8(request, id) :
    UpdateTable=specializeModel.objects.get(id = id)
    form=specializeForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable8.html', {"specializeModel":UpdateTable})

def editTable9(request, id) :
    editobject = recordModel.objects.get(id = id)
    return render(request, 'editTable9.html', {"recordModel":editobject})


def updateTable9(request, id) :
    UpdateTable=recordModel.objects.get(id = id)
    form=recordForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editTable9.html', {"recordModel":UpdateTable})











