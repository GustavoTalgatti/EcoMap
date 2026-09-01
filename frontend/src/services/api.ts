import type {
  AuthResponse,
  CollectionPoint,
  MaterialType,
  Suggestion,
  User,
} from "../types";

const TOKEN_KEY = "ecomap_token";

function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY);
}

function authHeaders(): HeadersInit {
  const token = getToken();
  const headers: HeadersInit = { "Content-Type": "application/json" };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }
  return headers;
}

async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const body = await response.json().catch(() => ({ detail: "Erro desconhecido" }));
    throw new Error(body.detail || "Erro na requisição");
  }
  return response.json();
}

export const api = {
  setToken(token: string | null) {
    if (token) {
      localStorage.setItem(TOKEN_KEY, token);
    } else {
      localStorage.removeItem(TOKEN_KEY);
    }
  },

  async getPoints(materials?: MaterialType[]): Promise<CollectionPoint[]> {
    const params = new URLSearchParams();
    materials?.forEach((m) => params.append("material", m));
    const query = params.toString();
    const url = query ? `/api/points?${query}` : "/api/points";
    const response = await fetch(url, { headers: authHeaders() });
    return handleResponse<CollectionPoint[]>(response);
  },

  async getPoint(id: number): Promise<CollectionPoint> {
    const response = await fetch(`/api/points/${id}`, { headers: authHeaders() });
    return handleResponse<CollectionPoint>(response);
  },

  async register(email: string, password: string, name: string): Promise<AuthResponse> {
    const response = await fetch("/api/auth/register", {
      method: "POST",
      headers: authHeaders(),
      body: JSON.stringify({ email, password, name }),
    });
    return handleResponse<AuthResponse>(response);
  },

  async login(email: string, password: string): Promise<AuthResponse> {
    const response = await fetch("/api/auth/login", {
      method: "POST",
      headers: authHeaders(),
      body: JSON.stringify({ email, password }),
    });
    return handleResponse<AuthResponse>(response);
  },

  async getMe(): Promise<User> {
    const response = await fetch("/api/auth/me", { headers: authHeaders() });
    return handleResponse<User>(response);
  },

  async createSuggestion(data: {
    name: string;
    latitude: number;
    longitude: number;
    address: string;
    material_types: MaterialType[];
    description?: string;
  }): Promise<Suggestion> {
    const response = await fetch("/api/suggestions", {
      method: "POST",
      headers: authHeaders(),
      body: JSON.stringify(data),
    });
    return handleResponse<Suggestion>(response);
  },
};
