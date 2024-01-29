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


class PersonDetailView(GenericAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):

        queryset = Person.objects.filter(
            id=self.kwargs.get('pk')
        )

        return queryset

    def get(self, request, *args, **kwargs):
        """ 
        Retrieve entry for person with the specified id (still delivered as a single entry inside an array)
        """

        person_queryset = self.get_queryset()

        if not person_queryset.exists():
            return get_response_schema([], {}, status.HTTP_404_NOT_FOUND)

        person_serializer = PersonSerializer(person_queryset.first())

        return get_response_schema(person_serializer.data, {}, status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """ 
        Update person specified by id
        """

        person_queryset = self.get_queryset()

        if not person_queryset.exists():
            return get_response_schema([], {}, status.HTTP_404_NOT_FOUND)

        person_serializer = PersonSerializer(person_queryset.first(), request.data)

        if person_serializer.is_valid():

            person_serializer.save()

            return get_response_schema(person_serializer.data, {}, status.HTTP_200_OK)

        else:
            # PersonSerializer serializer errors
            return get_response_schema([], person_serializer.errors, status.HTTP_400_BAD_REQUEST)
# End Person views
