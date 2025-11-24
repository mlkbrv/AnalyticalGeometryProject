from django.shortcuts import render, redirect
from .forms import QuizForm
from .models import QuizAttempt

def quiz_view(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = QuizForm()

    context = {
        'form': form,
        # --- NEW QUESTIONS TEXT ---
        'question_1_math': r'Find the **midpoint** of the segment connecting points $A=(3, 9)$ and $B=(7, 1)$.',
        'question_2_math': r'What is the **distance** between points $P=(0, -4)$ and $Q=(3, 0)$?',
        'question_3_math': r'Find the **square of the distance** (i.e., $d^2$) between points $R=(1, 2, 3)$ and $S=(4, 2, 0)$.',
    }
    return render(request, 'core/quiz.html', context)

def success_view(request):
    return render(request, 'core/success.html')