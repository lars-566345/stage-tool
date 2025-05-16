import { Button } from '@mui/joy';
import { useDrawer } from '../contexts/DrawerContext';

function OpenMenuButton() {
  const { onOpen } = useDrawer();

  return <Button onClick={onOpen}>Open Drawer</Button>;
}

export default OpenMenuButton;