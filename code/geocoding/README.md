# ArcGIS Geocoder

The `geocoder.py` script is designed to take an input CSV and generate a new CSV annotated with latitude, longitude and other metadata from the Stanford ArcGIS geocoding API.

To use it,  you should ensure your input file has the following columns:

* `Address` - the street address
* `City` - the Jurisdiction (e.g. `Alameda`)
* `Region` - aka the state postal code (e.g. `CA`)

Once you've updated your source data as above, you can attempt to geocode your original CSV by executing it with the path to the source data file.

## Usage

> The below assumes you're doing this work using our standard Datakit project workflow. We use a file containing a small set of housing data for Alameda for demonstration purposes.

Navigate to your Datakit project:

```
# Use the appropriate path for your machine and project
cd ~/code/my-project

# Install requests
pipenv install requests

# Activate the virtual environment
pipenv shell
```

Assuming you've saved `geocoder.py` in `scripts/`, you can run it as below:

```bash
cd scripts/

# Call the script with the path to the data file.
# Here we use an example data file that you can find in this code folder
python geocoder.py ~/code/my-project/data/alameda.csv
```

The script should create a new file in the same directory as the source data.

The new file will have a `_geocoded.csv` suffix. So in the above example, you should have a new file called `~/code/my-project/data/alameda_geocoded.csv`.
