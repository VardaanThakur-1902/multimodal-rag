import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import useChat from "../hooks/useChat";
import useSessions from "../hooks/useSessions";

const Home = () => {
  const {
      messages,
      setMessages,
      loading,
      sendMessage,
      stopGeneration,
  } = useChat();

  const {
      sessions,
      currentSession,
      setCurrentSession,
      createSession,
      loadMessages,
  } = useSessions();

  const handleSelectSession = async (
      sessionId,
  ) => {

      setCurrentSession(
          sessionId
      );

      const history =
          await loadMessages(
              sessionId
          );

      setMessages(history);

  };
  const handleSendMessage = (question) => {
    sendMessage(question, currentSession);
  };

  return (
    <div className="flex h-screen bg-neutral-900 text-white">

      <Sidebar
        sessions={sessions}
        currentSession={currentSession}
        createSession={createSession}
        selectSession={handleSelectSession}
      />

      <ChatWindow
        messages={messages}
        loading={loading}
        sendMessage={handleSendMessage}
        stopGeneration={stopGeneration}
      />

    </div>
  );
};

export default Home;