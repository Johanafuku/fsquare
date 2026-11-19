
import { useEffect, useState } from "react";
import "./App.css";

function App({ designId }) {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!designId) return;

    async function fetchMatches() {
      try {
        // Request the matching results from Django.
        const response = await fetch(
          `/selections/api/design/${designId}/`
        );

        if (!response.ok) {
          throw new Error("Unable to retrieve matching results.");
        }

        // Convert the JSON response into JavaScript data.
        const data = await response.json();

        setResults(data.results || []);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchMatches();
  }, [designId]);

  if (!designId) return <p>No design ID provided.</p>;
  if (loading) return <h2>Loading your matches...</h2>;
  if (error) return <p>{error}</p>;

  return (
    <div className="matching-page">
      <h1 className="matching-page-title">Matching Results</h1>

      {results.length === 0 ? (
        <p>No suppliers found for this design.</p>
      ) : (
        <div className="supplier-list">
          {results.map((result) => (
            <div className="supplier-card" key={result.id}>
              <h2>{result.supplier.name}</h2>

              <h3>{result.percentage}% Match</h3>

              <p>
                <strong>Sales contact:</strong>{" "}
                {result.supplier.contact_email}
              </p>

              <p>
                <strong>Fabrics:</strong>{" "}
                {result.supplier.fabric_types.join(", ")}
              </p>

              <p>
                <strong>Colours:</strong>{" "}
                {result.supplier.colors_available.join(", ")}
              </p>

              <p>
                <strong>Processing:</strong>{" "}
                {result.supplier.processing.join(", ")}
              </p>

              <p>
                <strong>Minimum metres:</strong>{" "}
                {result.supplier.min_meters}
              </p>

              <p>
                <strong>Minimum pieces:</strong>{" "}
                {result.supplier.number_of_pieces}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;



