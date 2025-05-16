import { Routes, Route } from 'react-router-dom';
import { DrawerProvider } from './contexts/DrawerContext';
import { GlobalDrawer } from './components/GlobalDrawer';
import Home from './pages/Home';
import Knowledgebase from './pages/Knowledgebase';
import Timeline from './pages/Timeline';
import Evaluations from './pages/Evaluations';
import Layout from './components/Layout';

function App() {
  return (
    <DrawerProvider>
      <GlobalDrawer />
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="knowledgebase" element={<Knowledgebase />} />
          <Route path="timeline" element={<Timeline />} />
          <Route path="evaluations" element={<Evaluations />} />
        </Route>
      </Routes>
    </DrawerProvider>
  );
}

export default App;