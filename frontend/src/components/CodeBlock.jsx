import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";
import { FiCopy } from "react-icons/fi";
import toast from "react-hot-toast";

const CodeBlock = ({
  language,
  value,
}) => {

  const copyCode = async () => {

    await navigator.clipboard.writeText(value);

    toast.success("Code copied!");

  };

  return (

    <div className="rounded-xl overflow-hidden border border-neutral-700 my-4">

      <div className="flex items-center justify-between px-4 py-2 bg-neutral-900">

        <span className="text-xs text-gray-400 uppercase">

          {language || "text"}

        </span>

        <button
          onClick={copyCode}
          className="hover:text-white"
          title="Copy code"
        >

          <FiCopy />

        </button>

      </div>

      <SyntaxHighlighter
        language={language}
        style={oneDark}
        customStyle={{
          margin: 0,
          borderRadius: 0,
          background: "#171717",
        }}
      >
        {value}
      </SyntaxHighlighter>

    </div>

  );

};

export default CodeBlock;