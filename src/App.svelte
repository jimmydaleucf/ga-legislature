<script>
  import LegMap from "./LegMap.svelte";
</script>

<main>
  <h1>Jimmy's Legislature Project</h1>
  <div class="container">
    <LegMap state="Florida" chamber="lower" />
    <!-- <LegMap state="Florida" chamber="upper" />
    <LegMap state="Georgia" chamber="lower" />
    <LegMap state="Georgia" chamber="upper" /> -->
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
