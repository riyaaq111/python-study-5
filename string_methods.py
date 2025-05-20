text= " learn python "
text_tit=text.title()
text=text.strip()
print(text_tit)
#reverse
text="hello"
reversed_text=text[::-1]
print(reversed_text)
#replace
text=" learn python "
text=text.replace(' ','_')
print(text)
#count
text="learn python"
print(text.count("a"))
#capitalize
text="learn python"
text_tit=text.title()
print(text_tit)
#clean email and extract the dormain
email=" john.Doe@Gmail.com  "
email=email.lower()
print(email)
email=email.strip()
print(email)
#clean name and creat formatted sentence "my name is john doe and I love Reading Book "
first="john"
second="Doe" 
first=first.capitalize()
print(first)
second=second.capitalize()
print(second)
hobby=" Reading Books"
hobby=hobby.strip()
text=f"my name is {first} {second} and i love {hobby} "
print(text)