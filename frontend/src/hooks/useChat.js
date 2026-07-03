import toast from "react-hot-toast";
import { useRef, useState } from "react";

const useChat = () => {

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const [sessions, setSessions] = useState([]);

  const [currentSession, setCurrentSession] = useState(null);

  const abortController = useRef(null);

  const sendMessage = async (question) => {

    const userMessage = {
      role: "user",
      content: question,
    };

    setSessions((prev) =>
      prev.map((session) => {

        if (session.id !== currentSession) {
          return session;
        }

        const title =
          session.title === "New Chat"
            ? (
                question.length > 30
                  ? question.substring(0, 30) + "..."
                  : question
              )
            : session.title;

        return {
          ...session,
          title,
        };

      })
    );

    setMessages((prev) => [
      ...prev,
      userMessage,
    ]);

    setLoading(true);

    try {

      abortController.current = new AbortController();

      const response = await fetch(
          "http://127.0.0.1:8000/api/v1/chat/stream",
          {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify({
                  question,
              }),
              signal: abortController.current.signal,
          }
      );

      const reader = response.body.getReader();

      const decoder = new TextDecoder();

      let assistantMessage = {
        role: "assistant",
        content: "",
        sources: [],
        streaming: true,
      };

      setMessages((prev) => [
        ...prev,
        assistantMessage,
      ]);

      while (true) {

        const { done, value } =
          await reader.read();

        if (done) break;

        const token = decoder.decode(value);

        assistantMessage.content += token;

        setMessages((prev) => {

          const copy = [...prev];

          copy[copy.length - 1] = {
            ...assistantMessage,
          };

          return copy;

        });

      }

      assistantMessage.streaming = false;

      setMessages((prev) => {

        const copy = [...prev];

        copy[copy.length - 1] = {
          ...assistantMessage,
        };

        return copy;

      });

    } catch (err) {

        if (err.name !== "AbortError") {

          toast.error(
            "Unable to connect to backend."
          );

        }

      } finally {

          setLoading(false);

        }

      };


  const stopGeneration = () => {

        if (abortController.current) {
            abortController.current.abort();
        }

        setLoading(false);
    };

  const createSession = () => {

    const session = {
        id: crypto.randomUUID(),
        title: "New Chat",
        messages: [],
    };

    setSessions(prev =>
        prev.map(session =>
            session.id === currentSession
                ? {
                      ...session,
                      messages: [
                          ...session.messages,
                          userMessage,
                      ],
                  }
                : session
        )
    );

    setCurrentSession(session.id);

    setMessages([]);

  };

  const selectSession = (sessionId) => {

    const session = sessions.find(
        s => s.id === sessionId
    );

    if (!session) return;

    setCurrentSession(sessionId);

    setMessages(session.messages);

};

  return {
    messages,
    loading,
    sessions,
    currentSession,
    setSessions,
    setCurrentSession,
    sendMessage,
    stopGeneration,
    createSession,
    selectSession,
  };

};

export default useChat;