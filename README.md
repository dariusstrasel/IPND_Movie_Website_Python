# HTML Movie Website Generator

Overview: This Python program will generate a movie trailer website using first-order class objects.

# How to use:
1. Open data.py and add/remove preferred movies.
```python
models.Movie("Spirited Away",
                 "Chihiro Ogino, a sullen ten-year-old girl who, while moving to "
                 "a new neighborhood, enters the spirit world.",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Spirited_Away_poster.JPG/220px-Spirited_Away_poster.JPG",
                 "Hayao Miyazaki",
                 "2008",
                 "https://www.youtube.com/watch?v=ByXuk9QqQkk"),
```

2. Execute main.py: your output HTML will be inside the "./output" folder.

3.  Profit!

# API Documentation
* HTML is processed using Python standard string.Template class. (No templating engine!) And is looking for $movie_tiles:
```html
    <div class="container" id="movie-tile">
      $movie_tiles
    </div>
```

# Screenshot:
![Screenshot](capture.png)