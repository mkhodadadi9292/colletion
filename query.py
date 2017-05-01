import couchdb
import random
import string
a=[]
b=[]
couch=couchdb.Server()
if "new1" in couch:
	db=couch['new1']
else:
	db=couch.create('new1')

for i in range(1,10):
	ran =''.join([random.choice(string.ascii_letters)for n in xrange(3)])
	ran_1 =''.join([random.choice(string.ascii_letters)for n in xrange(3)])
	doc = {'first_name':ran, 'last_name':ran_1}
	db.save(doc)
	print doc
for i in range(1,1000):
	ran =''.join([random.choice(string.ascii_letters)for n in xrange(3)])
	ran_1 =''.join([random.choice(string.ascii_letters)for n in xrange(3)])
	doc = {'first_name':ran, 'last_name':ran_1, 'age':20}
	db.save(doc)
	print doc
