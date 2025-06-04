import React from 'react';
import { Box, Typography, Input } from '@mui/joy';
import SidebarTeacher from '../Components/SidebarTeacher';
import StudentCard from '../Components/StudentCard';
import studentData from '../data/teacherStudents.json';

interface Student {
  id: number;
  name: string;
  semester: number;
  profilePicture: string;
  lastEvaluation: string;
  evaluations?: { date: string; text: string }[];
  // add any other fields your student object has
}

const Students: React.FC = () => {
  return (
    <Box sx={{ display: 'flex' }}>
      <SidebarTeacher />

      <Box sx={{ flex: 1, p: 4, backgroundColor: 'white' }}>
        <Typography
          sx={{
            fontSize: { xs: '24px', md: '32px' },
            fontWeight: 'bold',
            textAlign: 'center',
            mb: 3,
          }}
        >
          Students
        </Typography>

        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            mb: 4,
          }}
        >
          <Input
            placeholder="Zoeken..."
            sx={{
              width: '100%',
              maxWidth: 500,
              backgroundColor: '#eeeeee',
              borderRadius: 'lg',
            }}
          />
        </Box>

        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 2 }}>
          {studentData.map((student: Student, index: number) => (
            <StudentCard key={index} student={student} />
          ))}
        </Box>
      </Box>
    </Box>
  );
};

export default Students;
