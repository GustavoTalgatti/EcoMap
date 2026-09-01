import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import MapView from "../MapView";
import type { CollectionPoint } from "../../types";

vi.mock("react-leaflet", () => ({
  MapContainer: ({ children }: { children: React.ReactNode }) => (
    <div data-testid="map-container">{children}</div>
  ),
  TileLayer: () => null,
  Marker: ({ eventHandlers }: { eventHandlers?: { click?: () => void } }) => (
    <button data-testid="marker" onClick={eventHandlers?.click}>
      marker
    </button>
  ),
  Popup: ({ children }: { children: React.ReactNode }) => <div>{children}</div>,
}));

const mockPoint: CollectionPoint = {
  id: 1,
  name: "Ponto Teste",
  latitude: -23.601,
  longitude: -46.752,
  address: "Rua Teste, 1",
  description: null,
  material_types: ["plastic"],
  opening_hours: "Seg-Sex 8h-18h",
  status: "active",
  created_by: null,
  created_at: "2026-08-31T00:00:00",
};

describe("MapView", () => {
  it("renders map container and markers for each point", () => {
    render(<MapView points={[mockPoint]} onSelectPoint={() => {}} />);
    expect(screen.getByTestId("map-container")).toBeInTheDocument();
    expect(screen.getAllByTestId("marker")).toHaveLength(1);
  });
});
