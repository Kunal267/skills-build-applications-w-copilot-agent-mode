"""
Script to populate the octofit_db database with test data for users, teams, activities, leaderboard, and workouts.
Run this script after migrations.
"""

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

def run():
	# Clear existing data
	Leaderboard.objects.all().delete()
	Activity.objects.all().delete()
	Workout.objects.all().delete()
	User.objects.all().delete()
	Team.objects.all().delete()

	# Teams
	marvel = Team.objects.create(name='marvel', description='Marvel Team')
	dc = Team.objects.create(name='dc', description='DC Team')

	# Users
	ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True)
	captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True)
	batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True)
	superman = User.objects.create(email='superman@dc.com', name='Superman', team='dc', is_superhero=True)

	# Workouts
	pushups = Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='marvel')
	squats = Workout.objects.create(name='Squats', description='Lower body strength', suggested_for='dc')

	# Activities
	Activity.objects.create(user=ironman, type='run', duration=30, date='2024-01-01')
	Activity.objects.create(user=batman, type='cycle', duration=45, date='2024-01-02')
	Activity.objects.create(user=superman, type='swim', duration=60, date='2024-01-03')
	Activity.objects.create(user=captain, type='yoga', duration=20, date='2024-01-04')

	# Leaderboard
	Leaderboard.objects.create(user=ironman, points=120, rank=1)
	Leaderboard.objects.create(user=batman, points=110, rank=2)
	Leaderboard.objects.create(user=superman, points=100, rank=3)
	Leaderboard.objects.create(user=captain, points=90, rank=4)

	print('Test data populated successfully!')
