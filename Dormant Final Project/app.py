from cs50 import SQL
from flask import Flask, session, request, redirect, render_template, request, session, flash, send_from_directory, url_for
from flask_session import Session
import os
from helpers import apology, most_common
import random

# Configure application
app = Flask(__name__)

# Secret Key
app.secret_key = "jd702kfmco029mda472doun74kxmal383nxlu280230jhsg3g7eg8hd00bc7evc2790201bxw8gd738cv9bc0ieb02b7gx"


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

@app.route("/", methods = ["GET", "POST"])
def index():
    session.clear()
    return render_template("index.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    # Get username email and password
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        email = request.form["email"].lower()
        password = request.form["password"]
    # Initialize password requirements
        email_domains = ["@gmail.com", "@yale.edu", "@hotmail.com", "@yahoo.com"]
        special_characters = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
    # Check if email and password pass security strength
        if any(word in email for word in email_domains):
            if any(char in special_characters for char in password):
                if len(password) >= 6:
                    # Insert into database
                    try:
                        db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", name, email, password)
                    except:
                        return apology("Sorry, this account is already registered!")
                    check = db.execute("SELECT * FROM users WHERE email = ?", email)
                    if len(check) == 1:
                        flash("Ready to log in!")
                        return redirect("/login")
                    else:
                        return apology("Sorry, this account is already registered!")
                else: return apology("Your password must have at least 6 characters")
            else: return apology("Your password must contain a special character")
        else: return apology("Please enter a valid email address")
    # Continue
    else:
        return render_template("register.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    session.clear()

    # Get Email and Password from form, query database
    if request.method == "POST":
        email = request.form["email"]
        email = email.lower()
        password = request.form["password"]
        session["email"] = email
        row = db.execute("SELECT * FROM users WHERE email = ?", email)
        specific_pass = str(db.execute("SELECT password FROM users WHERE email = ?", email))
        display_name = str(db.execute("SELECT name FROM users WHERE email = ?", email))
        show_name = display_name[11:-3]
    # Check if email and password are correct/exist
        if len(row) == 0:
            session.clear()
            return apology("Invalid Username")
        if password != specific_pass[15:-3]:
            session.clear()
            return apology("Invalid Password")
        else:
            return render_template("start.html", show_name = show_name)
    # If not post request, bring continue
    else:
        return render_template("login.html")


@app.route("/roommate", methods = ["GET", "POST"])
def roommate():
    if request.method == "POST":
        # transfer from front end to back end
        email = session["email"]
        email = email.lower()
        name = db.execute("SELECT name FROM users where email = ?", email)[0]["name"]
        email_roommate = request.form["email"]
        email_roommate = email_roommate.lower()
        if email != email_roommate:
            return apology("Your email must match from the email you registered an account with!")
        # loading data into SQL database
        awake = request.form["awake"]
        sleep = request.form["sleep"]
        weekday = request.form["weekday"]
        weekend = request.form["weekend"]
        hobbies = request.form["hobbies"]
        music = request.form["music"]
        shower = request.form["shower"]
        cleanliness = request.form["cleanliness"]
        comfortability = request.form["comfortability"]
        share = request.form["share"]
        try:
            db.execute("INSERT INTO preferences (email, awake, sleep, weekday, weekend, hobbies, music, shower, cleanliness, comfortability, share, name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        , email, awake, sleep, weekday, weekend, hobbies, music, shower, cleanliness, comfortability, share, name)
        except:
            return apology("You must fill out all fields.")
        check_if_successful = db.execute("SELECT * FROM preferences WHERE email = ?", email)
        if len(check_if_successful) == 1:
            flash("Preferences updated successfully!")
            return redirect("/match")
        #next steps, create table and load all of this into it
    else:
        return render_template("roommate.html")



@app.route("/start", methods = ["GET", "POST"])
def start():
    return render_template("start.html")

@app.route("/match", methods = ["GET", "POST"])
def match():
    email = session["email"]
    check_match = db.execute("SELECT * FROM PREFERENCES WHERE email = ?", email)
    if len(check_match) != 1:
        return apology("To access this page, you must complete the Find a Roommates tab first.")

    # user awake
    user_awake = db.execute("SELECT awake FROM PREFERENCES WHERE email = ?", email)[0]["awake"]
    try:
        database_name_awake = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE awake = ? AND NOT email = ?", user_awake, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_awake = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_awake)[0]["email"]

    # user sleep
    user_sleep = db.execute("SELECT sleep FROM PREFERENCES WHERE email = ?", email)[0]["sleep"]
    try:
        database_name_sleep = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE sleep = ? AND NOT email = ?", user_sleep, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_sleep = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_sleep)[0]["email"]

    # user weekday
    user_weekday = db.execute("SELECT weekday FROM PREFERENCES WHERE email = ?", email)[0]["weekday"]
    try:
        database_name_weekday  = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE weekday  = ? AND NOT email = ?", user_weekday, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_weekday = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_weekday)[0]["email"]

    # user weekend
    user_weekend = db.execute("SELECT weekend FROM PREFERENCES WHERE email = ?", email)[0]["weekend"]
    try:
        database_name_weekend = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE weekend = ? AND NOT email = ?", user_weekend, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_weekend = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_weekend)[0]["email"]

    # user hobbies
    user_hobbies = db.execute("SELECT hobbies FROM PREFERENCES WHERE email = ?", email)[0]["hobbies"]
    try:
        database_name_hobbies = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE hobbies = ? AND NOT email = ?", user_hobbies, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_hobbies = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_hobbies)[0]["email"]

    # user music
    user_music = db.execute("SELECT music FROM PREFERENCES WHERE email = ?", email)[0]["music"]
    try:
        database_name_music = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE music = ? AND NOT email = ?", user_music, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_music = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_music)[0]["email"]

    # user shower
    user_shower = db.execute("SELECT shower FROM PREFERENCES WHERE email = ?", email)[0]["shower"]
    try:
        database_name_shower = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE shower = ? AND NOT email = ?", user_shower, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_shower = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_shower)[0]["email"]

    # user cleanliness
    user_cleanliness = db.execute("SELECT cleanliness FROM PREFERENCES WHERE email = ?", email)[0]["cleanliness"]
    try:
        database_name_cleanliness = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE cleanliness = ? AND NOT email = ?", user_cleanliness, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_cleanliness = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_cleanliness)[0]["email"]

    # user comfortability
    user_comfortability = db.execute("SELECT comfortability FROM PREFERENCES WHERE email = ?", email)[0]["comfortability"]
    try:
        database_name_comfortability = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE comfortability = ? AND NOT email = ?", user_comfortability, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_comfortability = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_comfortability)[0]["email"]

    # user share
    user_share = db.execute("SELECT share FROM PREFERENCES WHERE email = ?", email)[0]["share"]
    try:
        database_name_share = str(random.choice(db.execute("SELECT name FROM PREFERENCES WHERE share = ? AND NOT email = ?", user_share, email)))[10:-2]
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    database_email_share = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", database_name_share)[0]["email"]

    # perfect/most frequent match
    frequency_list = [database_name_awake, database_name_sleep, database_name_weekday, database_name_weekend, database_name_hobbies, database_name_music, database_name_shower, database_name_cleanliness, database_name_comfortability, database_name_share]
    try:
        overall_match_name = most_common(frequency_list)
    except:
        return apology("All fields of your profile must be complete. Please go back to the Find Roommate Tab and fill out each field")
    overall_match_email = db.execute("SELECT email FROM PREFERENCES WHERE name = ?", overall_match_name)[0]["email"]

    # transfer everything into match.html
    return render_template("match.html", awake_name = database_name_awake, awake_email = database_email_awake, sleep_name = database_name_sleep, sleep_email = database_email_sleep, weekday_name = database_name_weekday, weekday_email = database_email_weekday, weekend_name = database_name_weekend, weekend_email = database_email_weekend, hobbies_name = database_name_hobbies, hobbies_email = database_email_hobbies, music_name = database_name_music, music_email = database_email_music, shower_name = database_name_shower, shower_email = database_email_shower, cleanliness_name =  database_name_cleanliness, cleanliness_email = database_email_cleanliness, comfortability_name = database_name_comfortability, comfortability_email = database_email_comfortability, share_name = database_name_share, share_email = database_email_share, overall_match_name = overall_match_name, overall_match_email = overall_match_email)

@app.route("/profile", methods = ["GET", "POST"])
def profile():
    email = session["email"]
    check_match = db.execute("SELECT * FROM PREFERENCES WHERE email = ?", email)
    if len(check_match) != 1:
        return apology("To access this page, you must complete the Find a Roommates tab first.")

    name = db.execute("SELECT name FROM PREFERENCES WHERE email = ?", email)[0]["name"]
    user_awake = db.execute("SELECT awake FROM PREFERENCES WHERE email = ?", email)[0]["awake"]
    user_sleep = db.execute("SELECT sleep FROM PREFERENCES WHERE email = ?", email)[0]["sleep"]
    user_weekday = db.execute("SELECT weekday FROM PREFERENCES WHERE email = ?", email)[0]["weekday"]
    user_weekend = db.execute("SELECT weekend FROM PREFERENCES WHERE email = ?", email)[0]["weekend"]
    user_hobbies = db.execute("SELECT hobbies FROM PREFERENCES WHERE email = ?", email)[0]["hobbies"]
    user_music = db.execute("SELECT music FROM PREFERENCES WHERE email = ?", email)[0]["music"]
    user_shower = db.execute("SELECT shower FROM PREFERENCES WHERE email = ?", email)[0]["shower"]
    user_cleanliness = db.execute("SELECT cleanliness FROM PREFERENCES WHERE email = ?", email)[0]["cleanliness"]
    user_comfortability = db.execute("SELECT comfortability FROM PREFERENCES WHERE email = ?", email)[0]["comfortability"]
    user_share = db.execute("SELECT share FROM PREFERENCES WHERE email = ?", email)[0]["share"]

    return render_template("profile.html", name = name, email = email, user_awake = user_awake, user_sleep = user_sleep, user_weekday = user_weekday, user_weekend = user_weekend, user_hobbies = user_hobbies, user_music = user_music, user_shower = user_shower, user_cleanliness = user_cleanliness, user_comfortability = user_comfortability, user_share = user_share)

@app.route("/chat", methods = ["GET", "POST"])
def chat():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        db.execute("INSERT INTO messages (name, message) VALUES (?, ?)", name, message)
        chat = db.execute("SELECT * FROM messages")
        return render_template("chat2.html", chat = chat)
    else:
        return render_template("chat.html")

@app.route("/update", methods = ["GET", "POST"])
def update():
    if request.method == "POST":
        # transfer from front end to back end
        email = session["email"]
        email = email.lower()
        name = db.execute("SELECT name FROM users where email = ?", email)[0]["name"]
        email_roommate = request.form["email"]
        email_roommate = email_roommate.lower()
        if email != email_roommate:
            return apology("Your email must match from the email you registered an account with!")
        # loading data into SQL database
        awake = request.form["awake"]
        sleep = request.form["sleep"]
        weekday = request.form["weekday"]
        weekend = request.form["weekend"]
        hobbies = request.form["hobbies"]
        music = request.form["music"]
        shower = request.form["shower"]
        cleanliness = request.form["cleanliness"]
        comfortability = request.form["comfortability"]
        share = request.form["share"]
        try:
            db.execute("UPDATE preferences SET awake = ?,  sleep = ?, weekday = ?, weekend = ?, hobbies = ?, music = ?, shower = ?, cleanliness = ?, comfortability = ?, share = ? WHERE email = ?", awake, sleep, weekday, weekend, hobbies, music, shower, cleanliness, comfortability, share, email)
        except:
            return apology("You must update all fields in order to proceed. If only certain preferences have changed, simply enter your existing answers.")

        check_if_successful = db.execute("SELECT * FROM preferences WHERE email = ?", email)
        if len(check_if_successful) == 1:
            flash("Preferences updated successfully!")
            return redirect("/match")
        #next steps, create table and load all of this into it
    else:
        return render_template("update.html")
    return render_template("profile.html")

@app.route("/logout", methods = ["GET", "POST"])
def logout():
    session.clear()
    flash("You have logged out successfully!")
    return render_template("index.html")

