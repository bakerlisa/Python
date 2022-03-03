from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author
from flask_app.models.book_author_model import Book_Author
from flask_app.models.genre_model import Genre
from flask_app.models.series_model import Series
from flask_app.models.book_series_model import Book_Series
from flask_app.models.book_genre_model import Book_Genre

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ROUTE: Search for a book
@app.route('/books')
def books():
    return render_template('books.html')

# ROUTE: add a book
@app.route('/add_book')
def add_book():
    if 'books' not in session: 
        # Added it so data will presist if error is thrown (because...this is a heavily validated part of the website)
        session["books"] = data = {"title": "", "first_name": "", "last_name": "", "series_name": "", "num_series": "",  "page_num": "", "isbn": "", "genre": "", "description": "", "img": ""}
    return render_template('add_book.html')

# INSERT: new book to database
@app.route('/add_new_book',methods=["POST"])
def add_new_book():
    data = {
        "title": request.form['title'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "series_name": request.form['series_name'],
        "num_series": request.form['num_series'],
        "page_num": request.form['page_num'],
        "isbn": request.form['isbn'],
        "genre": request.form['genre'],
        "description": request.form['description'],
        "img": request.form['img']
    }
    # 1. check uniquness
    unique_author = Author.is_author_unique(data)
    unquie_isbn =  Book.is_isbn_unique(data)

    #1. overall input validations
    if not Book.validate_book(request.form):
        #1. make sure all required fields are vaild
        session["books"] = data
        return redirect('/add_book')
    else:
        #2. unique author : get author_id
        if len(unique_author) > 0:
            author_id = unique_author[0]["id"]
        else:
            author_id = Author.add_new_author(data)
        
        
        #3. ISBN !exsits 
        if not len(unquie_isbn) == 0:
            flash("ISBN already exsits. Check our database for the book. If we've made a mistake contact support.","books")
            return redirect('/add_book')
        else:
            
            #1. add new book to database
            new_book_id = Book.add_new_book(data)

            #2. add book_id and author_id to books_authors
            dataBookAuthor = {
                "book_id" : new_book_id,
                "author_id" : author_id
            }
            add_book_author = Book_Author.add_new_book_author(dataBookAuthor)

            #3. Genre information
            # if it has a genre
            if len(request.form['genre']) > 0:
                genres_string = request.form['genre']
                genre = genres_string.split(",")

                for cat in range(0,len(genre)):
                    dataCat = {
                        "genre" : genre[cat]
                    }
                    category = Genre.category_exsist(dataCat)
                    genre_id = category
                    print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")
                    print(genre_id)

                    if len(category) == 0:
                        genre = Genre.add_new_genre(dataCat)
                        genre_id = category[0]["id"]

                    #add to reference table
                    dataCatBook = {
                        "book_id" : new_book_id,
                        "genre_id": genre_id
                    }
                    new_genre = Book_Genre.add_new_book_genre(dataCatBook)

                # 4. if unique : add series && add book to new series
                if len(request.form['series_name']) > 0:
                    unique_series = Series.is_series_unique(data)

                    #new series add it to data base
                    dataSeries = {
                        "series_name" : request.form['series_name'],
                        "book_id" : new_book_id
                    }
                    new_series_id = Series.add_new_series(dataSeries)
                else:
                    dataSeries = {
                        "series_name" : unique_series,
                        "book_id" : new_book_id
                    }
                    new_series_id = Series.add_new_series(dataSeries)
                
            #5. check num in series
            # if in a series
            # if len(request.form['num_series']) > 0:
            #     dataBookSeries = {
            #         "book_id": new_book_id,
            #         "series_id" : new_series_id,
            #         "num" : request.form['num_series']
            #     }
            #     unique_series_order = Book_Series.is_series_order_unique(dataBookSeries)
            #     if not len(unique_series_order) == 0:
            #         flash("Hmmm...Looks like that book in the series already exsists. Double check your inputs. If still inccorect contact support.")
            #         return redirect('/add_book')
            #     else:
            #         Book_Series.add_book_to_series(dataBookSeries)
            return redirect(f"/single_book/{new_book_id}")


# ROUTE : to single book
@app.route('/single_book/<int:id>')
def singel_book(id):
    return render_template('single_book.html')