import React from 'react';
import { Box, Typography, Button } from '@mui/joy';
import SidebarStudent from '../Components/SidebarStudent';
import boxData from '../data/knowledgebaseData.json';

interface Article {
  tag: string;
  title: string;
  description: string;
}

const KnowledgebaseDetail: React.FC = () => {
  const pathParts = window.location.pathname.split('/');
  const articleIndex = parseInt(pathParts[pathParts.length - 1], 10);

  // Type assertion that boxData is an array of Article objects
  const articles = boxData as Article[];
  const article = articles[articleIndex];

  const searchParams = new URLSearchParams(window.location.search);
  const from = searchParams.get('from') || 'knowledgebase';

  const goBack = () => {
    if (from === 'dashboard') {
      window.location.href = '/dashboard';
    } else {
      window.location.href = '/knowledgebase';
    }
  };

  if (!article) {
    return (
      <Box sx={{ display: 'flex', height: '100vh' }}>
        <SidebarStudent />
        <Box sx={{ flex: 1, p: 4 }}>
          <Typography level="h2" sx={{ textAlign: 'center', fontWeight: 'bold', color: 'black' }}>
            Article Not Found
          </Typography>
        </Box>
      </Box>
    );
  }

  return (
    <Box sx={{ display: 'flex', height: '100vh' }}>
      <SidebarStudent />
      <Box sx={{ flex: 1, p: 4 }}>
        <Box sx={{ textAlign: 'center', mb: { xs: 5, lg: 7 } }}>
          <Typography level="h2" sx={{ fontWeight: 'bold', color: 'black' }}>
            {article.title}
          </Typography>
        </Box>
        <Box sx={{ mx: { xs: 2, sm: 10, md: 20 }, color: 'black' }}>
          <Typography level="body-md" sx={{ mb: 4 }}>
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
    </Box>
  );
};

export default KnowledgebaseDetail;
