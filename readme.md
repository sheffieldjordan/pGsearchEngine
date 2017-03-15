Homework 4: A Project Gutenberg search engine.


PHASE 1

Loads the search engine with the catalog of books through which it will search. It does this by reading a file provided: "catalog.txt”.

For example, catalog.txt could contains the following:
 
Pride and Prejudice,http://<a href="http://www.gutenberg.org/cache/epub/1342/pg1342.txt" target="_blank">www.gutenberg.org/cache/epub/1342/pg1342.txt</a>
The Yellow Wallpaper,http://<a href="http://www.gutenberg.org/cache/epub/1952/pg1952.txt" target="_blank">www.gutenberg.org/cache/epub/1952/pg1952.txt</a>

The program creates a dictionary Books with the book titles as a key.  For each key, the program assigns a value which is itself a 2-item list containing (a) a unique sequential number, starting with 0 and (b) the URL of the book.

For the above example, the contents of the dictionary Books is thus
 
{ 'Pride and Prejudice' : [0, '<a href="http://www.gutenberg.org/cache/epub/1342/pg1342.txt" target="_blank">http://www.gutenberg.org/cache/epub/1342/pg1342.txt</a>'], 'The Yellow Wallpaper' : [1, '<a href="http://www.gutenberg.org/cache/epub/1952/pg1952.txt" target="_blank">http://www.gutenberg.org/cache/epub/1952/pg1952.txt</a>'] }

At the same time, the program also makes a list Titles containing the titles of the books in book number order, e.g.,
 
['Pride and Prejudice', 'The Yellow Wallpaper']

We will give you two catalog.txt files -- one containing the top 10 titles on Project Gutenberg and the other one containing links to several short text files for debugging purposes.

PHASE 2

In the second phase, the program populates the search engine with the contents of the books in the catalog. The program uses urllib to open the URL of the books in the catalog, read the text file found at each URL and count the words. It creates a dictionary Words with words as an index.  

The value associated with each word will itself be a list, counting the frequency of that word in each book in the catalog, using the book numbers as an index to WordCounts.  

For example, if “declared" occurs 15 times in Pride and Prejudice but only once in The Yellow Wallpaper, while "daughters" occurs 50 times in Pride and Prejudice but does not occur in The Yellow Wallpaper, then:

The corresponding entries in the dictionary would be
 
Words['declared'] = [15, 1]
Words['daughters'] = [50, 0]

PHASE 3

The program also performs a search engine function based on input from the user.  It will run a loop asking for search words until it receives the word “<terminate>”.  It should report books sorted in the order of how many times a word appears in the book.

It uses the following debug commands:

“<catalog>” - prints out the contents of the dictionary Books in an easy to read format
“<titles>” - prints out the contents of the list Titles in an easy to read format

Here is a sample session:
 
Search term?  declared
1.  The word declared appears 15 times in Pride and Prejudice (link:  http://<a href="http://www.gutenberg.org/cache/epub/1342/pg1342.txt" target="_blank">www.gutenberg.org/cache/epub/1342/pg1342.txt</a>)
2.  The word declared appears 1 time in The Yellow Wallpaper (link:  http://<a href="http://www.gutenberg.org/cache/epub/1952/pg1952.txt" target="_blank">www.gutenberg.org/cache/epub/1952/pg1952.txt</a>)

Search term?  daughters
1.  The word daughters appears 50 times in Pride and Prejudice (link:  http://<a href="http://www.gutenberg.org/cache/epub/1342/pg1342.txt" target="_blank">www.gutenberg.org/cache/epub/1342/pg1342.txt</a>)

Search term?  groucho
The word groucho does not appear in any books in the library

Search term?  <catalog>
'Pride and Prejudice' : [0, '<a href="http://www.gutenberg.org/cache/epub/1342/pg1342.txt" target="_blank">http://www.gutenberg.org/cache/epub/1342/pg1342.txt</a>']
'The Yellow Wallpaper' : [1, '<a href="http://www.gutenberg.org/cache/epub/1952/pg1952.txt" target="_blank">http://www.gutenberg.org/cache/epub/1952/pg1952.txt</a>']

Search term?  <titles>
Pride and Prejudice
The Yellow Wallpaper

Search term?  <terminate>

hw4catalog.txt - this is a catalog file of the top 10 Project Gutenberg e-books
hw4localcatalog.txt - this is a locally stored catalog file of the top 10 Project Gutenberg e-books
hw4simplecatalog.txt - this is a catalog file pointing to several very short and simple books -- for debugging purposes.