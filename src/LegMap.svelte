<script>
  import { onMount } from "svelte";
  import { set_attributes } from "svelte/internal";

  let svgMarkup;
  let precinctData;

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
      // svg.setAttribute("style", "max-height:500px");
      svg.setAttribute("id", `${state}-${chamber}-map`);
      svgMarkup = map.innerHTML;
      getResults();
    });
  // });

  async function getResults() {
    const res = await fetch(`./output/${state}-${chamber}.json`);
    const results = await res.json();
    // console.log(results);
    if (res.ok) {
      //   debugger;
      precinctData = results;
      paintMap(precinctData);
    } else {
      throw new Error(text);
    }
  }

  const paintMap = () => {
    let demCount = 0;
    let gopCount = 0;
    for (let i = 0; i < precinctData.length; i++) {
      let district = precinctData[i].current_role.district;
      let party = precinctData[i].party;
      let map = document.getElementById(`${state}-${chamber}-map`);
      const mapTarget = map.getElementById(`${district}`);
      // console.log(chamber + district + party);
      if (party == "Democratic") {
        mapTarget.style.fill = "#4165D2";
        demCount++;
        // console.log(`demCount for ${state} ${chamber}` + " is " + demCount);
      } else if (party == "Republican") {
        mapTarget.style.fill = "#DC3D3D";
        gopCount++;
        // console.log(`gopCount for ${state} ${chamber}` + " is " + demCount);
      } else {
        // console.log("something else happened");
      }
    }
    // document.getElementById("dem").style.width = `${demCount}%`;
    // document.getElementById("gop").style.width = `${gopCount}%`;
  };
</script>

<main>
  <h2>{state} {chamber} Chamber</h2>
  <div class="container">
    {#if svgMarkup}
      <div class="map">{@html svgMarkup}</div>
    {/if}
  </div>
  <!-- <div class="bop">
    <div id="dem" />
    <div id="gop" />
  </div> -->
</main>

<style>
  main {
    width: 30%;
  }
  .bop {
    border-color: black;
    border-style: solid;
    min-height: 20px;
    margin: 20px;
    display: flex;
    flex-direction: row;
  }
  #dem {
    height: 20px;
    background-color: blue;
  }
  #gop {
    height: 20px;
    background-color: red;
  }
</style>
