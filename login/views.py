import uuid

from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import requests


def login(request):
    return render(request, 'login/login.html')





def gest_login(request):  # 이거 신경쓰지마셈 안돼
    if request.method == 'POST':
        # POST 요청이 오면 게스트 아이디 생성 후 세션에 저장
        guest_id = str(uuid.uuid4())  # 랜덤 아이디 생성
        request.session['guest_id'] = guest_id  # 세션에 아이디 저장
        return redirect('login/gest_login.html')  # 게스트 로그인 후 다른 페이지로 이동 추후에 알림창이든 뭐든 중간과정을 만들어야 함.

    return render(request, 'login/gest_login.html')


