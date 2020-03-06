from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fullname','student_no','course','score', 'grade')
        labels = {
            'fullname':'Full Name',
            'course':'Course',
            'grade':'Grade'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        #self.fields['position'].empty_label = "Select"
        self.fields['student_no'].required = False