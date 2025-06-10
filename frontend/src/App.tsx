// App.tsx
import { useEffect } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { DrawerProvider } from './contexts/DrawerContext';
import { GlobalDrawer } from './components/GlobalDrawer';
import LoginForm from './components/LoginForm';
import Dashboard from './_pages/Dashboard';
import Knowledgebase from './_pages/Knowledgebase';
import Timeline from './pages/Timeline';
import Evaluations from './_pages/Evaluations';
import { ApolloProvider } from '@apollo/client';
import { AuthProvider, PrivateRoute } from './components/AuthContext';
import client from './apolloClient';
import { config } from '../config';

function App() {
  useEffect(() => {
    fetch(config.apiUrl + '/csrf/', {
      method: 'GET',
      credentials: 'include',
    });
  }, []);

  return (
    <ApolloProvider client={client}>
      <DrawerProvider>
        <GlobalDrawer />
        <AuthProvider>
          <Routes>
            <Route path="/login" element={<LoginForm />} />
            <Route element={<PrivateRoute />}>
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/knowledgebase" element={<Knowledgebase />} />
              <Route path="/timeline" element={<Timeline />} />
              <Route path="/evaluations" element={<Evaluations />} />
            </Route>
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </AuthProvider>
      </DrawerProvider>
    </ApolloProvider>
  );
}

export default App;
