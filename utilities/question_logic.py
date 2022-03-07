from random import randint, shuffle, choice
import re
from . import utilities as lf
"""
Question templates in this file:
generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)
"""

########### dealing with code block questions. This all seems to work fine vvvvv
class Question():
    id = 1
    items = []
    used = []
    code = ''''''
    template_question = []

    def pick_one_many_times(self, item):
        while True:
            print('Inside class picking  one many times')
            if type(item) is str:
                print(item, 'is a string')
                return item
            else:
                item= item[randint(0, len(item)-1)]

    def pick_one(self, item):
        print('Inside class picking one')
        return item[randint(0, len(item)-1)]
        
    def raw_question_to_template_question(self, raw_question, placeholder_str):
        """Either way, placeholders need to be replaced as they appear...
        if raw_question is...
        - a string: assign one item as text and replace placeholder
        - a list of strings: for each item, replace placeholder, then assign each item as either text or code
        """
        if type(raw_question) is str:#assume that strings will never just be pure code... I can't think why they would ever be
            self.template_question.append({'text':raw_question.replace('PLACEHOLDER', placeholder_str)})
        else:
            for line in raw_question:
                #replace PLACEHOLDER
                replaced_question = line.replace('PLACEHOLDER', placeholder_str)
                if replaced_question[0] != '$':
                    self.template_question.append({'text':replaced_question})
                else:
                    self.template_question.append({'code':replaced_question[1:]})

    def populate_items(self, incorrect, comment = False):
        while len(self.items) != 4:
            item = pick_one(incorrect)
            print(item)
            print(self.used)
            if item not in self.used:
                self.add_possible_code_item(item, 'incorrect', comment)   
        
    def add_item(self, item, indicator):
        self.items.append({'item':item, 'indicator':indicator, 'id':f'item{self.id}'})
        self.id+=1
        self.used.append(item)
        
    def add_possible_code_item(self, item, indicator, comment = False):
        print('adding item', self.id)
        if item[0] == '$':
            self.items.append({'code':item[1:], 'indicator':indicator, 'id':f'item{self.id}'})
        else:
            if comment != True:
                self.items.append({'item': item, 'indicator':'incorrect', 'id':f'item{self.id}'})
            else:
                self.items.append({'code':'#' + item, 'indicator':'incorrect', 'id':f'item{self.id}'})
        self.id+=1
        self.used.append(item)

    def add_code_line(self, line):
        line= self.pick_one_many_times(line)
        self.code+= line + '\n'


class ErrorLines(Question):
    def __init__(self, valid, invalid):
        self.make_error_line_items_code(valid, invalid)

    def make_error_line_items_code(valid, invalid):
        """Relies on valid and invalid being the same length...
        """
        if randint(0, 1) == 0:#the code will fail...
            #pick which line will cause failure
            error_line = randint(0, len(valid)-1)
            self.items.append({'item':error_line+1, 'indicator':'correct', 'id':f'item{self.id}'})
            self.id+=1
            #pick three numbers which are not the same as error line
            if randint(0,1) == 0:#chance for statement that the code will run without error
                self.used.append('No failure')
                self.items.append({'item':'The code will execute successfully', 'indicator':'incorrect', 'id':f'item{self.id}'})
                self.id+=1
            while len(self.used) != 3:
                num = randint(0, len(valid)-1)
                if num != error_line:
                    self.used.append(num)
                    self.used = list(set(self.used))
            for num in self.used:
                if num != 'No failure':
                    self.items.append({'item': num+1, 'indicator':'incorrect', 'id':f'item{self.self.id}'})
                    self.id+=1
            #build a string with all but failing line correct
            for i in range(len(valid)):
                if i == error_line:
                    self.code+= pick_one(invalid[i]) + '\n'
                else: 
                    self.code+= pick_one(valid[i]) + '\n'
        else:#the code will actually not fail
            self.items.append({'item':'The code will execute successfully', 'indicator':'correct', 'id':f'item{self.id}'})
            self.id+=1
            while len(self.used) != 3:
                num = randint(0, len(valid)-1)
                if num not in self.used:
                    self.add_item(self, num+1, 'incorrect')
            for line in valid:
                self.add_code_line(line)

