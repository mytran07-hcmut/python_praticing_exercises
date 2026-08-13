COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
def resistor_label(colors):
    if len(colors) <= 4 and len(colors) > 1:
        digit1 = COLORS.index(colors[0])
        digit2 = COLORS.index(colors[1])
        exp = COLORS.index(colors[2])
        result = (digit1 * 10 + digit2) * (10 ** exp)
    elif len(colors) == 1:
        return "0 ohms"
    else:
        digit1 = COLORS.index(colors[0])
        digit2 = COLORS.index(colors[1])
        digit3 = COLORS.index(colors[2])
        exp = COLORS.index(colors[3])
        result = (digit1 * 100 + digit2 * 10 + digit3) * (10 ** exp)

    scale = [(10**9, " gigaohms"), (10**6, " megaohms"), (10**3," kiloohms"), (1, " ohms")]
    tolerance = ""
    match colors[-1]:
        case "grey":
           tolerance = " \u00b10.05%"
        case "violet":
           tolerance = " \u00b10.1%"
        case "blue":
           tolerance = " \u00b10.25%"
        case "green":
           tolerance = " \u00b10.5%"
        case "brown":
           tolerance = " \u00b11%"
        case "red":
           tolerance = " \u00b12%"
        case "gold":
           tolerance = " \u00b15%"
        case "silver":
           tolerance = " \u00b110%"

    for factor, prefix in scale:
        if result >= factor:
            final = result/factor
            if final.is_integer():
                return str(int(final)) + prefix + tolerance
            return str(result / factor) + prefix + tolerance
    return "0 ohms"
    
