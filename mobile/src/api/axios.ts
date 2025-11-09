import axios, { AxiosError, AxiosRequestConfig }from 'axios';
import Constants from 'expo-constants';
import { useAuthStore } from '../store/authStore';


const API_URL = Constants.expoConfig?.extra?.API_URL;
console.log("API_URL =", API_URL);

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  }
});


const refreshAccessToken = async (): Promise<string | null> => {
  const { refreshToken, setTokens, logout } = useAuthStore.getState();

  if (!refreshToken) return null;

  try {
    const response = await api.post('/auth/refresh/', { refresh: refreshToken });
    const newAccess = response.data.access;
    const newRefresh = response.data.refresh;


    setTokens(newAccess, newRefresh);

    return newAccess;
  } catch (err) {
    console.log("Erro ao tentar renovar token:", err);
    logout(); 
    return null;
  }
};

api.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config as AxiosRequestConfig & { _retry?: boolean };

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true; // evita loop infinito
      const newAccess = await refreshAccessToken();
      if (newAccess && originalRequest.headers) {
        originalRequest.headers.Authorization = `Bearer ${newAccess}`;
        return api(originalRequest); // refaz a requisição com token novo
      }
    }

    return Promise.reject(error);
  }
);


