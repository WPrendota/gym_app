import matplotlib
from django.db.models import AutoField

matplotlib.use('Agg')
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import NewWorkout, Treadmill, LatMachine, ChestPress, ChestFly, CrossTrainer, LowerBackBench, \
	ShoulderPress, SqueezingDumbellSlantingBench

from .forms import TreadmillForm, NewWorkoutForm, LatMachineForm, ChestPressForm, ChestFlyForm, CrossTrainerForm, \
	LowerBackBenchForm, ShoulderPressForm, SqueezingDumbellSlantingBenchForm

import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from pylab import *


def gym_app_done(request):
	context = {"done_page": "active"}
	return render(request, 'gym_app/gym_app_done.html', context)


def is_data_empty(data_input):
	return True if not data_input else False


# Graph creation function:
def graph_creator(x, y, y_means, y_std, y_labels):
	if is_data_empty(x):
		return "Data is empty"
	else:
		buf = BytesIO()

		plt.figure()
		for number, y_data in enumerate(y):
			plt.subplot(len(y_labels), 1, number + 1)
			plt.errorbar(x, y[y_data], yerr=expand_means_range(y_std[number], len(x)), fmt='.k')  # Adding errorbars
			plt.plot(x, expand_means_range(y_means[number], len(x)))  # Adding mean value

			plt.autoscale(enable=True, axis='both', tight=None)
			plt.ylabel(y_labels[number], fontsize=6)
			cur_axes = plt.gca()
			cur_axes.axes.get_xaxis().set_ticks([])

		plt.xlabel("Number of workout")
		xint = range(int(min(x)), int(math.ceil(max(x))) + 1)
		plt.xticks(xint)
		plt.savefig(buf, format='png', dpi=200)
		treadmill_image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
		buf.close()
		return treadmill_image_base64


# Function for expanding means range to fit number of workouts (xrange)
def expand_means_range(mean, max_range):
	means = []

	for number in range(0, max_range):
		means.append(mean)
	return means


# Means calculation:
def gym_app_mean(parameters):
	means = []

	for parameter in parameters.values():
		means.append(np.mean(parameter))
	return means


# Std calculation:
def gym_app_std(parameters):
	std = []

	for parameter in parameters.values():
		std.append(np.std(parameter))
	return std


# Get the list of objects fields
def get_object_fields(object):
	field_list = []

	for field in object._meta.get_fields():
		field_list.append(str(field))

	return field_list


def create_machine_container(querysets):
	machine_container = {}

	for queryset in querysets:
		for machine_object in queryset:
			for number, field in enumerate(machine_object.__dict__.items()):
				if '_id' in field[0]:
					pass
				elif number > 1:
					machine_container.update({field[0]: []})

	return machine_container


def fill_gym_machine_container(querysets, machine_container):
	counter = 0
	x_range = []

	for queryset in querysets:
		for machine_object in queryset:
			for number, field in enumerate(machine_object.__dict__.items()):
				if '_id' in field[0]:
					x_range.append(field[1])
				elif number > 1:
					machine_container[field[0]].append(field[1])

	y_range = machine_container

	return (x_range, y_range)


def generate_graph_with_statistics(filtered_data_container, y_scale_label):

	machine_container = create_machine_container(filtered_data_container)

	filled_machine_container = fill_gym_machine_container(filtered_data_container, machine_container)

	# Generate graph image:
	graph_image_base64 = graph_creator(filled_machine_container[0], filled_machine_container[1],
									   gym_app_mean(filled_machine_container[1]),
									   gym_app_std(filled_machine_container[1]), y_scale_label)

	return graph_image_base64


@login_required
def gym_app_stats(request):

	# General information about workouts:
	# Filtering data by users workouts:
	new_workout = NewWorkout.objects.filter(user=request.user)

	# Workouts numbers:
	workouts_numbers = []

	for new_workout_object in new_workout:
		workouts_numbers.append(new_workout_object.number)

	# Total number of workouts:
	number_of_workouts = len(new_workout)

	# First workout date:
	if new_workout.first() is not None:
		first_workout_date = new_workout.first().date
	else:
		first_workout_date = "None"

	# -----------------------------------------------------------------------------------
	# Gym Machines Statistics:

	# Graph labels types:
	ylabels_treadmill = ['Time [min]', 'Speed [km/h]', 'Slope [%]', 'Calories [kCal]', 'Distance [km]']
	ylabels_many = ['Series', 'Repetitions', 'Max weight [kg]', 'Min weight [kg]']
	ylabels_cross_trainer = ['Time [min]', 'Power [W]', 'Slip [slip/min]', 'Calories [kCal]', 'Distance [km]']

	gym_machine_images_base64 = {}

	machines_graph_labels = [('Treadmill', ylabels_treadmill),
					   ('LatMachine', ylabels_many),
					   ('ChestPress', ylabels_many), ('ChestFly', ylabels_many),
					   ('CrossTrainer', ylabels_cross_trainer),
					   ('LowerBackBench', ylabels_many),
					   ('ShoulderPress', ylabels_many), ('sdsb', ylabels_many),
					   ('ShoulderPress', ylabels_many)
					   ]

	# Filtered data container
	filtered_data_container = {"Treadmill": [], "LatMachine": [], "CrossTrainer": [],
							   'ChestPress': [], 'ChestFly': [], "ShoulderPress": [],
							   'LowerBackBench': [], 'sdsb': []
							}

	# Filter gym machine data by workouts numbers:
	for workout_number in workouts_numbers:
		filtered_data_container['Treadmill'].append(Treadmill.objects.filter(new_workout_tm=workout_number))
		filtered_data_container['LatMachine'].append(LatMachine.objects.filter(new_workout_lm=workout_number))
		filtered_data_container['ChestPress'].append(ChestPress.objects.filter(new_workout_cp=workout_number))
		filtered_data_container['ChestFly'].append(ChestFly.objects.filter(new_workout_cf=workout_number))
		filtered_data_container['CrossTrainer'].append(CrossTrainer.objects.filter(new_workout_ct=workout_number))
		filtered_data_container['LowerBackBench'].append(LowerBackBench.objects.filter(new_workout_lbb=workout_number))
		filtered_data_container['sdsb'].append(SqueezingDumbellSlantingBench.objects.filter(
			new_workout_sdsb=workout_number))
		filtered_data_container['ShoulderPress'].append(ShoulderPress.objects.filter(new_workout_sp=workout_number))

	# Generating graphs for each gym machine based on filtered data, their mean values and labels:
	for graph_label in machines_graph_labels:
		gym_machine_images_base64.update(
			{graph_label[0]: generate_graph_with_statistics(filtered_data_container[graph_label[0]], graph_label[1])})
	# -----------------------------------------------------------------------------------

	context = {"number_of_workouts": number_of_workouts,
			   "first_workout_date": first_workout_date,
			   "workouts_numbers": workouts_numbers,
			   "treadmill_image_base64":gym_machine_images_base64['Treadmill'],
			   "latmachine_image_base64": gym_machine_images_base64['LatMachine'],
			   "chest_press_image_base64": gym_machine_images_base64['ChestPress'],
			   "chest_fly_image_base64": gym_machine_images_base64['ChestFly'],
			   "cross_trainer_image_base64": gym_machine_images_base64['CrossTrainer'],
			   "lower_back_bench_image_base64": gym_machine_images_base64['LowerBackBench'],
			   "sdsb_image_base64": gym_machine_images_base64['sdsb'],
			   "shoulder_press_image_base64": gym_machine_images_base64['ShoulderPress'],
				}
	return render(request, 'gym_app/workout_stats.html', context)


