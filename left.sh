#!/bin/sh

# Este permite rotar la pantalla y el tactil

ROTATION="left"
COORDS="0 -1 1 1 0 0 0 0 1"

# Rota la pantalla
PANTALLA_ID="DSI-1"
xrandr --output "$PANTALLA_ID" --rotate "$ROTATION"

# Rota el tactil
TACTIL_ID="04F30732:00 04F3:0410"
xinput set-prop "$TACTIL_ID" --type=float "Coordinate Transformation Matrix" $COORDS
