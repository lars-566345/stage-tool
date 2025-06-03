import React from 'react';
import { Box, Typography } from '@mui/joy';

const SmallBox = ({ title, children }) => {
  return (
    <Box
      sx={{
        flex: 1,
        minHeight: 250,
        bgcolor: '#008489',
        borderRadius: 3,
        overflow: 'hidden',
        width: '100%',
      }}
    >
      <Box sx={{ bgcolor: '#b0d3d6', p: 1 }}>
        <Typography sx={{ color: 'white' }} fontWeight="bold">{title}</Typography>
      </Box>
      <Box sx={{ p: 2, color: 'white' }}>
        {children}
      </Box>
    </Box>
  );
};

export default SmallBox;
