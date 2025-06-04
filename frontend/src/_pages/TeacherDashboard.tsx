import React, { useState } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/joy';
import KeyboardArrowLeft from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowRight from '@mui/icons-material/KeyboardArrowRight';
import SidebarTeacher from '../Components/SidebarTeacher';
import SmallBox from '../Components/SmallBox';
import KnowledgebaseBox from '../Components/KnowledgebaseBox';
import studentData from '../data/teacherStudents.json';
import boxData from '../data/knowledgebaseData.json';

interface Student {
  id: number;
  name: string;
  semester: number;
  profilePicture: string;
  lastEvaluation: string;
  // add other fields if needed
}

interface KnowledgebaseItem {
  tag: string;
  title: string;
  description: string;
  // add other fields if needed
}

interface TeacherDashboardProps {
  navigate: (path: string) => void;
}

const TeacherDashboard: React.FC<TeacherDashboardProps> = ({ navigate }) => {
  const [currentStudent, setCurrentStudent] = useState<number>(0);

  const nextStudent = () => {
    setCurrentStudent((prev) => (prev + 1) % studentData.length);
  };

  const prevStudent = () => {
    setCurrentStudent((prev) => (prev - 1 + studentData.length) % studentData.length);
  };

  const student: Student = studentData[currentStudent];

  return (
    <Box sx={{ display: 'flex' }}>
      <SidebarTeacher />

      <Box sx={{ flex: 1, p: 4 }}>
        {/* Teacher name */}
        <Typography
          sx={{
            fontSize: { xs: '24px', md: '32px' },
            fontWeight: 'bold',
            textAlign: 'center',
            mb: 4,
          }}
        >
          Berry Dekkers
        </Typography>

        {/* Gekoppelde student */}
        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2, mb: 4, width: 350, height: 300 }}>
          <SmallBox title="Gekoppelde studenten">
            <Box
              sx={{
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                height: '100%',
                position: 'relative',
                px: 2,
                pt: 2,
              }}
            >
              {/* Arrows + Avatar */}
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <IconButton onClick={prevStudent} sx={{ color: 'white' }}>
                  <KeyboardArrowLeft />
                </IconButton>

                <img
                  src={student.profilePicture}
                  alt={student.name}
                  style={{
                    width: 80,
                    height: 80,
                    borderRadius: '50%',
                    objectFit: 'cover',
                  }}
                />

                <IconButton onClick={nextStudent} sx={{ color: 'white' }}>
                  <KeyboardArrowRight />
                </IconButton>
              </Box>

              {/* Student Info */}
              <Box sx={{ mt: 2, color: 'white', textAlign: 'left' }}>
                <Typography fontWeight="bold" fontSize="md" sx={{ mb: 0.5, color: 'white' }}>
                  {student.name}
                </Typography>
                <Typography sx={{ fontSize: '0.75rem', color: 'white' }}>
                  Semester {student.semester}
                </Typography>
                <Typography sx={{ fontSize: '0.75rem', color: 'white' }}>
                  Last Evaluation {student.lastEvaluation}
                </Typography>
              </Box>

              {/* Buttons */}
              <Box sx={{ mt: 2, display: 'flex', justifyContent: 'center', gap: 1 }}>
                <Button
                  size="sm"
                  sx={{
                    backgroundColor: '#b0d3d6',
                    color: 'white',
                  }}
                  onClick={() => navigate(`/teacher/student/${student.id}`)}
                >
                  Profile
                </Button>
                <Button
                  size="sm"
                  sx={{
                    backgroundColor: '#ffffff',
                    color: '#00838f',
                    fontWeight: 'bold',
                    '&:hover': {
                      backgroundColor: '#e0f7fa',
                    },
                  }}
                >
                  Portfolio
                </Button>
              </Box>
            </Box>
          </SmallBox>
        </Box>

        {/* Pinned Posts */}
        <Typography sx={{ fontWeight: 'bold', fontSize: '1.2rem' }}>Pinned Posts</Typography>

        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2 }}>
          {boxData.map((box: KnowledgebaseItem, index: number) => (
            <KnowledgebaseBox
              key={index}
              index={index}
              tag={box.tag}
              title={box.title}
              description={box.description}
              role="teacher-dashboard"
            />
          ))}
        </Box>
      </Box>
    </Box>
  );
};

export default TeacherDashboard;
