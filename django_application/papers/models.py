from django.db import models

# Create your models here.

class Researcher(models.Model):
    class Meta:
        verbose_name_plural = 'Researchers'
        verbose_name = 'Researcher'
    
    first_name = models.CharField(max_length=50, blank=True, null=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    third_name = models.CharField(max_length=50, blank=True, null=True)
    fourth_name = models.CharField(max_length=50, blank=True, null=True)
    alternative_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.third_name}'


class Degree(models.Model):
    class Meta:
        verbose_name_plural='Degrees'
        verbose_name='Degree'
    
    degree_type = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.degree_type


class Paper(models.Model):
    class Meta:
        verbose_name_plural = 'Papers'
        verbose_name = 'Paper'
    
    title = models.CharField(max_length=300, blank=True, null=True)
    researcher = models.ForeignKey(Researcher, on_delete=models.SET_NULL, blank=True, null=True)
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, blank=True, null=True)
    date_of_publishing = models.IntegerField( blank=True, null=True)
    paper_number = models.IntegerField( blank=True, null=True)
    other = models.CharField(max_length=200, blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title


class Supervisor(models.Model):
    class Meta:
        verbose_name_plural='Supervisors'
        verbose_name='Supervisor'
    
    first_name = models.CharField(max_length=20, blank=True, null=True)
    second_name = models.CharField(max_length=20, blank=True, null=True)
    third_name = models.CharField(max_length=20, blank=True, null=True)
    fourth_name = models.CharField(max_length=20, blank=True, null=True)
    alternative_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.third_name}'


class PaperSupervisor(models.Model):
    class Meta:
        verbose_name_plural='PaperSupervisors'
        verbose_name='PaperSupervisor'
    
    paper=models.ForeignKey(Paper,on_delete=models.SET_NULL,null=True,blank=True)
    supervisor=models.ForeignKey(Supervisor,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return f'{self.paper}, {self.supervisor}'



