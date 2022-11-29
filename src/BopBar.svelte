<script>
  export let state;
  let chamberSize;
  export let chamber;
  let chamberData;
  let chamberName;
  let demSeats;
  let gopSeats;
  let otherSeats;
  let totalIncumbents;
  let vacantSeats;
  let totalSeats;

  async function getChamberInfo() {
    const res = await fetch(`./output/bopRollup.json`);
    const results = await res.json();
    // console.log(results);
    const stateName = `${state}`;
    if (res.ok) {
      //   debugger;
      chamberData = results.states;
      const targetState = chamberData.find(
        ({ state }) => state === `${stateName}`
      );
      const organization = targetState.organizations.find(
        ({ classification }) => classification === `${chamber}`
      );
      chamberName = organization.org;
      totalSeats = organization.totalSeats;
      demSeats = organization.dem;
      gopSeats = organization.gop;
      otherSeats = organization.other;
      totalIncumbents = organization.incubmentTotal;
      vacantSeats = totalSeats - totalIncumbents;
      const demPercent = (demSeats / totalSeats) * 100;
      const gopPercent = (gopSeats / totalSeats) * 100;
      const vacantPercent = (vacantSeats / totalSeats) * 100;
      const thirdPercent = (otherSeats / totalSeats) * 100 + 0.001; //i added this .001 to solve the tiny gap that is showing up when 3 colors are displayed in the bar
      document.getElementById(
        `${state}-${chamber}-dem`
      ).style.width = `${demPercent}%`;
      document.getElementById(
        `${state}-${chamber}-gop`
      ).style.width = `${gopPercent}%`;
      document.getElementById(
        `${state}-${chamber}-third`
      ).style.width = `${thirdPercent}%`;
      document.getElementById(
        `${state}-${chamber}-vacant`
      ).style.width = `${vacantPercent}%`;
      return chamberSize;
    } else {
      throw new Error(text);
    }
  }

  getChamberInfo();
</script>

<main>
  {#if state != "Nebraska"}
    <h2 class="bop-title">
      {chamberName}
    </h2>
  {:else}
    <h2 class="bop-title">{chamberName}</h2>
  {/if}

  <div class="bar-container">
    <div class="midpoint" />
    <div class="midpoint">50%<br />|</div>
    <div id="{state}-{chamber}-bop" class="bop">
      {#if demSeats != 0}
        <div id="{state}-{chamber}-dem" class="dem">{demSeats}</div>{:else}{/if}
      {#if otherSeats != 0}
        <div id="{state}-{chamber}-third" class="third">{otherSeats}</div>
      {:else}{/if}
      {#if vacantSeats != 0}
        <div id="{state}-{chamber}-vacant" class="vacant">{vacantSeats}</div>
      {:else}{/if}
      {#if demSeats != 0}<div id="{state}-{chamber}-gop" class="gop">
          {gopSeats}
        </div>{:else}{/if}
    </div>
    <div class="footnote"><span>(Total Seats {totalSeats})</span></div>
  </div>
</main>

<style>
  main {
    width: 100%;
  }
  .bop {
    border-color: black;
    border-style: solid;
    min-height: 20px;
    /* margin-bottom: 20px; */
    margin-right: 20px;
    margin-left: 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  .bop-title {
    text-align: center;
    margin-top: 5px;
    margin-bottom: 5px;
  }
  .dem {
    height: 20px;
    color: white;
    font-weight: bold;
    background-color: #4165d2;
    display: flex;
    justify-content: center;
  }
  .footnote {
    font-size: 0.75em;
    text-align: center;
    padding: 5px;
  }
  .gop {
    color: white;
    font-weight: bold;
    height: 20px;
    background-color: #dc3d3d;
    display: flex;
    justify-content: center;
  }
  h2 {
    font-size: 1.2em;
  }
  /* .bar-container { */
  /* border-style: solid;
    border-color: black; */
  /* border-width: 2px; */
  /* } */
  .third {
    height: 20px;
    font-weight: bold;
    background-color: #e3bb1c;
    display: flex;
    justify-content: center;
  }
  .vacant {
    height: 20px;
    color: white;
    background-color: grey;
    display: flex;
    justify-content: center;
  }
  .midpoint {
    text-align: center;
    font-weight: bold;
    margin-top: 5px;
  }
</style>
