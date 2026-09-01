import { useCallback, useEffect, useState } from "react";
import FilterBar from "../components/FilterBar";
import MapView from "../components/MapView";
import PointModal from "../components/PointModal";
import { api } from "../services/api";
import type { CollectionPoint, MaterialType } from "../types";

export default function MapPage() {
  const [points, setPoints] = useState<CollectionPoint[]>([]);
  const [selectedMaterials, setSelectedMaterials] = useState<MaterialType[]>([]);
  const [selectedPoint, setSelectedPoint] = useState<CollectionPoint | null>(null);
  const [error, setError] = useState<string | null>(null);

  const loadPoints = useCallback(async (materials: MaterialType[]) => {
    try {
      setError(null);
      const data = await api.getPoints(materials.length > 0 ? materials : undefined);
      setPoints(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao carregar pontos");
    }
  }, []);

  useEffect(() => {
    loadPoints(selectedMaterials);
  }, [selectedMaterials, loadPoints]);

  return (
    <div className="map-page">
      <FilterBar selected={selectedMaterials} onChange={setSelectedMaterials} />
      {error && <p className="error-message">{error}</p>}
      <MapView points={points} onSelectPoint={setSelectedPoint} />
      <PointModal point={selectedPoint} onClose={() => setSelectedPoint(null)} />
    </div>
  );
}
