import { useState } from "react";
import { FiSend, FiPaperclip } from "react-icons/fi";

const ChatInput = ({
  sendMessage,
  stopGeneration,
  loading,
}) => {

  const [input, setInput] = useState("");

  const handleSend = (e) => {

    if (e) e.preventDefault();

    if (!input.trim()) return;

    sendMessage(input);

    setInput("");

  };

  const handleKeyDown = (e) => {

    if (
      e.key === "Enter" &&
      !e.shiftKey
    ) {

      e.preventDefault();

      handleSend();

    }

  };

  return (

    <div className="border-t border-neutral-800 bg-neutral-950 p-6">

      <form
        onSubmit={handleSend}
        className="max-w-5xl mx-auto"
      >

        <div className="flex items-end gap-3 rounded-2xl border border-neutral-700 bg-neutral-900 p-3 shadow-lg">

          {/* Upload */}

          <button
            type="button"
            className="rounded-xl p-3 hover:bg-neutral-800 transition"
          >
            <FiPaperclip size={18} />
          </button>

          {/* Input */}

          <textarea
            rows={1}
            value={input}
            onChange={(e) =>
              setInput(e.target.value)
            }
            onKeyDown={handleKeyDown}
            placeholder="Message Multimodal RAG..."
            className={`
              flex-1
              resize-none
              bg-transparent
              outline-none
              text-white
              placeholder:text-gray-500
              h-12
              leading-12
              overflow-hidden
              ${input ? "text-left" : "text-center"}
            `}
          />

          {/* Send / Stop */}

          {loading ? (

            <button
              type="button"
              onClick={stopGeneration}
              className="rounded-xl bg-red-600 px-5 py-3 hover:bg-red-700 transition"
            >
              Stop
            </button>

          ) : (

            <button
              type="submit"
              className="rounded-xl bg-blue-600 p-3 hover:bg-blue-700 transition"
            >
              <FiSend size={18} />
            </button>

          )}

        </div>

      </form>

    </div>

  );

};

export default ChatInput;