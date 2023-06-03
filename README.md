## Developer Guide

To reproduce the results summarized below:

```sh
make install
source venv/bin/activate
cp .env.sample .env    <--- Fill out credentials here!
python -m src.untappd
```

## Result Summary

Attempting to fetch all menu IDs from in the range 30458500 to 30458599 results in three distinct responses:

1. RecordNotFoundError for menu ids (aka does not exist)

    {00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,44,46,47,48,49,50,51,52,55,57,58,59,60,61,62,64,65,66,67,69,70,71,72,74,75,76,77,79,80,81,82,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99}

2. UnauthorizedError (aka - something exists, but credentials are wrong!)
	
    {30458538, 30458554, 30458556, 30458573, 30458584}

3. Then the 6 actual results for menu ids

    {30458543 ,30458545, 30458553, 30458563, 30458568, 30458578}
