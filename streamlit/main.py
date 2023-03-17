import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('''Comparison On Data Insertion and Retrieval of BTree and Hash Map Data Structures''')
st.markdown(''' Ali Fathi, Serkan Hiziroglu, Jonathan Koerber Affiliation (CS622, MSCS City University Seattle) ''')
st.markdown(''' fathiali@cityuniversity.edu, hizirogluserkan@cityuniversity.edu, koerberjonathan@cityuniversity.edu ''')

st.header('Abstract')
st.info('In this paper, we will take a deep dive into two data structures, BTree, and Hash Map, to understand how the two strategies compare in terms of time and space complexity. We want to understand the benefits and disadvantages of both data structures and, through the body of the paper, illiterate use cases for both structures. By presenting a review of current literature on both BTree and Hash Maps, with come to an understanding of how both compare in terms of time and space complexity for both insertion and deletion. We will present a rudimentary domain name server running benchmark tests on both data structures.')
st.markdown(
    '**Keywords**: *Balanced Trees*, *Hash Map*, *Domain Name Server*, *DNS*')

image = Image.open('introduction.png')
st.image(image, caption='Introduction')

st.header('Memory Management')
st.markdown('''In many descriptions of data, futuristic words like cloud storage and big data make us think that we should start thinking about mortgaging a condo in a cloud city and shopping for a lease of a flying car. But what are we talking about? It all comes down to one and zeros in computer memory. A particular data structure performance is liked by how well it organizes the data into memory, similar to how algorithms can use these structures to perform CRUD operations (Goodrich et al., 2013).  
 

We must remember that the data structure we have implemented will live in memory. All of the instructions and data are stored in memory registers. Any efficiency gained in processing is a direct result of how easily the system can access data while both data structures are trying to accomplish the same functionality, given a key string return a value.  
 

The two data structures that compare are a BTree and Hash Map. Each will have elements inserted from an unsorted list. Our example domain name server will contain a zone containing a target key, a URL, and the values we are interested in, the IP address. Both the balanced tree and Hash Map are trying to solve the same problem, return values from keys, in a timely fashion, but that is where the similarities stop. ''')
st.header('BTrees')
st.markdown('''BTree or Balanced Trees are a type of search tree that is based concept of binary search. This data structure is conducive when indexing databases and quickly searching large data sets. Search trees are data structures that organize data with pointers, allowing fragmented data to be searched efficiently. BTrees are unique in search trees as they attempt to solve one of the short comings of search trees that they can become unbalanced, which can result in poor search performance. 
 

A binary search algorithm searches an ordered list for a value in log N time. Binary search accomplishes this by reducing the search area by half for each operation. Given a sorted list, it finds the middle index by using modulo division on the length of the list. It then evaluates the value to see if the target is greater or less than the value at the middle index. If the target is larger than the value, the same operation is performed on the sub list from the previous middle value to the end of the list. If the target is less than the value, the search continues from the beginning of the slit to the middle value. BTrees take this concept and build a data structure that allows insertion from an unordered list, maintaining a similar length to all the branches (Search Tree, 2022).  
 

In a search tree, each value at the middle of the list becomes a node, and each time the list is broken apart, the tree gains a level. As a data structure for search, these perform well if used in an application with many inserts and deletions. Maintaining an efferent structure will require a lot of computation resources. While search trees offer an efficient search, they aren’t able to store data in the way that we are looking for. The significant downsides are that the search trees can become unbalanced as items are added and removed. They lack a way of reordering their nodes.  
 

BTrees try to balance the efficiency structure to use a binary search algorithm but avoid the tree but do not need to start with a sorted list. To implement a BTree in a real-world application, we need an interface to insert records and search by providing a key. Our BTree must also be able to balance itself when inserting records.  
 
We implement two classes in our BTree (Introduction of BTree, 2013). The first, BtreeNode, is an object that has three variables. The first leaf is a Boolean showing whether or not the node has data. Then two are lists, keys, and child. These are the values that the search algorithm uses to find a value. If the leaf value is false, we will use the keys list to hold the data values. When data is added to the tree, we will use sets with two values, key and value, and when we search, we will return a value object. 

For our test, we are looking to find how search speed is affected by the size of the data set and how many levels are in the BTree hierocracy. To make our comparison fair, we’ll use the same process for the BTree as for the Hash Map. Since our use case is for storage for a domain name server, we’ll store our values with a key and zone object.''')

image = Image.open('bTree1.png')
st.image(image, caption='Structure of a BTree')

image = Image.open('bTree2.png')
st.image(image, caption='Structure of a BTree')

