from flask import Flask,render_template,redirect,url_for,request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/emreercan/Documents/GalataQR/database.db'
db = SQLAlchemy(app)
app.app_context().push()
@app.route("/")
def index():
    return render_template("main.html")
@app.route("/kahvaltı")
def kahvaltı():
    fdiv = "fdivk.jpg"
    ürünler = Kahvalti.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/tost")
def tost():
    fdiv = "fdivt.jpg"
    ürünler = tost.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/hamburger")
def hamburger():
    fdiv = "fdivh.jpg"
    ürünler = hamburger.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/pizza")
def pizza():
    fdiv = "fdivp.jpg"
    ürünler = pizza.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/makarna")
def makarna():
    fdiv = "fdivm.jpg"
    ürünler = makarna.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/salata")
def salata():
    fdiv = "fdivsalad.jpg"
    ürünler = salata.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/yemek")
def yemek():
    fdiv = "fdivy.jpg"
    ürünler = yemek.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/tatlı")
def tatlı():
    fdiv = "fdivtat.jpg"
    ürünler = tatlı.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/waffle")
def waffle():
    fdiv = "fdivw.jpg"
    ürünler = waffle.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/sıcak_içecek")
def sıcak():
    fdiv = "fdivks-ic.jpg"
    ürünler = sıcak.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/bitki")
def sıcak2():
    fdiv = "fdivb.jpg"
    ürünler = sıcak2.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/sıcak_kahve")
def sıcak3():
    fdiv = "fdivs-k.jpg"
    ürünler = sıcak3.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/soğuk_içecek")
def soğuk():
    fdiv = "fdivso.jpg"
    ürünler = soğuk.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/vitamin")
def vitamin():
    fdiv = "fdiv.jpg"
    ürünler = vitamin.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv =fdiv)
@app.route("/meşrubat")
def meşrubat():
    fdiv = "fdivme.jpg"
    ürünler = meşrubat.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/nargile")
def nargile():
    fdiv = "fdivn.jpg"
    ürünler = nargile.query.all()
    return render_template("index.html",ürünler = ürünler,fdiv = fdiv)
@app.route("/admin")
def admin():
    return  render_template("maina.html")
@app.route("/akahvaltı")
def akahvaltı():
    add = "akahvaltı"
    ürünler = Kahvalti.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/atost")
def atost():
    add = "atost"
    ürünler = tost.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/ahamburger")
def ahamburger():
    add = "ahamburger"
    ürünler = hamburger.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/apizza")
def apizza():
    add = "apizza"
    ürünler = pizza.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/amakarna")
def amakarna():
    add = "amakarna"
    ürünler = makarna.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/asalata")
def asalata():
    add = "asalata"
    ürünler = salata.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/ayemek")
def ayemek():
    add = "ayemek"
    ürünler = yemek.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/atatlı")
def atatlı():
    add = "atatlı"
    ürünler = tatlı.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/awaffle")
def awaffle():
    add = "waffle"
    ürünler = waffle.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/asıcak_içecek")
def asıcak_içecek():
    add = "asıcak_içecek"
    ürünler = sıcak.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/abitki")
def abitki():
    add = "abitki"
    ürünler = sıcak2.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/asıcak_kahve")
def asıcak_kahve():
    add = "asıcak_kahve"
    ürünler = sıcak3.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/asoğuk_içecek")
def asoğuk_içecek():
    add = "asoğuk_içecek"
    ürünler = soğuk.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/avitamin")
def avitamin():
    add = "avitamin"
    ürünler = vitamin.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/ameşrubat")
def ameşrubat():
    add = "ameşrubat"
    ürünler = meşrubat.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/anargile")
def anargile():
    add = "anargile"
    ürünler = nargile.query.all()
    return render_template("indexa.html",ürünler = ürünler,add = add)
