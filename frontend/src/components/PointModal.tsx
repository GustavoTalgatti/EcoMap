import { MATERIAL_LABELS, type CollectionPoint } from "../types";

interface PointModalProps {
  point: CollectionPoint | null;
  onClose: () => void;
}

export default function PointModal({ point, onClose }: PointModalProps) {
  if (!point) {
    return null;
  }

  return (
    <div className="modal-overlay" onClick={onClose} role="presentation">
      <div
        className="modal-content"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-labelledby="point-modal-title"
      >
        <button type="button" className="modal-close" onClick={onClose} aria-label="Fechar">
          ×
        </button>
        <h2 id="point-modal-title">{point.name}</h2>
        <p>
          <strong>Endereço:</strong> {point.address}
        </p>
        <p>
          <strong>Materiais:</strong>{" "}
          {point.material_types.map((m) => MATERIAL_LABELS[m]).join(", ")}
        </p>
        {point.opening_hours && (
          <p>
            <strong>Horário:</strong> {point.opening_hours}
          </p>
        )}
        {point.description && (
          <p>
            <strong>Descrição:</strong> {point.description}
          </p>
        )}
      </div>
    </div>
  );
}