@login_required
def new_workout(request):
	if request.POST:
		new_workout_f = NewWorkoutForm(request.POST)
		treadmill_f = TreadmillForm(request.POST)
		latmachine_f = LatMachineForm(request.POST)
		chest_press_f = ChestPressForm(request.POST)
		chest_fly_f = ChestFlyForm(request.POST)
		cross_trainer_f = CrossTrainerForm(request.POST)
		lower_back_bench_f = LowerBackBenchForm(request.POST)
		shoulder_press_f = ShoulderPressForm(request.POST)
		squeezing_dumbell_slanting_bench_f = SqueezingDumbellSlantingBenchForm(request.POST)

		if new_workout_f.is_valid() and treadmill_f.is_valid() and latmachine_f.is_valid() and chest_press_f.is_valid() \
				and chest_fly_f.is_valid() and cross_trainer_f.is_valid() and lower_back_bench_f.is_valid() \
				and shoulder_press_f.is_valid() and squeezing_dumbell_slanting_bench_f.is_valid():
			new_workout_ = new_workout_f.save(commit=False)
			new_workout_.user = request.user
			new_workout_.save()

			treadmill = treadmill_f.save(commit=False)
			treadmill.new_workout_tm = new_workout_

			treadmill.save()

			latmachine = latmachine_f.save(commit=False)
			latmachine.new_workout_lm = new_workout_
			latmachine.save()

			chest_press = chest_press_f.save(commit=False)
			chest_press.new_workout_cp = new_workout_
			chest_press.save()

			chest_fly = chest_fly_f.save(commit=False)
			chest_fly.new_workout_cf = new_workout_
			chest_fly.save()

			cross_trainer = cross_trainer_f.save(commit=False)
			cross_trainer.new_workout_ct = new_workout_
			cross_trainer.save()

			lower_back_bench = lower_back_bench_f.save(commit=False)
			lower_back_bench.new_workout_lbb = new_workout_
			lower_back_bench.save()

			shoulder_press = shoulder_press_f.save(commit=False)
			shoulder_press.new_workout_sp = new_workout_
			shoulder_press.save()

			squeezing_dumbell_slanting_bench = squeezing_dumbell_slanting_bench_f.save(commit=False)
			squeezing_dumbell_slanting_bench.new_workout_sdsb = new_workout_
			squeezing_dumbell_slanting_bench.save()

			messages.success(request, "Added new workout!")
			return redirect('gym_app')
	else:
		new_workout_f = NewWorkoutForm()
		treadmill_f = TreadmillForm()
		latmachine_f = LatMachineForm()
		chest_press_f = ChestPressForm()
		chest_fly_f = ChestFlyForm()
		cross_trainer_f = CrossTrainerForm()
		lower_back_bench_f = LowerBackBenchForm()
		shoulder_press_f = ShoulderPressForm()
		squeezing_dumbell_slanting_bench_f = SqueezingDumbellSlantingBenchForm()

	content = {'new_workout_f': new_workout_f, 'treadmill_f': treadmill_f,
			   'latmachine_f': latmachine_f,
			   'chest_press_f': chest_press_f,
			   'chest_fly_f': chest_fly_f,
			   'cross_trainer_f': cross_trainer_f,
			   'lower_back_bench_f': lower_back_bench_f,
			   'shoulder_press_f': shoulder_press_f,
			   'squeezing_dumbell_slanting_bench_f': squeezing_dumbell_slanting_bench_f,
			   }
	return render(request, 'gym_app/new_workout.html', content)


@login_required
def gym_app(request):
	context = {"new_workout_page": "active"}
	return render(request, 'gym_app/gym_app.html', context)