@app.route("/add/<string:dba>",methods = ["POST"])
def addürün(dba):
    dba = str(dba)
    yeni = bos()
    isim = request.form.get("isim")
    fiyat = request.form.get("fiyat")
    text = request.form.get("text")
    if len(isim) > 0:
        if len(text) > 0:
            if len(fiyat) > 0:
                if dba == "akahvaltı":
                    yeni = Kahvalti(text = text,fiyat=fiyat,isim=isim)
                elif dba == "atost":
                    yeni = tost(text = text,fiyat=fiyat,isim=isim)
                elif dba == "ahamburger":
                    yeni = hamburger(text = text,fiyat=fiyat,isim=isim)
                elif dba == "apizza":
                    yeni = pizza(text = text,fiyat=fiyat,isim=isim)
                elif dba == "amakarna":
                    yeni = makarna(text = text,fiyat=fiyat,isim=isim)
                elif dba == "asalata":
                    yeni = salata(text = text,fiyat=fiyat,isim=isim)
                elif dba == "ayemek":
                    yeni = yemek(text = text,fiyat=fiyat,isim=isim)
                elif dba == "atatlı":
                    yeni = tatlı(text = text,fiyat=fiyat,isim=isim)
                elif dba == "awaffle":
                    yeni = waffle(text = text,fiyat=fiyat,isim=isim)
                elif dba == "asıcak_içecek":
                    yeni = sıcak(text = text,fiyat=fiyat,isim=isim)
                elif dba == "abitki":
                    yeni = sıcak2(text = text,fiyat=fiyat,isim=isim)
                elif dba == "asıcak_kahve":
                    yeni = sıcak3(text = text,fiyat=fiyat,isim=isim)
                elif dba == "asoğuk_içecek":
                    yeni = soğuk(text = text,fiyat=fiyat,isim=isim)
                elif dba == "avitamin":
                    yeni = vitamin(text = text,fiyat=fiyat,isim=isim)
                elif dba == "ameşrubat":
                    yeni = meşrubat(text = text,fiyat=fiyat,isim=isim)
                elif dba == "anargile":
                    yeni = nargile(text = text,fiyat=fiyat,isim=isim)
                db.session.add(yeni)
                db.session.commit()
        
    return redirect(url_for(dba))
@app.route("/change/<string:dba>/<string:id>",methods = ["POST"])
def changeürün(dba,id):
    dba = str(dba)
    print(dba)
    print(id)
    yeni = bos()
    fiyat = request.form.get("fiyat")
    if dba == "akahvaltı":
        yeni = Kahvalti.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "atost":
        yeni = tost.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "ahamburger":
        yeni = hamburger.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "apizza":
        yeni = pizza.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "amakarna":
        yeni = makarna.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "asalata":
        yeni = salata.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "ayemek":
        yeni = yemek.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "atatlı":
        yeni = tatlı.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "awaffle":
        yeni = waffle.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "asıcak_içecek":
        yeni = sıcak.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "abitki":
        yeni = sıcak2.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "asıcak_kahve":
        yeni = sıcak3.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "asoğuk_içecek":
        yeni = soğuk.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "avitamin":
        yeni = vitamin.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "ameşrubat":
        yeni = meşrubat.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "anargile":
        yeni = nargile.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    
    
    db.session.commit()
    return redirect(url_for(dba))
@app.route("/delete/<string:dba>/<string:id>",)
def deleteürün(dba,id):
    dba = str(dba)
    print(dba)
    print(id)
    yeni = bos()

    if dba == "akahvaltı":
        yeni = Kahvalti.query.filter_by(id = id).first()
    elif dba == "atost":
        yeni = tost.query.filter_by(id = id).first()
    elif dba == "ahamburger":
        yeni = hamburger.query.filter_by(id = id).first()
    elif dba == "apizza":
        yeni = pizza.query.filter_by(id = id).first()
    elif dba == "amakarna":
        yeni = makarna.query.filter_by(id = id).first()
    elif dba == "asalata":
        yeni = salata.query.filter_by(id = id).first()
    elif dba == "ayemek":
        yeni = yemek.query.filter_by(id = id).first()
    elif dba == "atatlı":
        yeni = tatlı.query.filter_by(id = id).first()
    elif dba == "awaffle":
        yeni = waffle.query.filter_by(id = id).first()
    elif dba == "asıcak_içecek":
        yeni = sıcak.query.filter_by(id = id).first()
    elif dba == "abitki":
        yeni = sıcak2.query.filter_by(id = id).first()
    elif dba == "asıcak_kahve":
        yeni = sıcak3.query.filter_by(id = id).first()
    elif dba == "asoğuk_içecek":
        yeni = soğuk.query.filter_by(id = id).first()
    elif dba == "avitamin":
        yeni = vitamin.query.filter_by(id = id).first()
    elif dba == "ameşrubat":
        yeni = meşrubat.query.filter_by(id = id).first()
    elif dba == "anargile":
        yeni = nargile.query.filter_by(id = id).first()
    
    
    db.session.delete(yeni)
    db.session.commit()
    return redirect(url_for(dba))
class Kahvalti(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer())
    isim = db.Column(db.String())
    text = db.Column(db.String())
class tost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class hamburger(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class pizza(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class makarna(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class salata(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class yemek(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class tatlı(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class waffle(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class sıcak(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class sıcak2(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class sıcak3(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class soğuk(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class vitamin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class meşrubat(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class nargile(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    text = db.Column(db.String)
class bos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
db.create_all()
if __name__ == "__main__":
    app.run(debug=True)

    