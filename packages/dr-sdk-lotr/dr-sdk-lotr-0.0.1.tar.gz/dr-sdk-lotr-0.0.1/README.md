# The Lord Of The Rings SDK
A SDK built upon The One API (https://the-one-api.dev/) written in Python.

## Installation
pip install dr-sdk-lotr==0.0.1

## Usage
To use the SDK, get an Access Token from https://the-one-api.dev/sign-up. Once installed and the Access Token is obtained, you can start using the SDK by following the below:

## Using the SDK

### Book Data
```
from dr_sdk_lotr.books import Books

books = Books('YOUR_API_KEY')

# Lists of all "The Lord of the Rings" Books
books.get_books()

# Request one specific Lord of the Rings book by ID
books.get_book_by_id('5cf58077b53e011a64671583')

# Request all chapters of one specific book
books.get_book_by_id('5cf58077b53e011a64671583')
```

### Character Data
```
from dr_sdk_lotr.chracters import Characters

characters = Characters('YOUR_API_KEY')

# Lists of all characters including metadata like name, gender, realm, race and more
characters.get_all_characters()

# Request one specific character by id
characters.get_character_by_id('5cd99d4bde30eff6ebccfbed')

# Request all movie quotes of one specific character
characters.get_quotes_by_character_id('5cd99d4bde30eff6ebccfbed')

# Get character details by name
characters.get_character_by_name('Gandalf')
```

### Movie Data
```
from dr_sdk_lotr.movies import Movies

movies = Movies('YOUR_API_KEY')

# List of all movies including "The Lord of the Rings" and the "The Hobbit" trilogies
movies.get_movies()

# Request one specific movie by id
movies.get_movie_by_id('5cd95395de30eff6ebccde56')

# Request all movie quotes for one specific movie (only working for LOTR Trilogy)
movies.get_all_quotes_by_movie('5cd95395de30eff6ebccde5c')
```

### Quote Data
```
from dr_sdk_lotr.quotes import Quotes

quotes = Quotes('YOUR_API_KEY')

#  List of all movie quotes
quotes.get_all_movie_quotes()

# Request one specific movie quote
quotes.get_movie_by_id("5cd96e05de30eff6ebccebce")
```

### Chapter Data
```
from dr_sdk_lotr.chapters import Chapters

chapters = Chapters('YOUR_API_KEY')

# Lists of all book chapters
chapters.get_all_book_chapters()

# Request one specific book chapter
chapters.get_book_chapter_by_id('6091b6d6d58360f988133bc5')

# Get book chapter by name
chapters.get_book_chapter_by_name('A Long-expected Party')