def estimate_energy_and_co2(
    tokens_input,
    tokens_output,
    energy_per_1k_tokens_wh,
    co2_g_per_kwh
):
    total_tokens = tokens_input + tokens_output

    energy_wh = (total_tokens / 1000) * energy_per_1k_tokens_wh
    energy_kwh = energy_wh / 1000
    co2_g = energy_kwh * co2_g_per_kwh

    return {
        "tokens": total_tokens,
        "energy_wh": round(energy_wh, 4),
        "energy_kwh": round(energy_kwh, 6),
        "co2_g": round(co2_g, 4)
    }
