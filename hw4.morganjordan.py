# Morgan Jordan
# INFO 206
# morgan.jordan@berkeley.edu
# hw4-test-morganjordan.txt



import urllib.request
import urllib.parse
from operator import itemgetter

# from collections import defaultdict

def open_file():
	with open('catalog.txt', 'r') as file_handle:
		Books = {}
		file_list = file_handle.read()

	file_list = file_list.splitlines()
	return file_list

def Books():
	file_list = open_file()
	Books = {}
	titles = []
	urls = []
	for item in file_list:
		if item.split(',')[0] != '': #accounts for empty lines in the .txt
			titles.append(item.split(",")[0]) 

	for item in file_list:
		if item.split(',')[0] != '': #accounts for empty lines in the .txt
			try:
				urls.append(item.split(",")[1])
			except:
				print("<<<catalog.txt not readable>>>")
				exit()

	for i, book in enumerate(file_list):
		try:
			Books[file_list[i].split(",")[0]] = [i, file_list[i].split(",")[1]]
		except:  #this handles empty lines in the .txt. Because they don't have anything to 'split,' they'll throw an error
			continue 

	return Books, titles, urls




def words_dict():	
	dictionary = Books()[0]
	file_list = open_file()
	
	Words = {} 
	val_list = [] #values of each word-count. index corresponds to book place number
	count = 0
	i = 0
	urls = Books()[2]
		
	for item in dictionary.values():
		url = item[1]
		content = urllib.request.urlopen(url)
		content = content.read().decode('utf-8')
		# THIS WAS MY ATTEMPT AT RESOLVING BROKEN URLS. IT CREATED OTHER ERRORS/PROBLEMS IN THE CODE THAT I DIDN'T HAVE TIME TO RESOLVE
		# try:
		# 		content = urllib.request.urlopen(url)
		# 		content = content.read().decode('utf-8')		
		# except urllib.error.HTTPError:
		#		print("url on line ",i+1," not readable.")

		filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
		text = [x for x in map(filter_punc, content.split()) if x]

		for word in text:
			Words[word] = [] 
	val_list = list(len(dictionary)*" ")
	while i < len(dictionary):
		book_dict = {}
		content = urllib.request.urlopen(urls[i])
		content = content.read().decode('utf-8')		
		filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
		text = [x for x in map(filter_punc, content.split()) if x]
		for word in text:
			book_dict[word] = 1 + book_dict.get(word, 0)
			
		for word in Words.keys(): #populating the the WordCount(s) list 
			if word not in book_dict.keys():
				Words[word].append(0) # value is 0 if word is not in the book
			else:
				Words[word].append(book_dict[word]) 
		i += 1
		continue	
	return Words
	
def search():
	Words = words_dict()
	urls = Books()[2]
	titles = Books()[1]
	catalog = Books()[0]
	query = ""
	while(True):
		results_list = [] # this was supposed to hold the search results, so I could print them in descending order. 
		i = -1
		count = 1
		query = ""
		try:
			query = input("Search term?  ")
			if query == "<terminate>":
				break
			elif query == "<catalog>":
				for key in catalog:
					print(key, catalog[key])
			elif query == "<titles>":
				for title in titles:
					print(title)
			else:
				while i < len(titles)-1: # THE COMMENTED CODE BELOW WAS MY ATTEMPT TO PRINT THE RESULTS IN DESCENDING ORDER
					# if Words.get(query)[i] == 1:
					# 	results_list.append("{}.  The word {} appears {} time in {} (link: {})".format(count, query, Words.get(query)[i], titles[i], urls[i]))
					# else: 
					# 	results_list.append("{}.  The word {} appears {} times in {} (link: {})".format(count, query, Words.get(query)[i], titles[i], urls[i]))
					if Words.get(query)[i] == 1:
						print("{}.  The word {} appears {} time in {} (link: {})".format(count, query, Words.get(query)[i], titles[i], urls[i]))
					else:
						print("{}.  The word {} appears {} times in {} (link: {})".format(count, query, Words.get(query)[i], titles[i], urls[i]))
					i += 1
					count += 1
					continue
				# for result in results_list:
				# 	print(sorted(result, key=Words.get(query)[i]))
				
		except: #to account for words entered that are not in the tree. Otherwise, it would throw an attribute error
			print("The word {} does not appear in any books in the library.".format(query))	
		
def main():
	search()

if __name__ == '__main__':
	main()