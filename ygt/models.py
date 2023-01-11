from django.db import models
from django.contrib.auth.models import User

# Messageクラス
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
        related_name='message_owner')
    content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'

        class Meta:
            ordering = ('-pub_date',)

# Examクラス
class Exam(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
        related_name='exam_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    certification = models.CharField(max_length=30)
    exam_date = models.DateField()
    book_tool_1 = models.CharField(max_length=30)
    book_tool_2 = models.CharField(max_length=30)
    book_tool_3 = models.CharField(max_length=30)
    schedule = models.TextField(max_length=1000)

# Goodクラス
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
        related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.exam) + '" (by ' + \
            str(self.owner) + ')'