import { ApolloClient, InMemoryCache, createHttpLink, from } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';
import { onError } from '@apollo/client/link/error';
import { config } from '../config';


function getCookie(name: string): string | null {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? decodeURIComponent(match[2]) : null;
}

const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors) {
    for (let err of graphQLErrors) {
      if (err.message.includes("Authentication required")) {
        window.location.href = "/login";
      }
    }
  }

  if (networkError && 'statusCode' in networkError && networkError.statusCode === 401) {
    window.location.href = "/login";
  }
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

const httpLink = createHttpLink({
  uri: config.apiUrl + '/graphql/',
  credentials: 'include', // Include JWT in cookies
});

const client = new ApolloClient({
  link: from([errorLink, authLink, httpLink]),
  cache: new InMemoryCache(),
});

export default client;
