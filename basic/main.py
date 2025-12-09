from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import numpy as np
import pickle

app = Flask(__name__)

# load your picke file here
app.config["SECRET_KEY"] = "your_secret_key"
upload_model = pickle.load(open("Eda-concrete_pkl_file", "rb"))
                               

# Route to pages
@app.route("/")
def index():
    return render_template("home.html")


@app.route('/predict', methods=['POST'])
def predict():
    # ... (rest of your predict function code)
    return render_template('predict.html', prediction_test=f'Predicted value: {predict}')




# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get form data
#     cement = float(request.form['Cement'])
#     superplasticizer = float(request.form['Superplasticizer'])
#     concrete_strength = float(request.form['Concrete compressive strength'])  # If this is a feature; remove if it's the target

#     # Prepare input for model (adjust based on your model's expected input shape)
#     input_features = np.array([[cement, superplasticizer, concrete_strength]])  # Example: 2D array

#     # Make prediction
#     prediction = upload_model.predict(input_features)[0]  # Adjust if your model outputs differently

#     # Render the template with the prediction
#     return render_template('home.html', prediction_test=f'Predicted value: {prediction}')




# @app.route("/member", methods=["GET", "POST"])
# def member():
#     name = False
#     email = False
#     form = MemberInfo()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         form.name.data = ""
#     return render_template("member.html", name=name, email=email, form=form)


# @app.route("/member/<name>")
# def member(name):
#     return render_template("member.html", name=name)


# Works
@app.route("/about")
def about():
    return render_template("about.html")


# Works
@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)

# def main():
#     print("Hello from basic!")


# if __name__ == "__main__":
#     main(debug=True)
