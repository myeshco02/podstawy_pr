#Write a program that checks whether
#a given person is a good influencer
#that is, whether the person has at least
#two of the following accounts: Facebook, Twitter or Instagram
#Use logical type variables: facebook, twitter, instagram
#the value of which indicates whether the person has an
#account on the social networking site.

facebook = True
twitter = False
instagram = False

#Boolean contain only 2 elements: True (1) False(0)
if (facebook + twitter + instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You need more accounts to be a good influencer.")
