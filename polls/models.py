# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="질")
    answer = models.CharField(max_length=100, verbose_name="답")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'questions' # 테이블명 지정
        verbose_name = 'Qs'
        verbose_name_plural='Qs'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Create your models here.
