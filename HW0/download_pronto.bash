mkdir pronto
cd pronto
mkdir data
cd data
curl https://s3.amazonaws.com/pronto-data/open_data_year_one.zip -O
unzip *.zip
head 2015_trip_data.csv
cp README.txt . ..
cd ..
