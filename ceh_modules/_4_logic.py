from random import randint, shuffle

from ceh.utilities import utilities as utl

#order...
#is part of...

def information_lifecycle_in_order():
    """official, secret, top secret
    decide whether most-least or least-most
    """
    item_id=1
    question=[
        {'text':f'What is the correct order of the stages in the information life cycle?'}
    ]
    real=['acquisition','utilisation','disposal']#least to most default
    spam=['official-secret','officiating','arbitration','leaking','sensitive','unofficial']
    correct_str=', '.join(real)
    used=[correct_str]
    items=[{'item':correct_str, 'indicator':'correct', 'id':'item1'}]
    all_options=real+spam
    while len(used)!=4:
        shuffle(all_options)
        new_str=', '.join(all_options[-3:])
        if new_str not in used:
            used.append(new_str)
            item_id+=1
            items.append({'item':new_str, 'indicator':'incorrect', 'id':f'item{item_id}'})
    shuffle(items)
    return question, items

def activity_is_carried_out_at_the_stage():
    stages=(
        ('acquisition', ['planning','identification','classification','source']),
        ('utilisation', ['storage','processing','sharing','transmission','validity','integrity']),
        ('transfer', ['validity', 'disposal', 'transfer', 'auditing']),
    )
    tf='true' if randint(0,1)==0 else 'false'
    base = 'VALUE is a part of the KEY stage'
    question=[{'text':f'Thinking about the information cycle, which of the following is {tf}:'}]
    item_id=1
    if tf=='true':
        correct_num=randint(0, len(stages)-1)
        correct_str=f"{utl.pick_one(stages[correct_num][1])} is a part of the {stages[correct_num][0]} stage"
        used=[correct_str]
        items=[{'item':correct_str, 'indicator':'correct', 'id':'item1'}]
        while len(used)!=4:
            stage_num, part_num=randint(0,2), randint(0,2)
            while stage_num==part_num:
                part_num=randint(0,2)
            incorrect_str=f'{utl.pick_one(stages[part_num][1])} is a part of the {stages[stage_num][0]} stage'
            if incorrect_str not in used:
                item_id+=1
                items.append({'item':incorrect_str, 'indicator':'incorrect', 'id':f'item{item_id}'})
                used.append(incorrect_str)
            else:
                continue
    else:
        stage_num, part_num=randint(0,2), randint(0,2)
        while stage_num==part_num:
            part_num=randint(0,2)
        incorrect_str=f'{utl.pick_one(stages[part_num][1])} is a part of the {stages[stage_num][0]} stage'
        used=[incorrect_str]
        items=[{'item':incorrect_str, 'indicator':'correct', 'id':'item1'}]
        while len(used)!=4:
            stage=randint(0,2)
            correct_str=f'{utl.pick_one(stages[stage][1])} is a part of the {stages[stage][0]} stage'
            if correct_str not in used:
                item_id+=1
                items.append({'item':correct_str, 'indicator':'incorrect', 'id':f'item{item_id}'})
                used.append(correct_str)
    shuffle(items)
    return question, items

def make_bifactor():
    options=[
        ('type 1', ['username and password','key phrase','number pattern','pin number','something you know', 'easiest to replicate']),
        ('type 2', ['smartcard','key fob','key','NFC token', 'something you have']),
        ('type 3', ['finger print', 'retinal scan', 'something you are']),
    ]
    shuffle(options)
    return ' and '.join([utl.pick_one(options[0][1]), utl.pick_one(options[1][1])])

def make_single_factor():
    options=[
        ('type 1', ['username and password','key phrase','number pattern','pin number','something you know', 'easiest to replicate']),
        ('type 2', ['smartcard','key fob','key','NFC token', 'something you have']),
        ('type 3', ['finger print', 'retinal scan', 'something you are']),
    ]
    shuffle(options)
    new_list = options[0][1]
    shuffle(new_list)
    return ' and '.join([new_list[0], new_list[1]])
