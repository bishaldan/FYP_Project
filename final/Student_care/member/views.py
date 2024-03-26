from django.http import JsonResponse
from nltk.stem import WordNetLemmatizer
import nltk
import pickle
import numpy as np
from tensorflow.keras.models import load_model
import json
import random
import io
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.db.models import Count
from django.utils import timezone
from .forms import AnnouncementForm  # You need to define this form
from .models import Announcement
from .models import Teacher, Student
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages  # Import messages module
from django.contrib import messages
from datetime import datetime
from .forms import AnnouncementForm
from django.http import HttpResponse


from django.shortcuts import render, redirect, get_object_or_404

from .forms import FeeStatusCheckForm
from .models import Student

import matplotlib.pyplot as plt
# Create your views here.


def index(request):
    return render(request,  'member/index.html')


# views.py


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user is a student
        student = Student.objects.filter(
            email=email, password=password).first()
        if student:
            # Redirect to student dashboard
            return redirect('student_dashboard')

        # Check if the user is a teacher
        teacher = Teacher.objects.filter(
            email=email, password=password).first()
        if teacher:
            # Redirect to teacher dashboard
            return redirect('teacher_dashboard')

        # Authentication failed
        return render(request, 'member/login.html', {'error': 'Invalid credentials'})

    return render(request, 'member/login.html')


def student_dashboard(request):
    return render(request, 'member/student.html')


def teacher_dashboard(request):
    # Set Matplotlib to use non-interactive backend
    import matplotlib
    matplotlib.use('Agg')

    # Get data for analysis
    joining_year_counts = Student.objects.values(
        'joining_year').annotate(count=Count('id'))
    subject_counts = Student.objects.values(
        'field_of_study').annotate(count=Count('id'))

    # Prepare data for plotting
    years = [entry['joining_year'] for entry in joining_year_counts]
    counts = [entry['count'] for entry in joining_year_counts]

    subjects = [entry['field_of_study'] for entry in subject_counts]
    subject_counts = [entry['count'] for entry in subject_counts]

    # Create Matplotlib bar graph for joining years
    plt.figure(figsize=(10, 5))
    plt.bar(years, counts)
    plt.xlabel('Joining Year')
    plt.ylabel('Number of Students')
    plt.title('Number of Students by Joining Year')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout to prevent overlap of labels

    # Save the joining year plot to a file
    joining_year_plot_file = r'C:\Users\Mr Bishal\OneDrive\FYP_project\Chatbot\final\Student_care\member\static\joining_year_plot.png'
    plt.savefig(joining_year_plot_file)
    plt.close()

    # Create Matplotlib pie chart for subjects
    plt.figure(figsize=(8, 8))
    plt.pie(subject_counts, labels=subjects, autopct='%1.1f%%', startangle=140)
    plt.title('Number of Students by Subject')
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')

    # Save the subject pie chart to a file
    subject_plot_file = r'C:\Users\Mr Bishal\OneDrive\FYP_project\Chatbot\final\Student_care\member\static\subject_plot.png'
    plt.savefig(subject_plot_file)
    plt.close()

    # Construct the URLs for the plot files
    # Assuming your STATIC_URL is '/static/'
    joining_year_plot_url = '/static/joining_year_plot.png'
    # Assuming your STATIC_URL is '/static/'
    subject_plot_url = '/static/subject_plot.png'

    return render(request, 'member/teacher_dashboard.html', {'joining_year_plot_url': joining_year_plot_url, 'subject_plot_url': subject_plot_url})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            # Get the name of the student that was added
            student_name = f'{student.first_name} {student.last_name}'
            # Add success message with the student's name
            messages.success(request, f'{student_name} added successfully')
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'member/add_student.html', {'form': form})


def announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.date = timezone.now()
            announcement.save()
            messages.success(request, 'Announcement posted successfully.')
            return redirect('announcement')
        else:
            messages.error(
                request, 'Form is not valid. Please correct the errors.')
    else:
        form = AnnouncementForm()
    announcements = Announcement.objects.order_by(
        '-date')[:5]  # Fetch latest 5 announcements
    return render(request, 'member/announcement.html', {'form': form, 'announcements': announcements})


def get_announcement(request):
    # # Logic to fetch announcements from the database
    # # Example query, adjust as per your model
    announcements = Announcement.objects.all()

    return render(request, 'member/get_announcement.html', {'announcements': announcements})


def announcement_student(request):
    announcements = Announcement.objects.all()
    return render(request,  'member/announcement_student.html', {'announcements': announcements})


def fee_status(request):
    if request.method == 'POST':
        form = FeeStatusCheckForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(email=email, password=password)
                fee_status = student.fee  # Assuming 'fee_status' is a field in the Student model
                return render(request, 'member/fee_status.html', {'student': student, 'fee_status': fee_status})
            except Student.DoesNotExist:
                error_message = "No student found with this email and password."
                return render(request, 'member/fee_status.html', {'form': form, 'error_message': error_message})
    else:
        form = FeeStatusCheckForm()
    return render(request, 'member/fee_status.html', {'form': form})


def payment_page(request):
    # Add your logic for the payment page view here
    return render(request, 'payment_page.html')


def edit_student(request, email):
    student = get_object_or_404(Student, email=email)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', email=email)
    else:
        form = StudentForm(instance=student)
    return render(request, 'member/edit_studnt.html', {'student': student, 'form': form})


# Chatbot

lemmatizer = WordNetLemmatizer()

THRESHOLD = 0.25
model = load_model(
    r'C:\Users\Mr Bishal\OneDrive\Chatbot\new chatbot\sav\models\chatbot_model.h5')
intents = json.loads(
    open(r'C:\Users\Mr Bishal\OneDrive\Chatbot\new chatbot\intents.json').read())
words = pickle.load(
    open(r'C:\Users\Mr Bishal\OneDrive\Chatbot\new chatbot\pickles\words.pkl', 'rb'))
classes = pickle.load(open(
    r'C:\Users\Mr Bishal\OneDrive\Chatbot\new chatbot\pickles\classes.pkl', 'rb'))

print('RESOURCES LOADED SUCESSFULLY!')

# applying lemmmatization


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(
        word.lower()) for word in sentence_words]
    return sentence_words

# creating bag_of_words


def bag_of_words(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"found in bag: {w}")
    return (np.array(bag))


def predict_class(sentence, model):
    p = bag_of_words(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    results = [[i, r] for i, r in enumerate(res) if r > THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({
            "intent": classes[r[0]],
            "probability": str(r[1])}
        )
    return return_list


def get_responses(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response(request):
    if request.method == 'GET':
        message = request.GET.get('msg', '')
        ints = predict_class(message, model)
        res = get_responses(ints, intents)
        return JsonResponse({'response': res})


def home(request):
    return render(request, 'member/chatbot.html')
