import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import useChat from "../hooks/useChat";
import useSessions from "../hooks/useSessions";
import toast from "react-hot-toast";
import sessionService from "../services/sessionService";
import { useEffect, useState } from "react";
import SessionDocumentsBar from "../components/SessionDocumentsBar";
import AttachDocumentsModal from "../components/AttachDocumentsModal";

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

  const [sessionDocuments, setSessionDocuments] =
    useState([]);

  const [showAttachModal, setShowAttachModal] =
    useState(false);

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
      await loadSessionDocuments(
          sessionId
      );

      setMessages(history);

  };

  const loadSessionDocuments = async (
      sessionId,
  ) => {

      try {

          const docs =
              await sessionService.getSessionDocuments(
                  sessionId
              );

          setSessionDocuments(
              docs
          );

      } catch (err) {

          console.error(err);

      }

  };

  const handleSendMessage = (question) => {

      if (!currentSession) {

          toast.error("Create or select a chat first.");

          return;

      }

      sendMessage(question, currentSession);

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

        setSessionDocuments([]);

      }

    } catch {

      toast.error("Unable to delete chat.");

    }

  };

  const handleRemoveDocument = async (
      documentId,
  ) => {

      try {

          await sessionService.removeDocument(
              currentSession,
              documentId,
          );

          await loadSessionDocuments(
              currentSession,
          );

          toast.success(
              "Document removed from session."
          );

      } catch {

          toast.error(
              "Unable to remove document."
          );

      }

  };

  const handleAttachDocuments = async (
      documentIds,
  ) => {

      try {

          await sessionService.attachDocuments(
              currentSession,
              documentIds,
          );

          await loadSessionDocuments(
              currentSession,
          );

          setShowAttachModal(false);

          toast.success(
              "Documents attached successfully."
          );

      } catch {

          toast.error(
              "Unable to attach documents."
          );

      }

  };

  useEffect(() => {

      if (currentSession) {

          loadSessionDocuments(
              currentSession
          );

      }

  }, [currentSession]);

  return (
    <div className="flex h-screen overflow-hidden bg-neutral-900 text-white">

      <Sidebar
        sessions={sessions}
        currentSession={currentSession}
        createSession={createSession}
        selectSession={handleSelectSession}
        deleteSession={handleDeleteSession}
      />

      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">

        <SessionDocumentsBar
            documents={sessionDocuments}
            onRemove={handleRemoveDocument}
            onAdd={() => {
                setShowAttachModal(true)
            }}
        />
    
        <ChatWindow
              messages={messages}
              loading={loading}
              sendMessage={handleSendMessage}
              stopGeneration={stopGeneration}
            />
      </div>

      {
          showAttachModal && (

              <AttachDocumentsModal

                  attachedDocuments={
                      sessionDocuments
                  }

                  onClose={() =>
                      setShowAttachModal(false)
                  }

                  onAttach={
                      handleAttachDocuments
                  }

              />

          )
      }
            
    </div>
  );
};

export default Home;