import axios from "axios";
import { API_URL } from "../utils/constants";
import { resetSession } from "../utils/session";

const axiosInstance = axios.create({
  baseURL: API_URL,
});

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      resetSession();
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
