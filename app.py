from flask import Flask, render_template, request, redirect, flash 
from models.models import Animal,  db
from sqlalchemy_utils import database_exists
from os import getcwd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dbFinal.db"
app.config['SECRET_KEY'] = 'supersecretkey'
db.init_app(app)

with app.app_context():
    if not database_exists(db.engine.url):
        db.create_all()
    

@app.route("/")
def index():
    animales=Animal.query.all()
    print (animales)
    return render_template('index.html', animals_db = animales)
    
@app.route("/read/<animals_id>", methods=["GET", "POST"])
def read(animals_id):
    animals = Animal.query.filter_by(id=animals_id).first()  # Get a single animal
    return render_template('read.html', animal=animals)



@app.route("/edit/<animals_id>", methods=["GET", "POST"])
def edit(animals_id):
    animals_db = Animal.query.filter_by(id=animals_id).first()
    if not animals_db:  # Check if animal exists
        return "Animal not found!"

    if request.method == "POST":
        animals_db.name = request.form["name"]
        animals_db.cientific_name = request.form["cientific_name"]
        animals_db.location = request.form["location"]
        animals_db.gender = request.form["gender"]
        animals_db.count = request.form["count"]

        try:
            db.session.commit()
            flash('animal actualizado correctamente','succes')
            return redirect("/")  # Redirect to main page after successful update
        except Exception as e:
            print(f"Error updating animal: {e}")
            return render_template("edit.html", animals=animals_db, error="Error updating animal")  # Handle error

    return render_template("edit.html", animals=animals_db)


@app.route("/delete/<animals_id>", methods = ["GET", "POST"])
def delete(animals_id):
    animals_db = Animal.query.filter_by(id=animals_id).first()
    if not animals_db:  # Check if animal exists
        return "Animal not found!"
    if request.method == "POST":
        try:
            db.session.delete(animals_db)
            db.session.commit()
            flash('Error al eliminar el animal', 'success')
            return redirect("/")
        except Exception as e:
            flash('Error al eliminar el animal', 'Error')
            print(f'Error al eliminar el animal: {e}')
            return redirect("/")
    return render_template('delete.html', animals=animals_db)

if __name__ == '__main__':
    app.run(debug=True)



   






