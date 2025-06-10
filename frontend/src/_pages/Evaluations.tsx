import React, { useState } from 'react';
import { Box, Typography, Avatar, Button } from '@mui/joy';
import SidebarStudent from '../_components/SidebarStudent';
import EvaluationBox from '../_components/EvaluationBox';
import { gql } from '@apollo/client';
import { useQuery } from '@apollo/client';
import { useAuth } from '../components/AuthContext';

// Interfaces
interface Evaluation {
  date: string;
  name: string;
  content: string;
  image: string;
}

interface UserData {
  name: string;
  profilePicture: string;
}

const GET_STUDENT_DETAILS = gql`
  query studentProfile($id: ID!) {
    studentProfile(id: $id) {
      firstName
      lastName
      evaluations {
        id
        feedback
        coachName
        createdAt
      }
    }
  }
`;

// Constants
const ITEMS_PER_PAGE = 3;

const Evaluations: React.FC = () => {
  const [evaluations, setEvaluations] = useState<Evaluation[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);

  const { user, loading: authLoading } = useAuth();

  const { loading: dataLoading, error: dataError, data } = useQuery(GET_STUDENT_DETAILS, {
      fetchPolicy: 'network-only',
      variables: { id: user?.id },
      skip: authLoading || !user?.id,
  })

  if (dataLoading) return <p>Loading...</p>;
  if (dataError) return <p>Error! {dataError.message}</p>;

  const student = data.studentProfile;

  // const addEvaluation = (text: string) => {
  //   const newEval: Evaluation = {
  //     date: new Date().toLocaleDateString('nl-NL'),
  //     name: typedUserData.name,
  //     content: text,
  //     image: typedUserData.profilePicture,
  //   };
  //   setEvaluations([newEval, ...evaluations]);
  //   setCurrentPage(1);
  // };

  const totalPages = Math.ceil(student.evaluations.length / ITEMS_PER_PAGE);
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const paginatedEvaluations = student.evaluations.slice(startIndex, startIndex + ITEMS_PER_PAGE);

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
          <Avatar src="/public/studentPicture.png" sx={{ mr: 2, width: 80, height: 80 }} />
          <Box>
            <Typography level="h4">{student.firstName + " " + student.lastName}</Typography>
            <Typography level="body-sm">
              {/* FIX GETTING CURRENT PROGRESS SEMESTER */}
              Semester 5<br />
              Preparing for internship<br />
              Last Evaluation 16-02-2025
            </Typography>
          </Box>
        </Box>

        {/* Evaluation Input */}
        {/* <EvaluationBox onSend={addEvaluation} /> */}

        {/* Paginated Evaluation List */}
        {paginatedEvaluations.map((evalItem:any, i: number) => (
          <Box
            key={startIndex + i}
            sx={{ backgroundColor: '#f2f2f2', borderRadius: 2, p: 2, mb: 2 }}
          >
            <Typography level="body-sm" mb={1}>
              Evaluation {student.evaluations.length - (startIndex + i)} &nbsp; | &nbsp; {evalItem.date}
            </Typography>
            <Box sx={{ display: 'flex', alignItems: 'flex-start' }}>
              <Avatar src="/public/studentPicture.png" sx={{ mr: 2 }} />
              <Box>
                <Typography fontWeight="bold">{evalItem.createdAt ? new Date(evalItem.createdAt).toISOString().split("T")[0] : ""}</Typography>
                <Typography>{evalItem.feedback}</Typography>
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
