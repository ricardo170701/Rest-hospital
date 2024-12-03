from django.test import TestCase
from django.urls import reverse
from patients.models import Patient
from .models import Doctor
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.
class DoctorViewSertTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="luis",
            last_name="martinez",
            date_of_birth="1990-12-05",
            contact_number="12312312",
            email="example@example.com",
            address="Direction de prueba",
            medical_history="ninguna",
        )
        self.doctor = Doctor.objects.create(
            first_name="carlos",
            last_name="ramirez",
            qualification="Profesional",
            contact_number="15412312",
            email="example2@example.com",
            address="medellin de prueba",
            biography="ninguna",
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_403(self):
        url = reverse(
            "doctor-appointments",
            kwargs={"pk": self.doctor.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
