from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvalicaoSerializer
from .permissions import SuperUser
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class CursoApiView(ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class CursoUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class AvaliacaoApiView(ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer
    
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()
        
class AvaliacaoUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer
    
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    
"""
API v2
"""

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (SuperUser,)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        
        if page is not None:
            serializer = AvalicaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = AvalicaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer