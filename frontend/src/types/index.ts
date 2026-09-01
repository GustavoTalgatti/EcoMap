export type MaterialType =
  | "plastic"
  | "glass"
  | "metal"
  | "paper"
  | "electronics"
  | "oil"
  | "organic";

export type UserRole = "user" | "admin";

export type SuggestionStatus = "pending" | "approved" | "rejected";

export interface CollectionPoint {
  id: number;
  name: string;
  latitude: number;
  longitude: number;
  address: string;
  description: string | null;
  material_types: MaterialType[];
  opening_hours: string | null;
  status: "active" | "inactive";
  created_by: number | null;
  created_at: string;
}

export interface User {
  id: number;
  email: string;
  name: string;
  role: UserRole;
  created_at: string;
}

export interface Suggestion {
  id: number;
  user_id: number;
  name: string;
  latitude: number;
  longitude: number;
  address: string;
  material_types: MaterialType[];
  description: string | null;
  status: SuggestionStatus;
  reviewed_by: number | null;
  reviewed_at: string | null;
  created_at: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export const MATERIAL_LABELS: Record<MaterialType, string> = {
  plastic: "Plástico",
  glass: "Vidro",
  metal: "Metal",
  paper: "Papel",
  electronics: "Eletrônicos",
  oil: "Óleo",
  organic: "Orgânico",
};

export const ALL_MATERIALS: MaterialType[] = [
  "plastic",
  "glass",
  "metal",
  "paper",
  "electronics",
  "oil",
  "organic",
];
