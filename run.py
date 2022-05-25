import os
from gamestar import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=eval(os.environ.get('DEBUG'))
    )