st.header('Hash Map')
st.markdown('''In Python, dictionaries are a very useful data structure that is a Hash Map that can given a key can return a value in constant or O(1) (TimeComplexity - Python Wiki). This is very remarkable. Here we will build our own implementation following literature (Goodrich et al., 2013) to try and understand its inner workings. We can implement this in Python and observe search times as the structure grows to see its advantages.  
 

Let's start by understanding Hash Maps at a high level. The data structure gets its name from how it decides where it will store a given key. It takes a hash value of a string or integer key value and returns a practical integer value. Often, a hash function will multiply an import by a large prime number. The result of with is too large to be practical, so it is then compressed into a more manageable value (Data Structures and algorithms). While it is more efficient concerning their program's memory, it does lead to name collision. (Hash Map in Python, 2020). What does this mean? In practice, the hash function creates a value that we then compress to get a bucket to sort the value into different buckets. When the Hash Map is searched, the Hash Map object can reverse the process, find the storage bucket then return the value. 
 

Name collision in a hash table is one of the technical hurdles that must be dealt with to have a robust data structure. Although rare, if a key is passed to a hash function, it multiplies the key by a prime number and then compresses the product. There lies the possibility of having two keys that return the same result. While there are many ways to solve this challenge, the most are by having an undistorted list to contain collisions. This adds some overhead, making it necessary to search through an unordered list of collided keys or by having a probing algorithm look for empty storage locations (Goodrich et al., 2013). In our structure, we have chosen to have a fixed number of buckets, so we cant test performance when keys collide—allowing us to set the number of buckets for each test. 
 

The Hash Map that will be used for this paper is designed to do something other than outright performance but rather to test some behaviors of Hash Maps. We are trying to see how the data structure behaves in deferent amounts of data. Our Hash Map is designed in a way that we set the number of buckets, so we can force key collision and see how search preference is affected by different data loads.  
 

The Hash Map that we implement when implemented uses a two-denominational array that acts as buckets for our zone objects. When initialized, the __init__ function takes a size variable that denotes the number of buckets the in the array. When a key-value pair is inserted, the Hash Map object runs a hash function which is then compressed to match up with one of the buckets. When searching, the key is hash and compressed to find the bucket holding value from the Hash Map. ''')


image = Image.open('hMap1.png')
st.image(image, caption='Structure of a Hash Map')


image = Image.open('hMap2.png')
st.image(image, caption='Structure of a Hash Map')

st.header('Testing')
st.markdown('''To find out the answer to how the two data structures hold up to each other, we will compare the two structures. Our goal for this project is to see how the two data structures perform as they are scaled up to store more data. As discussed in earlier sections, both the BTree and hash map implementations, we can control the shape of the structure by setting the number of levels in the case of the BTree and, in the case of the hash map, the number of buckets.''')
st.markdown('''We started with our hash map data structure. Hash maps offer an O(1) insert, delete, and search best case and O(n) in the worst case. As discussed earlier, the cause of poor performance is the handling of key conclusions within the data structure. In implementing the hash table, we can set the number of buckets used to store data. In the literature, .75 is regarded {} as a good trade-off between space and speed, but we wanted to see how that would look. We created one thousand records of dummy data and made hash tables with different amounts of data buckets, starting with fifty and working our way up to a thousand. We found that while very few containers poorly performed, we saw that even with a load factor of .3, we saw some noticeable performance increases. We will use .75 as our load factor for the rest of the test. ''')
image = Image.open('HTableSearch.png')
st.image(image, caption='Hash Table Search Performance 1000 Records')

st.markdown('''In contrast to the hash table, the BTree is a very different structure. The BTree builds itself with a series of layers to store the data keys and then allows the binary tree to search for a key. In our first test, we will perform some tests while changing the number of layers the structure has. We will start with zero levels and work up to 1000 in multiples of 50. We get the most performance in a sweet spot of about .07. Two layers or too high and have poor performance. Either case would require a lot of extra work on the part of the algorithm to search for a value.''')
image = Image.open('BtreeSearch.png')
st.image(image, caption='BTree Search Performance 1000 Records')

st.markdown('''The following two tests test how the two data structures scale in space and time. In the previous test, we found that the hash table needed seventy-five percent of the total amount of records as buckets, and for the BTree, we needed seven percent of the total amount of records as layers for the best results. Above is a graph showing search time as the number of records increases. In the graph Hash Table vs. BTree Search, you can see that depending on where the target values are entered in the tree can cause a more extended search time and the size of the data set—resulting in very unpredictable search times. The Hash Table, in contrast, when properly sized to avoid collisions, has a high-speed performance and scales very well, making it ideal for many applications. In the table above, we can see that both structures average time. We observed the BTree scales as expected with O(logN) and the hash map scales with O(1). The green line shows the BTree search time is a bit erratic but averages out to O(logN).''')
image = Image.open('HashvsBTree.png')
st.image(image, caption='Hash Table Search vs BTree Search')

