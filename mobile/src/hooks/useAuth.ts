// src/hooks/useAuth.ts
import { useAuthStore } from '../store/authStore';

export const useAuth = () => {
  const accessToken = useAuthStore((state) => state.accessToken);
  const refreshToken = useAuthStore((state) => state.refreshToken);
  const user = useAuthStore((state) => state.user);
  const login = useAuthStore((state) => state.login);
  const logout = useAuthStore((state) => state.logout);

  const isAuthenticated = !!accessToken && !!user;

  return {
    accessToken,
    refreshToken,
    user,
    login,
    logout,
    isAuthenticated,
  };
};
