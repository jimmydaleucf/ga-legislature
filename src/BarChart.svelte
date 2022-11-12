<script>

let chambers=[]; 
let chambObj = [];

fetch("/output/bopRollup.json")
.then((res) => res.text())
.then((res) => {
    chambers= res;
     chambObj = JSON.parse(chambers);
    console.log(chambObj)
});
</script>

<main>
    <div>
        {#each chambObj as chamb}
        <div>{chamb.state}</div>
            {/each}
    </div>
</main>
