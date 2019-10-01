from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sockeye.translate import run_translate
import os

# from .models import Question

# Create your views here.
def index(request):
    template = loader.get_template('translate/index.html')
    src_sent = request.POST.get('textsrc')
    context = {
    'conj_title': 'Переводчик',
    'src_sent': src_sent,
    'tgt_sent': ''
    }
    if src_sent is None or src_sent.strip() == '':
      return HttpResponse(template.render(context, request))
    if request.POST and ('do_edit' in request.POST):
        tgt_sent = chv_translate(src_sent.strip())
        context = {
        'conj_title': 'Переводчик',
        'src_sent': src_sent,
        'tgt_sent': tgt_sent
        }        
        return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))

def do_edit():
    return HttpResponse("Simple answer")
    
def chv_translate(src_sent):
    with open('translate/data/chv.textbox.tok', 'w', encoding="utf-8") as file:
        file.write(src_sent)
    os.system("dir")
    os.system("python translate/data/subword-nmt/subword_nmt/apply_bpe.py -c translate/data/enru_parent_10Kvocab50_train/bpe.codes --vocabulary translate/data/enru_parent_10Kvocab50_train/bpe.vocab.enchv --vocabulary-threshold 50 < translate/data/chv.textbox.tok > translate/data/chv.textbox.bpe")
    os.system("python -m sockeye.translate -m translate/data/chvru_parent_10Kvocab_model --input translate/data/chv.textbox.bpe --output translate/data/ru.textbox.bpe --use-cpu")
    with open('translate/data/ru.textbox.bpe', 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', '').replace('@@ ', '')
    return data