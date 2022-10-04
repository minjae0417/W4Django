from django.shortcuts import render, redirect
from random import *

# Create your views here.
# win(승리), draw(무승부), lose(패배) 횟수를 저장하는 전역변수 생성
win = 0
draw = 0
lose = 0

def rsp(request):
    # [미션] 함수에서 전역변수 설정하기
    

    context = {
        "win": win,
        "draw": draw,
        "lose": lose,
    }
    return render(request, "games/rsp.html", context)

def result(request, pick):
    # [미션] 함수에서 전역변수 설정하기
    
    
    rsp = ["가위", "바위", "보"]
    # [미션] 'com' 변수에 'rsp' 리스트의 원소들 중 하나를 랜덤하게 저장하기
    

    # [미션] 내가 선택한 'pick'과 'com' 변수에 저장된 가위바위보 결과를 비교해서 'result' 변수에 결과(승리, 무승부, 패배)를 저장하는 로직 작성하기
    # [미션] win(승리), draw(무승부), lose(패배) 횟수를 가위바위보 결과에 따라 증가시키기










    context = {
        "pick": pick,
        # [미션] 'com'키의 value값을 'com'변수값으로 만들기
        
        "result": result,
        "win": win,
        "draw": draw,
        "lose": lose,
    }

    return render(request, "games/result.html", context)

def reset(request):
    # [미션] 함수에서 전역변수 설정하기
    
    
    # [미션] win(승리), draw(무승부), lose(패배) 횟수를 초기화하기
    

    # 'urls.py'에서 설정한 app_name인 'games'의 url 경로중 별칭이 'rsp'인 경로로 리다이렉트
    return redirect("games:rsp")