from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import HilbertForm
import nltk
from textblob import Word
import random

from django_sirajnet.settings import DEBUG

# Make a base.html file with navigation
# ToDo: Make the page prettier

def make_mine(yours, swap_rate):
    print("make_mine")
    nltk.download('wordnet')
    mine = []
    for string_word in yours:
        word_object = Word(string_word)
        print("string_word: ", string_word)
        if random.randint(0, swap_rate - 1) == 0:
            print("Swap a word")
            meaning_count = len(word_object.synsets)
            print("word_object.sysnsets: ", word_object.synsets)
            print("Meaning count: ", meaning_count)
            if meaning_count > 0:
                # select a random synonym
                meaning_selected = random.randint(0, meaning_count - 1)
                lemmas = word_object.synsets[meaning_selected].lemmas()
                print("Lemmas: ", lemmas)
                synonym_count = len(lemmas)
                mine += [lemmas[random.randint(0, synonym_count - 1)].name()]
            else:
                mine += [string_word]
        else:
            mine += [string_word]

    return ' '.join(mine)

# Create your views here.
# here is the index page
def index(request):
    print("index")
    form = HilbertForm()
    form.fields['swap_rate'].initial = 1
    # process the data, and write it to the page
    context = {'form': form}
    return render(request, 'sirajnet/index.html', context=context)


def result(request):
    print("result")
    if request.method != 'POST':  # Keine Daten übermittelt; es wird ein leeres Formular erstellt.
        return HttpResponseRedirect(reverse('sirajnet:index'))
    else:
        # POST-Daten übermittelt; Daten werden verarbeitet.
        #print(request.POST)
        form = HilbertForm(data=request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            #print("form_data: ", form_data)
            print("form_data: ", form_data.your_text)
            print("form_data: ", form_data.swap_rate)
            my_text = make_mine(form_data.your_text.split(), form_data.swap_rate)
            print(my_text)
            context = {'your_text': form_data.your_text,
                       'my_text': my_text}
            # show the result
            return render(request, 'sirajnet/result.html', context=context)
        else:
            return HttpResponseRedirect(reverse('sirajnet:index'))
