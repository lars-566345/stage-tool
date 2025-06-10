import { gql, useQuery } from '@apollo/client';
import { useAuth } from '../components/AuthContext';

const GET_STUDENT_DETAILS = gql`
  query {
    studentProfile(id: 6) {
      firstName
      lastName
      evaluations {
        id
        createdAt
      }
      id
      earnedBadges {
        id
        label
      }
      favoriteArticles {
        id
        title
      }
      coaches {
        firstName
        lastName
      }
    }
  }
`;

function Evaluations() {
    const { user, loading: authLoading } = useAuth();

    const { loading: dataLoading, error: dataError, data } = useQuery(GET_STUDENT_DETAILS, {
        fetchPolicy: 'network-only',
        variables: { id: user?.id },
        skip: authLoading || !user?.id,
    })

    if (dataLoading) return <p>Loading...</p>;
    if (dataError) return <p>Error! {dataError.message}</p>;

    const student = data.studentProfile;

    return (
    <div>
      <h1>
        Welcome, {student.firstName} {student.lastName}
      </h1>

      <section>
        <h2>Evaluations</h2>
        <ul>
          {student.evaluations.map((evaluation: any) => (
            <li key={evaluation.id}>Created At: {new Date(evaluation.createdAt).toLocaleDateString()}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Earned Badges</h2>
        <ul>
          {student.earnedBadges.map((badge: any) => (
            <li key={badge.id}>{badge.label}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Favorite Articles</h2>
        <ul>
          {student.favoriteArticles.map((article: any) => (
            <li key={article.id}>{article.title}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Coaches</h2>
        <ul>
          {student.coaches.map((coach: any, index: number) => (
            <li key={index}>
              {coach.firstName} {coach.lastName}
            </li>
          ))}
        </ul>
      </section>
    </div>
    );
}
  
export default Evaluations;