import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'task_manager.settings')
django.setup()

import random
from django.utils import timezone
from tasks.models import Task

def generate_dummy_data(num_entries=50):
    task_titles = [
        "Buy groceries",
        "Finish project report",
        "Attend team meeting",
        "Pay bills",
        "Clean the house",
        "Go for a run",
        "Read a book",
        "Fix the car",
        "Prepare dinner",
        "Call a friend",
        "Study for exams",
        "Visit the doctor",
        "Watch a movie",
        "Start a new hobby",
        "Plan a trip",
        "Complete online course",
        "Organize the closet",
        "Write a blog post",
        "Volunteer for a cause",
        "Update resume",
        "Paint a picture",
        "Solve puzzles",
        "Learn a new language",
        "Create a budget",
        "Play a musical instrument",
        "Practice meditation",
        "Write a poem",
        "Explore a new city",
        "Attend a workshop",
        "Take photographs",
        "Try a new recipe",
        "Visit a museum",
        "Participate in a webinar",
        "Do gardening",
        "Design a website",
        "Go camping",
        "Take a yoga class",
        "Create a playlist",
        "Learn to code",
        "Attend a concert",
        "Do DIY projects",
        "Host a game night",
        "Try a new sport",
        "Listen to a podcast",
        "Create a vision board",
        "Watch a TED talk",
        "Go to the beach",
        "Attend a networking event",
    ]

    task_descriptions = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Pellentesque posuere elit sit amet ipsum luctus tincidunt.",
        "Vivamus venenatis sapien id mi placerat, vel varius neque bibendum.",
        "Nulla facilisi. Etiam euismod dui in est consectetur, a eleifend dolor vestibulum.",
        "Sed tempus ligula a neque eleifend, non tincidunt mi laoreet.",
        "In vel risus cursus, aliquam nisl eu, dictum nulla.",
        "Donec eu tortor vel tellus eleifend aliquam.",
        "Cras elementum purus ac orci faucibus euismod.",
    ]

    priority_choices = ['low', 'medium', 'high']

    for _ in range(num_entries):
        title = random.choice(task_titles)
        description = random.choice(task_descriptions)
        created_at = timezone.now() - timezone.timedelta(days=random.randint(0, 365))
        updated_at = created_at + \
            timezone.timedelta(days=random.randint(0, 30))
        # due_date = created_at + timezone.timedelta(days=random.randint(1, 30))
        is_completed = random.choice([True, False])
        priority = random.choice(priority_choices)

        Task.objects.create(
            title=title,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            # due_date=due_date,
            is_completed=is_completed,
            priority=priority,
        )


if __name__ == "__main__":
    generate_dummy_data()
