import React from 'react';
import { Box, Typography, Input } from '@mui/joy';
import Layout from '../_components/Layout';
import KnowledgebaseBox from '../_components/KnowledgebaseBox';
import { gql } from '@apollo/client';
import { useQuery } from '@apollo/client';
import { useAuth } from '../components/AuthContext';

const GET_ARTICLES = gql`
  query {
    articles {
      id
      tag
      title
      content
    }
  }
`;

const Knowledgebase: React.FC = () => {
  const { user, loading: authLoading } = useAuth();
  const { loading: dataLoading, error: dataError, data } = useQuery(GET_ARTICLES, {
      fetchPolicy: 'network-only',
      skip: authLoading || !user?.id,
  })

  if (dataLoading) return <p>Loading...</p>;
  if (dataError) return <p>Error! {dataError.message}</p>;

  const articles = data.articles;

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
          {articles.map((article: any) => (
            <KnowledgebaseBox
              key={article.id}
              tag={article.tag}
              title={article.title}
              description={article.content}
              index={article.id}
            />
          ))}
        </Box>
      </Box>
    </Layout>
  );
};

export default Knowledgebase;
