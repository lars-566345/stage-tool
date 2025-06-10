// AuthContext.tsx
import React, { createContext, useContext, useEffect, useState } from 'react';
import { useLazyQuery, gql } from '@apollo/client';
import { Navigate, Outlet } from 'react-router-dom';

type UserType = {
  id: string;
};

type AuthContextType = {
  user: UserType | null;
  loading: boolean;
};

export const GET_LOGGED_IN_USER = gql`
  query GetLoggedInUser {
    me {
      ... on CoachProfileType {
        id
        __typename
      }
      ... on StudentProfileType {
        id
        __typename
      }
    }
  }
`;

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [getUser, { data, loading: queryLoading, called }] = useLazyQuery(GET_LOGGED_IN_USER, {
    fetchPolicy: 'network-only',
  });

  const [user, setUser] = useState<UserType | null>(null);
  const [userLoading, setUserLoading] = useState(true);

  useEffect(() => {
    getUser();
  }, [getUser]);

  useEffect(() => {
    if (!queryLoading && called) {
      if (data?.me) {
        setUser(data.me);
      } else {
        setUser(null);
      }
      setUserLoading(false);
    }
  }, [data, queryLoading, called]);

  return (
    <AuthContext.Provider value={{ user, loading: userLoading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within an AuthProvider');
  return context;
};

export const PrivateRoute = () => {
  const { user, loading } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <Navigate to="/login" replace />;
  return <Outlet />;
};
