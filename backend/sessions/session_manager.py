from uuid import uuid4


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def create_session(self):

        session_id = str(uuid4())

        self.sessions[session_id] = []

        return session_id

    def get_messages(
        self,
        session_id,
    ):

        return self.sessions.get(
            session_id,
            [],
        )

    def add_message(
        self,
        session_id,
        message,
    ):

        self.sessions.setdefault(
            session_id,
            [],
        ).append(message)

    def delete_session(
        self,
        session_id,
    ):

        self.sessions.pop(
            session_id,
            None,
        )