import { useEffect, useRef } from "react";

import Message from "./Message";
import Loader from "./Loader";
import ChatInput from "./ChatInput";

const ChatWindow = ({
  messages,
  loading,
  sendMessage,
  stopGeneration,
}) => {

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  return (
    <div className="flex flex-col flex-1">

      <div className="flex-1 overflow-y-auto px-10 py-8 space-y-6">

        {messages.length === 0 && (
          <div className="text-center pt-20">

            <div className="flex flex-col items-center">

              <div className="w-20 h-20 rounded-3xl bg-blue-600 flex items-center justify-center text-5xl shadow-lg">

                🤖

              </div>

              <h1 className="mt-8 text-5xl font-extrabold tracking-tight">

                Multimodal RAG

              </h1>

              <p className="mt-4 text-lg text-gray-400">

                Your Local AI Assistant

              </p>

              <p className="mt-2 text-gray-500">

                Ask questions about PDFs, Images, Excel, URLs and more.

              </p>

            </div>

            <div className="mt-12 grid grid-cols-2 gap-4 max-w-3xl mx-auto">

              <button
                onClick={() => sendMessage("What is RAG?")}
                className="
                  rounded-xl
                  bg-neutral-800
                  p-4
                  text-left
                  transition-all
                  duration-200
                  hover:bg-neutral-700
                  hover:-translate-y-1
                  hover:shadow-xl
                  active:scale-95
                  "
              >
                📄 What is RAG?
              </button>

              <button
                onClick={() => sendMessage("Summarize my uploaded document")}
                className="rounded-xl bg-neutral-800 p-4 hover:bg-neutral-700 transition text-left"
              >
                📚 Summarize my document
              </button>

              <button
                onClick={() => sendMessage("Explain page 5")}
                className="rounded-xl bg-neutral-800 p-4 hover:bg-neutral-700 transition text-left"
              >
                📑 Explain page 5
              </button>

              <button
                onClick={() => sendMessage("Compare two documents")}
                className="rounded-xl bg-neutral-800 p-4 hover:bg-neutral-700 transition text-left"
              >
                ⚖ Compare documents
              </button>

            </div>

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
          stopGeneration={stopGeneration}
          loading={loading}
      />

    </div>
  );
};

export default ChatWindow;