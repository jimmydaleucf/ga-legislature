<script>
  async function getChamberInfo() {
    const res = await fetch(`./output/legislatureDataFile.json`);
    const results = await res.json();
    const stateName = `${state}`;
    if (res.ok) {
      //   debugger;
      chamberData = results;
      const targetState = chamberData.find(
        ({ state }) => state === `${stateName}`
      );
      const organizations = targetState.organizations.find(
        ({ classification }) => classification === `${chamber}`
      );
      const chamberSize = organizations.totalSeats;
      return chamberSize;
    } else {
      throw new Error(text);
    }
  }
</script>

<main>
  <div>
    <div id="{state}-{chamber}-bop" class="bop">
      <div id="{state}-{chamber}-dem" class="dem" />
      <div id="{state}-{chamber}-gop" class="gop" />
    </div>
  </div>
</main>

<style>
  .bop {
    border-color: black;
    border-style: solid;
    min-height: 20px;
    margin: 20px;
    display: flex;
    flex-direction: row;
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
</style>
