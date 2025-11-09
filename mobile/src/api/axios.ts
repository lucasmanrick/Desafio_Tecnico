import axios from 'axios';
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

api.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);



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




