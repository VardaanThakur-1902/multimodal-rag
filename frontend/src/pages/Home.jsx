import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import useChat from "../hooks/useChat";

const Home = () => {
  const {
    messages,
    loading,
    sendMessage,
  } = useChat();

  return (
    <div className="flex h-screen bg-neutral-900 text-white">

      <Sidebar />

      <ChatWindow
        messages={messages}
        loading={loading}
        sendMessage={sendMessage}
      />

    </div>
  );
};

export default Home;