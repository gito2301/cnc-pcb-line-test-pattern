mil = 0.0254

widthss = [round(6*mil,4), round(8*mil,4), round(10*mil,4), round(12*mil,4), round(18*mil,4), round(24*mil,4), round(30*mil,4), round(40*mil,4)]
spcs = [round(i*mil,4) for i in [6, 9, 12, 18, 24]]
x = 125
for lw in widthss:
    for i in range(5):
            print('  (segment (start {x} 90) (end {x} 100) (width {lw}) (layer "F.Cu") (net 0) (tstamp 163a15f7-da77-43aa-a08c-33dd9ba5d630))'.format(x=x, lw=lw))
            x = round(x+lw+spcs[i],4)
