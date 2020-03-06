from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Counting

def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "school/student_list.html", context)


def student_form(request, id=0):
    last_serial = Counting.objects.all().order_by('id').last() #get the last serial from Counting
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "school/student_form.html", {'form': form})
    else:
        #try to get the id of the request which will come back if it is in the model/db. If so, it is an edit, don't change student number
        if id == 0: #if this is true, it is an entirely new reg, serve the form
            form = StudentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                course = obj.course.title
                print("Last counter before increment is {0:03}".format(last_serial.counter))
                last_serial.counter 
                serial_no = last_serial.counter #make the serial number the last from record which is the counter field of the object serial_no
                new_serial_int = serial_no + 1
                student_no = course[:3] + '-' + "{0:03}".format(new_serial_int) #With the first three letters of course, concat a {0:03} format of the number
                last_serial.counter += 1
                last_serial.save()
                obj.student_no = student_no
                print("Counter after increment is {0:03}".format(last_serial.counter))
                obj.save()
        #else try to retrieve the user info as it is a returning user
        else:
            #try:
            print('trying to retrieve user')
            editor = Student.objects.get(pk=id)
            studnet_no = editor.student_no
            print(editor.student_no, studnet_no)
            #if we are here, it is an edit, get their detials by their id then serve the form with an isntance of it to edit
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance= student)
            #save the contents of the return form if valid
            if form.is_valid():
                obj = form.save(commit=False)
                hello = editor.student_no
                print("I am here", hello)
                obj.student_no = hello
                obj.save()
        return redirect('student_list')


def student_delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/list')