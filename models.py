# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
 
class Employee(models.Model):    
    Empolyee_name = models.CharField(max_length=100)
    Age = models.CharField(max_length=2)
    Joining_Date = models.DateField(default = '26-06-2018')
    Email = models.EmailField()  
    Contact = models.CharField(max_length=15)  
    
