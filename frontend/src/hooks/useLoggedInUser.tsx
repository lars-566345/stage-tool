import { useQuery, gql } from '@apollo/client';

const GET_ME = gql`
  query {
    me {
      id
      first_name
      last_name
    }
  }
`;

export const useLoggedInUser = () => {
  const { data, loading, error } = useQuery(GET_ME);
  return { user: data?.me, loading, error };
};

