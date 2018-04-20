from steem import Steem
import time
import re

s=Steem()

def follow_unfollow():
	x='a'
	y='a'
	current_follower=input("Number of follower:")
	current_following=input("Number of following:")
	follower=[]
	following=[]
	follower_=re.findall("'follower': '(.+?)'",str(s.get_followers('digital.mine',x,'blog',1000)))
	following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine',y,'blog',1000)))

	for i in follower_:
		follower.append(i)
	if len(follower)<int(current_follower):
		x=follower_[-1]
		follower_=re.findall("'follower': '(.+?)'",str(s.get_followers('digital.mine',x,'blog',1000)))
		for i in follower_:
			follower.append(i)
	print ('follower:',len(follower))

	for i in following_:
		following.append(i)
	if len(following)<int(current_following):
		x=following_[-1]
		following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine',x,'blog',1000)))
		for i in following_:
			following.append(i)
	print ('following:',len(following))
	
	num=len(follower)
	while num>0:
		for i in follower:
			if  i  not in following:
				s.follow(i)
				print ('follower:',i)
			num-=1

	num=len(following)
	while num>0:
		for i in following:
			if  i not in follower:
				s.unfollow(i)
				print ('following:',i)
			num-=1

follow_unfollow()
