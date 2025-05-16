import { Box, IconButton } from '@mui/joy';
import MenuIcon from '@mui/icons-material/Menu';
import { Outlet } from 'react-router-dom';
import { useDrawer } from '../contexts/DrawerContext';

export default function Layout() {
  const { onOpen } = useDrawer();

  return (
    <Box
      sx={{
        bgcolor: 'background.body',
        color: 'text.primary',
        minHeight: '100vh',
        p: 4,
      }}
    >
      {/* Top bar with drawer toggle */}
      <Box sx={{ mb: 2 }}>
        <IconButton onClick={onOpen} variant="outlined" size="md">
          <MenuIcon />
        </IconButton>
      </Box>

      {/* Renders the route's page content */}
      <Outlet />
    </Box>
  );
}