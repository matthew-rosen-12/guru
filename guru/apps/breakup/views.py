from rest_framework import serializers, viewsets
from .models import Person

# Serializers define the API representation.
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer