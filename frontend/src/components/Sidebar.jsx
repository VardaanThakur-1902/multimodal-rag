import {
  FiMessageSquare,
  FiFolder,
  FiSettings,
} from "react-icons/fi";

const Sidebar = (
  {
    sessions,
    currentSession,
    createSession,
    selectSession,
  }
) => {
  return (
    <aside className="w-72 bg-neutral-950 border-r border-neutral-800 flex flex-col">

      <div className="p-6 border-b border-neutral-800">
        <h1 className="text-xl font-bold">
          Multimodal RAG
        </h1>

        <p className="text-sm text-gray-400 mt-2">
          Local AI Assistant
        </p>
      </div>

      <button
        onClick={createSession}
        className="mx-4 mt-6 rounded-lg bg-blue-600 py-3 hover:bg-blue-700 transition"
      >
        + New Chat
      </button>

      <div className="mt-6 px-3 flex-1 overflow-y-auto">

        {sessions.map((session) => (

          <button
            key={session.id}
            onClick={() => selectSession(session.id)}
            className={`w-full text-left px-4 py-3 rounded-lg mb-2 transition ${
              currentSession === session.id
                ? "bg-neutral-700"
                : "hover:bg-neutral-800"
            }`}
          >

            💬 {session.title}

          </button>

        ))}

      </div>

      <nav className="mt-8 flex flex-col gap-2 px-3">

        <button className="flex items-center gap-3 rounded-lg px-4 py-3 hover:bg-neutral-800">
          <FiMessageSquare />
          Chats
        </button>

        <button className="flex items-center gap-3 rounded-lg px-4 py-3 hover:bg-neutral-800">
          <FiFolder />
          Documents
        </button>

        <button className="flex items-center gap-3 rounded-lg px-4 py-3 hover:bg-neutral-800">
          <FiSettings />
          Settings
        </button>

      </nav>

    </aside>
  );
};

export default Sidebar;