st.markdown('''Next, we created a test to see how our data structures scale with regard to space. We have results that are in keeping with what the literature states; however, we need more confidence in the accuracy of the results. Collecting results for the hash table was straightforward. As the data structure was created, we could use pythons ‘sys.getsizeof’ to find the size of the hash table object. The result was the size of the data usage, which was below the test data size. In python, objects are passed by reference, so we took this to mean that the hash table only held a reference to the data and not the data itself. We wanted to show a better view of the data and the hash table, so in the graph, the hash table size is added to the data size. Our results seem too low, and we would like to investigate the results further and see if our method for measuring is accurate. 

To get the size of the b tree, we created a method based on the print method in the original code (Introduction of B-Tree, 2013). This recursive went through each node and returned the size and added. Like the hash table, we would like to confirm the results of measuring the data structure. Because of the nature of the layered within the structure, the b tree as space uses additional space to manage the keys and child nodes. The implementation of the b tree leaves much to be desired. In future work, we would like to be improved. The structure insert method uses a set of keys and values as a key in each layer, which adds to the structure's size when measured. ''')
image = Image.open('HashBvsTreeMemory.png')
st.image(image, caption='Hash Table Search vs BTree Memory Usage')

st.markdown('''Our goal for performing these tests was to understand each data structure better. Both of these structures are suited to very different situations while having some overlapping use cases.''')


st.header('Next steps')
st.markdown('''During this project, we have had to scale back the scope of our work. Initially, we had hoped to build robust implementations of both the BTree and Hash Map and test them using the Python network library twisted. While this would deliver a working domain name server and be a more robust deliverable, we needed our class to be more transparent to observe the inner workings, have more control of the test, and see the inner workings of the data structures.  
 
We opted to use data structures found on Geeks for Geeks. These data structures offered us good visibility into the inner working of the implementation. To suit our use case of working with string keys, we had to modify the BTree to work function with keys string rather than numbers. To test the structures, we constructed a Jupiter notebook to execute tests and build data to display in the data section. In addition, we would like to further explore testing strategies and  
 
The next steps for the project will focus on building optimization for each data class and exploring the types of implementation strategies. We have identified a more robust implementation of both data structures in Data Structures and Algorithms in Python that uses Python's MutibleMapping class (Goodrich et al., 2013). In the domain of Hash Maps, we would like to explore in more detail the different hash generation, compression, and collision handling schemes. With our BTree implementation, we would also like to explore other implementations of tree structures, focusing on how they self-balance the tree. With both the BTree and Hash Map, we would like to add a delete function to both structures and observe how they perform.  
 
In implementing the domain name server, we would like to build it into a more robust service capable of handling requests and populating its zone files by passing requests to an authoritative name server following the libraries documentation (Twisted, n.d). We also want to see how we can implement data persistence in our program. In a more robust server environment where we will handle concurrent requests, we must also implement a locking mechanism to handle data race conditions. ''')

st.header('References')
st.markdown(''' Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). Data Structures and Algorithms in Python. Wiley. http://ebookcentral.proquest.com/lib/cityuseattle/detail.action?docID=4946360 

Hash Functions and list/types of Hash functions. (2021, December 19). GeeksforGeeks. https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/ 

Hash Map in Python. (2020, December 6). GeeksforGeeks. https://www.geeksforgeeks.org/hash-map-in-python/ 

howCode. (2022). HowDNS - DNS Server by howCode [Python]. https://github.com/howCodeORG/howDNS/blob/2f7dff732cb5fa9d0ce3a9a0ba53da0901980db9/dns.py (Original work published 2016) 

Introduction of B-Tree. (2013, April 21). GeeksforGeeks. https://www.geeksforgeeks.org/introduction-of-b-tree-2/

Python, R. (n.d.). Generating Random Data in Python (Guide) – Real Python. Retrieved February 12, 2023, from https://realpython.com/python-random/ 

TimeComplexity—Python Wiki. (n.d.). Retrieved February 11, 2023, from https://wiki.python.org/moin/TimeComplexity 

Twisted. (n.d.). Retrieved February 4, 2023, from https://twisted.org/  

Search tree. (2022). In Wikipedia. https://en.wikipedia.org/w/index.php?title=Search_tree&oldid=1123746773 

''')

st.header('Appendix')

image = Image.open('diagram.png')
st.image(image, caption='URL Diagram of the System')

image = Image.open('bTree.png')
st.image(image, caption='BTree Implementation')

image = Image.open('HashTable.png')
st.image(image, caption='Hash Table Implementation')

image = Image.open('dns.png')
st.image(image, caption='DNS Class Implementation')
