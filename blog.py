#flask framework'ünden flask sınıfını projeme dahil ediyorum
from flask import Flask, render_template

#web sunucusunu pc de çalıştırmak için bir uygulama oluşturup flasktan nesne oluşturup atama yapıyorum
app = Flask(__name__) #bu pythondaki özel bir değişken
 
"""
#her bir url adresi isteğine karşılık flask'ta bir fonksiyon var
@app.route("/")
def index(): #index yerine herhangi bir isim verebilirsin
    #burada herhangi bir yazı veya http response döndürebilirsin
    return "main page" #string

@app.route("/about")
def about():
    return "about" 
#başka bir örneğini gösterdim, eğer /about yazarsan url yerine o sayfaya gideceksin.

@app.route("/about/zilan")
def zilan():
    return "about of zilan"
#/about/zilan

"""
#template sayesinde yazdığımız html,css,boostrap kodlarını python kodlarında response olarak dönebiliyoruz.
#flask direkt-default olarak template şeklinde bir klasörün içine bakar.
"""
@app.route("/")
def index():
    #python içeriği göndermek istersek key kullanmamız lazım 
    number = 10
    #eğer sözlük göndermek istersek:
    article = dict()
    article["title"] = "test"
    article["body"] = "test 123"
    article["author"] = "zilan"

    return render_template("index.html", keynumber = 10, keyarticle = article) #mesela burda keynumber oluşturduğum ve atadığım 10 için anahtar, istediğim ismi verebilirim.
"""

#bu kısım kalıtım için: index.html den layouta miras
@app.route("/")
def indexL():
    return render_template("layout.html") 

if __name__ == "__main__":
    #debug = true bir hata oluştuğunda hata yığın izleri ve ayrıntılı istek bilgileri de dahil olmak üzere hata ayıklama bilgilerinin gösterilip gösterilmeyeceğini kontrol eder
    app.run(debug=True) #mümkün olduğunca sistem güvenliği için debug=false ayarında olmasını sağla 
