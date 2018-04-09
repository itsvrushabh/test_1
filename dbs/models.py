from django.db import models

# Create your models here.
class AbstractTools(models.Model):
    name =models.CharField(max_length=300)
    input_value = models.CharField(max_length=300)
    indicator = models.CharField(max_length=300)

class Square(AbstractTools):
    files = models.FileField(upload_to='./data/yml')
    pass

class Diamond(AbstractTools):
    pam1 = models.CharField(max_length=300)
    pam2 = models.CharField(max_length=300)
    conditions = (('1','>'),('2','<'),('3','='))
    condition = models.CharField(max_length=1, choices=conditions)

class Circle(AbstractTools):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    hostname = models.CharField(max_length=300)

class Parabola(AbstractTools):
    types = models.CharField(max_length=300)

class Workflow(models.Model):
    info = models.CharField(max_length=300)

class Steps(models.Model):
    steps_id = models.CharField(max_length=300)
    # workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    # workflow_id = models.ManyToOneRel(Workflow)
    # workflow_id = models.OneToOneField(Workflow,on_delete=models.CASCADE)
    workflow_id = models.ManyToManyField(Workflow)
    actiontool_id = models.OneToOneField(AbstractTools,on_delete=models.CASCADE)