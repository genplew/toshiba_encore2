#!/bin/sh

# Este permite rotar la pantalla y el tactil

ORIENTACION=$1
if [ -z "$ORIENTACION" ]; then
  >&2 echo
  >&2 echo "   COLOCA UNA ORIENTACION AL FINAL:"
  >&2 echo
  >&2 echo "   normal | inverted | left | right"
  >&2 echo
  exit 3
fi

if [ "$ORIENTACION" = "left" ]; then
  ROTATION="left"
  COORDS="0 -1 1 1 0 0 0 0 1"
elif [ "$ORIENTACION" = "right" ]; then
  ROTATION="right"
  COORDS="0 1 0 -1 0 1 0 0 1"
elif [ "$ORIENTACION" = "inverted" ]; then
  ROTATION="inverted"
  COORDS="-1 0 1 0 -1 1 0 0 1"
elif [ "$ORIENTACION" = "normal" ]; then
  ROTATION="normal"
  COORDS="0 0 0 0 0 0 0 0 0"
fi

# Rota la pantalla
PANTALLA_ID="DSI-1"
xrandr --output "$PANTALLA_ID" --rotate "$ROTATION"

# Rota el tactil
TACTIL_ID="04F30732:00 04F3:0410"
xinput set-prop "$TACTIL_ID" --type=float "Coordinate Transformation Matrix" $COORDS
