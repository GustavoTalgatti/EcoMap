import { describe, expect, it, vi } from "vitest";
import { api } from "../api";

describe("api.getPoints", () => {
  it("calls /api/points with material query params", async () => {
    const mockFetch = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, name: "Ponto" }],
    });
    vi.stubGlobal("fetch", mockFetch);

    await api.getPoints(["plastic"]);

    expect(mockFetch).toHaveBeenCalledWith(
      "/api/points?material=plastic",
      expect.objectContaining({ headers: expect.any(Object) })
    );
  });
});
