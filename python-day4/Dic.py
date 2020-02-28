def dictionary():
    swahili=dict()

    swahili['hello']='jambo'
    swahili['bye'] ='kwaheri'
    swahili['blue']='samawati'
    swahili['try']='jaribu'
    swahili['ready']='tayari'
    swahili['today']='leo'
    return swahili

swahili=dictionary()

 
#output='{bye} shati langu ni {blue}'.format(** swahili)
#output='uko {ready} ?'.format(** swahili)
output='{hello}  una hitaji usaidizi....{today}'.format(**swahili)
 
print(output)
