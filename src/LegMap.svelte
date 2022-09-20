<script>
  // let arrayList = [];

  // async function getData() {
  //   const res = await fetch(
  //     "https://v3.openstates.org/people?jurisdiction=Florida&org_classification=lower&page=1&per_page=50&apikey=f186a663-061d-462c-8364-f20e6f3594ce"
  //   );
  //   const results = await res.json();
  //   const pages = results.pagination.max_page;
  //   // console.log(pages);
  //   let list = results.results;
  //   console.log(list);
  //   console.log("printing list");
  //   arrayList.push(list);
  //   console.log("printing arrayList");
  //   console.log(arrayList);
  //   if (pages > 1) {
  //     for (let i = 2; i <= pages; i++) {
  //       const res = await fetch(
  //         `https://v3.openstates.org/people?jurisdiction=Florida&org_classification=lower&page=1&per_page=50&apikey=f186a663-061d-462c-8364-f20e6f3594ce&page=${i}`
  //       );
  //       const newBatch = await res.json();
  //       console.log("printing newBatch");
  //       console.log(newBatch);
  //       const newData = newBatch.results;
  //       console.log("printing newData");
  //       console.log(newData);
  //       arrayList.push(newData);
  //       console.log("printing updated arrayList");
  //       console.log(arrayList);
  //     }
  //   } else {
  //   }
  // }

  // getData();
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
