<script>
  let svgMarkup;
  export let state;
  export let chamber;

  let path = "https://jrd-primary-public.s3.amazonaws.com/hemicycles/";
  fetch(`./diagrams/${state}-${chamber}-diagram.svg`)
    .then((res) => res.text())
    .then((res) => {
      svgMarkup = res;
      let map = document.createElement("div");
      map.innerHTML = svgMarkup;
    });
  // let svg = get("public/diagrams/Georgia-House-diagram.svg");
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
