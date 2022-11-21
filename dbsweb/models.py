from django.db import models
from datetime import datetime 

class diseaseTypeModel(models.Model) :
    id = models.IntegerField(primary_key = True)
    description = models.CharField(max_length = 140)

    class Meta :
        db_table = "diseasetype"

    def __str__(self):
        return str(self.pk)

class countryModel(models.Model) :
    cname = models.CharField(max_length = 50, primary_key = True)
    population = models.BigIntegerField()

    class Meta :
        db_table = "country"
    
    def __str__(self):
        return str(self.pk)

class diseaseModel(models.Model) :
    diseasecode = models.CharField(max_length = 50, primary_key = True)
    pathogen = models.CharField(max_length = 20)
    description = models.CharField(max_length = 140)
    id = models.ForeignKey(diseaseTypeModel, on_delete = models.CASCADE, db_column = 'id')

    class Meta :
        db_table = "disease"

    def __str__(self):
        return str(self.pk)

class discoverModel(models.Model) :
    firstencdate = models.DateField(auto_now_add = False, auto_now = False, blank = False)
    diseasecode = models.ForeignKey(diseaseModel, on_delete = models.CASCADE, db_column = 'diseasecode')
    cname = models.ForeignKey(countryModel, on_delete = models.CASCADE, db_column = 'cname')
    id = models.IntegerField(primary_key = True)
    
    class Meta :
        db_table = "discover"

    def __str__(self):
        return str(self.pk)

class usersModel(models.Model) :
    email = models.CharField(max_length = 60, primary_key = True)
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 40)
    salary = models.IntegerField()
    phone = models.CharField(max_length = 20)
    cname = models.ForeignKey(countryModel, on_delete = models.CASCADE, db_column = 'cname')
    
    class Meta :
        db_table = "users"
    
    def __str__(self):
        return str(self.pk)

class publicservantModel(models.Model) :
    email = models.ForeignKey(usersModel, on_delete = models.CASCADE, db_column = 'email')
    department = models.CharField(max_length = 50)
    id = models.IntegerField(primary_key = True)

    class Meta :
        db_table = "publicservant"

    def __str__(self):
        return str(self.pk)

class doctorModel(models.Model) :
    email = models.ForeignKey(usersModel, on_delete = models.CASCADE, db_column = 'email')
    degree = models.CharField(max_length = 20)
    id = models.IntegerField(primary_key = True)

    class Meta :
        db_table = "doctor"

    def __str__(self):
        return str(self.pk)

class specializeModel(models.Model) :
    id = models.IntegerField(primary_key = True)
    specid = models.ForeignKey(diseaseTypeModel, on_delete = models.CASCADE, db_column = 'specid')
    email = models.ForeignKey(usersModel, on_delete = models.CASCADE, db_column = 'email')

    class Meta :
        db_table = "specialize"

    def __str__(self):
        return str(self.pk)

class recordModel(models.Model) :
    email = models.ForeignKey(usersModel, on_delete = models.CASCADE, db_column = 'email')
    cname = models.ForeignKey(countryModel, on_delete = models.CASCADE, db_column = 'cname')
    diseasecode = models.ForeignKey(diseaseModel, on_delete = models.CASCADE, db_column = 'diseasecode')
    totaldeaths = models.IntegerField()
    totalpatients = models.IntegerField()
    id = models.IntegerField(primary_key = True)
    
    class Meta :
        db_table = "record"

    def __str__(self):
        return str(self.pk)
