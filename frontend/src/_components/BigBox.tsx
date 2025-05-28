import React, { ReactNode } from 'react';
import { Box, Typography } from '@mui/joy';

interface BigBoxProps {
  title: string;
  children: ReactNode;
}

const BigBox: React.FC<BigBoxProps> = ({ title, children }) => {
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
        <Typography fontWeight="bold" sx={{ color: 'white' }}>
          {title}
        </Typography>
      </Box>
      <Box sx={{ p: 2 }}>
        {children}
      </Box>
    </Box>
  );
};

export default BigBox;
