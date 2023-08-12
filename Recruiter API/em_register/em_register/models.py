from django.db import models


class em_register(models.Model ):
    company_name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    job_tittle = models.CharField(max_length=100,default='')
    description=models.TextField(max_length=500,default='')
    requirments=models.TextField(max_length=500,default='')
    date=models.CharField(max_length=100,default="")
 




    def __str__(self):
        return self.job_tittle
    