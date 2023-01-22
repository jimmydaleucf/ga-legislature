# State Legislatures by Party Composition

In this project, I wanted to represent how each state's legislature was composed by party. To accomplish this, I needed to build a python machine to fetch, aggregate, and shape the data from several disparate APIs into a single JSON file. I then built a web page using svelte that is powered by this single JSON file/feed.

## Data Processing (Python)

### Summary

The data is pulled from an open source API built and maintained by [OpenStates.org](https://openstates.org/). Since the data provided by them is spread out over several APIs and endpoints, I built a python machine to do the following:

- Generate `ChambersTotal.json` using `getTotalMembers.py`. This file is more or less never needs updating once you generate it since the number of seats in a legislature remains constant.
- Generate <em>bopRollup.json</em> using <strong>updateEverything.py</strong>. This file runs the following:
  - `getIncumbents.py` to generate a unique json file for each chamber in each state and saves them in the `[/public/output]` folder with the naming convention of `[state]-[chamber].json`
  - After generating all of the incumbent files, `updateChambers.py` loops through them to generate the bopRollup.json file and the hemicycle diagrams based off of the `bopRollup.json` file.

### Getting Started

1. Ensure you have `python v3.xx` installed on your machine and upgrade if not.
2. Clone repo and then run:

   ```
   python3 -m venv python-env

   source python-env/bin/activate

   pip install -r requirements.txt
   ```

3. Sign up for a free API key at [Open States](https://openstates.org/accounts/login/?next=/accounts/profile/#apikey) (you can sign up for two using two different emails if you'd like)
4. Create an empty secrets.py file in the root directory `/ga-legislature` and add your API keys as:
   ```
   apikey1 = " YourApiKeyHERE "
   apikey2 = " YourSecondApiKeyHERE "
   ```
   Note: if you only request one API key from OpenStates, enter it in both spots in `secrets.py`, the code requires both to have a value to run successfully.
5. Run `python3 updateEverything.py` and watch it go!

## Front End (Svelte)

1. Install packages using `npm install`
2. Ensure you have populated your output folder by running the above python machine at least once successfully.
3. To open the dev environment run `npm run dev`<br>
