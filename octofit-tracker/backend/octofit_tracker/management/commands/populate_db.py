from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', username='IronMan', team=marvel),
            User(email='captain@marvel.com', username='CaptainAmerica', team=marvel),
            User(email='batman@dc.com', username='Batman', team=dc),
            User(email='wonderwoman@dc.com', username='WonderWoman', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-12-19')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-12-18')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-12-17')
        Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2025-12-16')

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength workout')
        workout2 = Workout.objects.create(name='Agility Training', description='Agility workout')
        workout1.suggested_for.add(marvel, dc)
        workout2.suggested_for.add(marvel, dc)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
