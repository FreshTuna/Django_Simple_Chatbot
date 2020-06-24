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
from django.shortcuts import render, redirect
from .serializers import QuestionSerializer
from django.http import HttpResponse
from .models import Question
from rest_framework import generics

class QuestionAPI(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



def get_q(request):
    qs = Question.objects.all()

    for row in qs.values_list():
        print(row[1])
    return redirect('/')