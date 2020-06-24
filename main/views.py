from django.shortcuts import render,redirect
from polls.models import Question
from django.core.paginator import Paginator
from .models import Log
# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def send_question(request):
    query = request.GET['question_text']
    qs = Question.objects.all()
    answer = "Sorry no answer for that."
    for row in qs.values_list():
        print(row[1])
        if row[1].lower() == query.lower():
            answer = row[2]

    log = Log()
    log.q = query
    log.a = answer
    log.save()


    return render(request,'main/answer.html', {'answer':answer ,'qs':query})


def send_to_log(request):
    logs = Log.objects.all()
    paginator = Paginator(logs,6)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    page_range = list(paginator.page_range[0:len(paginator.page_range)])

    return render(request,'main/log.html',{ 'pages':pages, 'page_range':page_range})
# Create your views here.