from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(email='ironman@marvel.com', username='IronMan', team=self.team)
        self.workout = Workout.objects.create(name='Super Strength', description='Strength workout')
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-12-19')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user(self):
        self.assertEqual(self.user.email, 'ironman@marvel.com')

    def test_team(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Super Strength')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
