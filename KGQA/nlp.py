# -*- coding: utf-8 -*-
import paddlehub as hub
module = hub.Module(name="lac")


def get_target_array(words):
    target_pos = ['PER','nr', 'n']
    target_array = []
    words_list = []
    words_list.append(words)
    inputs = {"text":words_list}
    results = module.lexical_analysis(data=inputs)

    for ix in range(0,len(results[0]['tag'])):
        if(results[0]['tag'][ix] in target_pos):
            target_array.append(results[0]['word'][ix])
    return target_array