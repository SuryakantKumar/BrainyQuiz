from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from quiz.models import Quiz, Question


@registry.register_document
class QuizDocument(Document):
    class Index:
        name = 'quizzes'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Quiz

        fields = [
            'title', 'id', 'description', 'average_score', 'difficulty', 'date_posted'
        ]


@registry.register_document
class QuestionDocument(Document):
    class Index:
        name = 'questions'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Question

        fields = [
            'title'
        ]
