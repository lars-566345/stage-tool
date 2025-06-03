import React from 'react';
import { Card, Typography, Box, IconButton } from '@mui/joy';
import StarIcon from '@mui/icons-material/Star';

const KnowledgebaseBox = ({ tag, title, description, index, role }) => {

  const handleReadMore = () => {
  const basePath = role?.startsWith('teacher') ? '/teacher/knowledgebase/' : '/knowledgebase/';
  const from = role === 'teacher-dashboard' ? 'teacher/dashboard' : 'teacher/knowledgebase';
  window.history.pushState({}, '', `${basePath}${index}?from=${from}`);
  window.dispatchEvent(new PopStateEvent('popstate'));
};

  return (
    <Card
      sx={{
        borderRadius: 'lg',
        padding: 2,
        minWidth: 250,
        flex: 1,
        maxWidth: 300,
        position: 'relative',
        backgroundColor: '#008387',
        color: 'white',
        boxShadow: 'md',
      }}
    >
      <Box
        sx={{
          position: 'absolute',
          top: 12,
          left: 16,
          bgcolor: 'white',
          color: '#008387',
          px: 1,
          py: 0.5,
          borderRadius: 'md',
          fontSize: 'xs',
          fontWeight: 'bold',
        }}
      >
        {tag}
      </Box>

      <IconButton
        variant="plain"
        sx={{ position: 'absolute', top: 8, right: 8, color: 'white' }}
      >
        <StarIcon />
      </IconButton>

      <Box sx={{ mt: 4 }}>
        <Typography level="title-lg" sx={{ color: 'white' }}>
          {title}
        </Typography>
        <Typography level="body-sm" sx={{ mt: 1, color: 'white' }}>
          {description}
        </Typography>
        <Typography
          level="body-xs"
          onClick={handleReadMore}
          sx={{
            mt: 2,
            textAlign: 'right',
            textDecoration: 'underline',
            color: 'white',
            cursor: 'pointer',
          }}
        >
          Read more
        </Typography>
      </Box>
    </Card>
  );
};

export default KnowledgebaseBox;
