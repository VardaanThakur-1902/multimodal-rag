import { useDropzone } from "react-dropzone";

const DropZone = ({
  onFileDrop,
  children,
}) => {

  const {
    getRootProps,
    getInputProps,
    isDragActive,
    } = useDropzone({
    onDrop: onFileDrop,
    multiple: false,
    accept: {
        "application/pdf": [".pdf"],
        "image/*": [],
        "text/plain": [".txt"],
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [".xlsx"],
        "text/csv": [".csv"],
    },
});

  return (

    <div
      {...getRootProps()}
      className={`h-full transition-all ${
        isDragActive
          ? "bg-blue-500/10 border-2 border-dashed border-blue-500"
          : ""
      }`}
    >

      <input {...getInputProps()} />

      {isDragActive ? (

        <div className="flex h-full items-center justify-center bg-blue-500/10 backdrop-blur-sm">

            <div className="rounded-3xl border-2 border-dashed border-blue-500 p-16 text-center">

                <div className="text-7xl">
                📄
                </div>

                <h2 className="mt-6 text-3xl font-bold">
                Drop files to upload
                </h2>

                <p className="mt-3 text-gray-400">
                PDFs, Images, Word, Excel and more
                </p>

            </div>

            </div>

      ) : (

        children

      )}

    </div>

  );

};

export default DropZone;