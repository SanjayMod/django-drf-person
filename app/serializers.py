# Package imports
from rest_framework import serializers

# Model imports
from app.models import Person


# Start Person serializers
class PersonSerializer(serializers.ModelSerializer):
    """ Serializer: Person """

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email')
# End Person serializers
