import React from 'react';
import Layout from '../_components/Layout';
import BigBox from '../_components/BigBox';
import SmallBox from '../_components/SmallBox';
import { Box, Typography } from '@mui/joy';
import userData from '../_data/users.json';

interface Timeline {
  title: string;
  subtitle: string;
}

interface SemesterCoach {
  name: string;
  image: string;
}

interface Badge {
  label: string;
  image: string;
}

interface UserData {
  name: string;
  evaluationDates: string[];
  timeline: Timeline;
  semesterCoach: SemesterCoach;
  pinnedPosts: string[];
  badges: Badge[];
}

const Dashboard: React.FC = () => {
  const {
    name,
    evaluationDates,
    timeline,
    semesterCoach,
    pinnedPosts,
    badges,
  } = userData as UserData;

  return (
    <Layout>
      <Box sx={{ textAlign: 'center', mb: 5 }}>
        <Typography
          sx={{
            fontSize: { xs: '24px', md: '32px' },
            fontWeight: 'bold',
            color: 'black',
          }}
        >
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
            {pinnedPosts.map((post, i) => (
              <Typography key={i} sx={{ textAlign: 'center', color: 'white' }}>
                {post}
              </Typography>
            ))}
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
                  {/* Optional: Uncomment if badge label is needed */}
                  {/* <Typography sx={{ color: 'white' }}>{badge.label}</Typography> */}
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
