import React from 'react';
import { Box, Typography, Avatar } from '@mui/joy';
import SidebarTeacher from '../_components/SidebarTeacher';
import studentData from '../_data/teacherStudents.json';

interface Evaluation {
  date: string;
  text: string;
}

interface Student {
  id: number;
  name: string;
  semester: number;
  profilePicture: string;
  lastEvaluation: string;
  evaluations?: Evaluation[];
}

interface StudentProfileTeacherProps {
  studentId: string | number;
}

const StudentProfileTeacher: React.FC<StudentProfileTeacherProps> = ({ studentId }) => {
  const student: Student | undefined = studentData.find(
    (s) => s.id === (typeof studentId === 'string' ? parseInt(studentId, 10) : studentId)
  );

  if (!student) {
    return <Typography sx={{ p: 4 }}>Student not found</Typography>;
  }

  const evaluations = student.evaluations || [];

  return (
    <Box sx={{ display: 'flex' }}>
      <SidebarTeacher />
      <Box sx={{ flex: 1, p: 4 }}>
        <Typography
          level="h1"
          sx={{
            fontSize: '32px',
            mb: 4,
            textAlign: 'center',
            width: '100%',
          }}
        >
          Student Profile
        </Typography>

        {/* Student Header */}
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
          <Avatar src={student.profilePicture} sx={{ width: 100, height: 100, mr: 2 }} />
          <Box>
            <Typography level="h2" sx={{ fontWeight: 'bold' }}>
              {student.name}
            </Typography>
            <Typography>Semester {student.semester}</Typography>
            <Typography>Preparing for internship</Typography>
            <Typography>Last Evaluation {student.lastEvaluation}</Typography>
          </Box>
        </Box>

        {/* Evaluations */}
        {evaluations.map((evalItem, index) => (
          <Box
            key={index}
            sx={{
              backgroundColor: '#e0e0e0',
              p: 2,
              borderRadius: 2,
              mb: 2,
            }}
          >
            <Typography level="body-sm" sx={{ mb: 1 }}>
              Evaluation {evaluations.length - index} &nbsp; | &nbsp; {evalItem.date}
            </Typography>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
              <Avatar src={student.profilePicture} sx={{ width: 30, height: 30, mr: 1 }} />
              <Typography fontWeight="bold">{student.name}</Typography>
            </Box>
            <Typography>{evalItem.text}</Typography>
          </Box>
        ))}
      </Box>
    </Box>
  );
};

export default StudentProfileTeacher;
