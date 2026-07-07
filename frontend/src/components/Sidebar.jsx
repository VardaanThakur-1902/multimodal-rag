import {
  FiMessageSquare,
  FiFolder,
  FiSettings,
  FiPlus,
  FiCpu,
} from "react-icons/fi";

import { NavLink } from "react-router-dom";
import { FiTrash2 } from "react-icons/fi";
import { useState } from "react";
import CreateSessionModal from "./CreateSessionModal";
import sessionService from "../services/sessionService";

const Sidebar = ({
  sessions,
  currentSession,
  createSession,
  selectSession,
  deleteSession,
}) => {

const [showCreateSession, setShowCreateSession] = useState(false);

  return (

    <aside className="w-72 bg-neutral-950 border-r border-neutral-800 flex flex-col">

      {/* Header */}

      <div className="p-6 border-b border-neutral-800">

        <div className="flex items-center gap-3">

          <div className="w-11 h-11 rounded-xl bg-blue-600 flex items-center justify-center text-xl">

            🤖

          </div>

          <div>

            <h1 className="font-bold text-lg">
              Multimodal RAG
            </h1>

            <p className="text-xs text-gray-400">
              Local AI Assistant
            </p>

          </div>

        </div>

      </div>

      {/* New Chat */}

      <div className="p-4">

        <button
          onClick={() => setShowCreateSession(true)}
          className="w-full flex items-center justify-center gap-2 rounded-xl bg-blue-600 py-3 font-medium hover:bg-blue-700 transition"
        >
          <FiPlus />
          New Chat
        </button>

      </div>

      {/* Chats */}
      
      <NavLink
        to="/"
        className={({ isActive }) =>
          `flex items-center gap-3 rounded-lg px-4 py-3 mb-4 ${
            isActive
              ? "bg-neutral-800"
              : "hover:bg-neutral-800"
          }`
        }
      >
        <FiMessageSquare />
        Chats
      </NavLink>

      <div className="px-4">

        <h2 className="text-xs uppercase tracking-widest text-gray-500 mb-3">

          {sessions.length === 0 && (

            <div className="text-center text-gray-500 mt-8">

              <FiMessageSquare
                className="mx-auto mb-3"
                size={32}
              />

              <p>No chats yet</p>

              <p className="text-xs mt-2">
                Click "New Chat" to begin
              </p>

            </div>

          )}

        </h2>

      </div>

      <div className="flex-1 overflow-y-auto px-3">

        {sessions.map((session) => (

          <div
            key={session.id}
            className={`group flex items-center justify-between rounded-xl px-4 py-3 mb-2 transition ${
              currentSession === session.id
                ? "bg-neutral-800 border border-blue-500"
                : "hover:bg-neutral-900"
            }`}
          >

            <button
              onClick={() => selectSession(session.id)}
              className="flex flex-1 items-center gap-3"
            >
              <FiMessageSquare />
              <span className="truncate">
                {session.name}
              </span>
            </button>

            <button
              onClick={(e) => {
                e.stopPropagation();
                deleteSession(session.id);
              }}
              className="opacity-0 group-hover:opacity-100 text-red-400 hover:text-red-300 transition"
            >
              <FiTrash2 size={16} />
            </button>

          </div>

        ))}

      </div>

      {/* Bottom */}

      <div className="border-t border-neutral-800 p-4 space-y-2">

        <NavLink
            to="/documents"
            className={({ isActive }) =>
                `flex items-center gap-3 rounded-lg px-4 py-3 ${
                    isActive
                        ? "bg-neutral-800"
                        : "hover:bg-neutral-800"
                }`
            }
        >

            <FiFolder />

            Documents

        </NavLink>

        <NavLink
          to="/settings"
          className={({ isActive }) =>
            `flex items-center gap-3 rounded-lg px-4 py-3 ${
              isActive
                ? "bg-neutral-800"
                : "hover:bg-neutral-800"
            }`
          }
        >
          <FiSettings />
          Settings
        </NavLink>

        <div className="mt-4 rounded-xl bg-neutral-900 p-3">

          <div className="flex items-center gap-3">

            <FiCpu className="text-green-400" />

            <div>

              <p className="text-sm font-medium">
                Llama 3.2
              </p>

              <p className="text-xs text-green-400">
                Running Locally
              </p>

            </div>

          </div>

        </div>

      </div>

      {
        showCreateSession && (

            <CreateSessionModal
                onClose={() =>
                    setShowCreateSession(false)
                }

                onCreate={async (
                    name,
                    documentIds,
                ) => {

                    try {

                        const session =
                            await createSession(name);

                        await sessionService.attachDocuments(
                            session.id,
                            documentIds,
                        );

                        selectSession(session.id);

                        setShowCreateSession(false);

                    } catch (err) {

                        console.error(err);

                    }

                }}
            />

        )
    }

    </aside>

  );

};

export default Sidebar;