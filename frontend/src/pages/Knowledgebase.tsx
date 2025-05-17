import { gql, useQuery } from '@apollo/client';

const GET_ARTICLES = gql`
    query {
        articles {
            id
            title
            content
        }
    }
`;

function Knowledgebase() {
    const { loading, error, data } = useQuery(GET_ARTICLES, {
        fetchPolicy: 'network-only'
    })

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error! {error.message}</p>;

    return (
        <>
            <h1>Knowledgebase</h1>
            {data.articles.map((article: any) => (
                <div key={article.id}>
                    <h3>{article.title}</h3>
                    <p>{article.content}</p>
                </div>
            ))}
        </>
    );
};
  
export default Knowledgebase;