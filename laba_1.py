from xml.dom.minidom import parse
import xml.dom.minidom
import lxml
from lxml import etree 


DOMTree = xml.dom.minidom.parse("library.xml")
collection = DOMTree.documentElement
authors = collection.getElementsByTagName("Author")
for author in authors:
	id = author.getAttribute("id")	
	name = author.getAttribute("name")
	print(id, name)
	books = author.getElementsByTagName("Book")
	for book in books:
		name = book.getAttribute("name")
		print("\t", name)

# Створення схеми і перевірка
xml_validator = lxml.etree.XMLSchema(file="schema.xsd")
xml_file = lxml.etree.parse("library.xml")
is_valid = xml_validator.validate(xml_file)


# Створюємо кореневий елемент
root = xml.dom.minidom.Document()
xml = root.createElement('library')
root.appendChild(xml)
author1 = root.createElement("author");
author1.setAttribute("id", "1");
author1.setAttribute("name", "IvanFranko");
xml.appendChild(author1)
author2 = root.createElement("author");
author2.setAttribute("id", "2");
author2.setAttribute("name", "TarasShevchenko");
xml.appendChild(author2);

book1 = root.createElement("book");
book1.setAttribute("id", "1");
book1.setAttribute("name", "Moisei");
book1.setAttribute("pages", "150");
book1.setAttribute("isadult", "1");
xml.appendChild(book1);
book2 = root.createElement("book");
book2.setAttribute("id", "2");
book2.setAttribute("name", "FarbovanyiLys");
book2.setAttribute("pages", "50");
book2.setAttribute("isadult", "0");
xml.appendChild(book2)
xml_str = root.toprettyxml(indent="\t")
save_path_file = "libraries.xml"
with open(save_path_file, "w") as f:
	f.write(xml_str)

class Author:
	def __init__(self, id, name):
		self.id = id
		self.name = name		

class Book:
	def __init__(self, id, name, isadult, pages, author):
		self.id = id
		self.name = name
		self.isadult = isadult
		self.pages = pages
		self.author = author
# Оголошуємо масив авторів
authors = []
authors.append(Author(1,'IvanFranko'))
authors.append(Author(2,'TarasShevchenko'))

class UkrAuthors:
	authors = []
	books = []
	def getAuthor(self, name): 
		try:
			DOMTree = xml.dom.minidom.parse("library.xml")
			collection = DOMTree.documentElement
			authors = collection.getElementsByTagName("Author")
			author=Author(self.id,self.name)
			for author in authors:	
				name = Author.getAttribute("name")
		except:
			print("can not find author with that name")	
	def getAuthorId(self, id):
		try:
			DOMTree = xml.dom.minidom.parse("library.xml")
			collection = DOMTree.documentElement
			authors = collection.getElementsByTagName("Author")
			author=Author(self.id,self.name)
			for author in authors:	
				name = Author.getAttribute("id")	
		except:
			print("can not find author with that id")

	def countAuthors(self):
		try:
			DOMTree = xml.dom.minidom.parse("library.xml")
			collection = DOMTree.documentElement
			authors = collection.getElementsByTagName("Author")
			author=Author(self.id,self.name)	
			authors = sum([1 for entry in dom.getiterator('author')])
			print(authors)
		except:
			print("can not find list of authors")
	def saveToFile(self, filename):
		et.write('library.xml')

	def addAuthor(self, id, name):
		xmlFile = minidom.parse( 'library.xml' )
		for author in AUTHORS:
				newAuthor = xmlFile.createElement("author")
				newAuthor.setAttribute("id", author.id)
				newAuthor.setAttribute("name", author.name)
				newAuthorText = xmlFile.createTextNode( author.description )
				newAuthor.appendChild( newAuthorText  )
		xmlFile.childNodes[0].appendChild( newAuthor)

	def deleteAuthor(self, id):
		for node in tree.iter():
			if tag == 'author':
				node.remove()

