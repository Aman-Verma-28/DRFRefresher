from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from locationapp.models import CountryModel, LocationModel
from locationapp.serializers import CountryModelSerializer, LocationModelSerializer
from locationapp import logger

from external_api_handlers.google_api import GoogleMapsAPIHandler


class CountryAPI(APIView):
    """
    API to list and add countries.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser, IsAuthenticated)

    def get(self, request):
        """
        List all countries.
        """
        qryset = CountryModel.objects.all()
        serialized = CountryModelSerializer(qryset, many=True)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Add a new country to the system
        """

        data = request.data
        ## Remove user-input slug from data as the slug is autogenerated upon instance creation.
        if 'slug' in data.keys():
            del data['slug']
        serialized = CountryModelSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                serialized.data,
                status=status.HTTP_201_CREATED
            )
        else:
            logger.info(serialized.errors)
            return Response(
                serialized._errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class IndividualCountryAPI(APIView):
    """
    API group to deal with individual countries.
    """

    def get(self, request, slug):
        """
        Get a single country.
        """
        try:
            country = CountryModel.objects.filter(slug=slug).first()
        except CountryModel.DoesNotExist:
            logger.info(f"Country with slug: {slug} does not exist")
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serialized = CountryModelSerializer(country)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, slug):
        """
        Update a single country.
        """
        try:
            country = CountryModel.objects.filter(slug=slug).first()
        except CountryModel.DoesNotExist:
            logger.info(f"Country with slug: {slug} does not exist")
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        data = request.data
        ## Remove user-input slug from data as the slug is autogenerated upon instance creation.
        if 'slug' in data.keys():
            del data['slug']
        serializer = CountryModelSerializer(country, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            logger.info(serializer.errors)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, slug):
        """
        Delete a single country.
        """
        try:
            country = CountryModel.objects.filter(slug=slug).first()
        except CountryModel.DoesNotExist:
            logger.info(f"Country with slug: {slug} does not exist")
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        country.delete()
        return Response(
            status=status.HTTP_200_OK
        )


class LocationAPI(APIView):
    """
    API to list and add locations.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser, IsAuthenticated)

    def get(self, request):
        """
        GET method to list all locations.
        """

        qryset = LocationModel.objects.all()
        serialized = LocationModelSerializer(qryset, many=True)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        POST method to add a new location.
        """

        data = request.data
        ## Remove user-input slug from data as the slug is autogenerated upon instance creation.
        if 'slug' in data.keys():
            del data['slug']
        serialized = LocationModelSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                serialized.data,
                status=status.HTTP_201_CREATED
            )
        else:
            logger.info(serialized.errors)
            return Response(
                serialized.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class IndividualLocationAPI(APIView):
    """
    API group to deal with individual locations.
    """

    def get(self, request, slug):
        """
        GET method to get a single location.
        """

        try:
            location = LocationModel.objects.get(slug=slug)
        except LocationModel.DoesNotExist:
            logger.info(f"Location with slug: {slug} does not exist")
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serialized = LocationModelSerializer(location)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, slug):
        """
        PUT method to update a single location.
        """

        try:
            location = LocationModel.objects.get(slug=slug)
        except LocationModel.DoesNotExist:
            logger.info(f"Location with slug: {slug} does not exist")
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        data = request.data
        ## Remove user-input slug from data as the slug is autogenerated upon instance creation.
        if 'slug' in data.keys():
            del data['slug']
        serializer = LocationModelSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            logger.info(serializer.errors)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, slug):
        """
        DELETE method to delete a single location.
        """

        try:
            location = LocationModel.objects.get(slug=slug)
        except LocationModel.DoesNotExist:
            logger.info(f"Location with slug: {slug} does not exist")
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        location.delete()
        return Response(
            status=status.HTTP_200_OK
        )

class GetLocationCodeAPI(APIView):
    """
    API to get location code.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        GET method to get location code.
        """

        location_name = request.query_params.get('location_name')
        location_obj = LocationModel.objects.filter(city_town=location_name.title()).first()
        if location_obj:
            geo_code = GoogleMapsAPIHandler.get_city_geocode(location=location_obj)
            return Response(
                geo_code,
                status=status.HTTP_200_OK
            )
        else:
            resp = {
                'error': 'Location not found in Native System',
                'hint': "Try only adding the CITY name. Example: 'Mumbai'"
            }
            return Response(
                resp,
                status=status.HTTP_404_NOT_FOUND
            )
