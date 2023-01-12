# State Legislatures by Party Composition

In this project, I wanted to represent how each state's legislature was composed by party. To accomplish this, I needed to build a python machine to fetch, aggregate, and shape the data from several disparate APIs into a single JSON file. I then built a web page using svelte that is powered by a single JSON.  This JSON is comprised of  aggregated data form various APIs within Open States that I have reformed to serve the neeeds of my components. 
## Data Processing
The data is pulled from an open source API built and maintained by [https://openstates.org/](OpenStates.com).



Since the data is provided by them spread out over several APIs and endpoints, I built a python machine to do the following:

