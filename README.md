# State Legislatures by Party Composition

In this project, I wanted to represent how each state's legislature was composed by party. To accomplish this, I needed to build a python machine to fetch, aggregate, and shape the data from several disparate APIs into a single JSON file. I then built a web page using svelte that is powered by this single JSON file/feed.

## Data Processing

The data is pulled from an open source API built and maintained by [https://openstates.org/](OpenState). Since the data provided by them is spread out over several APIs and endpoints, I built a python machine to do the following:

- Generate ChambersTotal.json using getTotalMembers.py. This file is more or less never changing once you generate it since the number of seats in a legislature remains constant.
- Generate <em>bopRollup.json</em> using <strong>updateEverything.py</strong>. This file runs the following:
  - <strong>getIncumbents.py</strong> to generate a unique json file for each chamber in each state and saves them in the [/public/output] folder with the naming convention of [state]-[chamber].json
  - After generating all of the incumbent files, <strong>updateChambers.py</strong> loops through them to generate the bopRollup.json file and the hemicycle diagrams based off of the bopRollup.json file.

## Getting Started

1. Clone repo and then run NPM i
2. Ensure you have python v3.xx installed on your machine.
3. Sign up for a free API key at [Openstates.com/profile]
