from django.db import models

class QuizAttempt(models.Model):
    # User's Name
    user_name = models.CharField(
        max_length=100,
        verbose_name="Your Name"
    )

    # Answer to Question 1 (Midpoint 2D)
    answer_1 = models.CharField(
        max_length=255,
        verbose_name="Answer to Q1: Midpoint Coordinates (x, y)"
    )

    # Answer to Question 2 (Distance 2D)
    answer_2 = models.CharField(
        max_length=255,
        verbose_name="Answer to Q2: Distance"
    )

    # Answer to Question 3 (Distance Squared 3D)
    answer_3 = models.CharField(
        max_length=255,
        verbose_name="Answer to Q3: Distance Squared"
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Attempt by {self.user_name} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"