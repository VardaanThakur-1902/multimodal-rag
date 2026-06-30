import { useState } from "react";
import { FiSend } from "react-icons/fi";

const ChatInput = ({
  sendMessage,
  loading,
}) => {
  const [input, setInput] = useState("");

  const handleSend = () => {
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
    <div className="border-t border-neutral-800 p-4">

      <div className="flex gap-3">

        <textarea
          rows={1}
          value={input}
          onChange={(e) =>
            setInput(e.target.value)
          }
          onKeyDown={handleKeyDown}
          placeholder="Ask anything..."
          className="flex-1 rounded-lg bg-neutral-800 p-3 resize-none outline-none"
        />

        <button
          onClick={handleSend}
          disabled={loading}
          className="rounded-lg bg-blue-600 px-5 hover:bg-blue-700 disabled:opacity-50"
        >
          <FiSend />
        </button>

      </div>

    </div>
  );
};

export default ChatInput;