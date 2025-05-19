import { gql, useQuery } from '@apollo/client';

const GET_EVALUATIONS = gql`
    query  {
        myEvaluations {
            id
            feedback
            date
            student {
                id
                firstName
                lastName
            }
            teacher {
                id
                firstName
                lastName
            }
            phase {
                id
                content
            }
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
                        <p><strong>Date:</strong> {new Date(evaluation.date).toLocaleDateString()}</p>
                        <p><strong>Feedback:</strong> {evaluation.feedback}</p>
                        <p><strong>Student:</strong> {evaluation.student.firstName} {evaluation.student.lastName}</p>
                        <p><strong>Teacher:</strong> {evaluation.teacher.firstName} {evaluation.teacher.lastName}</p>
                        <p><strong>Phase:</strong> {evaluation.phase.content}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
  
export default Evaluations;