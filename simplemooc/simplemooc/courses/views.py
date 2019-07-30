from django.shortcuts import render, get_object_or_404
#importando o modelo
from .models import Course
from .forms import ContactCourse

#responsavel por renderizar o template da listagem dos cursos
def courses(request):
# Course = model, objects = manage do model, all tras todos
	courses=Course.objects.all()
	template_name = 'courses/index.html'
	#dicionario para a renderização
	context={
		'courses':courses
	}
	return render(request, template_name, context)


#def details(request, pk):
	#course= Course.objects.get(pk=pk)
	#Course é uma model
#	course=get_object_or_404(Course, pk=pk)
#	context = {
#		'course':course
#	}
#	template_name = 'courses/details.html'
#	return render(request, template_name, context)


def details(request, slug):
	#course= Course.objects.get(pk=pk)
	#Course é uma model
	course=get_object_or_404(Course, slug=slug)
	if request.method =='POST':
		form=ContactCourse(request.POST)
	else:
		form=ContactCourse()
	context = {
		'course':course,
		'form':form
	}
	template_name = 'courses/details.html'
	return render(request, template_name, context)


		