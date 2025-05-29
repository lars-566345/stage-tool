import React, { ReactNode } from 'react';
import { Box } from '@mui/joy';
import SidebarStudent from './SidebarStudent';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: { xs: 'column', md: 'row' },
        height: '100vh',
        width: '100vw',
        overflow: 'hidden',
      }}
    >
      <SidebarStudent />
      <Box
        sx={{
          flex: 1,
          p: 2,
          overflow: 'hidden',
        }}
      >
        {children}
      </Box>
    </Box>
  );
};

export default Layout;
