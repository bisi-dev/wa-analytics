# import modules
from flask import Flask, render_template, request, redirect, url_for
from process import Analyse
import os

# initialise flask app
app = Flask(__name__)

# Set Configuration for receiving files --Max MB, --extension=".txt"
# app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = [".txt"]

# Index WebPage - Main Page for Onboarding
@app.route("/")
def index():
    return render_template("index.html")


# POST action by User
@app.route("/", methods=["POST"])
def upload_file():

    # Protect against unauthorized requests
    try:
        global filename
        uploaded_file = request.files["file"]
        filename = uploaded_file.filename

        # Wait till user adds a file
        if filename != "":
            file_ext = os.path.splitext(filename)[1]

            # Prevent malicious injections/unauthorized files.
            if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                return render_template("warning.html")

            else:
                # Save file
                uploaded_file.save(uploaded_file.filename)

                # Initialise Analytics for saved file
                analytics = Analyse()
                analytics.raw_to_df(filename, "12hr")

                # Get Information from functions
                messages_count = analytics.messages_count()
                users_count = analytics.users_count()[0]
                users_count_table = analytics.users_count()[1]
                image = analytics.infographics()

                # Clean application directory
                os.remove(filename)

                return render_template(
                    "result.html",
                    messages_count_html=f"Number of Messages in Chat: {messages_count}",
                    users_count_html=f"Number of Active people in Chat: {users_count}",
                    tables=[
                        users_count_table.to_html(
                            classes="data", header="true"
                        )
                    ],
                    image=image,
                )

        else:
            return render_template("warning.html")

    except:
        return render_template("warning.html")


# Test to Ping Application
@app.route("/test", methods=["GET"])
def test():
    return "Pinging Model Application!"


if __name__ == "__main__":
    # app.run(debug=True, host="127.0.0.1", port="5002")
    app.run(debug=True)
