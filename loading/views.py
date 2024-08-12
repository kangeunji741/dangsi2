# loading/views.py

from django.shortcuts import render
import time

def loading_page(request):
    # 2초 동안 로딩 페이지를 보여줌
    time.sleep(2)
    return render(request, 'loading/loading.html')