class Outcome(Question):
    def __init__(self, valid, invalid):
        self.code_outcome(valid, invalid)

    def code_outcome(self, valid, invalid):
        """items in invalid:
        (
            (('line0','outcome'),(('line0','alt line0'),'code outcome'), ....),
            ...
        )
        Each item is index[nth] line of code containing:
        [0] = either str or iterable of sample code
        [1] = code outcome of all code in [0]
        valid:
        (('sample code', ))
        [0] contains items which are each line of code
        [1] contains single string stating outcome of completed code 
        """
        #check that length of valid and invalid are the same
        if len(valid[0]) != len(invalid):
            print(f'Valid len ({len(valid[0])}) != invalid len ({len(invalid)})')
            return None
        #choose between one incorrect vs all correct
        if randint(0,3) in [0,1,2]:#one incorrect
            print('one correct')
            invalid_index = randint(0, len(valid[0])-1)#choose index of incorrect line   
            self.items.append({'item':valid[1], 'indicator':'incorrect', 'id':f'item{self.id}'})#incorrect item: code outcome successful
            self.id+=1#increment id
            correct_invalid_line_options = invalid[invalid_index]#get all entries
            correct_invalid_line = pick_one(correct_invalid_line_options)#get one entry
            self.add_possible_code_item(correct_invalid_line[1], 'correct')
            #select two other invalid outcomes NOT THE SAME AS THE correct answer
            while len(self.used)!=3:
                #select another invalid answer NOT matching index of correct_answer
                line= pick_one(invalid)#picking a line to take an error from
                if type(line) is not str:
                    attempt= pick_one(line)[1]#pick an item from the line and get the error at index[1] 
                else: 
                    attempt= line
                
                if attempt not in self.used:
                    self.add_possible_code_item(attempt, 'incorrect')

            #build code string
            for i in range(len(valid[0])):
                if i == invalid_index:
                    self.add_code_line(correct_invalid_line)
                else:
                    valid_line = valid[0][i]
                    self.add_code_line(valid_line)
        else:#all correct
            print('all correct')
            self.items.append({'item':valid[1], 'indicator':'correct', 'id':f'item{self.id}'})#use a correct answer
            self.id+=1#increment id
            #select three random unique incorrect answers
            while len(self.used)!=3:
                line_options = pick_one(invalid)#pick a line
                attempt = pick_one(line_options)[1]
                if attempt not in self.used:
                    self.add_possible_code_item(attempt, 'incorrect')
            for line in valid[0]:
                self.code+= line + '\n'



def raw_question_to_template_question(raw_question, placeholder_str):
    """Either way, placeholders need to be replaced as they appear...
    if raw_question is...
    - a string: assign one item as text and replace placeholder
    - a list of strings: for each item, replace placeholder, then assign each item as either text or code
    """
    template_question = []
    if type(raw_question) is str:#assume that strings will never just be pure code... I can't think why they would ever be
        template_question.append({'text':raw_question.replace('PLACEHOLDER', placeholder_str)})
    else:
        for line in raw_question:
            #replace PLACEHOLDER
            replaced_question = line.replace('PLACEHOLDER', placeholder_str)
            if replaced_question[0] != '$':
                template_question.append({'text':replaced_question})
            else:
                template_question.append({'code':replaced_question[1:]})
    return template_question

def add_item(item, indicator, items, id, used):
    """add item to items and used list
    """
    items.append({'item':item, 'indicator':indicator, 'id':f'item{id}'})
    id+=1
    used.append(item)
    return items, id, used
    
def add_possible_code_item(item, indicator, items, id, used, comment = False):
    #print('adding item', id)
    items = list(items)
    if item[0] == '$':
        items.append({'code':item[1:], 'indicator':indicator, 'id':f'item{id}'})
    else:
        if comment != True:
            items.append({'item': item, 'indicator':indicator, 'id':f'item{id}'})
        else:
            items.append({'code':'#' + item, 'indicator':indicator, 'id':f'item{id}'})
    id+=1
    used.append(item)
    return items, id, used

