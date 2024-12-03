from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)
from .models import Doctor, Department, DoctorAvailability, MedicalNote
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


class ListDoctorsView(ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailsDoctorView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = "pk"


class ListDepartmentView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailsDepartmentView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = "pk"


class ListDoctorAvailabilityView(ListCreateAPIView):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailsDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer
    lookup_field = "pk"


class ListMedicalNoteView(ListCreateAPIView):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailsMedicalNoteView(RetrieveUpdateDestroyAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
    lookup_field = "pk"
