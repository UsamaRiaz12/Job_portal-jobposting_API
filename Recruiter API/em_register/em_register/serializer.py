from rest_framework import serializers
from .models import em_register
class em_registerSerilaizer(serializers.ModelSerializer):
  class Meta:
    model=em_register
    fields=['id','company_name','email','job_tittle','description','requirments','date']