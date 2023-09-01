import json
import random
from django.utils import timezone
from django.contrib.auth import get_user_model
from common.models import Task
from question.models import Category

def HITE(question_lst):
    '''
    Total: 70 minutes
    Use 20 minutes to solve first question
    5 minutes break
    Use 20 minutes to solve second question
    5 minutes break
    Use 20 minutes to learn from the solution
    '''
    # Get 2 coding question base on user
    question_lst = get_recommend_question(user, 2, question_lst)
    # Build 
    step1 = Step(
        type='question', duration=20, question=question_lst[0],
        requirement=['quality', 'time_space', 'expected_length'])
    step2 = Step(type='break', duration=5)
    step3 = Step(
        type='question', duration=20, question=question_lst[1],
        requirement=['quality', 'time_space', 'expected_length'])
    step4 = Step(type='break', duration=5)
    step5 = Step(type='break', duration=20)
    task.step = [step1, step2, step3, step4, step5]
    return task


def get_practice_method(count):
    lst =['High Intensity Interval', 'Progressive Intensity', 'Breakthrough']
    random.shuffle(lst)
    return lst[:count]


def get_category_from_user(user, count):
    # TODO: Choose different category based on user
    category = Category.objects.all().order_by('?')[:count]
    return category


def get_task(ability, state, count, category):
    '''
    TODO: use ability later
    '''
    pass


def generate_daily_task_for_user():
    User = get_user_model()
    for u in User.objects.all():
        if not today_task_exist(u):
            # Generate New tasks
            create_and_save_today_task(u, 'New', 3)
            # Generate Review task
            create_and_save_today_task(u, 'Review', 1)


def generate_task(state='new', type='classic', method='HITE'):
    task = Task.objects.get(user=user.id)
    ques_lst = Submission.objects.filter(user=user.id)
    # Fliter question based on requirement
    if method == 'HITE':
        return HITE(ques_lst)
    elif method == 'PIE':
        return PIE(ques_lst)
    elif method == 'BE':
        return BE(ques_lst)


def today_task_exist(user):
    date_today = timezone.now().date()
    return Task.objects.filter(user_id=user, created_at__date=date_today).exists()


def get_today_task(user, state, count):
    date_today = timezone.now().date()
    return Task.objects.filter(user_id=user.id, state=state, created_at__date=date_today)[:count]


def create_and_save_today_task(user, state, count):
    lst = []
    category = get_category_from_user(user, count)
    method = get_practice_method(count)
    for i in range(count):
        task = Task(
            user_id=user.id, state=state,
            category=category[i], practice_method=method[i])
        task.save()
        lst.append(task)
    return lst