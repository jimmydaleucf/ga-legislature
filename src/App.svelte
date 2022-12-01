<script>
  import LegMap from "./LegMap.svelte";
  import BopBar from "./BopBar.svelte";
  import Diagram from "./Diagram.svelte";

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

  let stateListExperiment = ["California", "Florida", "Georgia", "New York"];

  let chamberList = ["upper", "lower"];
</script>

<main>
  <h1>Jimmy's Legislature Project</h1>
  <div class="flexy-thing">
    {#each stateList as state}
      <div class="state-container">
        <h2 class="state-name">{state}</h2>
        <div class="flex-container">
          {#if state != "Nebraska"}
            {#each chamberList as chamber}
              <div class="state-container spacer">
                <!-- <LegMap {state} {chamber} /> -->
                <Diagram {state} {chamber} />
                <BopBar {state} {chamber} />
              </div>
            {/each}
          {:else}
            <div class="bop-component nebraska">
              <BopBar {state} chamber="legislature" />
            </div>
          {/if}
        </div>
      </div>
    {/each}
  </div>
</main>

<style>
  main {
    height: 100%;
  }
  .state-container {
    justify-content: space-around;
    border-style: solid;
    border-color: black;
    border-width: 2px;
    /* padding: 15px; */
    margin-top: 20px;
    min-width: 45%;
  }
  .spacer {
    width: 45%;
    border-style: none;
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
    font-size: 30px;
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
      padding: 0;
      flex-direction: row;
      width: 100%;
    }
    .state-container .spacer {
      margin-top: 0;
    }
  }
</style>
