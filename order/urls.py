from django.urls import path,include
from .router import order_router
from .views import CreateRazorPayOrderId

urlpatterns = [
    path("",include(order_router.urls)),
    # path("transcation/",include(tran_router.urls))
    path("createOrderId",view=CreateRazorPayOrderId.as_view(),name="createOrderId")
]
