from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
from bson import ObjectId
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            _id=ObjectId(),
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes fighting for fitness!',
        )
        
        team_dc = Team.objects.create(
            _id=ObjectId(),
            name='Team DC',
            description='Justice League members crushing their fitness goals!',
        )
        
        # Create Users - Marvel Heroes
        self.stdout.write('Creating Marvel superhero users...')
        marvel_users = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'password': 'arc_reactor_3000'},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com', 'password': 'super_soldier'},
            {'name': 'Thor Odinson', 'email': 'thor@asgard.marvel.com', 'password': 'mjolnir_worthy'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'password': 'red_room_graduate'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'password': 'gamma_radiation'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'password': 'with_great_power'},
        ]
        
        # Create Users - DC Heroes
        self.stdout.write('Creating DC superhero users...')
        dc_users = [
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'password': 'dark_knight'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'password': 'krypton_last_son'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'password': 'themyscira_princess'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'password': 'speed_force'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'password': 'atlantis_king'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'password': 'willpower_ring'},
        ]
        
        created_users = []
        
        for user_data in marvel_users:
            user = User.objects.create(
                _id=ObjectId(),
                name=user_data['name'],
                email=user_data['email'],
                password=user_data['password'],
                team_id=str(team_marvel._id),
            )
            created_users.append(user)
        
        for user_data in dc_users:
            user = User.objects.create(
                _id=ObjectId(),
                name=user_data['name'],
                email=user_data['email'],
                password=user_data['password'],
                team_id=str(team_dc._id),
            )
            created_users.append(user)
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'HIIT']
        
        for user in created_users:
            # Create 5-10 activities per user
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = duration * random.randint(5, 12)
                days_ago = random.randint(1, 30)
                
                Activity.objects.create(
                    _id=ObjectId(),
                    user_id=str(user._id),
                    activity_type=activity_type,
                    duration=duration,
                    calories_burned=calories,
                    date=datetime.now() - timedelta(days=days_ago),
                    notes=f'{activity_type} session for hero training',
                )
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in created_users:
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_calories = sum(activity.calories_burned for activity in user_activities)
            total_activities_count = user_activities.count()
            
            Leaderboard.objects.create(
                _id=ObjectId(),
                user_id=str(user._id),
                team_id=user.team_id,
                total_calories=total_calories,
                total_activities=total_activities_count,
                rank=0,  # Will be updated based on sorting
            )
        
        # Update ranks based on total calories
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for idx, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = idx
            entry.save()
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Spider-Man Agility Training',
                'description': 'Web-slinging inspired agility workout focusing on flexibility and quick reflexes',
                'exercise_type': 'Agility',
                'difficulty_level': 'Intermediate',
                'estimated_duration': 30,
                'estimated_calories': 250,
            },
            {
                'name': 'Hulk Strength Builder',
                'description': 'Gamma-powered strength training for maximum muscle gains',
                'exercise_type': 'Strength',
                'difficulty_level': 'Advanced',
                'estimated_duration': 60,
                'estimated_calories': 500,
            },
            {
                'name': 'Flash Speed Circuit',
                'description': 'Speed Force inspired HIIT workout for maximum cardio',
                'exercise_type': 'Cardio',
                'difficulty_level': 'Advanced',
                'estimated_duration': 45,
                'estimated_calories': 600,
            },
            {
                'name': 'Wonder Woman Warrior Workout',
                'description': 'Amazonian warrior training combining strength and endurance',
                'exercise_type': 'Full Body',
                'difficulty_level': 'Intermediate',
                'estimated_duration': 50,
                'estimated_calories': 450,
            },
            {
                'name': 'Batman Dark Knight Training',
                'description': 'Gotham\'s finest combat and conditioning routine',
                'exercise_type': 'Mixed Martial Arts',
                'difficulty_level': 'Advanced',
                'estimated_duration': 75,
                'estimated_calories': 650,
            },
            {
                'name': 'Captain America Super Soldier',
                'description': 'Classic military-style calisthenics and endurance training',
                'exercise_type': 'Calisthenics',
                'difficulty_level': 'Intermediate',
                'estimated_duration': 40,
                'estimated_calories': 350,
            },
            {
                'name': 'Thor Asgardian Hammer Time',
                'description': 'Worthy workout combining functional movements with power training',
                'exercise_type': 'Functional Fitness',
                'difficulty_level': 'Advanced',
                'estimated_duration': 55,
                'estimated_calories': 500,
            },
            {
                'name': 'Aquaman Ocean Endurance',
                'description': 'Swimming and water-based resistance training',
                'exercise_type': 'Swimming',
                'difficulty_level': 'Beginner',
                'estimated_duration': 35,
                'estimated_calories': 300,
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(
                _id=ObjectId(),
                **workout_data
            )
        
        # Create unique index on email field
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        try:
            db.users.create_index([('email', 1)], unique=True)
            self.stdout.write(self.style.SUCCESS('Created unique index on email field'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Index might already exist: {e}'))
        
        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams created: {Team.objects.count()}')
        self.stdout.write(f'Users created: {User.objects.count()}')
        self.stdout.write(f'Activities created: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('\nSuperhero fitness challenge is ready!'))
