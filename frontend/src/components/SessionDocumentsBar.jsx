import { FiFileText, FiX, FiPlus } from "react-icons/fi";

const SessionDocumentsBar = ({
    documents,
    onRemove,
    onAdd,
}) => {

    return (

        <div className="border-b border-neutral-800 bg-neutral-950 px-6 py-3">

            <div className="flex items-center gap-3 flex-wrap">

                <span className="text-sm text-gray-400">

                    Documents:

                </span>

                {documents.map((doc) => (

                    <div
                        key={doc.id}
                        className="flex items-center gap-2 rounded-full bg-neutral-800 px-3 py-1 text-sm"
                    >

                        <FiFileText size={14} />

                        <span>

                            {doc.original_name}

                        </span>

                        <button
                            onClick={() =>
                                onRemove(doc.id)
                            }
                            className="text-red-400 hover:text-red-300"
                        >

                            <FiX size={14} />

                        </button>

                    </div>

                ))}

                <button
                    onClick={onAdd}
                    className="flex items-center gap-2 rounded-full border border-dashed border-blue-500 px-3 py-1 text-blue-400 hover:bg-blue-500/10"
                >

                    <FiPlus />

                    Add

                </button>

            </div>

        </div>

    );

};

export default SessionDocumentsBar;