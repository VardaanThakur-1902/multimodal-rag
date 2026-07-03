import { useEffect, useState } from "react";
import toast from "react-hot-toast";

import sessionService from "../services/sessionService";

const useSessions = () => {

  const [sessions, setSessions] =
    useState([]);

  const [currentSession, setCurrentSession] =
    useState(null);

  useEffect(() => {

    loadSessions();

  }, []);

  const loadSessions = async () => {

    try {

      const data =
        await sessionService.getSessions();

      setSessions(data);

      if (
        data.length > 0 &&
        !currentSession
      ) {

        setCurrentSession(
          data[0].id
        );

      }

    } catch {

      toast.error(
        "Unable to load sessions."
      );

    }

  };

  const createSession =
    async () => {

      try {

        const session =
          await sessionService.createSession();

        setSessions(prev => [
          session,
          ...prev,
        ]);

        setCurrentSession(
          session.id
        );

      } catch {

        toast.error(
          "Unable to create session."
        );

      }

    };

  const loadMessages = async (
      sessionId,
  ) => {

      try {

          const messages =
              await sessionService.getMessages(
                  sessionId
              );

          return messages;

      } catch {

          toast.error(
              "Unable to load messages."
          );

          return [];

      }

  };

  return {

    sessions,

    currentSession,

    setCurrentSession,

    createSession,

    loadMessages,

    loadSessions,

  };

};

export default useSessions;