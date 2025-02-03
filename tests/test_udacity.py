#import pytest
import sys
import os 
sys.path.insert(0, "C:/Users/Joseph Mockler/Documents/GitHub/TeLEX")
import telex.synth
import pandas

#templogicdata =  'G[0,6] F[b? 1;6,  a? 4;6](x1 > 2)'

# Runs paper example 1 - these formulae were given
#templogicdata =  [
#     'G[0, 220046461440] ( ((angle > 0.2) | (angle < -0.2)) -> (speed < a? 15;25) )',
#    'G[0, 220046461440] ( ((angle > 0.2) | (angle < -0.2)) -> ( (speed < a? 15;25) & (speed > b? -25;-15) ) )',
#]

# Runs paper example 2 - my implementation to check if true
# Upon running - looks like it matches!
templogicdata = ['G[0, 220046461440] ( ((torque > 1.6)|(torque < -1.6)) -> speed < a? 15;25)']

# Runs paper example 3 - CANNOT reproduce, but by inspection of the data,
# it's not possible to reproduce their results. Maybe they used a different formula/test set?
templogicdata = ['G[0, 220046461440] ( (angle > 0.06) -> torque > b? -1.5;2)']

#@pytest.mark.parametrize("tlStr", templogicdata)
def test_stl(tlStr):
    print(tlStr)
    #try:
    (stlsyn, value, dur) = telex.synth.synthSTLParam(tlStr, "C:/Users/Joseph Mockler/Documents/GitHub/TeLEX/tests/udacityData")
    #except ValueError:
    #    (stlsyn, value, dur) = telex.synth.synthSTLParam(tlStr, "C:/Users/Joseph Mockler/Documents/GitHub/TeLEX/tests/udacityData", "nogradient")
    print(" Synthesized STL formula: {}\n Theta Optimal Value: {}\n Optimization time: {}\n".format(stlsyn, value, dur))
    (bres, qres) = telex.synth.verifySTL(stlsyn, "C:/Users/Joseph Mockler/Documents/GitHub/TeLEX/tests/udacityData")
    print(" Test result of synthesized STL on each trace: {}\n Robustness Metric Value: {}\n".format(bres, qres))
#    print(tlStr)
#    (stlsyn, value, dur) = telex.synth.synthSTLParam(tlStr, "traces")
#    print(stlsyn, value, dur)
#    (bres, qres) = telex.synth.verifySTL(stlsyn, "traces")
#    print(bres, qres)


def main():
    for templ in templogicdata:
        test_stl(templ)

if __name__ == "__main__":
    main()

