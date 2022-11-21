<script>
  export let state;
  let chamberSize;
  export let chamber;
  let chamberData;
  let chamberName;

  async function getChamberInfo() {
    const res = await fetch(`./output/bopRollup.json`);
    const results = await res.json();
    // console.log(results);
    const stateName = `${state}`;
    if (res.ok) {
      //   debugger;
      chamberData = results;
      const targetState = chamberData.find(
        ({ state }) => state === `${stateName}`
      );
      const organization = targetState.organizations.find(
        ({ classification }) => classification === `${chamber}`
      );
      chamberName = organization.org;
      console.log(chamberName);
      const totalSeats = organization.totalSeats;
      const demSeats = organization.dem;
      const gopSeats = organization.gop;
      const otherSeats = organization.other;
      const demPercent = (demSeats / totalSeats) * 100;
      const gopPercent = (gopSeats / totalSeats) * 100;
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
      return chamberSize;
    } else {
      throw new Error(text);
    }
  }

  getChamberInfo();
</script>

<main>
  <h2 class="bop-title">{state} {chamberName}</h2>
  <div id="{state}-{chamber}-bop" class="bop">
    <div id="{state}-{chamber}-dem" class="dem" />
    <div id="{state}-{chamber}-third" class="third" />
    <div id="{state}-{chamber}-gop" class="gop" />
  </div>
</main>

<style>
  main {
    width: 35%;
  }
  .bop {
    border-color: black;
    border-style: solid;
    min-height: 20px;
    margin: 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  .bop-title {
    text-align: center;
  }
  .dem {
    height: 20px;
    background-color: #4165d2;
  }
  .gop {
    height: 20px;
    background-color: #dc3d3d;
    align-items: right;
  }
  .third {
    height: 20px;
    background-color: #e3bb1c;
    align-items: right;
  }
</style>
