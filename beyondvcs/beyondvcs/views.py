from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from commitwaitlist.models import Profile
from django.utils import timezone


def waiting_list(request):
	users = User.objects.filter(profile__is_waiting=True).order_by('profile__date_since_waiting').select_related(
		'profile')
	current_working_user = User.objects.filter(profile__allowed_to_commit=True)
	if current_working_user:
		current_working_user = current_working_user[0]

	return render(request, 'waitingList.html',
				  {'waiting_list_users': users, 'current_working_user': current_working_user})


def set_waiting(request):
	user = request.user
	profile = user.profile
	current_working_user = User.objects.filter(profile__allowed_to_commit=True)
	waiting_users = User.objects.filter(profile__is_waiting=True)
	if current_working_user:
		if current_working_user[0] != user:
			if current_working_user:
				if user not in waiting_users:
					profile.is_waiting = True
					profile.date_since_waiting = timezone.now()
					Profile.save(profile)
	else:
		profile.allowed_to_commit = True
		profile.date_since_commiting = timezone.now()
		Profile.save(profile)

	return waiting_list(request)


def set_not_waiting(request):
	profile = request.user.profile
	profile.is_waiting = False
	profile.date_since_waiting = None
	Profile.save(profile)

	return waiting_list(request)


def finished(request):
	profile = request.user.profile
	profile.allowed_to_commit = False
	profile.date_since_commiting = None
	Profile.save(profile)

	users_waiting = User.objects.filter(profile__is_waiting=True).order_by(
		'profile__date_since_waiting').select_related('profile')
	if users_waiting:
		profile_to_commit = users_waiting[0].profile
		profile_to_commit.allowed_to_commit = True
		profile_to_commit.is_waiting = False
		profile_to_commit.date_since_waiting = None
		profile_to_commit.date_since_commiting = timezone.now()
		Profile.save(profile_to_commit)

	return waiting_list(request)
