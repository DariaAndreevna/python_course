import string

slogan = input("Enter your string:")
slogan = str(slogan)

my_hashtag = slogan.title()
my_hashtag = my_hashtag.replace(" ", "")
for p in string.punctuation:
    my_hashtag = my_hashtag.replace(p, "")

my_hashtag = "#" + my_hashtag
my_hashtag = my_hashtag[:140]

print(my_hashtag)
