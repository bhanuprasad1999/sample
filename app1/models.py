from django.db import models

# Create your models here.
    
    
class CodeFormater(models.Model):
    code = models.TextField()
    
    
class CodeExecuter(models.Model):
    code_formater = models.ForeignKey(CodeFormater, on_delete=models.CASCADE)
    input_for_code = models.TextField()
    output_for_code = models.TextField()
    
    

class TestCases(models.Model):
    code_formater= models.ForeignKey(CodeFormater, on_delete=models.CASCADE)
    test_case = models.TextField(blank=False)