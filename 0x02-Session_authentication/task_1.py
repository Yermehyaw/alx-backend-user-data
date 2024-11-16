# in auth/session_auth.py
from api.v1.auth import Auth
import uuid

class SessionAuth(Auth):
    """Authenticates the session of a user

    Attributes;

    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a new session id for a user"""
        if not user_id:
            return None

        if not isinstance(user_id, str):
           return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id.update({session_id: user_id})

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns the id from a given session_id"""
        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)


# in app.py
if auth == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()

