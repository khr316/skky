from django.urls import path
from skky import views  # views.py에서 정의한 로그인 뷰를 가져옴
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('machine/', views.machine, name='기계정보'), 
    path('machine/collect/<int:machine_id>/', views.collect_machine, name='기계수거'),  # 수거 완료 URL 추가
    path('machine/edit/<int:machine_id>/', views.machine_edit, name='기계수정'),
    
    path('user/',views.user, name='회원정보'),
    path('user/delete/<int:user_id>/', views.delete_user, name='탈퇴'),
    path('user/detail/<int:user_id>/', views.user_detail, name='회원상세정보'),
    
    path('product/', views.product, name='상품정보'),
    path('product/upload/', views.product_upload, name='상품등록'),
    path('product/delete/<int:product_id>/', views.product_delete, name='상품삭제'),
    path('product/edit/<int:product_id>/', views.product_edit, name='상품수정'),
      
    path("admin/", admin.site.urls),
    path('', views.main, name='main'),  # 메인 페이지로 리디렉션 (임시로 main view가 필요)
    path("login/", views.login_action, name='login'),  # 로그인 URL 추가
    path("signup/", views.signup, name='signup'), # 회원가입 URL 추가
    path("logout/", views.logout_action, name='logout'),
    path("delivery_complete/<int:exchange_id>/", views.delivery_complete, name='배송완료')
          
]
