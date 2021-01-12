from . import admin


@admin.route("/")
def index():
    return "<h1>this is admin</h1>"
