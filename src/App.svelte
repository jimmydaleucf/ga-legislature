<script>
  import LegMap from "./LegMap.svelte";
</script>

<main>
  <h1>Jimmy's Legislature Project</h1>
  <div class="container">
    <LegMap state="FL" chamber="lower" />
    <LegMap state="FL" chamber="upper" />
  </div>
</main>

<style>
  main {
    height: 100%;
  }
  .container {
    flex-direction: row;
    display: flex;
    justify-content: space-around;
  }
</style>
