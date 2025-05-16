import Drawer from '@mui/joy/Drawer';
import ModalClose from '@mui/joy/ModalClose';
import Typography from '@mui/joy/Typography';
import List from '@mui/joy/List';
import ListItem from '@mui/joy/ListItem';
import ListItemButton from '@mui/joy/ListItemButton';
import { useDrawer } from '../contexts/DrawerContext';
import { Link as RouterLink } from 'react-router-dom';

export function GlobalDrawer() {
  const { open, onClose } = useDrawer();

  const navItems = [
    { label: 'Home', path: '/' },
    { label: 'Knowledgebase', path: '/knowledgebase' },
    { label: 'Timeline', path: '/timeline' },
    { label: 'Evaluations', path: '/evaluations' },
  ];

  return (
    <Drawer open={open} onClose={onClose} size="md">
      <ModalClose />
      <Typography level="h4" sx={{ mt: 2, mb: 1, ml: 2 }}>
        Fontys
      </Typography>
      <List>
        {navItems.map((item) => (
          <ListItem key={item.path}>
            <ListItemButton
              component={RouterLink}
              to={item.path}
              onClick={onClose}
            >
              {item.label}
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
}