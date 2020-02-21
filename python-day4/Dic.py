def dictionary():
    swahili=dict()

    swahili['hello']='jambo'
    swahili['bye'] ='kwaheri'
    swahili['blue']='samawati'
    return swahili

swahili=dictionary()

print(dictionary,swahili['hello'],swahili['bye'])
 
output='{bye} shati langu ni {blue}'.format(** swahili)
 
print(output)
