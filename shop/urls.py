from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from shop import views
from django.conf.urls import include
'''
from django.conf.urls import url, include
if settings.DEBUG:
    import debug_toolbar
'''


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('page/<str:slug>/', views.PageDisplay.as_view(), name='page-detail'),
    path('product/', views.ProductList.as_view(), name='product'),
    path('product/<str:slug>/', views.AuthorDetail.as_view(), name='product-detail'),
    path('category/<str:slug>/', views.category_detail.as_view(), name='category_detail'),
    path('shop/<str:slug>/', views.ShopDisplay.as_view(), name='shop-detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.cart_add, name='cart_add'),
    path('cart/update/<int:product_id>', views.cart_update, name='cart_update'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('to_bank/<int:order_id>', views.to_bank, name='to_bank'),
    path('callback/', views.callback, name='callback'),
    path('category/<str:slug>/', views.CategoryProductList.as_view(), name='category'),
    path('registration/register/', views.SignUp.as_view(), name='register'),
    path('registration/login/', auth_views.LoginView.as_view(), name="login"),
    path('registration/logout/', views.LogoutUser.as_view(), name="logout"),
    path('search/', views.search.as_view(), name="search"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
'''