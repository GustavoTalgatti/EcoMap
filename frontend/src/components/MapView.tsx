import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import L from "leaflet";
import type { CollectionPoint } from "../types";
import { MATERIAL_LABELS } from "../types";

const defaultIcon = L.icon({
  iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  iconRetinaUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
  shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

L.Marker.prototype.options.icon = defaultIcon;

const CENTER: [number, number] = [-23.601, -46.752];
const DEFAULT_ZOOM = 12;

interface MapViewProps {
  points: CollectionPoint[];
  onSelectPoint: (point: CollectionPoint) => void;
}

export default function MapView({ points, onSelectPoint }: MapViewProps) {
  return (
    <div className="map-view">
      <MapContainer center={CENTER} zoom={DEFAULT_ZOOM} className="map-container">
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {points.map((point) => (
          <Marker
            key={point.id}
            position={[point.latitude, point.longitude]}
            eventHandlers={{ click: () => onSelectPoint(point) }}
          >
            <Popup>
              <strong>{point.name}</strong>
              <br />
              {point.material_types.map((m) => MATERIAL_LABELS[m]).join(", ")}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}
