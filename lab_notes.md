code everything in one script. 
Main idea behind Part1: make title list
	read a file: title, url >> translate it into a dictionary where key== title , value==[number, url]
	get the data and store it in a variable in a specific format

Part 2:
	read data from urls
	use urllib
	main idea, take url, get a response; process response and stoe it in a certain form. 
	[word: [count of the word in book1, count of the word in book2]]
	we have a file that points to local ischool servers; files contain 10 books each. 

PArt 3: 
	once you have count for every word.
	ask for input, search for input from dict and print output
	functions to print diff outputs in diff formats

Extra:
	how do you create the file from a webpage. get the file names from the website. with the names you'll also have url, which is embedded in the html of the page. 
	tranform it into the right format. 

You can use regular expressions. Keshav will give us code to ignore spaces and special characters. Use that to clean the file. 

urllib: get data from online resources
	if you ask google servers for a fb page, it won't respond. 
	urllib helps you do these request/respond transactions
	we'll use 2 or 3 methods from urllib. 
	request library handles requests you send and responses. but what if something goes wrong? use the error library to handle exceptions
		except (er.URLError):
			content = ""
			print("url not working")
	it could be any kind of file based on what your requested. 
		re.urlopen(url) is like file.open()
		so you use file.read() just like with txt. use response.close()
	with in URLError, ther eare specific erros you could get. 

try:
	response = re.urlopen(url) #might get that webpage, you may not
	