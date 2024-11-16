#!/usr/bin/python3

# in app.py, Add this to the @app.before_request func
def mthd_with_before_req():
    """Ditto"""
    request.current_user = auth.current_user(request)

# in views/users.py
@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    # 1: Import the abort module from flask
    # 2: Append to the beginning of the method
    if user_id == 'me' and request.current_user is None:
        abort(404)
    if user_id == 'me' and request.current_user is not None:
        return jsonify(request.current_user.to_json())  ##

