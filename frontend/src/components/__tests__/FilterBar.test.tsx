import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import FilterBar from "../FilterBar";

describe("FilterBar", () => {
  it("toggles material chip selection", async () => {
    const user = userEvent.setup();
    const onChange = vi.fn();

    render(<FilterBar selected={[]} onChange={onChange} />);

    const plasticChip = screen.getByRole("button", { name: "Plástico" });
    await user.click(plasticChip);

    expect(onChange).toHaveBeenCalledWith(["plastic"]);
  });

  it("deselects an already selected material", async () => {
    const user = userEvent.setup();
    const onChange = vi.fn();

    render(<FilterBar selected={["plastic"]} onChange={onChange} />);

    const plasticChip = screen.getByRole("button", { name: "Plástico" });
    await user.click(plasticChip);

    expect(onChange).toHaveBeenCalledWith([]);
  });
});
