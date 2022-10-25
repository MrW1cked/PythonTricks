#Help:
#How to Access Dictionaries to prevent future errors

player_atributes = {
    "name" : "Username_001" ,
    "class" : "Paladin" ,
    "strength" : 10 ,
    "health" : 100
}

#********* Option1 *********
#if you use this sintax and you call an attribute that doesn't exist it gives you an error: "KeyError: '-attribute_called-'"
new_player = player_atributes['class']
print (new_player)

#********* Option2 *********
#to improve this use this method:
new_player = player_atributes.get('achievements',0) #get.(' -class_you_want_to_call- ', 'error_value_in_case_doesn't_exists)
print (new_player)