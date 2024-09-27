from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Machine, MachineUser, User, Product, Exchange, Delivery


def reword(request):
    products = Product.objects.all()  # 모든 상품 조회
    user_points = request.user.user_point  # 사용자의 현재 포인트 가져오기

    # count 최대값
    max_count = []
    
    available_products = []

    for product in products:
        # 사용자의 포인트보다 낮은 상품만
        if product.product_point <= user_points:
            # 교환 가능한 개수 계산
            count = user_points // product.product_point  
            # 1부터 count까지의 리스트 생성
            quantity_options = list(range(1, count + 1))  
            
            max_count.append(count)
            a = max(max_count)
            # 상품 정보와 함께 수량 옵션 추가
            available_products.append({
                'id': product.id,
                'name': product.product_name,
                'points': product.product_point,
                'count': count,
                'quantity_options': quantity_options  # 수량 옵션 추가
            })
    
    b = [i for i in range(1,a+1)]

    content = {
        "users": request.user,
        "products": products,  # 교환 가능한 상품 목록
        "b" : b,
        "available_products" : available_products,
    }

    return render(request, 'exchange/exchange.html', content)

def reword_action(request):
    user = request.user
    
    # POST로 전달된 데이터 받기
    product_id = request.POST.get('product')
    quantity = request.POST.get('quantity')
    
    product = Product.objects.get(id=product_id)
    
    return render(request, 'exchange/reword.html', {'user':user,'product':product, 'quantity':quantity})

def reword_action_action(request):
    var_user_id = request.POST.get('user_id')
    var_product_id = request.POST.get('product_id')
    var_product_cnt = request.POST.get('product_cnt')
    var_change_type = request.POST.get('change_type')
    var_address = request.POST.get('address')
    var_datetime = request.POST.get('datetime')
    
    Exchange.objects.create(user_id=var_user_id,
                            product_id=var_product_id,
                            change_cnt=var_product_cnt,
                            change_way=var_change_type,
                            change_app_dt=var_datetime)
    
    
    
    return redirect('main')