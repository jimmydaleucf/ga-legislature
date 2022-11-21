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
  <BopBar state="Nebraska" chamber="legislature" />

  {#each stateList as state}
    <div class="state-container">
      <h2 class="state-name">{state}</h2>
      <div class="flex-container">
        {#each chamberList as chamber}
          <div class="bop-component"><BopBar {state} {chamber} /></div>
        {/each}
      </div>
    </div>
  {/each}

  <!-- <BopBar state="Florida" chamber="upper" />
    <BopBar state="Florida" chamber="lower" />
    <BopBar state="New York" chamber="upper" />
    <BopBar state="New York" chamber="lower" />
    <BopBar state="Idaho" chamber="upper" />
    <BopBar state="Idaho" chamber="lower" />
    <BopBar state="Nebraska" chamber="legislature" /> -->

  <!-- <LegMap state="Florida" chamber="upper" /> -->
  <!-- <LegMap state="Florida" chamber="upper" />
    <LegMap state="Georgia" chamber="lower" />
    <LegMap state="Georgia" chamber="upper" />
    <LegMap state="California" chamber="upper" /> -->
  <!-- <LegMap state="California" chamber="lower" /> -->
  <!-- </div> -->
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
