from django.contrib import admin

from .models import Course

#colocando no menu admin as outras colunas
class CourseAdmin(admin.ModelAdmin):
	list_display = ['name','slug','start_date','created_at']
	search_fields = ['name','slug']
	#faz no admin  o 
	prepopulated_fields = {'slug': ['name']}



admin.site.register(Course,CourseAdmin)





