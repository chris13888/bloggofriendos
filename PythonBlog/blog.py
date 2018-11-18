import flask
from flask_misaka import markdown, Misaka

import pkg_resources

import time

blogs = open(pkg_resources.resource_filename(__name__, '/blogs/blogs.txt')).read().split('\n')
app = flask.Flask(__name__)

Misaka(app)

@app.route('/blog/<string:blogtitle>/')
def show_blog(blogtitle):
    return flask.render_template('blog.html', content=open(pkg_resources.resource_filename(__name__, f'/blogs/{blogtitle}.md'), 'r', encoding='utf8').read())

@app.route('/rawblog/<string:blogtitle>/')
def return_blog(blogtitle):
    return markdown(open(pkg_resources.resource_filename(__name__, f'/blogs/{blogtitle}.md'), 'r', encoding='utf8').read())

@app.route('/blog/')
def blog():
    html = ''
    for blog in blogs:
        if blog == '':
            break
        link, name, date, description = blog.split('@')
        html += f'<button class="story" onclick=\'load("{link}", "{name}");\'><em>{name}</em><br>{date}<br><br>{description}</button>'
    open(pkg_resources.resource_filename(__name__, '/templates/links.html'), 'w').write(html)
    return flask.render_template('mainblog.html')

@app.errorhandler(404)
def not_found(error):
    return flask.render_template('error.html')

@app.errorhandler(500)
def not_found(error):
    return flask.render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
