import React from 'react';
import { Button } from '@mui/joy';

interface TimelinePhaseProps {
  label: string;
  active: boolean;
  onClick?: () => void;
}

const TimelinePhase: React.FC<TimelinePhaseProps> = ({ label, active, onClick }) => {
  return (
    <Button
      variant="solid"
      onClick={onClick}
      sx={{
        borderRadius: 'xl',
        width: 300,
        height: 100,
        whiteSpace: 'normal',
        wordBreak: 'break-word',
        backgroundColor: active ? '#A5D2D4' : '#008387',
        color: 'white',
        fontSize: '1.1rem',
        textAlign: 'center',
        '&:hover': {
          backgroundColor: active ? '#94c3c5' : '#006b70',
        },
      }}
    >
      {label}
    </Button>
  );
};

export default TimelinePhase;
