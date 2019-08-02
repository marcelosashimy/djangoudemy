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


#adef details(request, slug):
	#course= Course.objects.get(pk=pk)
	#Course é uma model
def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)
#	context = {
#		'course':course,
#		'form':form
#	}
#	template_name = 'courses/details.html'
#	return render(request, template_name, context)


		