#!/bin/sh

uvicorn main:app --reload --host=0.0.0.0 --port=8000 --workers=4 