import React from 'react';
import { Box, List, ListItem } from '@mui/joy';

const SidebarStudent: React.FC = () => {
  return (
    <Box
      sx={{
        width: { xs: '100%', md: 220 },
        height: { xs: 'auto', md: '100vh' },
        bgcolor: 'black',
        color: 'white',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        p: 2,
      }}
    >
      <Box sx={{ mb: 2, width: '100%', textAlign: 'center' }}>
        <img
          src="img/fontyslogo.png"
          alt="Fontys Logo"
          style={{ width: '80%', height: 'auto' }}
        />
      </Box>
      <List
        size="lg"
        sx={{ '& .MuiListItem-root': { fontSize: '1.2rem' }, textAlign: 'center' }}
      >
        <ListItem component="a" href="/dashboard" sx={{ color: 'white' }}>
          Dashboard
        </ListItem>
        <ListItem component="a" href="/knowledgebase" sx={{ color: 'white' }}>
          Knowledgebase
        </ListItem>
        <ListItem component="a" href="/timeline" sx={{ color: 'white' }}>
          Timeline
        </ListItem>
        <ListItem component="a" href="/evaluations" sx={{ color: 'white' }}>
          Evaluations
        </ListItem>
      </List>
    </Box>
  );
};

export default SidebarStudent;
