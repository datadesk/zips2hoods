all: data/zips.geojson data/hoods.geojson data/zips2hoods.csv

data/zips.geojson:
	curl http://s3-us-west-2.amazonaws.com/boundaries.latimes.com/archive/1.0/boundary-set/zip-code-tabulation-areas-2012.geojson --output ./data/zips.geojson

data/hoods.geojson:
	curl http://s3-us-west-2.amazonaws.com/boundaries.latimes.com/archive/1.0/boundary-set/la-county-neighborhoods-v6.geojson --output ./data/hoods.geojson

data/zips2hoods.csv:
	pipenv run python src/join.py

clean:
	rm -f data/*.geojson
	rm -f data/*.csv

.PHONY: clean
