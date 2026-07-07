import { useEffect, useState } from "react";
import documentService from "../services/documentService";

const AttachDocumentsModal = ({
    attachedDocuments,
    onAttach,
    onClose,
}) => {

    const [documents, setDocuments] =
        useState([]);

    const [selected, setSelected] =
        useState([]);

    useEffect(() => {

        loadDocuments();

    }, []);

    const loadDocuments = async () => {

        try {

            const docs =
                await documentService.getDocuments();

            setDocuments(docs);

        } catch (err) {

            console.error(err);

        }

    };

    const attachedIds = attachedDocuments.map(
        doc => doc.id
    );

    const availableDocuments =
        documents.filter(
            doc => !attachedIds.includes(doc.id)
        );

    const toggle = (id) => {

        setSelected(prev =>

            prev.includes(id)

                ? prev.filter(x => x !== id)

                : [...prev, id]

        );

    };

    return (

        <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50">

            <div className="bg-neutral-900 rounded-xl w-112.5 p-6">

                <h2 className="text-xl font-semibold mb-4">

                    Attach Documents

                </h2>

                <div className="max-h-72 overflow-y-auto space-y-2">

                    {availableDocuments.map(doc => (

                        <label
                            key={doc.id}
                            className="flex items-center gap-3 p-2 rounded hover:bg-neutral-800 cursor-pointer"
                        >

                            <input
                                type="checkbox"
                                checked={selected.includes(doc.id)}
                                onChange={() =>
                                    toggle(doc.id)
                                }
                            />

                            <span>

                                {doc.original_name}

                            </span>

                        </label>

                    ))}

                    {availableDocuments.length === 0 && (

                        <p className="text-gray-400">

                            All uploaded documents are already attached.

                        </p>

                    )}

                </div>

                <div className="flex justify-end gap-3 mt-6">

                    <button
                        onClick={onClose}
                        className="px-4 py-2 rounded bg-neutral-700"
                    >
                        Cancel
                    </button>

                    <button
                        onClick={() =>
                            onAttach(selected)
                        }
                        className="px-4 py-2 rounded bg-blue-600"
                    >
                        Attach
                    </button>

                </div>

            </div>

        </div>

    );

};

export default AttachDocumentsModal;