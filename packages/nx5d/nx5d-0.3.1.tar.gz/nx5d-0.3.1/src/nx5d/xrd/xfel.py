#!/usr/bin/python3

'''
Experiment geometry defintion dictionary as needed by `LazyQMap`.
Strongly influenced by typical `xrayutilities` API.
'''
experimentTemplate = {
    "goniometerAxes": ('y-', 'z+', 'x+'),
    
    "detectorTARAxes": ('x+', None, None),

    # These were correct for the AGIPD1M detector at one point in time.
    # Might change over time, so you might need to adjust them.
    "imageAxes": ("x+", "y-"),
    "imageSize": "@/detector_size",
    "imageCenter": "@/detector_centre",

    # same unit as imageChannelSize
    "imageDistance": "@/sdd",

    # same unit as imageDistance (mm)    
    "imageChannelSize": ("@/pixel_size", "@/pixel_size"),

    "imageSize": "@/detector_size",

    # This could also be used instead of 'imageChannelSize' below.
    # It's the same physical quantity, but in degrees/channel
    # instead of relative length.
    #"imageChannelSpan": None,
    
    "sampleFaceUp": 'z+',
    "beamDirection": (0, 1, 0),
    
    "sampleNormal": (0, 0, 1),
    
    "beamEnergy": "@/photon_energy",

    "goniometerAngles": {
        'omega': '@/omega',
        'chi': '@/chi',
        'phi': '@/phi',
    },

    "detectorTARAngles": {
        '2theta': '@/twotheta',
    },
}
