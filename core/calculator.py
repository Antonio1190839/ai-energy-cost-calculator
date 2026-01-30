BASE_ENERGY_PER_TOKEN_WH = 0.0000006  # 6e-7 Wh per token (literature-based estimate)

def estimate_energy_and_co2(
    tokens_input,
    tokens_output,
    model,
    reasoning,
    region
):
    total_tokens = tokens_input + tokens_output

    energy_wh = (
        total_tokens
        * BASE_ENERGY_PER_TOKEN_WH
        * model["complexity_factor"]
        * reasoning["factor"]
        * model["architecture_efficiency"]
    )

    energy_kwh = energy_wh / 1000
    co2_g = energy_kwh * region["co2_g_per_kwh"]

    return {
        "tokens_total": total_tokens,
        "energy_wh": round(energy_wh, 6),
        "energy_kwh": round(energy_kwh, 8),
        "co2_g": round(co2_g, 4)
    }
