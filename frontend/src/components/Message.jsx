import ReactMarkdown from "react-markdown";

const Message = ({ message }) => {
  const isUser = message.role === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-3xl rounded-xl px-5 py-3 my-2 ${
          isUser
            ? "bg-blue-600"
            : "bg-neutral-800"
        }`}
      >
        <ReactMarkdown>
          {message.content}
        </ReactMarkdown>
      </div>
    </div>
  );
};

export default Message;