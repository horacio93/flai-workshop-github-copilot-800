from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            password='testpassword123'
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertIsNotNone(self.user._id)


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')
        self.assertIsNotNone(self.team._id)


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='507f1f77bcf86cd799439011',
            activity_type='Running',
            duration=30,
            calories_burned=300,
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 300)


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id='507f1f77bcf86cd799439011',
            team_id='507f1f77bcf86cd799439012',
            total_calories=1000,
            total_activities=5,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.total_calories, 1000)
        self.assertEqual(self.leaderboard.total_activities, 5)
        self.assertEqual(self.leaderboard.rank, 1)


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Morning Run',
            description='A refreshing morning run',
            exercise_type='Cardio',
            difficulty_level='Medium',
            estimated_duration=45,
            estimated_calories=400
        )
    
    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Morning Run')
        self.assertEqual(self.workout.difficulty_level, 'Medium')
        self.assertEqual(self.workout.estimated_duration, 45)


class UserAPITest(APITestCase):
    def test_create_user(self):
        url = '/api/users/'
        data = {
            'name': 'API Test User',
            'email': 'apitest@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Test User')


class TeamAPITest(APITestCase):
    def test_create_team(self):
        url = '/api/teams/'
        data = {
            'name': 'API Test Team',
            'description': 'Team created via API'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)


class ActivityAPITest(APITestCase):
    def test_create_activity(self):
        url = '/api/activities/'
        data = {
            'user_id': '507f1f77bcf86cd799439011',
            'activity_type': 'Cycling',
            'duration': 60,
            'calories_burned': 500,
            'date': datetime.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)


class WorkoutAPITest(APITestCase):
    def test_create_workout(self):
        url = '/api/workouts/'
        data = {
            'name': 'Evening Yoga',
            'description': 'Relaxing yoga session',
            'exercise_type': 'Flexibility',
            'difficulty_level': 'Easy',
            'estimated_duration': 30,
            'estimated_calories': 150
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
