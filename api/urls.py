from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.categories import CategoryViewSet
from .views.comments import CommentsViewSet
from .views.genres import GenreViewSet
from .views.reviews import ReviewsViewSet
from .views.titles import TitleViewSet
from .views.users import MyUserViewSet, get_token, registrations_request

router = DefaultRouter()
router.register(r'titles/(?P<title_id>[^/.]+)/reviews', ReviewsViewSet,
                basename='ReviewsView')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    CommentsViewSet, basename='CommentsView')
router.register(
    r'users', MyUserViewSet, basename='MyUserViewSet'
)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitleViewSet)

auth_paths = [path('email/', registrations_request), path('token/', get_token)]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_paths))
]
