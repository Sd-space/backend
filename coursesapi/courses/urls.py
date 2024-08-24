from django.urls import path
from .views import CourseViewSet, CourseInstanceViewSet

course_list = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

instance_create = CourseInstanceViewSet.as_view({
    'post': 'create'
})

instance_list = CourseInstanceViewSet.as_view({
    'get': 'list'
})

instance_detail = CourseInstanceViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    path('courses/', course_list, name='course-list-create'),
    path('courses/<int:pk>/', course_detail, name='course-detail-delete'),

    path('instances/', instance_create, name='instance-create'),
    path('instances/<int:year>/<int:semester>/', instance_list, name='instance-list'),
    path('instances/<int:year>/<int:semester>/<int:pk>/', instance_detail, name='instance-detail-delete'),
]
