from django.shortcuts import render,redirect,get_object_or_404
from .models import Subtopic,Subject,Topic,Student
from .forms import SubjectForm,StudentForm

def index(request):
    num_subject = Subject.objects.all().count()
    num_topic= Topic.objects.all().count()
    num_subtopic =Subtopic.objects.all().count()

    name_subject= Subject.objects.all()
    subject_name= name_subject[1].id
    all_topics= Topic.objects.all()
    return render(
        request,
        'index.html',
        context={'num_topics': num_topic,'num_subject':num_subject,'num_subtopics':num_subtopic,
                 'name_subject':subject_name,'topics':all_topics,'subject':name_subject},
    )


def subject_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('subject_detail')
    else:
        form = SubjectForm()
    return render(request, 'subject_edit.html', {'form': form})

def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', id=student.student_id)
    else:
        form = StudentForm()
    return render(request, 'student_edit.html', {'form': form})

def student_detail(request,id):


    student = Student.objects.get(student_id=id)

    return render(
        request,
        'Student_details.html',
        context={'student': student,}
    )
def subjects_display (request):
    num_subject = Subject.objects.all().count()
    num_topic= Topic.objects.all().count()
    num_subtopic =Subtopic.objects.all().count()

    name_subject= Subject.objects.all()
    subject_name= name_subject[1].id
    all_topics= Topic.objects.all()
    return render(
        request,
        'subjects_display.html',
        context={'num_topics': num_topic,'num_subject':num_subject,'num_subtopics':num_subtopic,
                 'name_subject':subject_name,'topics':all_topics,'subject':name_subject},
    )
def Student_subject(request, id):
    student= get_object_or_404(Student,pk=id)
    student_subject= list()
    student_subject.append(get_object_or_404(Subject, subject_name=student.subject1))
    student_subject.append(get_object_or_404(Subject, subject_name=student.subject2))
    student_subject.append(get_object_or_404(Subject, subject_name=student.subject3))

    return render(
        request,
        'student_record.html',
        context={'student':student,'student_subject':student_subject}
    )