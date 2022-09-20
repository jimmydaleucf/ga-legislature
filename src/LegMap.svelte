<script>
  import { onMount } from "svelte";
  import { query_selector_all } from "svelte/internal";

  let svgMarkup;
  let precinctData;
  onMount(() => {
    fetch("./assets/h000h9049.svg")
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
        svg.setAttribute("style", "max-height:500px");
        // svg.getElementById("19").setAttribute("fill", "blue");
        getResults();
        svgMarkup = map.innerHTML;
      });
  });

  async function getResults() {
    const res = await fetch(`./assets/combined.json`);
    const results = await res.json();
    console.log(results);
    if (res.ok) {
      //   debugger;
      precinctData = results;
      paintMap(precinctData);
    } else {
      throw new Error(text);
    }
  }

  const paintMap = () => {
    for (let i = 0; i < precinctData.length; i++) {
      let district = precinctData[i].current_role.district;
      let party = precinctData[i].party;
      console.log(district + party);
      if (party == "Democratic") {
        document.getElementById(`${district}`).style.fill = "blue";
      } else if (party == "Republican") {
        document.getElementById(`${district}`).style.fill = "red";
      }
    }
  };
</script>

<main>
  <div class="container">
    {#if svgMarkup}
      <div class="map">{@html svgMarkup}</div>
    {/if}
  </div>
</main>

<style>
</style>
