import { useEffect } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { DrawerProvider } from './contexts/DrawerContext';
import { GlobalDrawer } from './components/GlobalDrawer';
import LoginForm from './components/LoginForm';
import Dashboard from './pages/Dashboard';
import Knowledgebase from './pages/Knowledgebase';
import Timeline from './pages/Timeline';
import Evaluations from './pages/Evaluations';
import { ApolloProvider } from '@apollo/client';
import AuthProvider from "./components/AuthProvider";
import client from "./apolloClient";
import { config } from '../config';

function App() {
  useEffect(() => {
    fetch(config.apiUrl + '/csrf/', {
      method: 'GET',
      credentials: 'include',
    });
  }, []);

  return (
    <ApolloProvider client={client} >
    <DrawerProvider>
      <GlobalDrawer />
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<LoginForm />} />
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="knowledgebase" element={<Knowledgebase />} />
          <Route path="timeline" element={<Timeline />} />
          <Route path="evaluations" element={<Evaluations />} />
          <Route path="/" element={<Navigate to="/login" replace />} />
        </Routes>
      </AuthProvider>
    </DrawerProvider>
    </ApolloProvider>
  );
}

export default App;