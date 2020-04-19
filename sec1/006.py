if __name__ == "__main__":
    str_006_X, str_006_Y = "paraparaparadise", "paragraph"
    X, Y = {str_006_X[i:i+2] for i in range(len(str_006_X)-1)}, {str_006_Y[i:i+2] for i in range(len(str_006_Y)-1)}
    XorY, XandY, XdifY, YdifX = X | Y, X & Y, X - Y, Y - X
    print("","和集合:",XorY,"\n","積集合:",XandY,"\n","差集合X-Y:",XdifY,"\n","差集合Y-X:",YdifX,"\n")
    print("","se in 積集合:","se" in XandY)