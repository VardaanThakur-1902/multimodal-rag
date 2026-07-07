import api from "./api";

const sessionService = {

  async createSession(name) {

      const res = await api.post(
          "/sessions/",
          {
              name,
          }
      );

      return res.data;

  },

  async attachDocuments(
      sessionId,
      documentIds,
  ) {

      const res = await api.post(
          `/sessions/${sessionId}/documents`,
          {
              document_ids: documentIds,
          }
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