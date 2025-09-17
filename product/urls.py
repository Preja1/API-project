from django.urls import path,include

from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet
# 2 Get
# 1 Post
# 1 Delete
# 1 Patch
# 1 Put
# 6 method are implements

#browsable Api view
router= DefaultRouter()

router.register("product",ProductViewSet)

urlpatterns = [
    path("",include(router.urls))

]
