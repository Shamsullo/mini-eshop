from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update-item/', views.updateItem, name="update_item"),
	path('process-order/', views.processOrder, name="process_order"),

	path('category-products/<int:category_id>', views.category_view, name="by_category"),
	path('product-details/<int:product_id>', views.product_detail_view, name="product_details")
]