def value(colors):
    result = ""
    for i in range (len(colors)):
        if i > 1:
                return int(result)
        match colors[i]:
              case "black":
                result += "0"
              case "brown":
                result += "1"
              case "red": 
                result += "2"
              case "orange":
                result += "3"
              case "yellow":
                result += "4"
              case "green":
                result += "5"
              case "blue":
                result += "6"
              case "violet":
                result += "7"
              case "grey":
                result += "8"
              case "white":
                result += "9"
    return int(result)
