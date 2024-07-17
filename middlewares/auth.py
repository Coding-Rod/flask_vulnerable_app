from flask import redirect, url_for, session
from functools import wraps

# Models

## Users


def login_required(callback):
    """ This decorator is used to check if the user is logged in.

    Args:
        f (function): The function to be decorated. This function must be a 
        route either for render a template or for an API.

    Returns:
        function: The decorated function.
    """
    @wraps(callback)
    def decorated_function(*args, **kwargs):
        """
        A decorator function that checks if a token is present in the session.
        If the token is not present, it redirects to the signin route.
        Otherwise, it calls the callback function with the provided arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of the callback function.

        """
        if 'token' not in session:
            return redirect(url_for('routes.html_routes.login'))
        return callback(*args, **kwargs)
    return decorated_function

