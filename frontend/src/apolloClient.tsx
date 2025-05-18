import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';

function getCookie(name: string): string | null {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? decodeURIComponent(match[2]) : null;
}

const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql/',
  credentials: 'include', // must include cookies on cross-origin requests
});

const authLink = setContext((_, { headers }) => {
  const csrfToken = getCookie('csrftoken');


  return {
    headers: {
      ...headers,
      'X-CSRFToken': csrfToken ?? '',
    },
  };
});

const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
});

export default client;
