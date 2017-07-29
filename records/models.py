from django.contrib.auth.models import User
from django.db import models


class UserAadhar(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=1000, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name()


class Patient(models.Model):
    user = models.OneToOneField(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


class Doctor(models.Model):
    user = models.OneToOneField(User)
    created = models.DateTimeField(auto_now_add=True)
    specialities = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Case(models.Model):
    title = models.TextField()
    patient = models.ForeignKey(Patient, related_name="cases")
    doctor = models.ForeignKey(Doctor, related_name="cases")
    created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Document(models.Model):
    text = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to='docs', blank=True, null=True)

    def __str__(self):
        return self.text or "patient document"

    def serialize(self):
        url = self.upload.url if self.upload else None
        return dict(text=self.text, url=url)


class Record(models.Model):
    case = models.ForeignKey(Case, related_name="records")
    symptoms = models.TextField()
    prescription = models.ForeignKey(Document, related_name="prescriptions")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case.title

class RecordACL(models.Model):
    record = models.ForeignKey(Record, related_name="permissions")
    user = models.ForeignKey(User, related_name="record_accesses")
    can_view = models.BooleanField()
    can_edit = models.BooleanField()

    def __str__(self):
        return self.user.name


class Test(models.Model):
    patient = models.ForeignKey(Patient, related_name="tests")
    case = models.ForeignKey(
        Case, related_name="linked_tests", blank=True, null=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    report = models.ForeignKey(Document, related_name="tests")

    def __str__(self):
        return self.name
