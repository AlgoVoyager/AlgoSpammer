# AlgoSpammer
python script to spam anywhere on pc

Using CMD is recommended.

Requirements :- 

1 latest python

2 pyautogui  `pip install pyautogui`


## Multiple Options like:
#### *the spam lies where the cursor is...* ####
### 1. If run without providing any arguments-
`python AlgoSpammer.py`

this will click 'enter' infinite times untill you terminate program.

### 2. To spam only one word infinite times-
`python Algospammer.py yourWord`

### 3. To spam yourWord given no. of times-
`python Algospammer.py yourWord spamCount`

*or*

`python Algospammer.py yourWord 50`

*this will spam the word "yourWord" 50 times.*

### 4. To use default text file to spam-
`python Algospammer.py -uf`

*or*

`python Algospammer.py -usefile`

*this will read the default file in same directory to spam.*

  edit the default text file

### 5. To use custom text file to spam-
`python Algospammer.py -uf custom_filename.extention`

*or*

`python Algospammer.py -usefile custom_filename.extention`

*must provide full filename with extention*

`python Algospammer.py -uf custom.txt`


### 6. To use any file to spam given number of times-
`python Algospammer.py -uf filename.extention spamCount`

ex-

`python Algospammer.py -uf anyfile.txt 50`

*this will read file and spam given no. of times*


### Upcoming features are coming soon, like-
#### > take custom sentence as input, and their options like spam count etc.