def populate_items(incorrect, items, id, used, comment = False):
    while len(items) != 4:
        #print(incorrect)
        item = choice(incorrect)
        if item not in used:
            items, id, used= add_possible_code_item(item, 'incorrect', items, id, used, comment)
    print(items)   
    return items

def add_code_line(self, line, code):
    line= choice(line)
    code+= line + '\n'
    return code

def make_items_question_from_pairs(resource):
    raw_question_0=resource['question_with_0']
    raw_question_1=resource['question_with_1']
    pairs=resource['pairs']
    fillers=resource['fillers']
    
    used = []
    id = 1
    items = []
    chosen_pair = choice(list(pairs))
    #print(chosen_pair)

    item_question_num = (0, 1) if randint(0,1) == 0 else (1, 0)#if 0,1 code goes into question, if 1,0 code is in items
    item_num, question_num = item_question_num[0], item_question_num[1]
    
    if question_num == 0:
        raw_question = raw_question_0
    else:   
        raw_question = raw_question_0 if raw_question_1 == '' else raw_question_1
    #get one correct and incorrect item
    correct_item=choice(chosen_pair[item_num]) if type(chosen_pair[item_num])!=str else chosen_pair[item_num]
    question_item=choice(chosen_pair[question_num]) if type(chosen_pair[question_num])!=str else chosen_pair[question_num]

    #print('correct', correct_item)
    #print('question', question_item)
    incorrect=[]
    for pair in resource['pairs']:
        if pair!=chosen_pair:
            if type(pair[1])in(tuple, list):
                incorrect+=list(pair[1])
            else:
                incorrect.append(pair[1])
    for pair in resource['fillers']:
        if pair!=chosen_pair:
            if type(pair[1])in(tuple, list):
                incorrect+=list(pair[1])
            else:
                incorrect.append(pair[1])

    question_template = raw_question_to_template_question(raw_question, question_item)

    comment = False
    if item_num == 0:    
        items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    else:
        if question_item[0] == '$':
            comment = True
            items.append({'code':'#' + correct_item, 'indicator':'correct', 'id':f'item{id}'})
        else:
            items.append({'item':correct_item, 'indicator':'correct', 'id':f'item{id}'})
        used.append(chosen_pair[item_num])
        id+= 1
    
    items= populate_items(incorrect, items, id, used, comment)
    return question_template, items

def correct_incorrect_helper(correct, incorrect):         
    id = 1
    used = []
    items = []
    correct_item = choice(correct)
    items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    items = populate_items(incorrect, items, id, used)
    return items

def make_items_question_from_correct_incorrect(resource):
    raw_question=resource['question']
    positive=resource['positive']
    negative=resource['negative']
    correct=resource['correct']
    incorrect=resource['incorrect']
    
    use_in_question = positive if randint(0,1) == 1 else negative
    if use_in_question == positive:
        items = correct_incorrect_helper(correct, incorrect)
        placeholder_str = positive
    else:
        items = correct_incorrect_helper(incorrect, correct)
        placeholder_str = negative
    template_question = raw_question_to_template_question(raw_question, placeholder_str)
    return template_question, items



def generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers):
    """Creates random question and item string for questions about correct order e.g.
    Question: What is the correct order to count in from lowest to highest:
    1. 1,2,3
    2. 3,2,4
    3. 1,2,9
    4. 3,2,1
    num_choices=number of choices to be in item list
    question_text = "What is the correct order to count in from PLACEHOLDER?"
    ascending_order="lowest to highest"
    descending_order="highest to lowest"
    correct_list=[1,2,3]
    fillers=[4,6,7,8]
    """
    item_id=1
    order= ascending_order if randint(0,1)==0 else descending_order
    
    question_text=re.sub('PLACEHOLDER', order, question_text)
    
    question=[
        {'text':question_text}
    ]
    correct_str=', '.join(correct_list) if order==ascending_order else ', '.join(correct_list[::-1])
    used=[correct_str]
    items=[{'item':correct_str, 'indicator':'correct', 'id':'item1'}]
    all_options=correct_list+fillers
    while len(used)!=num_choices:
        shuffle(all_options)
        new_str=', '.join(all_options[-len(correct_list):])
        if new_str not in used:
            used.append(new_str)
            item_id+=1
            items.append({'item':new_str, 'indicator':'incorrect', 'id':f'item{item_id}'})
    shuffle(items)
    shuffle(items)
    return question, items


