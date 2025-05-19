import { ApolloClient, InMemoryCache, createHttpLink, from } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';
import { onError } from '@apollo/client/link/error';

// Get CSRF token from cookie
function getCookie(name: string): string | null {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? decodeURIComponent(match[2]) : null;
}

// --- Handle Authentication Errors Globally ---
const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors) {
    for (let err of graphQLErrors) {
      if (err.message.includes("Authentication required")) {
        // Automatically redirect to login
        window.location.href = "/login";
      }
    }
  }

  if (networkError && 'statusCode' in networkError && networkError.statusCode === 401) {
    window.location.href = "/login";
  }
});

// --- Add CSRF Token to Each Request ---
const authLink = setContext((_, { headers }) => {
  const csrfToken = getCookie('csrftoken');

  return {
    headers: {
      ...headers,
      'X-CSRFToken': csrfToken ?? '',
    },
  };
});

// --- Define GraphQL Endpoint ---
const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql/',
  credentials: 'include', // Include JWT in cookies
});

// --- Combine Links ---
const client = new ApolloClient({
  link: from([errorLink, authLink, httpLink]),
  cache: new InMemoryCache(),
});

export default client;
