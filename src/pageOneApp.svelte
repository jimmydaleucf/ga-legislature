<script>
  // import LegMap from "./LegMap.svelte";
  import BopBar from "./BopBar.svelte";
  import Diagram from "./Diagram.svelte";
  import { onMount } from "svelte";

  let testDataObj;
  let year;
  let path = "https://jrd-primary-public.s3.amazonaws.com/2023/bopRollup.json";

  onMount(async () => {
    const res = await fetch(`${path}`);
    const results = await res.json();
    testDataObj = results.states;
    year = results.year;
  });

  let stateList = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
  ];
  let chamberList = ["upper", "lower"];
</script>

<main>
  {#if testDataObj}
    <h1>State Legislatures Party Composition</h1>
    <h1>{year}</h1>
    <div class="flexy-thing">
      <!-- <BopBar state="US" chamber="National" /> -->
      {#each stateList as state}
        <div class="state-container">
          <h2 class="state-name">{state}</h2>
          <div class="flex-container">
            {#if state != "Nebraska"}
              {#each chamberList as chamber}
                <div class="state-container spacer">
                  <!-- <LegMap {state} {chamber} /> -->
                  <Diagram {state} {chamber} />
                  {#if testDataObj}
                    <BopBar {testDataObj} {state} {chamber} />{/if}
                </div>
              {/each}
            {:else}
              <div class="bop-component nebraska">
                <Diagram {state} chamber="legislature" />
                <BopBar {testDataObj} {state} chamber="legislature" />
                <p>
                  Nebraska's Legislature is unicameral (only one chamber) and
                  its members run as non-partisan.
                </p>
              </div>
            {/if}
          </div>
        </div>
      {/each}
    </div>{/if}
</main>

<style>
  main {
    height: 100%;
  }

  p {
    margin: 10px;
    text-align: center;
  }
  .state-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* justify-content: space-around; */
    border-style: solid;
    border-color: black;
    border-width: 4px;
    /* padding: 15px; */
    margin-top: 20px;
    width: 45%;
  }
  .spacer {
    width: 45%;
    border-style: none;
  }
  h1 {
    font-size: 2.5em;
  }
  .flexy-thing {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }

  .nebraska {
    width: 100%;
  }
  .flex-container {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
  .state-container .spacer {
    width: 100%;
    margin-top: 0;
  }
  .state-name {
    text-align: center;
    font-size: 36px;
    margin-bottom: 0px;
  }

  @media only screen and (max-width: 600px) {
    .flex-container {
      flex-direction: column;
      padding: 5px;
    }
    .spacer {
      width: 100%;
    }
    .state-container {
      display: block;
      padding: 0;
      flex-direction: row;
      width: 100%;
    }
    .state-container .spacer {
      margin-top: 0;
    }
  }
</style>
