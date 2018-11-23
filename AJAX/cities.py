#!/usr/bin/env python
import cgi,cgitb
cgitb.enable()
form=form.cgiFieldStorage()
city = form.getvalue('term')
name = form.getvalue('name')
def html():
    html = '<html>'
    html += '<head>'
    html += '<title>{} in {}</title>'.format(name,city)
    html += '</head>'
    html += '<body>'
    html += '<p>{} lives in {}</p>.format(name,city)
    html += '</body>
    html += '</html>'
    print(html)
if __name__=="__main__":
    print(html)

'''cities = ['New York', 'London', 'Los Angeles',
          'Paris', 'San Francisco', 'Adelaide']

if environ['PATH_INFO'] == "/suggestjson":
    return suggest_json_application(environ, start_response)


def suggest_json_application(environ, start_response):
    //Return JSON array of completions for a city name

    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)

    if form.has_key('term'):
        print "form has key"
        q = form.getvalue("term", "")
        matches = [c for c in cities if c.lower().startswith(q.lower())]
    else:
        print "form has no key"
        matches = []

    return json.dumps(matches)'''
