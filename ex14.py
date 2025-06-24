from sys import argv

script, user_name = argv

prompt = ">"

print("Hi %s, i'm the %s script"%(user_name,script))
print("I'd like to ask you afew questions")
print("do you like me %s"%user_name)
likes = input(prompt)

print("where do you live %s"%user_name)
lives = input(prompt)

print("what kind of computer do you have")
computer = input(prompt)

print("""
Alright so you said %r about liking me,
you also said you lived at %r, have no clue to where that is
And you have a %r computer. Nice
 """%(likes,lives,computer))