def multi_option_from_correct_incorrect(resource):
    #choose whether right answers are correct or incorrect
    if randint(0,1)==0:
        right, wrong = (resource['positive'],resource['correct']), (resource['negative'],resource['incorrect'])
    else:
        right, wrong = (resource['negative'],resource['incorrect']), (resource['positive'],resource['correct'])  
    first_question_part = re.sub('PLACEHOLDER', right[0], resource['question'])
    first_question_part=re.sub(' is ', ' are ', first_question_part)
    right, wrong = list(right[1]), list(wrong[1])
    shuffle(wrong)#randomise order of both
    shuffle(right)
    #make first part of question
    
    question = [{'text':first_question_part}]
    #choose number of right answers
    
    max_right=4
    number_right = randint(0, max_right)
    letters_list = ['a', 'b', 'c', 'd']
    building_items_letters_list=['a', 'b', 'c', 'd']
    #print('number right',number_right)
    #print('question', question)
    #print('right', right)
    #print('wrong', wrong)
    for i in range(2):
        changes_made=0
        #note there must be enough right and wrong answers for this  to work... loop checks this!
        if len(wrong)<4-number_right:#if less wrong answers available than we need
            number_right=max_right-len(wrong)#use max number of wrong answers by altering number_right
            changes_made+=1

        if len(right)<number_right:#if less right answers available than we need
            number_right=len(right)#use max number of right answers by altering number_right
            changes_made+=1

        #print(changes_made)
        if changes_made==2:#if we've changed both, then it is impossible to create this question because it doesn't have enough right or wrong answers
            if i == 1:#If this is the case on the second time around, question building is doomed to fail when popping answers below
                print('Error: question resource does not have enough right or wrong answers!')      
                break
            max_right=3#try reducing the number of letters available and try again...
            number_right = randint(0, max_right)
            letters_list = ['a', 'b', 'c']
            building_items_letters_list=['a', 'b', 'c']
            continue
        break

    #print('max_right:', max_right)

    if number_right==0:
        wrong_answers=wrong[0:max_right-number_right]
        #print('wrong answers:', wrong_answers)
        correct='none of the above'
        for i in range(number_right+len(letters_list)):
            question.append({'text':f'{letters_list[i]}. {wrong_answers[i]}'})
    elif number_right==max_right:
        correct='all of the above'
        right_answers=right[0:max_right]
        for i in range(max_right):
            question.append({'text':f'{letters_list[i]}. {right_answers[i]}'})
    else:
        letters_dict = {'a':None, 'b':None, 'c':None, 'd':None}
        right_letters, wrong_letters=[], []
        right_answers=right[:number_right]
        wrong_answers=wrong[0:max_right-number_right]
        shuffle(letters_list)
        for i in range(len(right_answers)):
            #print('right letters:', letters_list)
            #print('right answers:', right_answers)
            letter=letters_list.pop()
            letters_dict[letter]=right_answers[i]
            right_letters.append(letter)
        while len(letters_list)!=0:
            #print('wrong letters:', letters_list)
            #print('wrong answers:', wrong_answers)
            letter=letters_list.pop()
            letters_dict[letter]=wrong_answers.pop()
            wrong_letters.append(letter)
        right_letters.sort()
        correct=', '.join(right_letters)
        for letter in building_items_letters_list:
            question.append({'text':f'{letter}. {letters_dict[letter]}'})
    item_id=1
    items=[{'item':correct, 'indicator':'correct', 'id':f'item{item_id}'}]
    used=[correct]

    #make incorrect answers
    while len(items)!=4:#we want there to be four items
        
        number = randint(0, max_right)#pick type of wrong answer using max_right (usually 4, 3 if inadequate numbers of right or wrong answers)
        if number==0:
            incorrect='none of the above'
        elif number==max_right:
            incorrect='all of the above'
        else:
            letters=building_items_letters_list
            shuffle(letters)
            letters = letters[0:number]
            letters.sort()
            incorrect=', '.join(letters)
        if incorrect not in used:
            item_id+=1
            items.append({'item':incorrect, 'indicator':'incorrect', 'id':f'item{item_id}'})
            used.append(incorrect)
        else:
            continue
    shuffle(items)
    shuffle(items)
    return question, items




