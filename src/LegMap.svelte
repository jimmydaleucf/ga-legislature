<script>
  import { onMount } from "svelte";

  let svgMarkup;
  let precinctData;
  let chamberData;
  let chamberSize;

  export let state;
  export let chamber;
  //
  // onMount(() => {
  fetch(`./assets/2012/${state}-${chamber}.svg`)
    .then((res) => res.text())
    .then((res) => {
      svgMarkup = res;
      let map = document.createElement("div");
      map.innerHTML = svgMarkup;
      let svg = map.querySelector("svg");
      svg.classList.add("svg-map");
      svg.setAttribute("height", "100%");
      svg.setAttribute("fill", "gray");
      svg.setAttribute("stroke", "black");
      svg.setAttribute("width", "100%");
      svg.setAttribute("font-size", "3em");
      let paths = svg.querySelectorAll("path");
      for (let i = 0; i < paths.length; i++) {
        let path = paths[i];
        path.addEventListener("mouseover", mouseOver);
        path.addEventListener("mouseout", mouseOut);
      }
      // svg.setAttribute("style", "max-height:500px");
      svg.setAttribute("id", `${state}-${chamber}-map`);
      svgMarkup = map.innerHTML;
      getChamberInfo().then(getResults());
    });
  // });

  function mouseOver() {
    target.style.fill = "green";
  }

  function mouseOut() {
    target.style.fill = "pink";
  }

  async function getResults() {
    const res = await fetch(`./output/${state}-${chamber}.json`);
    const results = await res.json();
    // console.log(results);
    if (res.ok) {
      //   debugger;
      precinctData = results;
      paintMap();
    } else {
      throw new Error(text);
    }
  }
  async function getChamberInfo() {
    const res = await fetch(`./output/ChambersTotal.json`);
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
      const thing = organizations.totalSeats;
      chamberSize = thing;
      return chamberSize;
    } else {
      throw new Error(text);
    }
  }

  const paintMap = () => {
    let demCount = 0;
    let gopCount = 0;
    let thirdCount = 0;
    for (let i = 0; i < precinctData.length; i++) {
      let district = precinctData[i].current_role.district;
      let party = precinctData[i].party;
      let map = document.getElementById(`${state}-${chamber}-map`);
      const mapTarget = map.getElementById(`${district}`);
      // console.log(chamber + district + party);
      if (party == "Democratic") {
        mapTarget.style.fill = "#4165D2";
        demCount++;
      } else if (party == "Republican") {
        mapTarget.style.fill = "#DC3D3D";
        gopCount++;
      } else {
        mapTarget.style.fill = "#E3BB1C";
        thirdCount++;
        // console.log("something else happened");
      }
    }
    // console.log(`demCount for ${state} ${chamber}` + " is " + demCount);
    // console.log(`gopCount for ${state} ${chamber}` + " is " + gopCount);
    const demPercent = (demCount / chamberSize) * 100;
    // console.log(demPercent);
    const gopPercent = (gopCount / chamberSize) * 100;
    const thirdPercent = (thirdCount / chamberSize) * 100 + 0.001; //i added this .001 to solve the tiny gap that is showing up when 3 colors are displayed in the bar
    // console.log(gopPercent);
    // console.log(demPercent);
    document.getElementById(
      `${state}-${chamber}-dem`
    ).style.width = `${demPercent}%`;
    document.getElementById(
      `${state}-${chamber}-gop`
    ).style.width = `${gopPercent}%`;
    document.getElementById(
      `${state}-${chamber}-third`
    ).style.width = `${thirdPercent}%`;
  };
</script>

<main>
  <h2>{state} {chamber} Chamber</h2>
  <div class="container">
    {#if svgMarkup}
      <div class="map">{@html svgMarkup}</div>
    {/if}
  </div>
  <div id="{state}-{chamber}-bop" class="bop">
    <div id="{state}-{chamber}-dem" class="dem" />
    <div id="{state}-{chamber}-third" class="third" />
    <div id="{state}-{chamber}-gop" class="gop" />
  </div>
  <!-- <Tooltip title="this is a greeting from component">
    <h1>Hello world from component!</h1>
  </Tooltip> -->
</main>

<style>
  main {
    width: 35%;
  }

  .active {
    border-color: white;
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
