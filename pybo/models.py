from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name='author_question')
    subject = models.CharField(max_length=200)  #글자수가 제한된 텍스트는 charfield
    content =models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date=models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    
    def __str__(self):
        return self.subject
    
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey는 다른 모델과 연결을 위해 사용 , on_delete=models.CASCADE 는 이 답변과 연결된 질문이 삭제될 경우 답변도 삭제
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    create_date = models.DateTimeField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

