import React from 'react';
import { Box, Typography, Input } from '@mui/joy';
import SidebarTeacher from '../Components/SidebarTeacher';
import KnowledgebaseBox from '../Components/KnowledgebaseBox';
import boxData from '../data/knowledgebaseData.json';

interface KnowledgebaseItem {
  tag: string;
  title: string;
  description: string;
}

const KnowledgebaseTeacher: React.FC = () => {
  const data: KnowledgebaseItem[] = boxData;

  return (
    <Box sx={{ display: 'flex' }}>
      <SidebarTeacher />

      <Box sx={{ flex: 1, p: 4, backgroundColor: 'white' }}>
        <Typography
          level="h2"
          sx={{
            display: 'flex',
            justifyContent: 'center',
            fontWeight: 'bold',
            mb: { xs: 5, lg: 7 },
            color: 'black',
          }}
        >
          Knowledgebase
        </Typography>

        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            mb: { xs: 5, lg: 6 },
          }}
        >
          <Input
            placeholder="Zoeken..."
            sx={{
              backgroundColor: '#f5f5f5',
              borderRadius: 'md',
              width: '100%',
              maxWidth: 400,
            }}
          />
        </Box>

        <Box
          sx={{
            display: 'flex',
            flexWrap: 'wrap',
            gap: 2,
            justifyContent: 'flex-start',
          }}
        >
          {data.map((box, index) => (
            <KnowledgebaseBox
              key={index}
              index={index}
              tag={box.tag}
              title={box.title}
              description={box.description}
              role="teacher"
            />
          ))}
        </Box>
      </Box>
    </Box>
  );
};

export default KnowledgebaseTeacher;
