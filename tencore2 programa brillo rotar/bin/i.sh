#!/bin/bash

# created by Ruben Barkow (@rubo77)
# modified by Rahul Pillai (@theGeekyLad)
# remodified to Toshiba encore 2 by Eduardo lopez (@genplew)

ROTATION="inverted"
COORDS="-1 0 1 0 -1 1 0 0 1"

# Rota la pantalla
#PANTALLA_ID="DSI-1"
xrandr --output "$1" --rotate "$ROTATION"

# Rota el tactil
#TACTIL_ID="04F30732:00 04F3:0410"
xinput set-prop "$2" --type=float "Coordinate Transformation Matrix" $COORDS