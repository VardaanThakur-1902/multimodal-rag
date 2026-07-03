from sessions.session_manager import SessionManager


def main():

    manager = SessionManager()

    session = manager.create_session()

    manager.add_message(
        session,
        {
            "role": "user",
            "content": "Hello"
        }
    )

    manager.add_message(
        session,
        {
            "role": "assistant",
            "content": "Hi!"
        }
    )

    print(manager.get_messages(session))


if __name__ == "__main__":
    main()