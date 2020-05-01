import requests
from bs4 import BeautifulSoup
from random import randrange
import time
import sqlite3
import argparse

def SQLiteActivate():

	conn = sqlite3.connect('Insta_DB.db')
	c_conn = conn.cursor()
	c_conn.execute('CREATE TABLE IF NOT EXISTS insta_user (user_id INT PRIMARY KEY, user_name TEXT,full_name TEXT)')
	
def SQLiteDectivate():

	conn = sqlite3.connect('Insta_DB.db')
	c_conn = conn.cursor()
	c_conn.close()
	conn.close()

def SQLiteInsert(user_id,user_name,full_name):

	try:
		conn = sqlite3.connect('Insta_DB.db')
		c_conn = conn.cursor()
		c_conn.execute('INSERT INTO insta_user (user_id,user_name,full_name) VALUES (?,?,?)',(user_id,user_name,full_name))
		conn.commit()

	except:
		pass
	
def random_text(length):

	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l'
	,'m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	
	l = length
	RandomText =""
	i = 0
	while i < l:	 
		l_random_index = randrange(0,len(alphabet))
		l_random = alphabet[l_random_index]
		RandomText = l_random+RandomText		
		i = i+1
	print('\033[1;37mRandom Text to Search: ' + '\033[93m'+RandomText+'\033[1;m')
	CodeofaNinja(RandomText)

def CodeofaNinja(RandomText):

	IG_USER_LIST = []

	with requests.Session() as s:
	    url = 'https://codeofaninja.com/tools/find-instagram-id-answer.php?instagram_username={}'.format(RandomText)
	    GET_URL = s.get(url,verify=True)
	    soup = BeautifulSoup(GET_URL.content,'lxml')	    
	    StartDiv = soup.findAll('div',{'class':'overflow-hidden'})
	 
	    for i in StartDiv:
	    	Name_ID = i.find_all('b')
	    	try:
	    		user_id = str(Name_ID[0]).split("<b>")[1].split("</b>")[0]
	    		user_name = str(Name_ID[1]).split("<b>")[1].split("</b>")[0]
	    		full_name = str(Name_ID[2]).split("<b>")[1].split("</b>")[0]  		
	    	except:
	    		pass

	    	if user_name not in IG_USER_LIST:
	    		IG_USER_LIST.append(user_name)
	    		SQLiteInsert(user_id,user_name,full_name)
	for IG_USER in IG_USER_LIST:
		print('\033[92m'+IG_USER)
	
def CodeofaNinjaBot(iteration,IterationCounter,number):

	MyRange = [i for i in range(10)]
	counter = 1
	while counter < number+1:
		print()
		print('\033[1;96mBatch Number: '+str(IterationCounter)+ ' of ' + str(iteration)+'\033[1;m')
		print()
		print('\033[1;37mSearch Number: '+str(counter)+ ' of ' + str(number)+'\033[1;m')
		MyRange_random_index = randrange(0,len(MyRange))
		MyRange_random = MyRange[MyRange_random_index]
		random_text(MyRange_random)
		counter = counter +1
		
def Master(n):

	SQLiteActivate()
	
	iteration = int(n/100)+1
	
	if iteration < 2:
		iteration = 2
	
	for IterationCounter in range(1,iteration):
		CodeofaNinjaBot(iteration,IterationCounter,100)
		time.sleep(60)

	SQLiteDectivate()


def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("NumberofIGRequests", help="Number of IG Requests")
	args = parser.parse_args()
	Num_Requests = str(args.NumberofIGRequests)
	Master(int(Num_Requests))
	
if __name__ == '__main__':
	Main()

