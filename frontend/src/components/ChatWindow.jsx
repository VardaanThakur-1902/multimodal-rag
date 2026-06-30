import { useEffect, useRef } from "react";

import Message from "./Message";
import Loader from "./Loader";
import ChatInput from "./ChatInput";

const ChatWindow = ({
  messages,
  loading,
  sendMessage,
}) => {

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  return (
    <div className="flex flex-col flex-1">

      <div className="flex-1 overflow-y-auto p-8">

        {messages.length === 0 && (
          <div className="text-center mt-40">

            <h2 className="text-4xl font-bold">
              👋 Welcome
            </h2>

            <p className="text-gray-400 mt-4">
              Ask anything to your local AI assistant.
            </p>

          </div>
        )}

        {messages.map((message, index) => (
          <Message
            key={index}
            message={message}
          />
        ))}

        {loading && <Loader />}

        <div ref={bottomRef}></div>

      </div>

      <ChatInput
        sendMessage={sendMessage}
        loading={loading}
      />

    </div>
  );
};

export default ChatWindow;