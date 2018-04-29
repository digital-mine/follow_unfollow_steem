from steem import Steem
import time
import re

s=Steem()

def follow_unfollow():
	x='a'
	y='a'
	inc=0
	follower=[]
	following=[]
	follower_=re.findall("'follower': '(.+?)'",str(s.get_followers('digital.mine',x,'blog',1000)))
	following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine',y,'blog',1000)))

	for i in follower_:
		follower.append(i)
	while inc==0:
		if len(follower_)==1000:
			x=follower_[-1]
			follower_=re.findall("'follower': '(.+?)'",str(s.get_followers('digital.mine',x,'blog',1000)))
			for i in follower_:
				if i not in follower:
					follower.append(i)
		else:
			x=follower_[-1]
			follower_=re.findall("'follower': '(.+?)'",str(s.get_followers('digital.mine',x,'blog',1000)))
			for i in follower_:
				if i not in follower:
					follower.append(i)
			inc=1
	print ('follower:',len(follower))
	incc=0
	for i in following_:
		following.append(i)
	while incc==0:
		if len(following_)==1000:
			x=following_[-1]
			following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine',x,'blog',1000)))
			for i in following_:
				if i not in following:
					following.append(i)	
		else:
			x=following_[-1]
			following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine',x,'blog',1000)))
			for i in following_:
				if i not in following:
					following.append(i)
			incc=1
	print ('following:',len(following))
	
	num=len(follower)
	count=0
	while num>0:
		for i in follower:
			if  i  not in following:
				s.follow(i)
				print ('follower:',i)
				count+=1
			num-=1
			if count==1000:
				count=0
				time.sleep(3600)
			

	num=len(following)
	count=0
	while num>0:
		for i in following:
			if  i not in follower:
				try:
					s.unfollow(i)
					count+=1
				except Exception:
					pass
					print (i, 'FAILED')
				print ('following:',i)
			num-=1
			if count==1000:
				count=0
				time.sleep(3600)

follow_unfollow()
