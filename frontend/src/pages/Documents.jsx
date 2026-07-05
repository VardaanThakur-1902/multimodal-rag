import { useEffect, useState } from "react";
import documentService from "../services/documentService";
import toast from "react-hot-toast";
import DocumentCard from "../components/DocumentCard";
import DocumentPreview from "../components/DocumentPreview";
import { useRef } from "react";

const Documents = () => {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [previewDoc, setPreviewDoc] = useState(null);
  const fileInputRef = useRef(null);

  const loadDocuments = async () => {
    try {
      const docs =
          await documentService.getDocuments();

      setDocuments(docs);
    } catch (err) {
      console.error("Failed to load documents:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleUpload = async (e) => {

    const file = e.target.files?.[0];

    if (!file) return;

    try {

      await documentService.upload(file);

      toast.success(
        "Document uploaded successfully."
      );

      loadDocuments();

    } catch {

      toast.error(
        "Upload failed."
      );

    }

  };

  const handleDelete = async (documentId) => {

    const confirmed = window.confirm(
      "Are you sure you want to delete this document?"
    );

    if (!confirmed) return;

    try {

      await documentService.delete(documentId);

      toast.success("Document deleted.");

      loadDocuments();

    } catch {

      toast.error("Delete failed.");

    }

  };

  useEffect(() => {
    loadDocuments();
  }, []);

  return (
    <div className="p-8">

      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <h1 className="text-3xl font-bold">
          Documents
        </h1>

        <button
            onClick={() => fileInputRef.current?.click()}
            className="rounded-xl bg-blue-600 px-5 py-3 hover:bg-blue-700 transition"
        >
            + Upload
        </button>
      </div>

      {/* Search */}
      <input
        type="text"
        placeholder="Search documents..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="w-full mb-8 rounded-xl border border-neutral-700 bg-neutral-900 px-4 py-3 text-white outline-none focus:border-blue-500"
      />

      {/* Content */}
      {loading ? (
        <div className="text-center text-gray-400">
          Loading documents...
        </div>
      ) : documents.length === 0 ? (

        <div className="flex flex-col items-center justify-center mt-24">

          <div className="text-7xl">
            📂
          </div>

          <h2 className="mt-6 text-2xl font-bold">
            No documents uploaded
          </h2>

          <p className="mt-2 text-gray-400">
            Upload your first document to start chatting.
          </p>

        </div>

      ) : (

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

          {documents
            .filter((doc) =>
                doc.original_name
                    ?.toLowerCase()
                    .includes(search.toLowerCase())
            )
            .map((doc) => (
              <DocumentCard
                  key={doc.id}
                  document={doc}
                  onDelete={handleDelete}
                  onPreview={setPreviewDoc}
              />
            ))}

        </div>

      )}

      <DocumentPreview
          document={previewDoc}
          open={!!previewDoc}
          onClose={() => setPreviewDoc(null)}
      />

      <input
          ref={fileInputRef}
          type="file"
          hidden
          onChange={handleUpload}
      />

    </div>
  );
};

export default Documents;