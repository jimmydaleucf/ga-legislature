<script>
  import LegMap from "./LegMap.svelte";
  import BarChart from "./BarChart.svelte";
</script>

<main>
  <h1>Jimmy's Legislature Project</h1>
  <div class="container">
    <BarChart />
    <!-- <LegMap state="Florida" chamber="upper" /> -->
    <!-- <LegMap state="Florida" chamber="upper" />
    <LegMap state="Georgia" chamber="lower" />
    <LegMap state="Georgia" chamber="upper" />
    <LegMap state="California" chamber="upper" /> -->
    <!-- <LegMap state="California" chamber="lower" /> -->
  </div>
</main>

<style>
  main {
    height: 100%;
  }
  .container {
    flex-direction: row;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }
</style>
