import React from 'react';
import Layout from '../Components/Layout';
import BigBox from '../Components/BigBox';
import SmallBox from '../Components/SmallBox';
import { Box, Typography } from '@mui/joy';
import userData from '../data/users.json';
import boxData from '../data/knowledgebaseData.json';

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

interface KnowledgeBaseItem {
  title: string;
  tag: string;
}

const Dashboard: React.FC = () => {
  const {
    name,
    evaluationDates,
    timeline,
    semesterCoach,
    badges
  } = userData as UserData;

  return (
    <Layout>
      <Box sx={{ textAlign: 'center', mb: 5 }}>
        <Typography sx={{ fontSize: { xs: '24px', md: '32px' }, fontWeight: 'bold', color: 'black' }}>
          {name}
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
              {evaluationDates.map((date, i) => (
                <React.Fragment key={i}>
                  <Typography
                    sx={{
                      color: 'white',
                      textAlign: 'center',
                      fontSize: '1.2rem',
                      fontWeight: 'medium',
                    }}
                  >
                    {date}
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
                src={semesterCoach.image}
                alt={semesterCoach.name}
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
                {semesterCoach.name}
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
              {(boxData as KnowledgeBaseItem[]).map((box, index) => (
                <Box
                  key={index}
                  onClick={() => (window.location.href = `/knowledgebase/${index}?from=dashboard`)}
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
                    src="/img/knowledgebasePicture.png"
                    alt={box.title}
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
                      {box.title}
                    </Typography>
                    <Typography
                      sx={{
                        fontSize: '0.85rem',
                        color: 'white',
                        opacity: 0.8,
                      }}
                    >
                      {box.tag}
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
              {badges.map((badge, i) => (
                <Box key={i} sx={{ textAlign: 'center' }}>
                  <img
                    src={badge.image}
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
