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

fetch('/output/ChambersTotal.json').then((res)=> res.text())
</script>

<main>
    <div class="box">
        {#each chambObj as chamb}
        <table>
        <th>{chamb.state} {chamb.chamberInfo[0].chamber} </th>
        <tr><div class="gop" style="width:({chamb.chamberInfo[0].gop}/{chamb.chamberInfo[0].incubmentTotal})%; height:5px"></div></tr>
        <!-- <tr>DEM Members: </tr>
        <tr>OTHER Members: {chamb.chamberInfo[0].other}</tr> -->
        </table>
         {/each}
    </div>
</main>

<style>
    .box{
        display:flex;
        flex-wrap: wrap
    }
    .gop{
        background-color:red
    }
    table{
        margin: 5px;
    }
    </style>
