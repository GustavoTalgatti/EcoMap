const request = require("supertest");
const app = require("../src/app");

describe("GET /pontos", () => {
  it("retorna a pagina de listagem de pontos", async () => {
    const response = await request(app).get("/pontos");

    expect(response.status).toBe(200);
    expect(response.headers["content-type"]).toMatch(/html/);
    expect(response.text).toContain("Pontos de Coleta");
    expect(response.text).toContain("/api/pontos");
  });
});
