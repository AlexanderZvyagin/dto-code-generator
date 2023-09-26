rm -rf output
cgdto --schema=schema.py --output=output --run-tests --languages=cpp,python,typescript
(cp -a doc output/doc; cd doc; make html)
