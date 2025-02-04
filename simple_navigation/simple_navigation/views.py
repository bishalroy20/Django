from django.shortcuts import render

def home(request):
    # return render(request , 'index.html')
    f = {'author' : 'Bishal' , 'age' : '22' , 'lst' : ['python','is','best']}
    return render(request , 'index.html' , f)