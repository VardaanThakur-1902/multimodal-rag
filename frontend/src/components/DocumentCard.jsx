import {
  FiFileText,
  FiImage,
  FiFile,
  FiTrash2,
  FiEye,
} from "react-icons/fi";

const DocumentCard = ({
  document,
  onDelete,
}) => {

  const getIcon = () => {

    switch (document.type) {

      case "pdf":
        return <FiFileText size={24} />;

      case "image":
        return <FiImage size={24} />;

      default:
        return <FiFile size={24} />;

    }

  };

  return (

    <div className="rounded-2xl border border-neutral-800 bg-neutral-900 p-5 hover:border-blue-500 transition">

      <div className="flex items-start justify-between">

        <div className="flex gap-4">

          <div className="text-blue-500">

            {getIcon()}

          </div>

          <div>

            <h3 className="font-semibold">

              {document.name}

            </h3>

            <p className="text-sm text-gray-400 mt-1">

              {document.type.toUpperCase()}

            </p>

          </div>

        </div>

        <button
          onClick={() => onDelete(document.id)}
          className="text-red-400 hover:text-red-300"
        >
          <FiTrash2 />
        </button>

      </div>

    </div>

  );

};

export default DocumentCard;