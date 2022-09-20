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

  let svgMarkup;

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
        svg.setAttribute("fill", "white");
        svg.setAttribute("stroke", "black");
        svg.setAttribute("width", "100%");
        svg.setAttribute("font-size", "3em");
        svg.setAttribute("style", "max-height:300px");
        svgMarkup = map.innerHTML;
      });
  });
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
