from django.contrib import admin
from .models import Researcher,Supervisor,Paper,PaperSupervisor,Degree
# Register your models here.
@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
	list_display = ('id','first_name', 'second_name', 'third_name')

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
	list_display = ('id','first_name', 'second_name', 'third_name')

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
	list_display = ('id','title')

@admin.register(PaperSupervisor)
class PaperSupervisorAdmin(admin.ModelAdmin):
	list_display = ('id','paper','supervisor')

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
	list_display = ('id','degree_type')
