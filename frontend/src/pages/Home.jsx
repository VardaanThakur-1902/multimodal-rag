import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import useChat from "../hooks/useChat";

const Home = () => {
  const {
  messages,
  loading,
  sendMessage,
  stopGeneration,
  sessions,
  currentSession,
  createSession,
  setCurrentSession,
  selectSession
} = useChat();

  return (
    <div className="flex h-screen bg-neutral-900 text-white">

      <Sidebar
        sessions={sessions}
        currentSession={currentSession}
        createSession={createSession}
        selectSession={selectSession}
      />

      <ChatWindow
        messages={messages}
        loading={loading}
        sendMessage={sendMessage}
        stopGeneration={stopGeneration}
      />

    </div>
  );
};

export default Home;