from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Question (models.Model):
    question = models.CharField(max_length=500, null=False, blank=False)
    op1 = models.CharField(max_length=500, null=False, blank=False)
    op2 = models.CharField(max_length=500, null=False, blank=False)
    op3 = models.CharField(max_length=500, null=False, blank=False)
    ansPosition = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], null=False, blank=False)

    def __str__(self):
        return self.question

    def getOption(self, position):
        if position == 1:
            return self.op1
        elif position == 2:
            return self.op2
        elif position == 3:
            return self.op3
        else:
            raise ValueError("Invalid Position: position can be 1, 2 or 3")

    def getAnswer(self):
        if self.ansPosition == 1:
            return self.op1
        elif self.ansPosition == 2:
            return self.op2
        elif self.ansPosition == 3:
            return self.op3

    def checkPosition(self, position):
        if position == self.ansPosition:
            return True
        elif position <= 3 and position >= 1:
            return False
        else:
            raise ValueError("Invalid Position: position can be 1, 2 or 3")
