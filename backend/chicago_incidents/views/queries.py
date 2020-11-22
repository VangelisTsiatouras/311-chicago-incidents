import typing

from django.db.models import Count
from drf_yasg import utils
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from .. import serializers
from ..models import Incident


class QueriesViewSet(viewsets.GenericViewSet):
    """The queries view set
    """
    queryset = ''

    @utils.swagger_auto_schema(
        operation_summary='The total requests per type that were created within a specified time range and sort them '
                          'in a descending order',
        operation_description='',
        query_serializer=serializers.DateRangeParams
    )
    @action(
        methods=['get'], detail=False, url_path='totalRequestsPerType',
        serializer_class=serializers.TotalRequestsPerTypeSerializer
    )
    def total_requests_per_type(self, request):
        query_params = serializers.DateRangeParams(data=self.request.query_params, context={'request': request})
        query_params.is_valid(raise_exception=True)
        data = query_params.validated_data
        # Raw SQL query (printed out executing print(queryset.query)") (the dates are examples):
        # SELECT "incidents"."type_of_service_request", COUNT("incidents"."type_of_service_request") AS
        #   "number_of_requests" FROM "incidents" WHERE ("incidents"."creation_date" >= 2010-10-10 00:00:00+00:00 AND
        #   "incidents"."creation_date" <= 2012-10-10 00:00:00+00:00) GROUP BY "incidents"."type_of_service_request"
        #   ORDER BY "number_of_requests" DESC;
        queryset = Incident.objects.filter(creation_date__gte=data.get('start_date'),
                                           creation_date__lte=data.get('end_date'))\
            .values('type_of_service_request').annotate(number_of_requests=Count('type_of_service_request'))\
            .order_by('-number_of_requests')
        serializer = serializers.TotalRequestsPerTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self) -> typing.List[BasePermission]:
        """Instantiates and returns the list of permissions that this view requires.
        """
        return [IsAuthenticated()]
