from .models import project
from rest_framework import viewsets, permissions
from .serializers import projectserializer 

class projectviewset(viewsets.ModelViewSet):
    # La consulta está en la misma línea
    queryset = project.objects.all()  
    permission_classes = [permissions.AllowAny]
    serializer_class = projectserializer