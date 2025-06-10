import { gql, useQuery } from '@apollo/client';

const GET_EVALUATIONS = gql`
    query {
        myEvaluations {
            id
            feedback
            createdAt
            studentName
            coachName
        }
    }
`;

function Evaluations() {
    const { loading: dataLoading, error: dataError, data } = useQuery(GET_EVALUATIONS, {
        fetchPolicy: 'network-only'
    })

    if (dataLoading) return <p>Loading...</p>;
    if (dataError) return <p>Error! {dataError.message}</p>;

    return (
        <div className="p-4">
            <h1 className="text-2xl font-semibold mb-4">Evaluations</h1>
            <div className="space-y-4">
                {data.myEvaluations.map((evaluation: any) => (
                    <div key={evaluation.id} className="border rounded-xl p-4 shadow">
                        <p><strong>Date:</strong> {new Date(evaluation.createdAt).toLocaleDateString()}</p>
                        <p><strong>Feedback:</strong> {evaluation.feedback}</p>
                        <p><strong>Student:</strong> {evaluation.studentName}</p>
                        <p><strong>Teacher:</strong> {evaluation.coachName}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
  
export default Evaluations;