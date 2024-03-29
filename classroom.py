from flask import Flask, render_template

app = Flask('__name__')


# these are the view for the website
# each route is a view or webpage for the display
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/desks/')
def desks():
    return render_template('desks.html')

@app.route('/chairs/')
def chairs():
    return render_template('chairs.html')

@app.route('/books/')
def books():
    return render_template('books.html')

@app.route('/equipment/')
def equipment():
    return render_template('equipment.html')

if __name__ == '__main__':
    app.run()
    