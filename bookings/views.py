from .serializers import AppointmentSerializer, MedicalNotesSerializer
from .models import Appointment, MedicalNote
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# GET /api/patients => listar
# POST /api/patients => Crear
# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Modificar
# DELETE /api/patients/<pk> => Borrar


class ListAppointmentView(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class DetailsAppointmentView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = "pk"


class ListMedicalNoteView(ListCreateAPIView):
    serializer_class = MedicalNotesSerializer
    queryset = MedicalNote.objects.all()


class DetailsMedicalNoteView(RetrieveUpdateDestroyAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNotesSerializer
    lookup_field = "pk"
