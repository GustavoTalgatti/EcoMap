import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { MemoryRouter } from "react-router-dom";
import { describe, expect, it, vi } from "vitest";
import LoginPage from "../LoginPage";

const mockLogin = vi.fn();

vi.mock("../../context/AuthContext", () => ({
  useAuth: () => ({ login: mockLogin, user: null, loading: false }),
}));

describe("LoginPage", () => {
  it("submits email and password", async () => {
    const user = userEvent.setup();
    mockLogin.mockResolvedValue(undefined);

    render(
      <MemoryRouter>
        <LoginPage />
      </MemoryRouter>
    );

    await user.type(screen.getByLabelText("Email"), "user@ecomap.dev");
    await user.type(screen.getByLabelText("Senha"), "user123");
    await user.click(screen.getByRole("button", { name: "Entrar" }));

    expect(mockLogin).toHaveBeenCalledWith("user@ecomap.dev", "user123");
  });
});