###new functions what a waste of my life



def posneg_pairs(resource):
    """
    requires:
    resource = {
        'question_with_0':'Which isPOSNEG an example of PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs'],
        'course_code':'',
        'pairs':[
            ('correct',['A','B','C']),
            ('incorrect',['1', '2','3']),#minimum!
        ],
        'fillers': (
        )
    }
    """
    
    focus_pair = choice(resource['pairs'])
    print(focus_pair)
    correct = focus_pair[1]
    print(correct)


    incorrect = []
    for pair in resource['pairs']:
        if pair[0]!=focus_pair[0]:
            if type(pair[1])in(tuple, list):
                incorrect+=list(pair[1])
            else:
                incorrect.append(pair[1])
    for pair in resource['fillers']:
        if pair[0]!=focus_pair[0]:
            if type(pair[1])in(tuple, list):
                incorrect+=list(pair[1])
            else:
                incorrect.append(pair[1])

    print('incorrect:', incorrect)
    posneg = randint(0,1)
    raw_question=re.sub('POSNEG', resource['positive_negative'][posneg], resource['question_with_0'])
    if posneg==1:
        correct, incorrect=incorrect, correct

    item_question_num = (0, 1) if posneg == 0 else (1, 0)#if 0,1 code goes into question, if 1,0 code is in items
    item_num, question_num = item_question_num[0], item_question_num[1]
    
    used = []
    id = 1
    items = []

    correct_item=choice(correct) 
    question_item=choice(focus_pair[0]) if type(focus_pair[0])in(list, tuple) else focus_pair[0]
    
    question_template = raw_question_to_template_question(raw_question, question_item)

    comment = False
    if item_num == 0:    
        items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    else:
        if question_item[0] == '$':
            comment = True
            items.append({'code':'#' + correct_item, 'indicator':'correct', 'id':f'item{id}'})
        else:
            items.append({'item':correct_item, 'indicator':'correct', 'id':f'item{id}'})
        used.append(focus_pair[1])
        id+= 1
    items = populate_items(incorrect, items, id, used, comment)
    shuffle(items)
    shuffle(items)
    return question_template, items


def new_pairs(resource):
    """
    requires
    resource = {
        'question_with_0':'Which isPOSNEG an example of PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':[
            ('correct',['A','B','C','D']),
            ('incorrect',['1', '2', '3','4']),
            ('ambiguous',['0', '9', '8','7']),
            ('backwards',['z', 'y', 'x','w']),
        ],
        'fillers': (
            ()
        )
    }
    """
    pairs=resource['pairs']
    fillers=resource['fillers']
    used = []
    id = 1
    items = []
    chosen_pair = choice(pairs)

    item_question_num = (0, 1) if randint(0,1) == 0 else (1, 0)#if 0,1 code goes into question, if 1,0 code is in items
    item_num, question_num = item_question_num[0], item_question_num[1]
    
    if question_num == 0:
        raw_question = resource['question_with_0']
    else:   
        raw_question = resource['question_with_0'] if resource['question_with_1'] == '' else resource['question_with_1']
    #get one correct and incorrect item
    raw_question=re.sub('POSNEG', '', raw_question)

    
    correct_item=choice(chosen_pair[item_num]) if type(chosen_pair[item_num])in(list, tuple) else chosen_pair[item_num] 
    question_item=choice(chosen_pair[question_num]) if type(chosen_pair[question_num])in(list, tuple) else chosen_pair[question_num]
            
    list(pairs).remove(chosen_pair)
    incorrect = []
    for pair in pairs:
        if pair[0]!=chosen_pair[0]:
            if type(pair[item_num])in(tuple, list):
                incorrect+=list(pair[item_num])
            else:
                incorrect.append(pair[item_num])
    for pair in fillers:
        if pair[0]!=chosen_pair[0]:
            if type(pair[item_num])in(tuple, list):
                incorrect+=list(pair[item_num])
            else:
                incorrect.append(pair[item_num])
    
    question_template = raw_question_to_template_question(raw_question, question_item)

    comment = False
    if item_num == 0:    
        items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    else:
        if question_item[0] == '$':
            comment = True
            items.append({'code':'#' + correct_item, 'indicator':'correct', 'id':f'item{id}'})
        else:
            items.append({'item':correct_item, 'indicator':'correct', 'id':f'item{id}'})
        used.append(chosen_pair[item_num])
        id+= 1
   
    items = populate_items(incorrect, items, id, used, comment)
    shuffle(items)
    shuffle(items)
    return question_template, items


