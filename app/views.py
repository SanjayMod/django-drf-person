from rest_framework.generics import GenericAPIView
from rest_framework import status

# Serializer imports
from app.serializers import PersonSerializer

# Model imports
from app.models import Person

# Utility imports
from person_drf.utils import get_response_schema


# Start Person views
class PersonCreateListView(GenericAPIView):

    serializer_class = PersonSerializer

    def get(self, request):
        """ 
        Get list of persons
        """

        queryset = Person.objects.all()

        person_serializer = PersonSerializer(queryset, many=True)

        return get_response_schema(person_serializer.data, {}, status.HTTP_200_OK)

    def post(self, request):
        """ 
        Create New User 
        
        Create a new person.
        """

        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return get_response_schema(serializer.data, {}, status.HTTP_201_CREATED)

        else:
            # PersonSerializer serializer errors
            return get_response_schema([], serializer.errors, status.HTTP_400_BAD_REQUEST)
# End Person views
