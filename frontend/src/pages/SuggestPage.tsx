import { FormEvent, useState } from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api } from "../services/api";
import { ALL_MATERIALS, MATERIAL_LABELS, type MaterialType } from "../types";

export default function SuggestPage() {
  const { user, loading } = useAuth();
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [latitude, setLatitude] = useState("-23.601");
  const [longitude, setLongitude] = useState("-46.752");
  const [description, setDescription] = useState("");
  const [materials, setMaterials] = useState<MaterialType[]>([]);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  if (loading) {
    return <p>Carregando...</p>;
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  function toggleMaterial(material: MaterialType) {
    setMaterials((prev) =>
      prev.includes(material) ? prev.filter((m) => m !== material) : [...prev, material]
    );
  }

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (materials.length === 0) {
      setError("Selecione pelo menos um material");
      return;
    }
    setSubmitting(true);
    setError(null);
    try {
      await api.createSuggestion({
        name,
        address,
        latitude: parseFloat(latitude),
        longitude: parseFloat(longitude),
        material_types: materials,
        description: description || undefined,
      });
      setSuccess(true);
      setName("");
      setAddress("");
      setDescription("");
      setMaterials([]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao enviar sugestão");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="form-page">
      <h1>Sugerir Ponto de Coleta</h1>
      {success && (
        <p className="success-message">
          Sugestão enviada! Um administrador irá revisar em breve.
        </p>
      )}
      <form onSubmit={handleSubmit} className="form-card">
        {error && <p className="error-message">{error}</p>}
        <label htmlFor="suggest-name">Nome do ponto</label>
        <input
          id="suggest-name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          minLength={2}
        />
        <label htmlFor="suggest-address">Endereço</label>
        <input
          id="suggest-address"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          required
          minLength={5}
        />
        <label htmlFor="suggest-lat">Latitude</label>
        <input
          id="suggest-lat"
          value={latitude}
          onChange={(e) => setLatitude(e.target.value)}
          required
        />
        <label htmlFor="suggest-lng">Longitude</label>
        <input
          id="suggest-lng"
          value={longitude}
          onChange={(e) => setLongitude(e.target.value)}
          required
        />
        <label htmlFor="suggest-desc">Descrição (opcional)</label>
        <textarea
          id="suggest-desc"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          rows={3}
        />
        <fieldset>
          <legend>Materiais aceitos</legend>
          <div className="filter-chips">
            {ALL_MATERIALS.map((material) => (
              <button
                key={material}
                type="button"
                className={`filter-chip ${materials.includes(material) ? "filter-chip--active" : ""}`}
                onClick={() => toggleMaterial(material)}
              >
                {MATERIAL_LABELS[material]}
              </button>
            ))}
          </div>
        </fieldset>
        <button type="submit" disabled={submitting}>
          Enviar Sugestão
        </button>
      </form>
    </div>
  );
}
