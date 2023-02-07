# Define favicon file:
favicon = open("../static/favicon.ico", "r")

@argent.route("/favicon.ico")
def favicon(request):
    return(200, {}, favicon)
