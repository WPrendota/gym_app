from django.test import TestCase
from .models import NewWorkout
from datetime import datetime
from django.contrib.auth.models import User


class NewWorkoutModelsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(NewWorkoutModelsTest, cls).setUpClass()
        user = User.objects.create_user(username="Witek", email="test@test.pl", password="password1234")
        new_workout = NewWorkout.objects.create(number=1, weight=120, user=user,
                                                gym_name="cityfit", gym_city="Kraków")

    def testNumberLabel(self):
        field_label = NewWorkout._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    # gym_name:

    def testGymName(self):
        field_label = NewWorkout._meta.get_field('gym_name').verbose_name
        self.assertEquals(field_label, 'Gym name: ')

    def testGymNameLength(self):
        field_length = NewWorkout._meta.get_field('gym_name').max_length
        self.assertEquals(field_length, 30)

    def testGymNameDefault(self):
        field_default = NewWorkout._meta.get_field('gym_name').default
        self.assertEquals(field_default, 'CityFit')

    def testGymNameBlank(self):
        field_blank = NewWorkout._meta.get_field('gym_name').blank
        self.assertEquals(field_blank, True)

# ----------------------------------------------------------------------------
