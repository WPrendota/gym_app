from django import forms
from .models import Treadmill, NewWorkout, LatMachine, ChestPress, ChestFly, CrossTrainer, LowerBackBench, ShoulderPress, \
    SqueezingDumbellSlantingBench


class TreadmillForm(forms.ModelForm):

    class Meta:
        model = Treadmill
        fields = ['time_tm', 'avg_speed_tm', 'avg_slope_tm', 'calories_tm', 'distance_tm',]
        exclude = ('new_workout_tm',)


class LatMachineForm(forms.ModelForm):

    class Meta:
        model = LatMachine
        fields = ['series_lm', 'repetitions_lm', 'max_weight_lm', 'min_weight_lm',]
        exclude = ('new_workout_lm',)


class ChestPressForm(forms.ModelForm):

    class Meta:
        model = ChestPress
        fields = ['series_cp', 'repetitions_cp', 'max_weight_cp', 'min_weight_cp',]
        exclude = ('new_workout_cp',)


class ChestFlyForm(forms.ModelForm):

    class Meta:
        model = ChestFly
        fields = ['series_cf', 'repetitions_cf', 'max_weight_cf', 'min_weight_cf',]
        exclude = ('new_workout_cf',)


class CrossTrainerForm(forms.ModelForm):

    class Meta:
        model = CrossTrainer
        fields = ['time_ct', 'power_ct', 'slip_ct', 'calories_ct', 'distance_ct']
        exclude = ('new_workout_ct',)


class LowerBackBenchForm(forms.ModelForm):

    class Meta:
        model = LowerBackBench
        fields = ['series_lbb', 'repetitions_lbb', 'max_weight_lbb', 'min_weight_lbb',]
        exclude = ('new_workout_lbb',)


class ShoulderPressForm(forms.ModelForm):

    class Meta:
        model = ShoulderPress
        fields = ['series_sp', 'repetitions_sp', 'max_weight_sp', 'min_weight_sp',]
        exclude = ('new_workout_sp',)


class SqueezingDumbellSlantingBenchForm(forms.ModelForm):

    class Meta:
        model = SqueezingDumbellSlantingBench
        fields = ['series_sdsb', 'repetitions_sdsb', 'max_weight_sdsb', 'min_weight_sdsb',]
        exclude = ('new_workout_sdsb',)


class NewWorkoutForm(forms.ModelForm):
    class Meta:
        model = NewWorkout
        fields = ['number', 'gym_name', 'gym_city', 'weight',]
