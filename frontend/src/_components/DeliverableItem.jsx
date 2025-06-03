import React from 'react';
import { Box, Typography } from '@mui/joy';

const DeliverableItem = ({ label, completed, selected, onClick }) => {
  const circleColor = selected || completed ? '#00838f' : 'transparent';
  const circleBorderColor = '#00838f';

  return (
    <Box
      onClick={onClick}
      sx={{
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        gap: 1,
        px: 1,
        py: 0.5,
      }}
    >
      <Box
      data-testid="deliverable-dot"
        sx={{
          width: 20,
          height: 20,
          borderRadius: '50%',
          backgroundColor: circleColor,
          border: `2px solid ${circleBorderColor}`,
          transition: 'background-color 0.3s ease',
        }}
      />
      <Typography>{label}</Typography>
    </Box>
  );
};

export default DeliverableItem;
