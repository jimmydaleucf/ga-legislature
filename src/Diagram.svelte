<script>
  import App from "./App.svelte";

  let svgMarkup;
  export let state;
  export let chamber;

  export let diagramPath;

  fetch(`${diagramPath}${state}-${chamber}-diagram.svg`)
    .then((res) => res.text())
    .then((res) => {
      svgMarkup = res;
      let map = document.createElement("div");
      map.innerHTML = svgMarkup;
    });
</script>

<main>
  <div class="diagram-container">{@html svgMarkup}</div>
</main>

<style>
  main {
    color: blue;
  }
  .diagram-container {
    margin-top: 10px;
    display: flex;
    justify-content: center;
  }
</style>
