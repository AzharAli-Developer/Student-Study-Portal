import wikipedia
from django.shortcuts import render,redirect,get_object_or_404
from .models import Notes,Homework,Todo
from .form import stuNotes,stuHomework,studyform,todoForm,ConversionForm,\
    ConversionLengthForm,ConversionMassForm,Registeration
from youtubesearchpython import VideosSearch
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
import wikipedia




# Create your views here.
def home(request):
    return  render(request,'dash/home.html')



@login_required
def book(request):
    if request.method == 'POST':
        fm = studyform(request.POST)
        text = request.POST.get('text')  # Use .get() to avoid MultiValueDictKeyError
        url="https://www.googleapis.com/books/v1/volumes?q="+text
        r=requests.get(url)
        answer=r.json()
        result_list=[]
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink'),

            }
            result_list.append(result_dict)
        return render(request, 'dash/books.html', {'fm': fm, 'result': result_list})
    else:
        fm = studyform()
    return render(request, 'dash/books.html', {'fm': fm})





@login_required
def conversion(request):
    if request.method=='POST':
        form=ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form=ConversionLengthForm()
            context={
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first=request.POST['measure1']
                second=request.POST['measure2']
                input=request.POST['input']
                answer=''
                if input and int(input) >=0:
                    if first == 'yard' and second == 'foot' :
                        answer=f'{input}yard = {int(input)*3} foot'
                    if first == 'foot' and second == 'yard' :
                        answer=f'{input}foot = {int(input)/3} yard'
                context ={
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }

        if request.POST['measurement'] == 'mass':
            measurement_form=ConversionMassForm
            context={
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first=request.POST['measure1']
                second=request.POST['measure2']
                input=request.POST['input']
                answer=''
                if input and int(input) >=0:
                    if first == 'pound' and second == 'kilogram' :
                        answer=f'{input}pound = {int(input)*0.453592} kilogram'
                    if first == 'kilogram' and second == 'pound' :
                        answer=f'{input}kilogram = {int(input)*2.20462} pound'
                context ={
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }
    else:
        form = ConversionForm()
        context = {
            'form': form,
            'input': False
        }
    return  render(request,'dash/conversion.html',context)



@login_required
def dictionary(request):
    if request.method == 'POST':
        form = studyform(request.POST)
        text = request.POST.get('text')  # Use .get() to avoid MultiValueDictKeyError
        url="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r=requests.get(url)
        answer=r.json()
        try:
            phonetics=answer[0]['phonetics'][0]['text']
            audio=answer[0]['phonetics'][0]['audio']
            definition=answer[0]['meanings'][0]['definitions'][0]['definition']
            example =answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms =answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context={
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms,
            }
        except:
            context={
                'form':form,
                'input':''
            }
        return render(request, 'dash/dictionary.html',context)
    else:
        form = studyform()
        context = {'form': form}
    return  render(request,'dash/dictionary.html',context)



@login_required
def homework(request):
    if request.method=='POST':
        work=stuHomework(request.POST)
        if work.is_valid():
            work.save()
            messages.success(request, "Data has been saved in Database")
        else:
            messages.error(request, "Error saving data")
    work=stuHomework()
    fm=Homework.objects.filter(user=request.user)
    if len(fm) == 0:
        work_done = True
    else:
        work_done= False
    return  render(request,'dash/homework.html',{'work':work,'fm':fm,'work_done':work_done})


def update_work(request, pk):
    work=Homework.objects.get(id=pk)
    if work.status == False:
        work.status = True
    else:
        work.status = False
    work.save()
    return redirect('homework')



def delete_work(request,pk):
    work=Homework.objects.filter(pk=pk)
    work.delete()
    return redirect('homework')




def login(request):
    return  render(request,'dash/login.html')



@login_required
def notes(request):
    if request.method == 'POST':
        fm = stuNotes(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Data has been saved in Database.")
        else:
            messages.error(request, "Error saving data")
    fm = stuNotes()
    notes = Notes.objects.filter(user=request.user)
    notes_done = len(notes) == 0
    return render(request, 'dash/notes.html', {'fm': fm, 'notes': notes, 'notes_done': notes_done})



def notes_details(request,pk):
    note=Notes.objects.filter(pk=pk)
    return render(request,'dash/notes_detail.html',{'note':note})



def notes_delete(request,pk):
    note=Notes.objects.filter(pk=pk)
    note.delete()
    return redirect('notes')




def profile(request):
    list=Todo.objects.filter(user=request.user)
    if len(list) == 0:
        todo_done = True
    else:
        todo_done= False
    fm=Homework.objects.filter(user=request.user)
    if len(fm) == 0:
        work_done = True
    else:
        work_done =False
    return  render(request,'dash/profile.html',{'list':list,'todo_done':todo_done,'fm':fm,'work_done':work_done})



def register(request):
    if request.method == 'POST':
        form = Registeration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Registeration()
    return  render(request,'dash/register.html',{'form':form})



@login_required
def todo(request):
    if request.method=='POST':
        form=todoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data has been saved in Database")
        else:
            messages.error(request, "Error saving data")
    form=todoForm()
    list=Todo.objects.filter(user=request.user)
    if len(list) == 0:
        todo_done= True
    else:
        todo_done= False
    return  render(request,'dash/todo.html',{'form':form,'list':list,'todo_done':todo_done})



def update_todo(request,pk):
    todo=Todo.objects.get(id=pk)
    if todo.status == True:
        todo.status = False
    else:
        todo.status = True
    todo.save()
    return redirect('todo')




def todo_delete(request,pk):
    item=Todo.objects.get(pk=pk)
    item.delete()
    return redirect('todo')



@login_required
def wiki(request):
    if request.method =='POST':
        text=request.POST.get('text')
        form=studyform(request.POST)
        search=wikipedia.page(text)
        context={
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary
        }
        return render(request, 'dash/wiki.html', context)
    else:
        form = studyform()
        context = {
            'form': form
        }
    return  render(request,'dash/wiki.html',context)




@login_required
def youtube(request):
    if request.method == 'POST':
        fm = studyform(request.POST)
        text = request.POST.get('text')  # Use .get() to avoid MultiValueDictKeyError
        if text:
            video = VideosSearch(text, limit=10)
            result_list = []
            for i in video.result()['result']:
                result_dict = {
                    'input': text,
                    'title': i['title'],
                    'duration': i['duration'],
                    'thumbnail': i['thumbnails'][0]['url'],
                    'channel': i['channel']['name'],
                    'link': i['link'],
                    'views': i['viewCount']['short'],
                    'published': i['publishedTime']
                }
                desc = ''
                if i.get('descriptionSnippet'):
                    for j in i['descriptionSnippet']:
                        desc += j['text']
                result_dict['description'] = desc
                result_list.append(result_dict)
            return render(request, 'dash/youtube.html', {'fm': fm, 'result': result_list})
    else:
        fm = studyform()
    return render(request, 'dash/youtube.html', {'fm': fm})
