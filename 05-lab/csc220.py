
# Ken Urban's module for csc220 
# TODO:
#    to incorporate forms using the GET method
# DONE:
#   automatic 'Content type'

import os
import sys
import getpass
from datetime import date
import urllib.parse

_formInfo = {}
_isItWeb = False
_outputDone = False
_version = "4.0"

def getInput(name='textarea'):
    global _isItWeb
    global _formInfo
    if not _isItWeb:
        return _formInfo[name]
    if name in _formInfo:
        return _formInfo[name][0]
    else:
        return ''

def showForm(comment='Sample Comment', method='POST'):
    global _isItWeb
    global _formInfo
    global _version
    if not _isItWeb:
        _formInfo['textarea'] = input("Enter the textarea:")
        _formInfo['textbox'] = input("Enter the textbox:")
        return
    print("<div class='w3-container w3-cell-middle w3-cell-row' >")

    print("<div class='w3-container w3-cell w3-blue-grey w3-card-4' >")

    today = date.today()
    print("<p>CSC220 form version {}.  Run on {}. </p>".format( _version, today ))
    print("<p>{}</p>".format( comment )) 
    print("</div>")
    

    print("<div class='w3-container w3-cell w3-khaki w3-card-4 ' >")
    print("<table align='center' cellpadding='4' bgcolor='khaki'>")
    print("<form method='{}'>".format(method))

    contents=getInput('textarea')
    print("<tr>") 
    print("<td align='right'>textarea</td>")
    print ("<td>")
    print("<textarea name='{}' rows='20' cols='80'>{}</textarea>".format( 'textarea', contents ))
    print("</td>")
    print("</tr>")

    contents=getInput('textbox')
    print("<tr>") 
    print("<td align='right'>textbox</td>")
    print("<td>")
    print("<input type='text' name='{}' value='{}' />".format( 'textbox', contents ))
    print("</td></tr>")

    print("<tr>") 
    print("<td align='right'>Click</td>")
    print("<td>")
    print("<input type='submit' value='Submit the contents and run the program'  />")
    print("</td><tr>")

    print("</form>")
    print("</table>")
    print("</div>")

    print("</div>")

# toplevel code
if 'REQUEST_METHOD' in os.environ:
    request_method =  os.environ['REQUEST_METHOD'];
    _isItWeb = True
    print("Content-type: text/html\n\n")
    print("<html><head>")
    print('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')
    print("</head><body>")
    #_w3css_panel("Request Method is {}".format( request_method ))
    if request_method == "GET":
        queryStr = os.environ['QUERY_STRING']     
        queryStr = queryStr.replace("%0D",'')
    elif request_method == "POST":
        queryStr = sys.stdin.read()
        queryStr = queryStr.replace("%0D",'')
    #_w3css_panel("Querystring is {}".format( queryStr ))     
    _formInfo = urllib.parse.parse_qs(queryStr)
    #for k in formInfo:
    #    line = formInfo[k]
    #    formInfo[k] = line.replace('\r', '')
    #_w3css_panel("Querystring is {}".format( _formInfo ))     

else:
    print("csc220 module is loaded.")




