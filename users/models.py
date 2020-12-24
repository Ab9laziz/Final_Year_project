from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from home.models import CommonInfo


class UserAccountManager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff status.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser status')

        return self._create_user(email, email, password, **extra_fields)

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )


MEMBERSHIP_CHOICES = (
    ('admin', 'admin'),
    ('trainer', 'trainer'),
    ('player', 'player'),
)

class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='users/profile-photos/', null=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=30,choices=MEMBERSHIP_CHOICES,default='admin')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='male')
    date_of_birth = models.DateField(null=True, blank=True)
    staff_id = models.CharField(max_length=50, null=True, blank=True)
    id_no = models.PositiveIntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = UserAccountManager()

    def __str__(self):
        return f"{self.get_full_name()}"

User = get_user_model()
class PlayerProfile(models.Model):
    user = models.OneToOneField(User, related_name='player_profile', on_delete=models.CASCADE)
    estate = models.CharField(max_length=254)
    guardian_email = models.EmailField(verbose_name='Guardian\'s Email')
    guardian_name = models.CharField(max_length=254, verbose_name='Guardian\'s Name')
    guardian_phone_number = models.CharField(max_length=30, verbose_name='Guardian\'s Phone Number')

    def __str__(self) -> str:
        return self.user.username

class PlayerMedicalRecord(CommonInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_records')
    description = models.TextField()
    special_instruction = models.TextField(null=True, blank=True)
    doctor_name = models.CharField(max_length=254, blank=True, null=True, verbose_name='Doctor\'s Name')
    doctor_phone_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Doctor\'s Phone Number')


class ConsentForm(CommonInfo):
    user = models.OneToOneField(User, related_name='consent_form', on_delete=models.CASCADE)
    scanned_consent_form = models.ImageField(upload_to='players/consent-forms', null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.get_username()
