import { FiX, FiFileText, FiImage, FiFile } from "react-icons/fi";
import { Document, Page, pdfjs } from "react-pdf";
import "react-pdf/dist/Page/AnnotationLayer.css";
import "react-pdf/dist/Page/TextLayer.css";
import { useState } from "react";
import documentService from "../services/documentService";

pdfjs.GlobalWorkerOptions.workerSrc = "/pdf.worker.min.mjs";

const DocumentPreview = ({
  document,
  open,
  onClose,
}) => {

  

  const [numPages, setNumPages] = useState(null);

  const onLoadSuccess = ({ numPages }) => {
    setNumPages(numPages);
  };

  if (!open || !document) return null;

  const fileType = document.file_type?.replace(".", "").toLowerCase();

  return (
    <>
      {/* Overlay */}
      <div
        onClick={onClose}
        className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
      />

      {/* Drawer */}
      <div className="fixed right-0 top-0 h-full w-150 bg-neutral-950 border-l border-neutral-800 z-50 shadow-2xl flex flex-col">

        <div className="flex justify-between items-center p-6 border-b border-neutral-800">

          <div>

            <h2 className="text-xl font-bold">
              {document.original_name}
            </h2>

            <p className="text-sm text-gray-400">
              {fileType.toUpperCase()}
            </p>

          </div>

          <button
            onClick={onClose}
            className="rounded-lg p-2 hover:bg-neutral-800"
          >
            <FiX size={22} />
          </button>

        </div>

        <div className="flex-1 overflow-auto p-6">

          {fileType === "pdf" && (

            <div className="flex flex-col items-center mt-20">

              <Document
                file={documentService.previewUrl(document.id)}
                onLoadSuccess={onLoadSuccess}
                loading="Loading PDF..."
              >
                {Array.from(
                  new Array(numPages),
                  (_, index) => (
                    <Page
                      key={index}
                      pageNumber={index + 1}
                      width={520}
                    />
                  )
                )}
              </Document>

            </div>

          )}

          {(fileType === "png" ||
            fileType === "jpg" ||
            fileType === "jpeg") && (

            <div className="flex flex-col items-center mt-20">

              <img
                src={documentService.previewUrl(document.id)}
                alt={document.original_name}
                className="max-w-full rounded-xl"
              />

              <h3 className="mt-6 text-xl font-semibold">
                Image Preview
              </h3>

            </div>

          )}

          {fileType !== "pdf" &&
            fileType !== "png" &&
            fileType !== "jpg" &&
            fileType !== "jpeg" && (

              <div className="flex flex-col items-center mt-20">

                <FiFile size={80} />

                <h3 className="mt-6 text-xl font-semibold">
                  Preview coming soon...
                </h3>

              </div>

          )}

        </div>

      </div>

    </>
  );

};

export default DocumentPreview;