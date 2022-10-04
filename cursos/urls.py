from django.urls import path
from .views import (CursoApiView, AvaliacaoApiView, CursoUpdateDestroy, AvaliacaoUpdateDestroy, 
                    CursoViewSet, AvaliacaoViewSet)

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet) #api v2

urlpatterns = [ #api v1
    path('cursos/', CursoApiView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoUpdateDestroy.as_view(), name='curso_edit_delete'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacaoApiView.as_view(), name='curso_avaliacao'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoUpdateDestroy.as_view(), name='curso_avaliacao_edit'),
    
    path('avaliacoes/', AvaliacaoApiView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoUpdateDestroy.as_view(), name='avaliacao_edit_delete'),
]