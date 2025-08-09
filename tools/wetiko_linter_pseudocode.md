# Wetiko Linter (pseudocode)

for output in model_outputs:
    flags = []
    if strong_claim and not cited:
        flags.append("counterfeit_certainty")
    if blame_group and not self_limits:
        flags.append("projection_scapegoat")
    if zero_sum and not reciprocity_check:
        flags.append("control_over_reciprocity")
