from django.urls import path
from .views import (
    HelloView,
    StockListView,
    StockUpdateView,
    StockDeleteView,
    view_requestsforadmin,
    add_feedback,
    addrequests,
    view_requests,
    approve_request,
    reject_request,
    AgronomistLoginView,
    CodeView,
    IndexView,
    StockManagementView,
    FarmerCreateView,
    AdminDashboardView,
    FarmerLoginView,
    AddFarmerView,
    FarmersDashboardView,
    FarmerManagementView,
    EditFarmerView,
    DeleteFarmerView,
    settings_view,
    AboutUsView,

)

urlpatterns = [
    path('admin_dashboard/', FarmersDashboardView.as_view(), name='admin_dashboard'),
    path('farmer_management/', FarmerManagementView.as_view(), name='farmer_management'),
    path('farmers/edit/<int:id>/', EditFarmerView.as_view(), name='edit_farmer'),
    path('farmers/delete/<int:id>/', DeleteFarmerView.as_view(), name='delete_farmer'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),  # Define the URL for About Us

    path('settings/', settings_view, name='settings'),

    path('view_requestsforadmin/', view_requestsforadmin, name='view_requestsforadmin'),
    path('add-feedback/<int:id>/', add_feedback, name='add_feedback'),
    path('approve-request/<int:id>/', approve_request, name='approve_request'),
    path('reject-request/<int:id>/', reject_request, name='reject_request'),
    path('view-requests/', view_requests, name='view_requests'),
    path('addrequests/', addrequests, name='addrequests'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('code/', CodeView.as_view(), name='code'),
    path('index/', IndexView.as_view(), name='index'),
    path('stock_management/', StockManagementView.as_view(), name='stock_management'),
    path('farmer_register/', FarmerCreateView.as_view(), name='farmer_register'),
    path('add_farmer/', AddFarmerView.as_view(), name='add_farmer'),
    path('farmer_login/', FarmerLoginView.as_view(), name='farmer_login'),
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('agronomist_login/', AgronomistLoginView.as_view(), name='agronomist_login'),
    
    # Stock management URLs
    path('stocks/', StockListView.as_view(), name='stock_list'),
    path('stocks/edit/<int:pk>/', StockUpdateView.as_view(), name='edit_stock'),
    path('stocks/delete/<int:pk>/', StockDeleteView.as_view(), name='delete_stock'),
]