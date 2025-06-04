import React from 'react';
import { Box, Typography, Button } from '@mui/joy';
import SidebarTeacher from '../Components/SidebarTeacher';
import boxData from '../data/knowledgebaseData.json';

interface Article {
  tag: string;
  title: string;
  description: string;
}

interface KnowledgebaseDetailTeacherProps {
  id: number;
}

const KnowledgebaseDetailTeacher: React.FC<KnowledgebaseDetailTeacherProps> = ({ id }) => {
  const articles = boxData as Article[];
  const article = articles[id];

  const searchParams = new URLSearchParams(window.location.search);
  const from = searchParams.get('from') || 'teacher/knowledgebase';

  const goBack = () => {
    if (from === 'teacher/dashboard') {
      window.history.pushState({}, '', '/teacher/dashboard');
    } else {
      window.history.pushState({}, '', '/teacher/knowledgebase');
    }
    window.dispatchEvent(new PopStateEvent('popstate'));
  };

  if (!article) return <div>Article not found.</div>;

  return (
    <Box sx={{ display: 'flex' }}>
      <SidebarTeacher />

      <Box sx={{ flex: 1, p: 4, backgroundColor: 'white', color: 'black' }}>
        <Typography
          sx={{
            fontSize: { xs: '24px', md: '32px' },
            fontWeight: 'bold',
            textAlign: 'center',
            mb: 4,
          }}
        >
          {article.title}
        </Typography>

        <Typography sx={{ fontSize: '1rem', lineHeight: 1.8, mb: 4 }}>
          {article.description}
        </Typography>
        <Button
          onClick={goBack}
          sx={{
            backgroundColor: '#00838f',
            color: 'white',
            '&:hover': {
              backgroundColor: '#006974',
            },
          }}
        >
          ← Back to overview
        </Button>
      </Box>
    </Box>
  );
};

export default KnowledgebaseDetailTeacher;
