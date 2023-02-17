import os
import requests
import urllib.parse


from flask import redirect, render_template, request, session
from functools import wraps

def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", top=code, bottom=message), code

def most_common(frequency_list):
    return max(set(frequency_list), key = frequency_list.count)