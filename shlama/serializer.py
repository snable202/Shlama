from rest_framework.serializers import ModelSerializer
from .models import contact


class ContactSerializer(ModelSerializer):
    class Meta :
        model=contact
        fields='__all__'