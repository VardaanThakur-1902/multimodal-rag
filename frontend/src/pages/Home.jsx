import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import useChat from "../hooks/useChat";
import useSessions from "../hooks/useSessions";
import DropZone from "../components/DropZone";
import toast from "react-hot-toast";
import api from "../services/api";
import sessionService from "../services/sessionService";

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
      loadSessions,
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

      if (!currentSession) {

          toast.error("Create or select a chat first.");

          return;

      }

      sendMessage(question, currentSession);

  };

  

  const handleUpload = async (files) => {

    if (!files.length) return;

    const formData = new FormData();

    formData.append("file", files[0]);

    try {

      await api.post(
        "/api/v1/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      toast.success("Document uploaded successfully!");

      // We'll add document refresh later

    } catch {

      toast.error("Upload failed.");

    }

  };

  const handleDeleteSession = async (sessionId) => {

    if (!window.confirm("Delete this chat?"))
      return;

    try {

      await sessionService.deleteSession(sessionId);

      toast.success("Chat deleted.");

      await loadSessions();

      if (currentSession === sessionId) {

        setMessages([]);

        setCurrentSession(null);

      }

    } catch {

      toast.error("Unable to delete chat.");

    }

  };

  

  

  return (
    <div className="flex h-screen bg-neutral-900 text-white">

      <Sidebar
        sessions={sessions}
        currentSession={currentSession}
        createSession={createSession}
        selectSession={handleSelectSession}
        deleteSession={handleDeleteSession}
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