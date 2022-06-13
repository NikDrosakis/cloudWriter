# coding=utf-8
import sqlite3,sys,os
sys.path.append('lib')
import mar,red,wiki,tok,grep
from flask import g, Flask, render_template, request,url_for,jsonify

DATABASE = '/var/www/sqlite/org.db'
#red.set('a','123');
#print(wiki.ask("Linkoln"), file=sys.stderr) 
#print(tok.tik("test"), file=sys.stderr) 

app = Flask(__name__)
@app.route('/', methods =["GET","POST"])
def home():
    getid=request.args.get("id") or "1"    
    print(getid, file=sys.stderr)
    rows=os.listdir('/var/www/store')
    #list dirs #onclick dirs change var folder ajax
    #list files #onclick file ajax read file
    print(rows)
    uri="/var/www/store/2022b.md";
    with open("/var/www/store/2022b.md", "r") as f:
        content = f.read()
        smaller=tok.tik("/var/www/store/2022b.md")
    #return render_template('index.html', rows = cur.fetchall(),content=content,smaller=smaller,id=getid,uri=uri)
    return render_template('index.html', rows = rows,content=content,smaller=smaller,id=getid,uri=uri)

@app.route('/ajax', methods=['POST','GET'])
def ajax():
    a=request.args.get("a")
    fun=request.args.get("fun")
    q=request.args.get("q")
    #if request.method == "POST":
        #res=request.get_json()
    #    print(getq)
    #if request.method == "GET":
    #    #res=request.get_json()
    #    print(getq)        
    #module = __import__(mod)
    #func = getattr(module, fun)
    #console.log(jsonify(func(q)))
    file="/var/www/store/ΣΥΛΛΟΓΗ ελευθερία ΤΕΛΙΚΑ13.docx".decode('latin-1').encode("utf-8")
    content=open(file).read().decode('string-escape').decode("utf-8")
    print(content)
    return content
    #return jsonify({a:a,q:q})
    #return jsonify(func(q))
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)  
   