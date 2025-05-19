name="JOHn."
x=name.lower()
x=x.replace(" .", " ")
name=name.strip()
print(name)
print(x)
#starting_index:ending_index+1
sentence_one="The Dog Breed is German Sherpherd"
print(sentence_one[8:24])
sentence_two="Defeats for the Clinton forces,this was her moment of triumph"
print(sentence_two[16:30])
#splitting
sentence="The lazy dog;ran so fast;it hit the wall."
part=sentence.split(";")
print(part)
print(len(part))
first_name="joh.n"
first_name=first_name.replace("."," ")
first_name=first_name.strip()
second_name="Do,e"
second_name=second_name.replace(".","")