def multi_option_pairs(resource):
    """
    resource = {
        'question_with_0':'Which isPOSNEG an example of PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['multi_pairs'],
        'course_code':'',
        'pairs':[
            ('correct',['A','B','C','D']),
            ('incorrect',['1', '2', '3','4']),
            ('ambiguous',['0', '9', '8','7']),
            
        ],
        'fillers': (
            ('backwards',['z', 'y', 'x','w']),
        )
    }

    """
    #select a 'right' row
    right_row = choice(resource['pairs'])
    posneg=randint(0,1)
    
    question_item=0
    answer_item=1
  
    first_question_part = re.sub('POSNEG', resource['positive_negative'][posneg], resource['question_with_0'])

    #different to multi_from_correct_incorrect because no need to have positive and negative at this stage    
    try:
        first_question_part = re.sub('PLACEHOLDER', right_row[question_item], first_question_part)
    except:
        first_question_part = re.sub('PLACEHOLDER', choice(right_row[question_item]), first_question_part)        
    first_question_part = re.sub(' is ', ' are ', first_question_part)


    if type(right_row[answer_item]) in (list,tuple):
        right=right_row[answer_item]
    else:
        right=[right_row[answer_item]]

    wrong=[]
    for row in resource['pairs']:
        if row[0]!=right_row[0]:
            if type(row[answer_item])in(list, tuple):
                wrong+=row[answer_item]
            else:
                wrong+=[row[answer_item]]
    for row in resource['fillers']:
        if type(row[answer_item])in(list, tuple):
            wrong+=list(row)
        else:
            wrong+=[row[answer_item]]
    if posneg==1:
        right, wrong=wrong, right
    
    #following code identical to other pairs stuff...
    
    shuffle(wrong)#randomise order of both
    shuffle(right)
    #make first part of question
    
    question = [{'text':first_question_part}]
    #choose number of right answers
    
    max_right=4
    number_right = randint(0, max_right)
    letters_list = ['a', 'b', 'c', 'd']
    building_items_letters_list=['a', 'b', 'c', 'd']
    print('number right',number_right)
    print('question', question)
    print('right', right)
    print('wrong', wrong)
    for i in range(2):
        changes_made=0
        #note there must be enough right and wrong answers for this  to work... loop checks this!
        if len(wrong)<4-number_right:#if less wrong answers available than we need
            number_right=max_right-len(wrong)#use max number of wrong answers by altering number_right
            changes_made+=1

        if len(right)<number_right:#if less right answers available than we need
            number_right=len(right)#use max number of right answers by altering number_right
            changes_made+=1

        #print(changes_made)
        if changes_made==2:#if we've changed both, then it is impossible to create this question because it doesn't have enough right or wrong answers
            if i == 1:#If this is the case on the second time around, question building is doomed to fail when popping answers below
                print('Error: question resource does not have enough right or wrong answers!')      
                break
            max_right=3#try reducing the number of letters available and try again...
            number_right = randint(0, max_right)
            letters_list = ['a', 'b', 'c']
            building_items_letters_list=['a', 'b', 'c']
            continue
        
        break

    #print('max_right:', max_right)

    if number_right==0:
        wrong_answers=wrong[0:max_right-number_right]
        #print('wrong answers:', wrong_answers)
        correct='none of the above'
        for i in range(number_right+len(letters_list)):
            question.append({'text':f'{letters_list[i]}. {wrong_answers[i]}'})
    elif number_right==max_right:
        correct='all of the above'
        right_answers=right[0:max_right]
        for i in range(max_right):
            question.append({'text':f'{letters_list[i]}. {right_answers[i]}'})
    else:
        letters_dict = {'a':None, 'b':None, 'c':None, 'd':None}
        right_letters, wrong_letters=[], []
        right_answers=right[:number_right]
        wrong_answers=wrong[0:max_right-number_right]
        shuffle(letters_list)
        for i in range(len(right_answers)):
            #print('right letters:', letters_list)
            #print('right answers:', right_answers)
            letter=letters_list.pop()
            letters_dict[letter]=right_answers[i]
            right_letters.append(letter)
        while len(letters_list)!=0:
            #print('wrong letters:', letters_list)
            #print('wrong answers:', wrong_answers)
            letter=letters_list.pop()
            letters_dict[letter]=wrong_answers.pop()
            wrong_letters.append(letter)
        right_letters.sort()
        correct=', '.join(right_letters)
        for letter in building_items_letters_list:
            question.append({'text':f'{letter}. {letters_dict[letter]}'})
    item_id=1
    items=[{'item':correct, 'indicator':'correct', 'id':f'item{item_id}'}]
    used=[correct]

    #make incorrect answers
    while len(items)!=4:#we want there to be four items
        
        number = randint(0, max_right)#pick type of wrong answer using max_right (usually 4, 3 if inadequate numbers of right or wrong answers)
        if number==0:
            incorrect='none of the above'
        elif number==max_right:
            incorrect='all of the above'
        else:
            letters=building_items_letters_list
            shuffle(letters)
            letters = letters[0:number]
            letters.sort()
            incorrect=', '.join(letters)
        if incorrect not in used:
            item_id+=1
            items.append({'item':incorrect, 'indicator':'incorrect', 'id':f'item{item_id}'})
            used.append(incorrect)
        else:
            continue
    shuffle(items)
    shuffle(items)
    return question, items

