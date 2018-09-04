# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    question=models.TextField(max_length=500)
    option1=models.CharField(max_length=20)
    option2=models.CharField(max_length=20)
    option3=models.CharField(max_length=20)
    option4=models.CharField(max_length=20)
    answer=models.CharField(max_length=20)


    def __str__(self):
    	return self.question


class Result(models.Model):
	score_count=models.IntegerField(null=True)
	wrong_count=models.IntegerField(null=True)
	unattempt=models.IntegerField(null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)


	def __str__(self):
		return "Results of " + str(self.user) + "    and   Student ID : " + str(self.pk)
