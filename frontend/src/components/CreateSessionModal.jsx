
import { useEffect, useState } from "react";

import documentService from "../services/documentService";

const CreateSessionModal = ({
    onClose,
    onCreate,
}) => {

    const [name, setName] =
        useState("");

    const [documents, setDocuments] = useState([]);

    const [selectedDocuments, setSelectedDocuments] = useState([]);

    const loadDocuments = async () => {

        try {

            const docs =
                await documentService.getDocuments();

            setDocuments(docs); 

        } catch (err) {

            console.error(err);

        }

    };

    useEffect(() => {

        loadDocuments();

    }, []);

    return (

        <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50">

            <div className="bg-neutral-900 rounded-xl p-6 w-96">

                <h2 className="text-xl font-semibold mb-4">

                    Create New Session

                </h2>

                <input
                    value={name}
                    onChange={(e) =>
                        setName(e.target.value)
                    }
                    placeholder="Session Name"
                    className="w-full rounded-lg bg-neutral-800 p-3 mb-6"
                />

                <div className="mb-6">

                    <p className="text-sm text-gray-400 mb-3">

                        Select Documents

                    </p>

                    <div className="max-h-48 overflow-y-auto rounded-lg border border-neutral-700">

                        {documents.length === 0 ? (

                            <div className="p-3 text-sm text-gray-400">

                                No documents uploaded.

                            </div>

                        ) : (

                            documents.map((doc) => (

                                <label
                                    key={doc.id}
                                    className="flex items-center gap-3 p-3 hover:bg-neutral-800 cursor-pointer"
                                >

                                    <input
                                        type="checkbox"
                                        checked={selectedDocuments.includes(doc.id)}
                                        onChange={(e) => {

                                            if (e.target.checked) {

                                                setSelectedDocuments(prev => [
                                                    ...prev,
                                                    doc.id,
                                                ]);

                                            } else {

                                                setSelectedDocuments(prev =>
                                                    prev.filter(id => id !== doc.id)
                                                );

                                            }

                                        }}
                                    />

                                    <span className="truncate">

                                        📄 {doc.original_name}

                                    </span>

                                </label>

                            ))

                        )}

                    </div>

                </div>

                <div className="flex justify-end gap-3">

                    <button
                        onClick={onClose}
                        className="px-4 py-2 rounded-lg bg-neutral-700"
                    >
                        Cancel
                    </button>

                    <button
                        onClick={() =>
                            onCreate(
                                name,
                                selectedDocuments,
                            )
                        }
                        className="px-4 py-2 rounded-lg bg-blue-600"
                    >
                        Create
                    </button>

                </div>

            </div>

        </div>

    );

};

export default CreateSessionModal;