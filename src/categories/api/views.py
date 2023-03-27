from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer

from categories.api.permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer    
    #queryset = Category.objects.all() #El Endpoint retorna absolutamente todos los elementos que esten registrados en la DB
    queryset = Category.objects.filter(published=True) #El Endpoint retorna unicamente los elementos que esten publicados (Published=True) 
    #queryset = Category.objects.filter(published=False) #El Endpoint retorna unicamente los elementos que NO esten publicados (Published=False) 

    
    lookup_field = 'slug'  #Cambiar el ID por la propiedad 'slug'. Cuando se envien parametros a la API no se envia el ID de la categoria, debe enviarse el SLUG.

    # filter_backends = [DjangoFilterBackend]         # Se incorpora el filtro de busquedas de Django (DjangoFilterBackend)
    # filterset_fields = ['published','title']        # Se indican los campos por los que pueden filtrarse los resultados del EndPoint
