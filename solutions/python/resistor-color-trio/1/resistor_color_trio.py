COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
def label(colors):
    digit1 = COLORS.index(colors[0])
    digit2 = COLORS.index(colors[1])
    exp = COLORS.index(colors[2])

    result = (digit1 * 10 + digit2) * (10 ** exp)

    scale = [(10**9, " gigaohms"), (10**6, " megaohms"), (10**3," kiloohms"), (1, " ohms")]

    for factor, prefix in scale:
        if result >= factor:
            return str(result // factor) + prefix
    return "0 ohms"
   
    
        
