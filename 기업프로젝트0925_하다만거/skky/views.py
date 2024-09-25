from django.shortcuts import render

# 쿼리문 직접 작성하여 DB 사용
from django.shortcuts import render
from django.db import connection
import pandas as pd
from django.contrib import messages

def test(request):
    # SQL 쿼리 작성 (상품 테이블에서 데이터를 가져옴)
    sql_query = "SELECT seq,category_name FROM Category"
    
    # pandas를 사용하여 SQL 쿼리 실행 및 DataFrame으로 변환
    df = pd.read_sql(sql_query, connection)
    
    # DataFrame을 리스트 형태로 변환하여 HTML 템플릿으로 전달
    data = df.to_dict(orient='records')
    
    # 'data_view.html' 템플릿에 data를 전달하여 렌더링
    return render(request, 'test.html', {'data': data})

def login(request):
    if request.method == 'POST':
        # 폼에서 user_id와 user_pw 받아오기
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')

        # SQL 쿼리 작성 (해당 user_id를 가진 유저를 찾기)
        login_query = "SELECT user_id, user_pw FROM Users WHERE user_id = %s"
        
        # pandas를 사용하여 SQL 쿼리 실행 및 DataFrame으로 변환
        df = pd.read_sql(login_query, connection, params=[user_id])

        # 사용자가 입력한 비밀번호와 데이터베이스에서 가져온 비밀번호를 비교
        if not df.empty and df.iloc[0]['user_pw'] == user_pw:
            # 로그인 성공 처리
            return render(request, 'main.html', {'user_id': user_id})
        else:
            # 로그인 실패 처리
            messages.error(request, '아이디 또는 비밀번호가 틀렸습니다.')
            return render(request, 'user/login.html')

    # GET 요청 시 로그인 페이지 렌더링
    return render(request, 'user/login.html')

