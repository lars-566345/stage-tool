import React, { useState } from 'react';
import { Box, Typography, Avatar, Button } from '@mui/joy';
import SidebarStudent from '../_components/SidebarStudent';
import EvaluationBox from '../_components/EvaluationBox';
import userData from '../_data/users.json';

interface Evaluation {
  date: string;
  name: string;
  content: string;
  image: string;
}

const ITEMS_PER_PAGE = 3;

const Evaluations: React.FC = () => {
  const [evaluations, setEvaluations] = useState<Evaluation[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);

  const addEvaluation = (text: string): void => {
    const newEval: Evaluation = {
      date: new Date().toLocaleDateString('nl-NL'),
      name: userData.name,
      content: text,
      image: userData.profilePicture,
    };
    const updatedEvals = [newEval, ...evaluations];
    setEvaluations(updatedEvals);
    setCurrentPage(1); 
  };

  const totalPages = Math.ceil(evaluations.length / ITEMS_PER_PAGE);
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const paginatedEvaluations = evaluations.slice(startIndex, startIndex + ITEMS_PER_PAGE);

  return (
    <Box sx={{ display: 'flex' }}>
      <SidebarStudent />

      <Box sx={{ flex: 1, p: 4 }}>
        {/* Title */}
        <Box sx={{ textAlign: 'center', mb: 4 }}>
          <Typography level="h2" sx={{ fontWeight: 'bold' }}>
            Evaluations
          </Typography>
        </Box>

        {/* User Info */}
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 4 }}>
          <Avatar src={userData.profilePicture} sx={{ mr: 2, width: 80, height: 80 }} />
          <Box>
            <Typography level="h4">{userData.name}</Typography>
            <Typography level="body-sm">
              Semester 5<br />
              Preparing for internship<br />
              Last Evaluation 16-02-2025
            </Typography>
          </Box>
        </Box>

        {/* Evaluation Input */}
        <EvaluationBox onSend={addEvaluation} />

        {/* Paginated Evaluation List */}
        {paginatedEvaluations.map((evalItem, idx) => (
          <Box
            key={startIndex + idx}
            sx={{ backgroundColor: '#f2f2f2', borderRadius: 2, p: 2, mb: 2 }}
          >
            <Typography level="body-sm" mb={1}>
              Evaluation {evaluations.length - (startIndex + idx)} &nbsp; | &nbsp; {evalItem.date}
            </Typography>
            <Box sx={{ display: 'flex', alignItems: 'flex-start' }}>
              <Avatar src={evalItem.image} sx={{ mr: 2 }} />
              <Box>
                <Typography fontWeight="bold">{evalItem.name}</Typography>
                <Typography>{evalItem.content}</Typography>
              </Box>
            </Box>
          </Box>
        ))}

        {/* Pagination Controls */}
        {totalPages > 1 && (
          <Box sx={{ display: 'flex', justifyContent: 'center', mt: 3, gap: 2 }}>
            <Button
              disabled={currentPage === 1}
              onClick={() => setCurrentPage(currentPage - 1)}
              sx={{ backgroundColor: '#00838f' }}
            >
              Previous
            </Button>
            <Typography>{`Page ${currentPage} of ${totalPages}`}</Typography>
            <Button
              disabled={currentPage === totalPages}
              onClick={() => setCurrentPage(currentPage + 1)}
              sx={{ backgroundColor: '#00838f' }}
            >
              Next
            </Button>
          </Box>
        )}
      </Box>
    </Box>
  );
};

export default Evaluations;
