from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Red', members=[str(user1._id), str(user2._id)])
        team2 = Team.objects.create(name='Team Blue', members=[str(user3._id)])

        # Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout2 = Workout.objects.create(name='Running', description='Run 1 mile')

        # Activities
        Activity.objects.create(user=user1, activity_type='Pushups', duration=10)
        Activity.objects.create(user=user2, activity_type='Running', duration=20)
        Activity.objects.create(user=user3, activity_type='Pushups', duration=15)

        # Leaderboard
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=80)
        Leaderboard.objects.create(user=user3, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
