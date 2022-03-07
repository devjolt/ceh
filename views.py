from django.views.generic.base import TemplateView
from django.shortcuts import render
from random import randint, shuffle, choice

import time

from .ceh_modules import _1, _3, _4#, _2, _3
from ceh.utilities import utilities as utl

class HomeView(TemplateView):
    template_name = "ceh/home.html"

class RandomModuleView(TemplateView):
    modules = ()#set this in views
    template_name = 'ceh/multichoice.html'
    
    def get_context_data(self, **kwargs):
        start = time.time()
        context = super().get_context_data(**kwargs)#we're going to mess with context data, so making a context object
        module = choice(self.modules)#select a module from the dict in that module
        print('module:',module)
        key = choice(tuple(module.questions.keys()))#from module, get key
        print('key:',key)
        question_type = 'multi-choice'#always multiple choice for now... we don't need drag and drop here...
        #uncomment for a specific question in a specific module:
        #module = _1
        #key = 'test_question'
        if type(module.questions[key]) == dict:#if that module and key contains a dict, we can use it directly to produce question and items
            question_dict = module.questions[key]#get the dict
            
            if type(question_dict['type'])==str:
                resource_type=question_dict['type']
            else:
                resource_type=choice(question_dict['type'])
            print('resource_type:',resource_type)

            question_logic={
                'correct_incorrect':utl.make_items_question_from_correct_incorrect,
                'multi_from_correct':utl.multi_option_from_correct_incorrect,
                'old_pairs':utl.make_items_question_from_pairs,
                'posneg_pairs':utl.posneg_pairs,
                'new_pairs':utl.new_pairs,
                'multi_option_pairs':utl.multi_option_pairs,
                'order_from_pairs':utl.order_from_pairs
            }
            """
            'posneg_pairs':utl.posneg_pairs,
            'new_pairs':utl.new_pairs,
            'multi_option_pairs':utl.multi_option_pairs,
            'order_from_pairs':utl.order_from_pairs

            """
            if resource_type in question_logic.keys():
                template_question, items = question_logic[resource_type](question_dict)

        else:
            print('logic type question')#self contained generating its own question and items
            template_question, items = module.questions[key]()
        
    
        shuffle(items)
        context['question'], context['items'] = template_question, items
        context['question_type'] = question_type
        context['key'] = key
        key_link = key.replace(',', '')
        context['key_link'] = key_link.replace(' ', '+').lower()
        stop = time.time()
        print('time taken:', stop-start)#interesting to know...
        return context

def test_question(request):
    module = e_files_os
    key = 'SQLite3 methods and attributes'
    #callable
    #items, question = module.questions[key]()
    context = {
        'question_type':'multi-choice',
        'items':items, 
        'question':question,
        'key':key,
        }
    return render(request, 'cismp/multichoice.html', context)



