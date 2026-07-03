from sqlmodel import Session

from database.database import engine
from services.message_service import MessageService
from services.session_service import SessionService


def main():

    with Session(engine) as session:

        chat = SessionService.create(session)

        MessageService.add(
            session,
            chat.id,
            "user",
            "Hello",
        )

        MessageService.add(
            session,
            chat.id,
            "assistant",
            "Hi!",
        )

        messages = MessageService.list(
            session,
            chat.id,
        )

        for message in messages:
            print(message.role, message.content)


if __name__ == "__main__":
    main()