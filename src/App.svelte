<script>
  import LegMap from "./LegMap.svelte";
  import BopBar from "./BopBar.svelte";

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
  <h1>Jimmy's Legislature Project</h1>
  {#each stateList as state}
    <div class="state-container">
      <h2 class="state-name">{state}</h2>
      <div class="flex-container">
        {#if state != "Nebraska"}
          {#each chamberList as chamber}
            <div class="bop-component"><BopBar {state} {chamber} /></div>
          {/each}
        {:else}
          <div class="bop-component">
            <BopBar {state} chamber="legislature" />
          </div>
        {/if}
      </div>
    </div>
  {/each}
</main>

<style>
  main {
    height: 100%;
  }
  .state-container {
    flex-direction: column;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    border-style: solid;
    border-color: black;
    padding: 15px;
    margin-top: 20px;
  }
  .flex-container {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
  }
  .bop-component {
    width: 45%;
  }
  .state-name {
    text-align: center;
    font-size: 40px;
    margin: 0px;
  }
</style>
