from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(db_column='_id', primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    team_id = models.CharField(max_length=24, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(db_column='_id', primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
        
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(db_column='_id', primary_key=True)
    user_id = models.CharField(max_length=24)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
        
    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(db_column='_id', primary_key=True)
    user_id = models.CharField(max_length=24)
    team_id = models.CharField(max_length=24)
    total_calories = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        
    def __str__(self):
        return f"Rank {self.rank} - {self.total_calories} calories"


class Workout(models.Model):
    _id = models.ObjectIdField(db_column='_id', primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    exercise_type = models.CharField(max_length=50)
    difficulty_level = models.CharField(max_length=20)
    estimated_duration = models.IntegerField()  # in minutes
    estimated_calories = models.IntegerField()
    
    class Meta:
        db_table = 'workouts'
        
    def __str__(self):
        return f"{self.name} ({self.difficulty_level})"
