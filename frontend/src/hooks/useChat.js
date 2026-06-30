import { useState } from "react";
import toast from "react-hot-toast";

import api from "../services/api";

const useChat = () => {

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] =
    useState(false);

  const sendMessage = async (
    question
  ) => {

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

      const res = await api.post(
        "/chat",
        {
          question,
        }
      );

      const assistantMessage = {
        role: "assistant",
        content: res.data.answer,
      };

      setMessages((prev) => [
        ...prev,
        assistantMessage,
      ]);

    } catch (err) {

      toast.error(
        "Unable to connect to backend."
      );

    } finally {

      setLoading(false);

    }
  };

  return {
    messages,
    loading,
    sendMessage,
  };
};

export default useChat;