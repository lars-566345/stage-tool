import React from 'react';
import { Box, Typography, Input } from '@mui/joy';
import Layout from '../_components/Layout';
import KnowledgebaseBox from '../_components/KnowledgebaseBox';
import boxData from '../_data/knowledgebaseData.json';

interface KnowledgebaseItem {
  tag: string;
  title: string;
  description: string;
}

const Knowledgebase: React.FC = () => {
  return (
    <Layout>
      <Box sx={{ width: '100%' }}>
        <Typography
          level="h2"
          sx={{
            display: 'flex',
            justifyContent: 'center',
            fontWeight: 'bold',
            mb: { xs: 5, lg: 7 },
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
          {(boxData as KnowledgebaseItem[]).map((box, index) => (
            <KnowledgebaseBox
              key={index}
              tag={box.tag}
              title={box.title}
              description={box.description}
            />
          ))}
        </Box>
      </Box>
    </Layout>
  );
};

export default Knowledgebase;
