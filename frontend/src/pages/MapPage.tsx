import { useEffect, useState } from "react";
import MapView from "../components/MapView";
import { api } from "../services/api";
import type { CollectionPoint } from "../types";

export default function MapPage() {
  const [points, setPoints] = useState<CollectionPoint[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .getPoints()
      .then(setPoints)
      .catch((err: Error) => setError(err.message));
  }, []);

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  return (
    <MapView
      points={points}
      onSelectPoint={(point) => console.log("selected", point.id)}
    />
  );
}
