import {
  FiFileText,
  FiImage,
  FiFile,
  FiTrash2,
  FiEye,
  FiRefreshCw,
  FiCalendar,
} from "react-icons/fi";

const DocumentCard = ({
  document,
  onDelete,
  onPreview,
  onReindex,
}) => {

  const getIcon = () => {

    switch (document.file_type?.toLowerCase()) {

      case "pdf":
        return <FiFileText size={26} />;

      case "image":
      case "png":
      case "jpg":
      case "jpeg":
        return <FiImage size={26} />;

      default:
        return <FiFile size={26} />;

    }

  };

  return (

    <div className="group rounded-2xl border border-neutral-800 bg-neutral-900 p-6 transition-all duration-300 hover:border-blue-500 hover:shadow-xl hover:shadow-blue-500/10 hover:-translate-y-1">

      <div className="flex justify-between items-start">

        <div className="flex gap-4">

          <div className="w-12 h-12 rounded-xl bg-blue-500/10 text-blue-500 flex items-center justify-center">

            {getIcon()}

          </div>

          <div>

            <h3 className="font-semibold text-lg truncate max-w-xs text-white ">

              {document.original_name}

            </h3>

            <p className="text-sm text-gray-200 mt-1">

              {document.file_type?.toUpperCase()}

            </p>

          </div>

        </div>

        <button
          onClick={() => onDelete(document.id)}
          className="rounded-lg p-2 text-red-400 hover:bg-red-500/10 transition"
        >

          <FiTrash2 />

        </button>

      </div>

      <div className="mt-6 space-y-2 text-sm text-gray-200">

        <div className="flex justify-between">

          <span>Chunks</span>

          <span>{document.chunk_count ?? "-"}</span>

        </div>

        <div className="flex justify-between">

          <span>Size</span>

          <span>{document.size ?? "-"}</span>

        </div>

        <div className="flex justify-between items-center">

          <span className="flex items-center gap-2">

            <FiCalendar size={14} />

            Uploaded

          </span>

          <span>

            {document.uploaded_at
              ? new Date(document.uploaded_at).toLocaleDateString()
              : "-"}

          </span>

        </div>

      </div>

      <div className="mt-6 flex gap-3 text-white font-medium">

        <button
          onClick={() => onPreview?.(document)}
          className="flex-1 rounded-xl border border-neutral-700 py-2 hover:bg-neutral-800 transition flex items-center justify-center gap-2"
        >

          <FiEye />

          Preview

        </button>

        <button
          onClick={() => onReindex?.(document.id)}
          className="flex-1 rounded-xl border border-neutral-700 py-2 hover:bg-neutral-800 transition flex items-center justify-center gap-2"
        >

          <FiRefreshCw />

          Re-index

        </button>

      </div>

    </div>

  );

};

export default DocumentCard;