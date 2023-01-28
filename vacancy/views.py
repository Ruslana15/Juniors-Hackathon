from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404

from .models import Vacancy
from .serializers import VacancySerializer


class VacancyAPIView(APIView):

    def get_object(self, pk):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Vacancy.objects.all()

        serializer = VacancySerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = VacancySerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Vacancy Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        todo_to_update = Vacancy.objects.get(pk=pk)
        serializer = VacancySerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Vacancy Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        todo_to_delete = Vacancy.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Vacancy Deleted Successfully'
        })
