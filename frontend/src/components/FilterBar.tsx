import { ALL_MATERIALS, MATERIAL_LABELS, type MaterialType } from "../types";

interface FilterBarProps {
  selected: MaterialType[];
  onChange: (materials: MaterialType[]) => void;
}

export default function FilterBar({ selected, onChange }: FilterBarProps) {
  function toggleMaterial(material: MaterialType) {
    if (selected.includes(material)) {
      onChange(selected.filter((m) => m !== material));
    } else {
      onChange([...selected, material]);
    }
  }

  return (
    <div className="filter-bar">
      <span className="filter-label">Filtrar por material:</span>
      <div className="filter-chips">
        {ALL_MATERIALS.map((material) => {
          const isActive = selected.includes(material);
          return (
            <button
              key={material}
              type="button"
              role="button"
              aria-pressed={isActive}
              className={`filter-chip ${isActive ? "filter-chip--active" : ""}`}
              onClick={() => toggleMaterial(material)}
            >
              {MATERIAL_LABELS[material]}
            </button>
          );
        })}
      </div>
    </div>
  );
}
