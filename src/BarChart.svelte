<script>
  const thing = "thing";
</script>

<main>
  <div class="bar">
    <div class="bar-container">
      <div class="gop" />
      <div class="dem" />
    </div>
  </div>
</main>

<style>
  .bar {
    border-style: solid;
    border-color: black;
    width: 50%;
    min-height: 20px;
  }
  .bar-container {
    width: 100%;
    height: 100%;
    display: inline;
  }
  .dem {
    width: 59%;
    height: 100%;
    background-color: blue;
  }
  .gop {
    width: 20%;
    height: 100%;
    background-color: red;
  }

  main {
    width: 100%;
    display: flex;
  }
</style>
