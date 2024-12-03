from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from datetime import date


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    availabilities = DoctorAvailabilitySerializer(many=True, read_only=True)
    experience = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = [
            "id",
            "first_name",
            "last_name",
            "qualification",
            "experience",
            "contact_number",
            "email",
            "address",
            "biography",
            "is_on_vacation",
            "availabilities",
            "appointments",
        ]

    def get_experience(self, obj):
        first_availability = obj.availabilities.order_by("start_date").first()
        if first_availability:
            experience_td = date.today() - first_availability.start_date
            return experience_td.days // 365

    def validate_email(self, value):
        if "@example.com" in value:
            return value
        raise serializers.ValidationError("El correo debe incluir @example.com")

    def validate(self, attrs):
        if len(attrs["contact_number"]) < 10 and attrs["is_on_vacation"]:
            raise serializers.ValidationError(
                "Ingrese un numero valido antes de ir de vacaciones"
            )

        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"
