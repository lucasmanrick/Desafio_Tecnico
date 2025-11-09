// src/store/authStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { LoginResponse} from '../types';

interface AuthStore {
  accessToken: string | null;
  refreshToken: string | null;
  user: LoginResponse['user'] | null;
  login: (data: LoginResponse) => void;
  setTokens: (access: string, refresh: string) => void;
  logout: () => void;
}

const storage = {
  getItem: async (name: string) => {
    const value = await AsyncStorage.getItem(name);
    if (!value) return null;
    try {
      return JSON.parse(value);
    } catch {
      return null;
    }
  },
  setItem: async (name: string, value: any) => {
    await AsyncStorage.setItem(name, JSON.stringify(value));
  },
  removeItem: async (name: string) => {
    await AsyncStorage.removeItem(name);
  },
};

export const useAuthStore = create<AuthStore>()(
  persist(
    (set) => ({
      accessToken: null,
      refreshToken: null,
      user: null,
      login: (data: LoginResponse) =>
        set({
          accessToken: data.access,
          refreshToken: data.refresh,
          user: data.user,
        }),
      setTokens: (access: string, refresh: string) =>
        set({ accessToken: access, refreshToken: refresh }),
      logout: () =>
        set({
          accessToken: null,
          refreshToken: null,
          user: null,
        }),
    }),
    {
      name: 'auth-storage',
      storage,
    }
  )
);
