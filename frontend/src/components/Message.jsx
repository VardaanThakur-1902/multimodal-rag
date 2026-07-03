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

        {
            message.streaming && (
                <span className="animate-pulse">
                    ▌
                </span>
            )
        }

        {!isUser &&
          message.sources &&
          message.sources.length > 0 && (

            <div className="mt-4 border-t border-neutral-700 pt-3">

              <h4 className="text-sm font-semibold mb-2 text-gray-300">
                Sources
              </h4>

              {message.sources.map((source, index) => (

                <div
                  key={index}
                  className="text-xs text-gray-400 mb-2"
                >

                  📄 {source.document}

                  <br />

                  Page {source.page}

                  <br />

                  Type: {source.type}

                </div>

              ))}

            </div>

          )}

      </div>

    </div>
  );
};

export default Message;