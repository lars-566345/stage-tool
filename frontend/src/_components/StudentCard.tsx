import React from 'react';
import { Box, Button, Typography } from '@mui/joy';

interface Student {
  id: string | number;
  name: string;
  semester: number | string;
  lastEvaluation: string;
  profilePicture: string;
}

interface StudentCardProps {
  student: Student;
}

const StudentCard: React.FC<StudentCardProps> = ({ student }) => {
  const handleProfileClick = () => {
    // Verander de URL zonder pagina te herladen
    window.history.pushState({}, '', `/teacher/student/${student.id}`);
    window.dispatchEvent(new PopStateEvent('popstate')); // Triggert App.js om de juiste component te laden
  };

  return (
    <Box
      sx={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        backgroundColor: 'white',
        width: '100%',
        maxWidth: 900,
        px: 3,
        py: 2,
        borderBottom: '1px solid #e0e0e0',
      }}
    >
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
        <img
          src={student.profilePicture}
          alt={student.name}
          style={{ width: 60, height: 60, borderRadius: '50%' }}
        />
        <Box>
          <Typography fontWeight="bold">{student.name}</Typography>
          <Typography fontSize="sm">Semester {student.semester}</Typography>
          <Typography fontSize="sm">Preparing for internship</Typography>
          <Typography fontSize="sm">Last Evaluation {student.lastEvaluation}</Typography>
        </Box>
      </Box>

      <Box sx={{ display: 'flex', gap: 1 }}>
        <Button
          size="sm"
          sx={{ backgroundColor: '#008387', color: 'white' }}
          onClick={handleProfileClick}
        >
          Profile
        </Button>
        <Button size="sm" sx={{ backgroundColor: '#000', color: 'white' }}>
          Portfolio
        </Button>
      </Box>
    </Box>
  );
};

export default StudentCard;
