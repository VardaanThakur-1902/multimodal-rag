import { useRef, useState } from "react";
import toast from "react-hot-toast";

const useChat = () => {

  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const abortController = useRef(null);

  const sendMessage = async (question,sessionId) => {

    const userMessage = {
      role: "user",
      content: question,
    };

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
            session_id: sessionId,
          }),
          signal: abortController.current.signal,
        }
      );

      if (!response.ok) {
        throw new Error("Request failed");
      }

      if (!response.body) {
        throw new Error("No response body");
      }

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

        const token = decoder.decode(
          value,
          {
            stream: true,
          }
        );

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

      abortController.current = null;

    }

  };

  const stopGeneration = () => {

    if (abortController.current) {

      abortController.current.abort();

    }

    setLoading(false);

  };

  return {
    messages,
    loading,
    setMessages,
    sendMessage,
    stopGeneration,
  };

};

export default useChat;