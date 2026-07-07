import api from "./api";

const documentService = {

  async getDocuments() {

    const res = await api.get(
      "/documents"
    );

    return res.data.data;

  },

  async upload(file, sessionId) {

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    const res = await api.post(
      "/upload",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    return res.data;

  },

  async delete(documentId) {

    const res = await api.delete(
      `/documents/${documentId}`
    );

    return res.data;

  },

  previewUrl(documentId) {

    return `http://127.0.0.1:8000/api/v1/documents/${documentId}/preview`;

  },

};

export default documentService;