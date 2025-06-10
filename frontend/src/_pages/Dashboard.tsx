import React from 'react';
import Layout from '../_components/Layout';
import BigBox from '../_components/BigBox';
import SmallBox from '../_components/SmallBox';
import { Box, Typography } from '@mui/joy';
import userData from '../_data/users.json';
import { gql } from '@apollo/client';
import { useAuth } from '../components/AuthContext';
import { useQuery } from '@apollo/client';

// Type definitions for imported data
interface Badge {
  image: string;
  label: string;
}

interface SemesterCoach {
  name: string;
  image: string;
}

interface Timeline {
  title: string;
  subtitle: string;
}

interface UserData {
  name: string;
  evaluationDates: string[];
  timeline: Timeline;
  semesterCoach: SemesterCoach;
  badges: Badge[];
}

const GET_STUDENT_DETAILS = gql`
  query studentProfile($id: ID!) {
    studentProfile(id: $id) {
      firstName
      lastName
      evaluations {
        id
        createdAt
      }
      id
      earnedBadges {
        id
        label
      }
      favoriteArticles {
        id
        title
        tag
      }
      coaches {
        firstName
        lastName
      }
    }
  }
`;

const Dashboard: React.FC = () => {
  const { user, loading: authLoading } = useAuth();

  const { loading: dataLoading, error: dataError, data } = useQuery(GET_STUDENT_DETAILS, {
      fetchPolicy: 'network-only',
      variables: { id: user?.id },
      skip: authLoading || !user?.id,
  })

  if (dataLoading) return <p>Loading...</p>;
  if (dataError) return <p>Error! {dataError.message}</p>;

  const student = data.studentProfile;

  const {
    timeline,
  } = userData as UserData;

  return (
    <Layout>
      <Box sx={{ textAlign: 'center', mb: 5 }}>
        <Typography sx={{ fontSize: { xs: '24px', md: '32px' }, fontWeight: 'bold', color: 'black' }}>
          {student.firstName + " " + student.lastName}
        </Typography>
      </Box>

      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2 }}>
        {/* Evaluations */}
        <Box sx={{ flex: 1, minWidth: 260 }}>
          <SmallBox title="Evaluations">
            <Box
              sx={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                height: '100%',
                gap: 1.5,
                mt: 2,
              }}
            >
              {student.evaluations.map((evaluation: any, i: number) => (
                <React.Fragment key={i}>
                  <Typography
                    sx={{
                      color: 'white',
                      textAlign: 'center',
                      fontSize: '1.2rem',
                      fontWeight: 'medium',
                    }}
                  >
                    {evaluation.createdAt ? new Date(evaluation.createdAt).toISOString().split("T")[0] : ""}
                  </Typography>
                  <Box
                    sx={{
                      width: '70%',
                      height: '2px',
                      backgroundColor: 'white',
                      opacity: 0.6,
                    }}
                  />
                </React.Fragment>
              ))}
            </Box>
          </SmallBox>
        </Box>

        {/* Timeline */}
        <Box sx={{ flex: 2, minWidth: 300 }}>
          <BigBox title="Timeline">
            <Box
              sx={{
                backgroundColor: '#A5D2D4',
                borderRadius: '16px',
                padding: 2,
                maxWidth: 300,
                margin: '0 auto',
                textAlign: 'center',
                marginTop: 5,
              }}
            >
              <Typography
                sx={{
                  fontSize: '1.2rem',
                  fontWeight: 'bold',
                  color: '#ffffff',
                }}
              >
                {/*FIX THIS TO TIMELINE FROM DB*/}
                {timeline.title}
              </Typography>
              <Typography
                sx={{
                  fontSize: '1.1rem',
                  fontWeight: 'regular',
                  color: '#ffffff',
                  mt: 0.5,
                }}
              >
                {timeline.subtitle}
              </Typography>
            </Box>
          </BigBox>
        </Box>

        {/* Semester Coach */}
        <Box sx={{ flex: 1, minWidth: 260 }}>
          <SmallBox title="Semestercoach">
            <Box
              sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'flex-end',
                alignItems: 'center',
                pb: 2,
              }}
            >
              <img
                src="/public/coachImage.jpg"
                alt={student.coaches[0].firstName + " " + student.coaches[0].lastName}
                style={{
                  width: 80,
                  height: 80,
                  borderRadius: '50%',
                  objectFit: 'cover',
                  marginBottom: '1rem',
                  marginTop: 15,
                }}
              />
              <Typography
                sx={{
                  color: 'white',
                  fontSize: '1.2rem',
                  fontWeight: 'medium',
                  textAlign: 'center',
                }}
              >
                {student.coaches[0].firstName + " " + student.coaches[0].lastName}
              </Typography>
            </Box>
          </SmallBox>
        </Box>
      </Box>

      {/* Bottom row */}
      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2, mt: 2 }}>
        {/* Pinned Posts */}
        <Box sx={{ flex: 1, minWidth: 300 }}>
          <BigBox title="Pinned Posts">
            <Box
              sx={{
                display: 'grid',
                gridTemplateColumns: 'repeat(2, 1fr)',
                gap: 2,
                overflow: 'hidden',
              }}
            >
              {student.favoriteArticles.map((article: any, i: number) => (
                <Box
                  key={i}
                  onClick={() => (window.location.href = `/knowledgebase/${i}?from=dashboard`)}
                  sx={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 1.5,
                    padding: 1.5,
                    borderRadius: 2,
                    cursor: 'pointer',
                    transition: 'transform 0.2s ease-in-out',
                    '&:hover': {
                      transform: 'scale(1.02)',
                    },
                  }}
                >
                  <img
                    src="/public/knowledgebasePicture.png"
                    alt={article.title}
                    style={{
                      width: 48,
                      height: 48,
                      borderRadius: '12px',
                      objectFit: 'cover',
                    }}
                  />
                  <Box>
                    <Typography
                      sx={{
                        fontWeight: 'bold',
                        color: 'white',
                        fontSize: '1rem',
                      }}
                    >
                      {article.title}
                    </Typography>
                    <Typography
                      sx={{
                        fontSize: '0.85rem',
                        color: 'white',
                        opacity: 0.8,
                      }}
                    >
                      {article.tag}
                    </Typography>
                  </Box>
                </Box>
              ))}
            </Box>
          </BigBox>
        </Box>

        {/* Badges */}
        <Box sx={{ flex: 1, minWidth: 300 }}>
          <BigBox title="Badges">
            <Box
              sx={{
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'center',
                gap: 4,
                flexWrap: 'wrap',
                paddingTop: 5,
              }}
            >
              {student.earnedBadges.map((badge: any, i: number) => (
                <Box key={i} sx={{ textAlign: 'center' }}>
                  <img
                    src="/public/interviewBadge.png"
                    alt={badge.label}
                    style={{
                      width: 100,
                      height: 100,
                      borderRadius: '50%',
                      objectFit: 'cover',
                      marginBottom: 8,
                    }}
                  />
                </Box>
              ))}
            </Box>
          </BigBox>
        </Box>
      </Box>
    </Layout>
  );
};

export default Dashboard;
