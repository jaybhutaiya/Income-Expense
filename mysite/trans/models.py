from django.db import models
from datetime import datetime


choice = [
    ('income','Income'),
    ('expense','Expense'),
]

class income(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=choice)
    date = models.DateTimeField(default=datetime.now())
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
# class expense(models.Model):
#     name = models.CharField(max_length=100)
#     ex_pense = models.IntegerField()
#     date = models.DateTimeField(default=datetime.now())

#     def __str__(self) -> str:
#         return self.name