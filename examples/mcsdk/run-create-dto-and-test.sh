rm -rf output
#cgdto --schema=schema.py --output=output --languages=cpp,python,typescript
cgdto --schema=schema.py --output=output --run-tests --languages=cpp,python,typescript
