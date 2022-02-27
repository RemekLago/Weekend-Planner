from flask import Blueprint, render_template

additional = Blueprint("additional", __name__, url_prefix="/")

@additional.route("/activities")
def activities():
    return render_template("activities.html")


@additional.route("/propositions")
def propositions():
    return render_template("propositions.html")


@additional.route("/gallery")
def gallery():
    return render_template("gallery.html")
