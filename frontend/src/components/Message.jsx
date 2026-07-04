import ReactMarkdown from "react-markdown";
import {
  FiUser,
  FiCpu,
  FiCopy,
} from "react-icons/fi";

import remarkGfm from "remark-gfm";
import toast from "react-hot-toast";
import CodeBlock from "./CodeBlock";

const Message = ({ message }) => {

  const isUser = message.role === "user";

  const copyMessage = async () => {

    try {

      await navigator.clipboard.writeText(
        message.content
      );

      toast.success("Copied to clipboard!");

    } catch {

      toast.error("Failed to copy.");

    }

  };

  return (

    <div
      className={`flex gap-4 my-8 ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}
    >
      {!isUser && (

        <div className="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center shrink-0">

          <FiCpu />

        </div>

      )}

      <div
        className={`max-w-4xl rounded-2xl px-6 py-5 shadow-lg ${
          isUser
            ? "bg-blue-600"
            : "bg-neutral-800 border border-neutral-700"
        }`}
      >

        <div className="prose prose-invert max-w-none">

          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            components={{
              code({
                inline,
                className,
                children,
                ...props
              }) {

                const match =
                  /language-(\w+)/.exec(className || "");

                if (!inline && match) {

                  return (
                    <CodeBlock
                      language={match[1]}
                      value={String(children).replace(/\n$/, "")}
                    />
                  );

                }

                return (
                  <code className={className} {...props}>
                    {children}
                  </code>
                );

              },
            }}
          >
            {message.content}
          </ReactMarkdown>

          {message.streaming && (
            <span className="inline-block w-2 h-5 ml-1 bg-white rounded animate-pulse"></span>
          )}

        </div>

        {!isUser &&
        message.sources?.length > 0 && (

          <div className="mt-6 border-t border-neutral-700 pt-4">

            <h3 className="text-sm font-semibold mb-3 text-gray-300">
              Sources
            </h3>

            <div className="space-y-3">

              {message.sources.map((source, index) => (

                <div
                  key={index}
                  className="rounded-xl bg-neutral-900 border border-neutral-700 p-4"
                >

                  <div className="font-medium text-white">
                    📄 {source.document}
                  </div>

                  <div className="text-sm text-gray-400 mt-2">
                    Page {source.page}
                  </div>

                  <div className="text-xs text-blue-400 mt-1">
                    {source.type}
                  </div>

                </div>

              ))}

            </div>

          </div>

        )}

        {!isUser && (

          <div className="flex justify-end mt-4">

            <button
              onClick={copyMessage}
              title="Copy response"
              className="text-gray-400 hover:text-white transition"
            >

              <FiCopy />

            </button>

          </div>

        )}

      </div>

      {isUser && (

        <div className="w-10 h-10 rounded-xl bg-neutral-700 flex items-center justify-center shrink-0">

          <FiUser />

        </div>

      )}

    </div>

  );

};

export default Message;