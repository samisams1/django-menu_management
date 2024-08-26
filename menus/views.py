from rest_framework import generics
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer

class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save()
        self.set_depth(instance)

    def set_depth(self, instance):
        if instance.parent:
            instance.depth = instance.parent.depth + 1
        else:
            instance.depth = 1
        instance.save()

class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer