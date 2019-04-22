from sys import argv

script, user_name = argv
promt = ">"

print "Hi %s, i am the %s script." %(user_name, script)
print "Id like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(promt)

print "Where do you live %s" % user_name
lives= raw_input(promt)

print "what kind of computer do you have?"
computer = raw_input(promt)

print """

Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
and you have a %r computer. Nice.
""" % (likes, lives, computer)