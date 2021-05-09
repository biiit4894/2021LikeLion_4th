from django.shortcuts import render
import random

def home(request):
    return render(request, 'lottoapp/home.html')

def result(request):

    list = ('강연우', '강윤서', '김서영', '김소은', '김유진', '노은성', '문다연', '박경나',
            '박도윤', '박혜준', '송주연', '안현주', '오예림', '유수화', '윤정인', '이민정', '이연수',
            '전수현', '김정운', '장한빛', '조원아', '최진영', '황서경')
    buddy = random.sample(list, 1)

    return render(request, 'lottoapp/result.html', {'buddy':buddy})


