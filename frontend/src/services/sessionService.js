import api from "./api";

const sessionService = {

  async createSession() {

    const res = await api.post(
      "/sessions"
    );

    return res.data;

  },

  async getSessions() {

    const res = await api.get(
      "/sessions"
    );

    return res.data;

  },

  async renameSession(
    id,
    title,
  ) {

    const res = await api.patch(
      `/sessions/${id}`,
      null,
      {
        params: {
          title,
        },
      }
    );

    return res.data;

  },

  async deleteSession(
    id,
  ) {

    await api.delete(
      `/sessions/${id}`
    );

  },

  async getMessages(sessionId) {

      const res = await api.get(
          `/messages/${sessionId}`
      );

      return res.data;

  },

};

export default sessionService;