import { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useQuery, gql } from '@apollo/client';

const PUBLIC_ROUTES = ['/login'];

export const GET_LOGGED_IN_USER = gql`
  query GetLoggedInUser {
    me {
      id
    }
  }
`;

const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const location = useLocation();
  const navigate = useNavigate();
  const currentPath = location.pathname;

  const isPublic = PUBLIC_ROUTES.includes(currentPath);

  const { data, loading } = useQuery(GET_LOGGED_IN_USER, {
    fetchPolicy: 'network-only',
    skip: isPublic,
  });

  useEffect(() => {
    if (!isPublic && !loading && !data?.me) {
      navigate('/login');
    }
  }, [loading, data, isPublic, navigate]);

  if (!isPublic && loading) return <div>Loading...</div>;

  return <>{children}</>;
};

export default AuthProvider;
