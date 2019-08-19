from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class NewWorkout(models.Model):
    # Workout number:
    number = models.AutoField(primary_key=True)

    # User name:
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # User weight:
    weight = models.FloatField("Weight [kg]:", default=0, blank=True, null=True)

    # Date:
    date = datetime.now()

    # Gym name:
    gym_name = models.CharField("Gym name: ", default='CityFit', max_length=30, blank=True)

    # Gym city:
    gym_city = models.CharField("City: ", default='Cracow', max_length=30, blank=True)

    def __str__(self):
        return str(self.number)


#Gym machines:
class Treadmill(models.Model):
    # Gym Machine Name:
    name_tm = "Treadmill"

    # Gym Machine Value:
    time_tm = models.FloatField("Time [min]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    avg_speed_tm = models.FloatField("Avg. Speed [km/h]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    avg_slope_tm = models.FloatField("Avg. Slope [%]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    calories_tm = models.FloatField("Calories [kCal]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    distance_tm = models.FloatField("Distance [km]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_tm = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_tm


class LatMachine(models.Model):
    # Gym Machine Name:
    name_lm = "LatMachine"

    # Gym Machine Value:
    series_lm = models.IntegerField("Series:", default=0, null=True, blank=True)

    # Gym Machine Value:
    repetitions_lm = models.IntegerField("Repetitions:", default=0, null=True, blank=True)

    # Gym Machine Value:
    max_weight_lm = models.FloatField("Max weight [kg]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    min_weight_lm = models.FloatField("Min weight [kg]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_lm = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_lm


class ChestPress(models.Model):
    # Gym Machine Name:
    name_cp = "ChestPress"

    # Gym Machine Value:
    series_cp = models.IntegerField("Series:", default=0, null=True, blank=True)

    # Gym Machine Value:
    repetitions_cp = models.IntegerField("Repetitions:", default=0, null=True, blank=True)

    # Gym Machine Value:
    max_weight_cp = models.FloatField("Max weight [kg]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    min_weight_cp = models.FloatField("Min weight [kg]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_cp = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_cp


class ChestFly(models.Model):
    # Gym Machine Name:
    name_cf = "ChestFly"

    # Gym Machine Value:
    series_cf = models.IntegerField("Series:", default=0, null=True, blank=True)

    # Gym Machine Value:
    repetitions_cf = models.IntegerField("Repetitions:", default=0, null=True, blank=True)

    # Gym Machine Value:
    max_weight_cf = models.FloatField("Max weight [kg]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    min_weight_cf = models.FloatField("Min weight [kg]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_cf = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_cf


class CrossTrainer(models.Model):
    # Gym Machine Name:
    name_ct = "CrossTrainer"

    # Gym Machine Value:
    time_ct = models.FloatField("Time [min]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    power_ct = models.FloatField("Power [W]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    slip_ct = models.FloatField("Slip [slip/min]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    calories_ct = models.FloatField("Calories [kCal]:", default=0, null=True, blank=True)
    
    # Gym Machine Value:
    distance_ct = models.FloatField("Distance [km]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_ct = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)


class LowerBackBench(models.Model):
    # Gym Machine Name:
    name_lbb = "LowerBackBench"

    # Gym Machine Value:
    series_lbb = models.IntegerField("Series:", default=0, null=True, blank=True)

    # Gym Machine Value:
    repetitions_lbb = models.IntegerField("Repetitions:", default=0, null=True, blank=True)

    # Gym Machine Value:
    max_weight_lbb = models.FloatField("Max weight [kg]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    min_weight_lbb = models.FloatField("Min weight [kg]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_lbb = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_lbb


class ShoulderPress(models.Model):
    # Gym Machine Name:
    name_sp = "ShoulderPress"

    # Gym Machine Value:
    series_sp = models.IntegerField("Series:", default=0, null=True, blank=True)

    # Gym Machine Value:
    repetitions_sp = models.IntegerField("Repetitions:", default=0, null=True, blank=True)

    # Gym Machine Value:
    max_weight_sp = models.FloatField("Max weight [kg]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    min_weight_sp = models.FloatField("Min weight [kg]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_sp = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_sp


class SqueezingDumbellSlantingBench(models.Model):
    # Gym Machine Name:
    name_sdsb = "SqueezingDumbellSlantingBench"

    # Gym Machine Value:
    series_sdsb = models.IntegerField("Series:", default=0, null=True, blank=True)

    # Gym Machine Value:
    repetitions_sdsb = models.IntegerField("Repetitions:", default=0, null=True, blank=True)

    # Gym Machine Value:
    max_weight_sdsb = models.FloatField("Max weight [kg]:", default=0, null=True, blank=True)

    # Gym Machine Value:
    min_weight_sdsb = models.FloatField("Min weight [kg]:", default=0, null=True, blank=True)

    # NewWorkout:
    new_workout_sdsb = models.ForeignKey(NewWorkout, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_sdsb

#----------------------------------------------------------------------------------
