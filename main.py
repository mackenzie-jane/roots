from flask import Flask, render_template, request, redirect, url_for
import accounts
import artifacts
import communities

'''
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<script src="{{ url_for('static', filename='script.js') }}" defer></script> <!-- Link to the JavaScript file -->
'''

'''
<h2>Artifacts</h2>
                <ul>
                    {% for artifact in artifactsList %}
                        <li>
                            <h2>Name: {{ artifact.getName() }}</h2>
                            <p>Type: {{ artifact.getType() }}</p>
                            <p>Media:</p><img src="{{ artifact.getMedia() }}" alt="Artifact Media" style="max-width: 300px;">
                            <p>Comments: {{ artifact.getComments() }}</p>
                            <p>Hashtags: {{ artifact.getHashtags() }}</p>
                        </li>
                    {% else %}
                        <p>No artifacts added yet.</p>
                    {% endfor %}

                </ul>
'''

# Create object of Flask
app = Flask(__name__)

account1, account2, account3 = accounts.accounts()
artifactsList = []
foodList, artList, languageList = communities.foodCulture()

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route("/addArtifact.html", methods=['GET', 'POST'])
def addArtifact():

    if request.method == 'POST':

        name = request.form.get('name')
        type = request.form.get('type')
        media = request.form.get('media')
        comments = request.form.get('comments')
        hashtags = request.form.get('hashtags')

        newArtifact = artifacts.Artifact(name, type, media, comments, hashtags)

        artifactsList.append(newArtifact)

        return redirect(url_for('profile'))

    return render_template('addArtifact.html')  # Render the HTML form

@app.route("/myProfile.html", methods=['GET', 'POST'])
def profile():

    return render_template('myProfile.html', account1=account1, account2=account2, account3=account3, artifactsList=artifactsList)  # Render the HTML form

@app.route("/home.html")
def home():
    return render_template('home.html')  # Render the HTML form

@app.route("/community.html")
def community():
    return render_template('community.html', foodList = foodList, artList = artList, languageList = languageList)  # Render the HTML form
    


if __name__ == "__main__":
    print(5)
    app.run(debug=True)