#question, items = multi_option_from_pairs(resource)

def order_from_pairs(resource):
    """Creates random question and item string for questions about correct order e.g.
    Question: What is the correct order to count in from lowest to highest:
    1. 1,2,3
    2. 3,2,4
    3. 1,2,9
    4. 3,2,1

    requires
    resource = {
        'question_order':'What best describes the killchain from PLACEHOLDER?',
        'ascending_descending':('first to last', 'last to first'),
        'type':['order_pairs'],
        'course_code':'',
        'pairs':[
            ('correct',['A','B','C','D']),
            ('incorrect',['1', '2', '3','4']),
            ('ambiguous',['0', '9', '8','7']),
            
        ],
        'fillers': (
            ('backwards',['z', 'y', 'x','w']),
        )
    }
    """
    num_choices=4#number of options to present
    item_id=1
    #order= ascending_order if randint(0,1)==0 else descending_order
    asc_des=randint(0,1)
    
    #0 uses only the name part
    #1 uses only the description part  

    question_text=re.sub('PLACEHOLDER', resource['ascending_descending'][asc_des], resource['question_order'])
    
    question=[
        {'text':question_text}
    ]
    name_or_description = randint(0,1)#0 to use names, 1 to use descriptions
    correct_list=[]
    for item in resource['pairs']:
        if type(item[name_or_description])in(tuple, list):
            correct_list.append(choice(item[name_or_description]))
        else:
            correct_list.append(item[name_or_description])
        
    correct_str=', '.join(correct_list) if asc_des==0 else ', '.join(correct_list[::-1])
    used=[correct_str]
    items=[{'item':correct_str, 'indicator':'correct', 'id':'item1'}]

    fillers=[]
    for item in resource['fillers']:
        if type(item[name_or_description])in(tuple, list):
            fillers.append(choice(item[name_or_description]))
        else:
            fillers.append(item[name_or_description])
    
    all_options=correct_list+fillers
    while len(used)!=num_choices:
        shuffle(all_options)
        new_str=', '.join(all_options[-len(correct_list):])
        if new_str not in used:
            used.append(new_str)
            item_id+=1
            items.append({'item':new_str, 'indicator':'incorrect', 'id':f'item{item_id}'})
    shuffle(items)
    shuffle(items)
    return question, items
