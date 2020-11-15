from django.shortcuts import render

# Create your views here.

from .models import Quiz
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User


def home(request):#TOPページ
    if request.user.is_authenticated:
        params={'message':request.user}
        return render(request, 'quiz/home.html',params)
    else:
        return render(request, 'account/index.html')

@ensure_csrf_cookie
def json(request):
    import json
    import pprint
    
    dict = {"id": str(request.user)}
    
    json_file = open('sample.json', 'w')
    json.dump(dict, json_file)
    json_file = open('sample.json', 'r')
    data = json.load(json_file)
    pprint.pprint(data)

    return JsonResponse(data)



#def list(request):
#    if request.user.is_authenticated:
#        data=Quiz.objects.all()
#        params={'data':data}
#        return render(request,'quiz/list.html',params)
#    else:
#        return render(request, 'account/index.html')


#def add_problems(request):
#    if request.user.is_authenticated:
#        params = {'message': '', 'form': None}
#        if request.method == 'POST':
#            form = QuizForm(request.POST)
#            if form.is_valid() :
#                form.save()
#                return redirect('list_check')#データ整合チェック
#            else:
#                params['message'] = '再入力して下さい'
#                params['form'] = form
#        else:
#            params['form'] = QuizForm()
#        return render(request, 'quiz/add_problems.html', params)
#    else:
#        return render(request, 'account/index.html')
##

