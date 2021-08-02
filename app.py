from flask import Flask, app, render_template, send_from_directory, url_for
from flask_flatpages import FlatPages
from datetime import datetime

app = Flask(__name__)

app.config['FLATPAGES_EXTENSION'] = '.md'

pages = FlatPages(app)

@app.route('/<path:path>.html')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)


@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/blog')
def blog():
	posts = [p for p in pages if "date" in p.meta]
	sorted_pages = sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta['date'], '%d %b %y'))

	return render_template('blog.html', pages=sorted_pages)

# Handle gathering images
@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('images', path)


if __name__ == "__main__":
	app.run(debug=True)
