from celery.decorators import task
from quiz.models import Quiz
import json


@task(name="download_contents")
def download_contents(req):
    quiz_list = Quiz.objects.filter(
        author=req['user']).select_related('author')

    if req['method'] == 'GET':
        data = {}
        if quiz_list.count() != 0:
            data['quizzes'] = []
            for quiz in quiz_list:
                per_quiz_data = {'id': quiz.id, 'title': quiz.title,
                                 'description': quiz.description, 'questions': []}

                ques_list = quiz.question_set.all()
                for ques in ques_list:
                    per_question_data = {'id': ques.id,
                                         'title': ques.title, 'options': []}

                    option_list = ques.option_set.all()
                    for option in option_list:
                        per_option_data = {
                            'title': option.title, 'is_correct': option.correctness}

                        per_question_data['options'].append(per_option_data)
                    per_quiz_data['questions'].append(per_question_data)
                data['quizzes'].append(per_quiz_data)

    formatted_json_data = json.dumps(data, indent=3)
    return formatted_json_data
